#!/usr/bin/env python3
"""Trading-Journal: legt jeden Day Trade als Notiz im Obsidian-Vault ab.

    python3 journal.py write                         # trader/*.json -> Trading/Trades/<Datum> <SYMBOL> <setup>.md
    python3 journal.py close --exit 370.04           # Trade schließen: Ausstieg, R, Gewinn
    python3 journal.py close --exit 358.32 --reason stop --symbol TSLA
    python3 journal.py stats --write                 # -> Trading/Statistik.md
    python3 journal.py list                          # alle Trades, neueste zuerst

Liest nur, was die trader-Skills in trader/ geschrieben haben (plan.json, entry.json,
timemachine.json, orders.json, state/risk.json, state/broker.json), und schreibt nur
Markdown in den Vault. Kein Netzwerk, keine Orders.

Eine Notiz wird bei jedem `write` aufgefrischt: der Block zwischen den journal-Markern
und die automatischen Eigenschaften werden neu geschrieben, alles andere bleibt, was du
selbst ergänzt hast (Reflexion, eigene Eigenschaften, Links).
"""

import argparse
import datetime
import json
import os
import re
import sys

AUTO_START = "<!-- journal:auto:start -->"
AUTO_END = "<!-- journal:auto:end -->"
TRADES_DIR = os.path.join("Trading", "Trades")
STATS_FILE = os.path.join("Trading", "Statistik.md")

# Eigenschaften in dieser Reihenfolge; was nicht hier steht, hängt der Nutzer selbst an
KEYS = ["datum", "symbol", "setup", "richtung", "status", "paper",
        "einstieg", "stop", "ziel", "risiko_je_aktie", "crv", "flat_bis",
        "stueck", "max_verlust",
        "tm_ziel", "tm_stop", "tm_offen", "tm_urteil",
        "hist_ausgeloest", "hist_ziel", "hist_stop",
        "risiko_check",
        "einstieg_ist", "ausstieg", "ausstieg_grund", "ergebnis_r", "gewinn_usd",
        "tags"]
# Eigenschaften, die nur close setzt oder der Nutzer pflegt: write überschreibt sie nie mit leer
KEEP_IF_EMPTY = {"einstieg_ist", "ausstieg", "ausstieg_grund", "ergebnis_r", "gewinn_usd"}

STATUS = {"approved": "freigegeben", "declined": "abgelehnt", "denied": "abgelehnt",
          "placed": "platziert", "failed": "fehlgeschlagen", "filled": "offen"}
# Einträge im Broker-Log
LOG_LABEL = dict(STATUS, filled="ausgeführt")


class JournalError(Exception):
    pass


# ---------------------------------------------------------------- Dateien

def read_json(path, required=True):
    if not os.path.exists(path):
        if required:
            raise JournalError("%s fehlt" % path)
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except ValueError as e:
        raise JournalError("%s ist kein gültiges JSON: %s" % (path, e))


