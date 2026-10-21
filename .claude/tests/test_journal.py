"""Tests für das Trading-Journal. Laufen offline:

    python3 -m unittest discover -s .claude/tests -v

Die Daten sind der TSLA-Trade aus dem Beispiel der Day-Trader-Skills (19.10.2026),
so wie trader-entry, -exit, -timemachine, -budget und -risk ihn in trader/ schreiben.
"""

import importlib.util
import io
import json
import os
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "..", "skills", "trading-journal", "journal.py")
spec = importlib.util.spec_from_file_location("journal", SCRIPT)
journal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(journal)

PLAN = {"created_by": "trader-exit", "symbol": "TSLA", "side": "buy", "date": "2026-10-19", "setup": "orb",
        "entry": 364.18, "entry_time": "10:15 AM", "entry_bar": 8, "interval": "5m",
        "opening_range": {"high": 362.18, "low": 354.47, "minutes": 15},
        "stop": 358.32, "stop_rule": "or_mid", "stop_label": "opening-range midpoint",
        "target": 370.04, "target_r": 1.0, "target_label": "1R (one times the risk)",
        "risk_per_share": 5.86, "reward_risk": 1.0, "flat_by": "15:55"}
ENTRY = {"created_by": "trader-entry", "symbol": "TSLA", "setup": "orb", "side": "buy", "date": "2026-10-19",
         "status": "triggered", "price": 364.18, "reason": "the 10:10 bar closed above the range high"}
TM = {"created_by": "trader-timemachine",
      "plan": {"symbol": "TSLA", "date": "2026-10-19", "entry": 364.18, "stop": 358.32, "target": 370.04},
      "mc": {"replays": 10000, "seed": 19, "p_target": 0.2938, "p_stop": 0.2548, "p_neither": 0.4514},
      "history": {"sessions": 59, "triggered": 33, "target": 13, "stop": 15, "close": 5},
      "verdict": "Close to a coin flip: target first 29.4 % vs stop first 25.5 %."}
ORDERS = {"created_by": "trader-budget", "status": "proposed", "paper": True,
          "orders": [{"symbol": "TSLA", "side": "buy", "qty": "8", "type": "market", "order_class": "bracket",
                      "take_profit_limit_price": "370.04", "stop_loss_stop_price": "358.32",
                      "plan": {"entry": 364.18, "stop": 358.32, "target": 370.04, "risk_per_share": 5.86,
                               "max_loss": 46.88, "setup": "orb"}}]}
RISK = {"date": "2026-10-19", "paper": True,
        "results": [{"index": 1, "symbol": "TSLA", "side": "buy", "kind": "entry", "verdict": "PASS",
                     "reasons": [], "warnings": [],
                     "info": ["max loss $46.88 (limit $50), reward:risk 1.00 (min 1)"]}]}


def broker(*recs):
    return {"orders": [dict(date="2026-10-19", symbol="TSLA", **r) for r in recs]}