def write_text(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.replace(tmp, path)


def num(v):
    if v is None or v == "":
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def clean(v):
    """8.0 -> 8, damit Obsidian ganze Zahlen ohne .0 zeigt."""
    if isinstance(v, float) and v.is_integer():
        return int(v)
    return v


# ---------------------------------------------------------------- Frontmatter

def fm_value(raw):
    raw = raw.strip()
    if raw == "" or raw in ("null", "~"):
        return None
    if raw in ("true", "false"):
        return raw == "true"
    if raw.startswith('"'):
        try:
            return json.loads(raw)
        except ValueError:
            return raw.strip('"')
    if raw.startswith("'") and raw.endswith("'") and len(raw) > 1:
        return raw[1:-1].replace("''", "'")
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        return [fm_value(x) for x in inner.split(",")] if inner else []
    if re.match(r"^-?\d+$", raw):
        return int(raw)
    if re.match(r"^-?\d+\.\d+$", raw):
        return float(raw)
    return raw


def parse_note(text):
    """-> (frontmatter dict in Dateireihenfolge, body). Versteht auch Obsidians Listen-Schreibweise."""
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if not m:
        return {}, text
    fm, key = {}, None
    for line in m.group(1).split("\n"):
        item = re.match(r"^\s+-\s*(.*)$", line)
        if item and key is not None:
            if not isinstance(fm.get(key), list):
                fm[key] = []
            fm[key].append(fm_value(item.group(1)))
            continue
        kv = re.match(r"^([^\s:#][^:]*):(.*)$", line)
        if kv:
            key = kv.group(1).strip()
            fm[key] = fm_value(kv.group(2))
    return fm, text[m.end():]


def fm_dump(v):
    if v is None:
        return ""
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return repr(clean(v))
    if isinstance(v, list):
        return "\n" + "\n".join("  - %s" % fm_dump(x) for x in v) if v else "[]"
    return json.dumps(str(v), ensure_ascii=False)


def render_frontmatter(fm):
    order = [k for k in KEYS if k in fm] + [k for k in fm if k not in KEYS]
    lines = []
    for k in order:
        val = fm_dump(fm[k])
        lines.append("%s:%s" % (k, val if val.startswith("\n") else (" " + val if val else "")))
    return "---\n" + "\n".join(lines) + "\n---\n"


# ---------------------------------------------------------------- Trade aus trader/ lesen

def same_trade(rec, symbol, date):
    return str(rec.get("symbol", "")).upper() == symbol and (rec.get("date") in (None, date))


def collect(trader):
    plan = read_json(os.path.join(trader, "plan.json"))
    symbol = str(plan.get("symbol", "")).upper()
    date = plan.get("date")
    if not symbol or not date:
        raise JournalError("trader/plan.json hat kein symbol oder date; erst /trader-exit laufen lassen")
    entry = read_json(os.path.join(trader, "entry.json"), required=False)
    if entry and not same_trade(entry, symbol, date):
        entry = None
    tm = read_json(os.path.join(trader, "timemachine.json"), required=False)
    if tm:
        tp = tm.get("plan") or {}
        if str(tp.get("symbol", "")).upper() != symbol or tp.get("date") not in (None, date):
            tm = None
    orders = read_json(os.path.join(trader, "orders.json"), required=False) or {}
    order = next((o for o in orders.get("orders", [])
                  if str(o.get("symbol", "")).upper() == symbol and o.get("side") == plan.get("side", "buy")),
                 None)
    risk_doc = read_json(os.path.join(trader, "state", "risk.json"), required=False) or {}
    risk = None
    if risk_doc.get("date") in (None, date):
        risk = next((r for r in risk_doc.get("results", [])
                     if str(r.get("symbol", "")).upper() == symbol and r.get("kind", "entry") == "entry"), None)
    broker = read_json(os.path.join(trader, "state", "broker.json"), required=False) or {}
    log = [r for r in broker.get("orders", []) if same_trade(r, symbol, date)]
    return {"plan": plan, "entry": entry, "tm": tm, "order": order, "risk": risk, "log": log,
            "paper": orders.get("paper", risk_doc.get("paper"))}


def avg_fill(log, side):
    qty = cost = 0.0
    for r in log:
        if r.get("status") == "filled" and r.get("side") == side:
            q, p = num(r.get("qty")), num(r.get("price"))
            if q and p:
                qty += q
                cost += q * p
    return (round(cost / qty, 4), qty) if qty else (None, 0.0)


def outcome(side, entry, exit_, risk_per_share, qty):
    sign = 1 if side == "buy" else -1
    r = round((exit_ - entry) * sign / risk_per_share, 2) if risk_per_share else None
    pnl = round((exit_ - entry) * sign * qty, 2) if qty else None
    return r, pnl


def guess_reason(side, exit_, stop, target):
    """ziel / stop / flat, aus dem Ausstiegspreis gegen den Plan."""
    if stop is None or target is None:
        return "manuell"
    if side == "buy":
        return "ziel" if exit_ >= target - 0.01 else ("stop" if exit_ <= stop + 0.01 else "flat")
    return "ziel" if exit_ <= target + 0.01 else ("stop" if exit_ >= stop - 0.01 else "flat")


def auto_fields(t):
    plan, order, tm, risk = t["plan"], t["order"], t["tm"], t["risk"]
    side = plan.get("side", "buy")
    f = {"datum": plan["date"], "symbol": plan["symbol"].upper(), "setup": plan.get("setup"),
         "richtung": "long" if side == "buy" else "short",
         "paper": t["paper"] if t["paper"] is not None else True,
         "einstieg": num(plan.get("entry")), "stop": num(plan.get("stop")), "ziel": num(plan.get("target")),
         "risiko_je_aktie": num(plan.get("risk_per_share")), "crv": num(plan.get("reward_risk")),
         "flat_bis": plan.get("flat_by"),
         "stueck": num(order.get("qty")) if order else None,
         "max_verlust": num((order.get("plan") or {}).get("max_loss")) if order else None,
         "tags": ["trade", plan.get("setup") or "setup"]}
    if tm:
        mc, hist = tm.get("mc") or {}, tm.get("history") or {}
        for key, src in (("tm_ziel", "p_target"), ("tm_stop", "p_stop"), ("tm_offen", "p_neither")):
            p = num(mc.get(src))
            f[key] = round(p * 100, 1) if p is not None else None
        f["tm_urteil"] = tm.get("verdict")
        f["hist_ausgeloest"] = hist.get("triggered")
        f["hist_ziel"] = hist.get("target")
        f["hist_stop"] = hist.get("stop")
    f["risiko_check"] = risk.get("verdict") if risk else None

    status = "geplant"
    if risk and risk.get("verdict") == "BLOCK":
        status = "blockiert"
    if t["log"]:
        status = STATUS.get(t["log"][-1].get("status"), status)
    buy_side, sell_side = side, ("sell" if side == "buy" else "buy")
    entry_px, entry_qty = avg_fill(t["log"], buy_side)
    exit_px, exit_qty = avg_fill(t["log"], sell_side)
    f["einstieg_ist"] = entry_px
    if entry_px is not None and exit_px is not None and exit_qty >= entry_qty:
        f["ausstieg"] = exit_px
        f["ausstieg_grund"] = guess_reason(side, exit_px, f["stop"], f["ziel"])
        f["ergebnis_r"], f["gewinn_usd"] = outcome(side, entry_px, exit_px, f["risiko_je_aktie"], entry_qty)
        status = "geschlossen"
    elif entry_px is not None:
        status = "offen"
    f["status"] = status
    return {k: clean(v) if isinstance(v, float) else v for k, v in f.items()}


# ---------------------------------------------------------------- Notiz

def money(v):
    return "–" if v is None else "$%s" % format(v, ",.2f")


def px(v):
    return "–" if v is None else format(v, ".2f")


def rr(v):
    return "–" if v is None else "%+.2f R" % v


def result_line(exit_, reason, r, pnl):
    return "Ausstieg %s (%s): **%s**, %s." % (px(exit_), reason or "–", rr(r), money(pnl))


def auto_block(t, f):
    plan, entry, tm, risk = t["plan"], t["entry"], t["tm"], t["risk"]
    out = [AUTO_START, "",
           "> [!warning] Keine Anlageberatung",
           "> Automatisch aus `trader/` übernommen. Eine Simulation ist keine Vorhersage.", "",
           "## Plan", "",
           "| | |", "| --- | --- |",
           "| Setup | %s (%s) |" % (plan.get("setup") or "–", f["richtung"]),
           "| Einstieg | %s um %s |" % (px(f["einstieg"]), plan.get("entry_time") or "–"),
           "| Stop | %s (%s) |" % (px(f["stop"]), plan.get("stop_label") or plan.get("stop_rule") or "–"),
           "| Ziel | %s (%s) |" % (px(f["ziel"]), plan.get("target_label") or "–"),
           "| Risiko je Aktie | %s |" % px(f["risiko_je_aktie"]),
           "| Flat bis | %s New York |" % (f["flat_bis"] or "–")]
    if f.get("stueck") is not None:
        out.append("| Größe | %s Stück, max. Verlust %s |" % (f["stueck"], money(f["max_verlust"])))
    if entry and entry.get("reason"):
        out += ["", "Auslöser: %s." % entry["reason"]]
    if tm:
        out += ["", "## Time Machine", "",
                "%s replays: Ziel zuerst **%s %%**, Stop zuerst **%s %%**, offen bis Schluss %s %%."
                % (format((tm.get("mc") or {}).get("replays", 0), ","), f["tm_ziel"], f["tm_stop"], f["tm_offen"])]
        if f.get("hist_ausgeloest") is not None:
            out.append("Dieselbe Regel in der Historie: %s-mal ausgelöst, %s Ziel, %s Stop."
                       % (f["hist_ausgeloest"], f["hist_ziel"], f["hist_stop"]))
        if tm.get("verdict"):
            out += ["", "> %s" % tm["verdict"]]
    if risk:
        out += ["", "## Risiko-Check", "", "**%s**" % risk.get("verdict")]
        for line in (risk.get("reasons") or []) + (risk.get("warnings") or []) + (risk.get("info") or []):
            out.append("- %s" % line)
    if t["log"]:
        out += ["", "## Broker-Log", ""]
        for r in t["log"]:
            out.append("- %s · %s · %s" % (r.get("at", "–"), LOG_LABEL.get(r.get("status"), r.get("status")),
                                            r.get("plain", "")))
    out += ["", "## Ergebnis", ""]
    if f.get("ausstieg") is not None:
        out.append(result_line(f["ausstieg"], f.get("ausstieg_grund"), f.get("ergebnis_r"), f.get("gewinn_usd")))
    else:
        out.append("Noch offen. Schließen mit `journal.py close --exit PREIS`.")
    out += ["", AUTO_END]
    return "\n".join(out)


def note_path(vault, f):
    name = "%s %s %s.md" % (f["datum"], f["symbol"], f.get("setup") or "trade")
    return os.path.join(vault, TRADES_DIR, re.sub(r'[\\/:*?"<>|]', "-", name))


def new_body(f, block):
    return "\n".join([
        "# %s %s, %s" % (f["symbol"], f.get("setup") or "", f["datum"]), "",
        "Tag: [[Tagesnotizen/%s]] · Regeln: [[Trading/Regeln]]" % f["datum"], "",
        block, "",
        "## Reflexion", "",
        "- Warum dieser Trade?",
        "- An den Plan gehalten? Wenn nein, warum nicht?",
        "- Was nehme ich mit? Wichtiges nach [[Gedächtnis/Erkenntnisse/Trading]] übertragen.", ""])


def merge(old_fm, f):
    fm = dict(old_fm)
    for k, v in f.items():
        if v is None and (k in KEEP_IF_EMPTY or old_fm.get(k) is not None):
            continue
        fm[k] = v
    if old_fm.get("status") == "geschlossen":
        fm["status"] = "geschlossen"
    tags = list(old_fm.get("tags") or [])
    fm["tags"] = tags + [x for x in f["tags"] if x not in tags]
    return fm


def cmd_write(a):
    t = collect(a.trader)
    f = auto_fields(t)
    path = note_path(a.vault, f)
    block = auto_block(t, f)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            old_fm, body = parse_note(fh.read())
        fm = merge(old_fm, f)
        if AUTO_START in body and AUTO_END in body:
            pre, rest = body.split(AUTO_START, 1)
            body = pre + block + rest.split(AUTO_END, 1)[1]
        else:
            body = body.rstrip("\n") + "\n\n" + block + "\n"
        verb = "Aktualisiert"
    else:
        fm, body, verb = merge({}, f), new_body(f, block), "Angelegt"
    write_text(path, render_frontmatter(fm) + "\n" + body.lstrip("\n"))
    print("%s: %s (Status %s)" % (verb, os.path.relpath(path, a.vault), fm["status"]))
    return 0


# ---------------------------------------------------------------- Schließen, Liste, Statistik

def load_trades(vault):
    d = os.path.join(vault, TRADES_DIR)
    out = []
    if os.path.isdir(d):
        for name in sorted(os.listdir(d)):
            if name.endswith(".md"):
                p = os.path.join(d, name)
                with open(p, encoding="utf-8") as fh:
                    fm, body = parse_note(fh.read())
                out.append((p, fm, body))
    out.sort(key=lambda x: (str(x[1].get("datum") or ""), os.path.getmtime(x[0])), reverse=True)
    return out


def cmd_close(a):
    trades = [x for x in load_trades(a.vault)
              if (not a.symbol or str(x[1].get("symbol", "")).upper() == a.symbol.upper())]
    if a.file:
        trades = [x for x in trades if os.path.basename(x[0]) in (a.file, a.file + ".md")]
    else:
        trades = [x for x in trades if x[1].get("status") != "geschlossen"]
    if not trades:
        raise JournalError("kein offener Trade gefunden%s" % (" für " + a.symbol.upper() if a.symbol else ""))
    path, fm, body = trades[0]
    side = "buy" if fm.get("richtung", "long") == "long" else "sell"
    entry = num(a.entry) or num(fm.get("einstieg_ist")) or num(fm.get("einstieg"))
    qty = num(a.qty) or num(fm.get("stueck"))
    exit_ = num(a.exit)
    if entry is None or exit_ is None:
        raise JournalError("Einstieg oder Ausstieg fehlt (--entry, --exit)")
    r, pnl = outcome(side, entry, exit_, num(fm.get("risiko_je_aktie")), qty)
    fm.update({"einstieg_ist": clean(entry), "ausstieg": clean(exit_),
               "ausstieg_grund": a.reason or guess_reason(side, exit_, num(fm.get("stop")), num(fm.get("ziel"))),
               "ergebnis_r": r, "gewinn_usd": pnl, "status": "geschlossen"})
    if AUTO_START in body and AUTO_END in body:
        pre, rest = body.split(AUTO_START, 1)
        inner, post = rest.split(AUTO_END, 1)
        line = result_line(exit_, fm["ausstieg_grund"], r, pnl)
        inner = re.sub(r"(## Ergebnis\n\n).*?(\n\n|$)", lambda m: m.group(1) + line + m.group(2), inner,
                       count=1, flags=re.S)
        body = pre + AUTO_START + inner + AUTO_END + post
    write_text(path, render_frontmatter(fm) + "\n" + body.lstrip("\n"))
    print("Geschlossen: %s, %s, %s" % (os.path.basename(path), rr(r), money(pnl)))
    return 0


def cmd_list(a):
    trades = load_trades(a.vault)
    if not trades:
        print("Noch keine Trades in %s." % TRADES_DIR)
        return 1
    for p, fm, _ in trades:
        r = fm.get("ergebnis_r")
        print("%-10s %-6s %-6s %-12s %s" % (fm.get("datum"), fm.get("symbol"), fm.get("setup"),
                                            fm.get("status"), "" if r is None else "%+.2f R" % r))
    return 0


def summarize(rows):
    closed = [fm for fm in rows if fm.get("status") == "geschlossen" and num(fm.get("ergebnis_r")) is not None]
    rs = [num(fm["ergebnis_r"]) for fm in closed]
    tm = [num(fm.get("tm_ziel")) for fm in closed if num(fm.get("tm_ziel")) is not None]
    return {"trades": len(rows), "geschlossen": len(closed),
            "gewinner": sum(1 for r in rs if r > 0),
            "trefferquote": round(100.0 * sum(1 for r in rs if r > 0) / len(rs), 1) if rs else None,
            "schnitt_r": round(sum(rs) / len(rs), 2) if rs else None,
            "summe_r": round(sum(rs), 2) if rs else None,
            "gewinn_usd": round(sum(num(fm.get("gewinn_usd")) or 0 for fm in closed), 2),
            "ziel_erreicht": round(100.0 * sum(1 for fm in closed if fm.get("ausstieg_grund") == "ziel")
                                   / len(closed), 1) if closed else None,
            "tm_ziel_schnitt": round(sum(tm) / len(tm), 1) if tm else None}


def fmt(v, suffix=""):
    return "–" if v is None else "%s%s" % (v, suffix)


def cmd_stats(a):
    rows = [fm for _, fm, _ in load_trades(a.vault)]
    s = summarize(rows)
    setups = sorted({str(fm.get("setup") or "–") for fm in rows})
    lines = ["---", "tags:", "  - trading", "  - statistik", "---", "",
             "# Trading-Statistik", "",
             "Erzeugt von `journal.py stats --write` am %s. Nicht von Hand bearbeiten, "
             "Gedanken dazu gehören nach [[Gedächtnis/Erkenntnisse/Trading]]." % datetime.date.today().isoformat(), "",
             "| | |", "| --- | --- |",
             "| Trades im Journal | %s |" % s["trades"],
             "| Geschlossen | %s |" % s["geschlossen"],
             "| Trefferquote | %s |" % fmt(s["trefferquote"], " %"),
             "| Schnitt je Trade | %s |" % fmt(s["schnitt_r"], " R"),
             "| Summe | %s, %s |" % (fmt(s["summe_r"], " R"), money(s["gewinn_usd"])),
             "| Ziel erreicht | %s |" % fmt(s["ziel_erreicht"], " %"),
             "| Time Machine sagte im Schnitt | %s Ziel zuerst |" % fmt(s["tm_ziel_schnitt"], " %"), "",
             "## Nach Setup", "",
             "| Setup | Trades | geschlossen | Trefferquote | Schnitt R |", "| --- | --- | --- | --- | --- |"]
    for setup in setups:
        ss = summarize([fm for fm in rows if str(fm.get("setup") or "–") == setup])
        lines.append("| %s | %s | %s | %s | %s |" % (setup, ss["trades"], ss["geschlossen"],
                                                     fmt(ss["trefferquote"], " %"), fmt(ss["schnitt_r"])))
    text = "\n".join(lines) + "\n"
    if a.write:
        write_text(os.path.join(a.vault, STATS_FILE), text)
        print("Geschrieben: %s" % STATS_FILE)
    if a.json:
        print(json.dumps(s, indent=2, ensure_ascii=False))
    elif not a.write:
        print(text)
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description="Trading-Journal im Obsidian-Vault.")
    p.add_argument("--vault", default=".", help="Wurzel des Vaults (Standard: aktueller Ordner)")
    p.add_argument("--trader", default="trader", help="Ordner der trader-Skills (Standard: trader)")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("write", help="Trade aus trader/ ins Journal schreiben oder auffrischen")
    c = sub.add_parser("close", help="Trade schließen")
    c.add_argument("--exit", required=True, help="Ausstiegspreis")
    c.add_argument("--entry", help="tatsächlicher Einstieg, falls abweichend vom Plan")
    c.add_argument("--qty", help="Stückzahl, falls abweichend")
    c.add_argument("--reason", choices=["ziel", "stop", "flat", "manuell"])
    c.add_argument("--symbol", help="nur Trades dieses Symbols")
    c.add_argument("--file", help="Dateiname der Notiz in Trading/Trades")
    sub.add_parser("list", help="alle Trades")
    s = sub.add_parser("stats", help="Trefferquote, R, Vergleich mit der Time Machine")
    s.add_argument("--write", action="store_true", help="nach Trading/Statistik.md schreiben")
    s.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    if not os.path.isabs(a.trader):
        a.trader = os.path.join(a.vault, a.trader)
    try:
        return {"write": cmd_write, "close": cmd_close, "list": cmd_list, "stats": cmd_stats}[a.cmd](a)
    except JournalError as e:
        print("journal.py: %s" % e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