class Journal(unittest.TestCase):
    def setUp(self):
        self.vault = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.vault)
        self.put("plan.json", PLAN)
        self.put("entry.json", ENTRY)
        self.put("timemachine.json", TM)
        self.put("orders.json", ORDERS)
        self.put("state/risk.json", RISK)
        self.note = os.path.join(self.vault, "Trading", "Trades", "2026-10-19 TSLA orb.md")

    def put(self, name, doc):
        path = os.path.join(self.vault, "trader", name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(doc, fh)

    def run_cli(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = journal.main(["--vault", self.vault] + list(args))
        return code, out.getvalue(), err.getvalue()

    def read(self):
        with open(self.note, encoding="utf-8") as fh:
            return journal.parse_note(fh.read())

    def test_write_creates_the_note_with_plan_and_odds(self):
        code, out, _ = self.run_cli("write")
        self.assertEqual(code, 0)
        self.assertIn("Angelegt", out)
        fm, body = self.read()
        self.assertEqual(fm["symbol"], "TSLA")
        self.assertEqual(fm["status"], "geplant")
        self.assertEqual(fm["einstieg"], 364.18)
        self.assertEqual(fm["stop"], 358.32)
        self.assertEqual(fm["stueck"], 8)
        self.assertEqual(fm["max_verlust"], 46.88)
        self.assertEqual(fm["tm_ziel"], 29.4)
        self.assertEqual(fm["tm_stop"], 25.5)
        self.assertEqual(fm["hist_ausgeloest"], 33)
        self.assertEqual(fm["risiko_check"], "PASS")
        self.assertIs(fm["paper"], True)
        self.assertEqual(fm["tags"], ["trade", "orb"])
        self.assertIn("[[Tagesnotizen/2026-10-19]]", body)
        self.assertIn("Ziel zuerst **29.4 %**", body)
        self.assertIn("## Reflexion", body)

    def test_rewrite_keeps_what_the_user_wrote(self):
        self.run_cli("write")
        with open(self.note, encoding="utf-8") as fh:
            text = fh.read()
        text = text.replace("tags:", "stimmung: \"ruhig\"\ntags:")
        text = text.replace("- Warum dieser Trade?", "- Warum dieser Trade? Saubere Range, Volumen dabei.")
        with open(self.note, "w", encoding="utf-8") as fh:
            fh.write(text)
        self.put("state/broker.json", broker({"status": "approved", "at": "2026-10-19T10:16", "plain": "BUY 8 TSLA"}))
        code, out, _ = self.run_cli("write")
        self.assertIn("Aktualisiert", out)
        fm, body = self.read()
        self.assertEqual(fm["status"], "freigegeben")
        self.assertEqual(fm["stimmung"], "ruhig")
        self.assertIn("Saubere Range, Volumen dabei.", body)
        self.assertIn("freigegeben · BUY 8 TSLA", body)
        self.assertEqual(body.count(journal.AUTO_START), 1)

    def test_fills_close_the_trade_on_their_own(self):
        self.put("state/broker.json", broker(
            {"status": "filled", "side": "buy", "qty": "8", "price": 364.20,
             "plain": "BUY 8 TSLA at 364.20"},
            {"status": "filled", "side": "sell", "qty": "8", "price": 370.04}))
        self.run_cli("write")
        fm, body = self.read()
        self.assertEqual(fm["status"], "geschlossen")
        self.assertEqual(fm["einstieg_ist"], 364.2)
        self.assertEqual(fm["ausstieg_grund"], "ziel")
        self.assertEqual(fm["ergebnis_r"], 1.0)
        self.assertEqual(fm["gewinn_usd"], 46.72)
        self.assertIn("**+1.00 R**", body)
        self.assertIn("ausgeführt · BUY 8 TSLA at 364.20", body)

    def test_close_by_hand_at_the_stop(self):
        self.run_cli("write")
        code, out, _ = self.run_cli("close", "--exit", "358.32")
        self.assertEqual(code, 0)
        fm, body = self.read()
        self.assertEqual(fm["status"], "geschlossen")
        self.assertEqual(fm["ausstieg_grund"], "stop")
        self.assertEqual(fm["ergebnis_r"], -1.0)
        self.assertEqual(fm["gewinn_usd"], -46.88)
        self.assertIn("Ausstieg 358.32 (stop): **-1.00 R**", body)
        # ein späteres write macht den Trade nicht wieder auf
        self.run_cli("write")
        fm, _ = self.read()
        self.assertEqual(fm["status"], "geschlossen")
        self.assertEqual(fm["ergebnis_r"], -1.0)

    def test_close_without_an_open_trade(self):
        code, _, err = self.run_cli("close", "--exit", "1")
        self.assertEqual(code, 2)
        self.assertIn("kein offener Trade", err)

    def test_stale_timemachine_is_ignored(self):
        self.put("timemachine.json", dict(TM, plan={"symbol": "NVDA", "date": "2026-10-19"}))
        self.run_cli("write")
        fm, body = self.read()
        self.assertNotIn("tm_ziel", fm)
        self.assertNotIn("## Time Machine", body)

    def test_missing_plan_says_what_to_do(self):
        os.remove(os.path.join(self.vault, "trader", "plan.json"))
        code, _, err = self.run_cli("write")
        self.assertEqual(code, 2)
        self.assertIn("plan.json fehlt", err)

    def test_stats(self):
        self.run_cli("write")
        self.run_cli("close", "--exit", "370.04")
        self.put("plan.json", dict(PLAN, symbol="NVDA", entry=100.0, stop=99.0, target=101.0, risk_per_share=1.0))
        self.run_cli("write")
        self.run_cli("close", "--exit", "99.5", "--symbol", "NVDA", "--qty", "10")
        code, out, _ = self.run_cli("stats", "--write", "--json")
        self.assertEqual(code, 0)
        s = json.loads(out[out.index("{"):])
        self.assertEqual(s["trades"], 2)
        self.assertEqual(s["geschlossen"], 2)
        self.assertEqual(s["trefferquote"], 50.0)
        self.assertEqual(s["schnitt_r"], 0.25)
        self.assertEqual(s["gewinn_usd"], 41.88)  # 8 x 5.86 - 10 x 0.50
        self.assertTrue(os.path.exists(os.path.join(self.vault, "Trading", "Statistik.md")))

    def test_frontmatter_round_trip_and_obsidian_lists(self):
        fm, body = journal.parse_note('---\nsymbol: "TSLA"\nstueck: 8\npaper: true\nleer:\ntags:\n'
                                      '  - trade\n  - orb\nnotiz: frei geschrieben\n---\nText\n')
        self.assertEqual(fm, {"symbol": "TSLA", "stueck": 8, "paper": True, "leer": None,
                              "tags": ["trade", "orb"], "notiz": "frei geschrieben"})
        self.assertEqual(body, "Text\n")
        again, _ = journal.parse_note(journal.render_frontmatter(fm) + "Text\n")
        self.assertEqual(again, fm)


if __name__ == "__main__":
    unittest.main()
