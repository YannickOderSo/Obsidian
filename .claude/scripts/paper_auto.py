#!/usr/bin/env python3
"""Autonomer Ausführer für das Paper-Experiment.

Ersetzt im Paper-Betrieb das Ja je Order (trader-broker), sonst nichts:
trader-risk muss die Order heute mit PASS geprüft haben, und alles läuft nur
gegen das Paper-Konto von Alpaca. Freigabe des Nutzers am 2026-10-22, siehe
Gedächtnis/Entscheidungen/2026-10-22 Autonomes Paper Trading.md.

    python3 .claude/scripts/paper_auto.py status
    python3 .claude/scripts/paper_auto.py place --index 1
    python3 .claude/scripts/paper_auto.py sync
    python3 .claude/scripts/paper_auto.py flatten [--symbol TSLA]
    python3 .claude/scripts/paper_auto.py say "Text"

Schlüssel kommen aus APCA_API_KEY_ID und APCA_API_SECRET_KEY und werden nie ausgegeben.
Ist DISCORD_WEBHOOK_URL gesetzt, gehen Orders, Fills, Glattstellungen und `say` an Discord.
"""

import argparse
import datetime
import importlib.util
import json
import os
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PAPER_URL = "https://paper-api.alpaca.markets"
REPLY = "autonom: Paper-Experiment, Freigabe des Nutzers vom 2026-10-22"


class AutoError(Exception):
    pass


def _ticket():
    path = os.path.join(ROOT, ".claude", "skills", "trader-broker", "ticket.py")
    spec = importlib.util.spec_from_file_location("ticket", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


T = _ticket()


def guard(cfg):
    """Nur Paper: Config und Endpunkt müssen beide Paper sein."""
    if cfg.get("paper") is not True:
        raise AutoError('"paper" ist nicht true in trader/config.json; autonom wird nur Paper gehandelt')
    base = os.environ.get("APCA_API_BASE_URL", PAPER_URL).rstrip("/")
    if base.endswith("/v2"):
        base = base[:-3]
    if base != PAPER_URL:
        raise AutoError("APCA_API_BASE_URL zeigt nicht auf das Paper-Konto; abgebrochen")
    if not os.environ.get("APCA_API_KEY_ID") or not os.environ.get("APCA_API_SECRET_KEY"):
        raise AutoError("APCA_API_KEY_ID oder APCA_API_SECRET_KEY fehlt in der Umgebung")
    return base


def api(base, method, path, body=None):
    req = urllib.request.Request(base + "/v2/" + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None)
    req.add_header("APCA-API-KEY-ID", os.environ["APCA_API_KEY_ID"])
    req.add_header("APCA-API-SECRET-KEY", os.environ["APCA_API_SECRET_KEY"])
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            raw = r.read()
    except urllib.error.HTTPError as e:
        raise AutoError("Alpaca %s %s: HTTP %s %s" % (method, path, e.code, e.read().decode()[:300]))
    return json.loads(raw) if raw else None


def notify(text):
    """Nachricht an den Discord-Webhook in DISCORD_WEBHOOK_URL; ohne Variable still nichts."""
    url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not url:
        return False
    req = urllib.request.Request(url, method="POST",
                                 data=json.dumps({"content": text[:1990], "username": "Paper-Autopilot"}).encode())
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "paper-autopilot")
    try:
        urllib.request.urlopen(req, timeout=10).read()
        return True
    except (urllib.error.URLError, OSError) as e:
        print("Discord nicht erreicht: %s" % getattr(e, "code", e))
        return False


def paths():
    return {k: os.path.join(ROOT, v) for k, v in (
        ("orders", "trader/orders.json"), ("config", "trader/config.json"),
        ("risk", "trader/state/risk.json"), ("state", "trader/state/broker.json"),
        ("portfolio", "trader/portfolio.json"))}


def load_cfg(p):
    return T.read_json(p["config"], "config", required=False) or {}


def cmd_status(a):
    p = paths()
    base = guard(load_cfg(p))
    acc = api(base, "GET", "account")
    print("Konto %s: Eigenkapital %s, Bargeld %s, gestern %s" % (
        acc["status"], acc["equity"], acc["cash"], acc["last_equity"]))
    for pos in api(base, "GET", "positions"):
        print("Position %s: %s Stück zu %s, jetzt %s, offen %s" % (
            pos["symbol"], pos["qty"], pos["avg_entry_price"], pos["current_price"], pos["unrealized_pl"]))
    for o in api(base, "GET", "orders?status=open&nested=true"):
        print("Offen: %s %s %s %s (%s)" % (o["side"], o["qty"], o["symbol"], o["type"], o["id"]))
    clock = api(base, "GET", "clock")
    print("Markt %s, nächste Öffnung %s, nächster Schluss %s" % (
        "offen" if clock["is_open"] else "zu", clock["next_open"], clock["next_close"]))
    return 0


def rest_body(order):
    """place_stock_order-Felder (flach, wie der MCP-Server) in die Form der REST-API bringen:
    Bracket-Beine verschachtelt als take_profit / stop_loss."""
    body = T.tool_input(order)
    tp = body.pop("take_profit_limit_price", None)
    sl = body.pop("stop_loss_stop_price", None)
    sll = body.pop("stop_loss_limit_price", None)
    if tp is not None:
        body["take_profit"] = {"limit_price": tp}
    if sl is not None:
        body["stop_loss"] = {"stop_price": sl}
        if sll is not None:
            body["stop_loss"]["limit_price"] = sll
    return body


def retry_ok(state, fp, today, risk):
    """Eine gescheiterte Order darf erneut raus, wenn trader-risk sie danach noch einmal geprüft hat."""
    rec = T.latest(state, fp, today)
    if not rec or rec.get("status") != "failed" or not risk:
        return False
    try:
        checked = datetime.datetime.fromisoformat(str(risk.get("checked_at", "")).replace("Z", "+00:00"))
        failed = datetime.datetime.fromisoformat(str(rec.get("at", "")))
    except ValueError:
        return False
    return checked > failed


def cmd_place(a):
    p = paths()
    cfg = load_cfg(p)
    base = guard(cfg)
    now, today = T._clock(a)
    orders = T.read_json(p["orders"], "orders")
    orders = orders.get("orders", orders) if isinstance(orders, dict) else orders
    risk = T.read_json(p["risk"], "risk check", required=False)
    state = T.load_state(p["state"])
    order = T._pick(orders, a.index)
    ready, label, rv = T.status_of(order, risk, state, today)
    if not ready and rv and rv.get("verdict") == "PASS" and retry_ok(state, T.fingerprint(order), today, risk):
        ready = True
    if not ready:
        raise AutoError("Order %d nicht bereit: %s" % (a.index, label))
    loss, stop = T.max_loss(order)
    rec = {"at": T.ny_iso(now), "date": today, "index": a.index, "fingerprint": T.fingerprint(order),
           "symbol": str(order.get("symbol", "")).upper(), "side": order.get("side"),
           "qty": order.get("qty"), "kind": T.kind_of(order, rv), "max_loss": loss, "stop": stop,
           "plain": T.plain(order), "status": "approved", "reply": REPLY,
           "paper": True, "broker": "alpaca"}
    state.setdefault("orders", []).append(rec)
    T.write_json(p["state"], state)
    done = {k: rec[k] for k in ("date", "index", "fingerprint", "symbol", "side", "plain",
                                "qty", "kind", "max_loss", "stop") if rec.get(k) is not None}
    try:
        res = api(base, "POST", "orders", rest_body(order))
    except AutoError as e:
        state["orders"].append(dict(done, at=T.ny_iso(T.parse_now(None)), status="failed", note=str(e)[:300]))
        T.write_json(p["state"], state)
        raise
    state["orders"].append(dict(done, at=T.ny_iso(T.parse_now(None)), status="placed",
                                broker_order_id=res["id"]))
    T.write_json(p["state"], state)
    print("Platziert (Paper): %s, Alpaca-ID %s, Status %s" % (T.plain(order), res["id"], res["status"]))
    why = order.get("why") or ""
    notify("🟢 **Order platziert (Paper)**\n%s\nmax. Verlust am Stop: %s $%s" % (
        T.plain(order), loss if loss is not None else "?", ("\nWarum: " + why) if why else ""))
    print("Danach: paper_auto.py sync, sobald gefüllt; dann journal.py write")
    return 0


def cmd_sync(a):
    """Gefüllte Orders von heute (Einstieg und Bracket-Beine) ins Protokoll und Portfolio übernehmen."""
    p = paths()
    cfg = load_cfg(p)
    base = guard(cfg)
    now, today = T._clock(a)
    seen = {r.get("alpaca_fill_id") for r in T.load_state(p["state"]).get("orders", [])}
    flat = []
    for o in api(base, "GET", "orders?status=closed&nested=true&limit=200&after=%sT04:00:00Z" % today):
        flat.append(o)
        flat.extend(o.get("legs") or [])
    new = 0
    for o in sorted(flat, key=lambda o: o.get("filled_at") or ""):
        if o.get("status") != "filled" or o["id"] in seen:
            continue
        T.apply_fill(p["portfolio"], cfg, o["symbol"], o["side"], o["filled_qty"],
                     o["filled_avg_price"], today)
        state = T.load_state(p["state"])
        state.setdefault("orders", []).append({
            "at": T.ny_iso(now), "date": today, "status": "filled", "symbol": o["symbol"],
            "side": o["side"], "qty": o["filled_qty"], "price": float(o["filled_avg_price"]),
            "alpaca_fill_id": o["id"], "filled_at": o.get("filled_at"),
            "plain": "%s %s %s at %s" % (o["side"].upper(), o["filled_qty"], o["symbol"],
                                         T._p(o["filled_avg_price"]))})
        T.write_json(p["state"], state)
        print("Fill erfasst: %s %s %s zu %s (%s)" % (o["side"], o["filled_qty"], o["symbol"],
                                                    o["filled_avg_price"], o.get("filled_at")))
        notify("%s **Ausgeführt:** %s %s %s zu %s $" % ("📥" if o["side"] == "buy" else "📤",
               "Kauf" if o["side"] == "buy" else "Verkauf", o["filled_qty"], o["symbol"], o["filled_avg_price"]))
        new += 1
    if not new:
        print("Keine neuen Fills.")
    return 0


def cmd_flatten(a):
    """Offene Orders des Symbols streichen und die Position glattstellen (nur Paper)."""
    p = paths()
    base = guard(load_cfg(p))
    positions = api(base, "GET", "positions")
    if a.symbol:
        positions = [x for x in positions if x["symbol"] == a.symbol.upper()]
    if not positions:
        print("Nichts offen.")
        return 0
    for pos in positions:
        sym = pos["symbol"]
        for o in api(base, "GET", "orders?status=open&nested=true&symbols=" + sym):
            api(base, "DELETE", "orders/" + o["id"])
            print("Gestrichen: %s %s %s (%s)" % (o["side"], o["qty"], sym, o["id"]))
        res = api(base, "DELETE", "positions/" + sym)
        print("Glattstellung %s: %s Stück, Order %s" % (sym, pos["qty"], (res or {}).get("id")))
        notify("🔴 **Glattstellung** %s: %s Stück, offen %s $" % (sym, pos["qty"], pos["unrealized_pl"]))
    print("Danach: paper_auto.py sync, dann journal.py write oder close")
    return 0


def report_text(base):
    """Stand aller offenen Positionen: Kurs, Stop, Ziel, P&L, R. None, wenn nichts offen ist."""
    positions = api(base, "GET", "positions")
    if not positions:
        return None
    legs, opened, entries, realized = {}, {}, 0, 0.0
    for o in api(base, "GET", "orders?status=all&nested=true&limit=100&after=%s" %
                 datetime.date.today().isoformat()):
        if o.get("order_class") != "bracket" or o.get("status") != "filled":
            continue
        entries += 1
        if o.get("filled_at"):
            t = datetime.datetime.fromisoformat(o["filled_at"][:19] + "+00:00")
            opened[o["symbol"]] = max(opened.get(o["symbol"], t), t)
        for l in o.get("legs") or []:
            if l.get("status") == "filled":
                realized += (float(l["filled_avg_price"]) - float(o["filled_avg_price"])) * float(l["filled_qty"])
            if l.get("status") in ("new", "held", "accepted", "partially_filled"):
                key = "stop" if l["type"] in ("stop", "stop_limit") else "target"
                legs.setdefault(o["symbol"], {})[key] = float(l.get("stop_price") or l.get("limit_price"))
    acc = api(base, "GET", "account")
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-4)))
    lines = ["📊 **Stand %s NY**" % now.strftime("%H:%M")]
    unreal = sum(float(p["unrealized_pl"]) for p in positions)
    day = float(acc["equity"]) - float(acc["last_equity"])
    at_risk = sum(max(0.0, (float(p["avg_entry_price"]) - legs.get(p["symbol"], {}).get("stop", float(p["avg_entry_price"])))
                      * float(p["qty"])) for p in positions)
    lines.append("📋 **Übersicht:** %d offen · Trades heute %d · Risiko am Stop gesamt %.0f $ · offen %+.2f $ · "
                 "realisiert %+.2f $" % (len(positions), entries, at_risk, unreal, realized))
    for p in positions:
        t = opened.get(p["symbol"])
        if t:
            mins = int((now - t).total_seconds() // 60)
            lines.append("• %s seit %s NY (%d h %02d min)" % (p["symbol"], t.astimezone(now.tzinfo).strftime("%H:%M"),
                                                           mins // 60, mins % 60))
    for p in positions:
        sym, qty = p["symbol"], float(p["qty"])
        entry, cur = float(p["avg_entry_price"]), float(p["current_price"])
        pl, plpc = float(p["unrealized_pl"]), float(p["unrealized_plpc"]) * 100
        lg = legs.get(sym, {})
        stop, target = lg.get("stop"), lg.get("target")
        parts = ["**%s** %g Stück, Einstieg %.2f, jetzt %.2f" % (sym, qty, entry, cur),
                 "P&L **%+.2f $** (%+.2f %%)" % (pl, plpc)]
        if stop:
            r = (cur - entry) / (entry - stop) if entry > stop else 0
            parts.append("Stop %.2f (%.2f %% entfernt, max. Verlust %.0f $)" % (
                stop, (cur - stop) / cur * 100, (entry - stop) * qty))
            parts.append("aktuell %+.2f R" % r)
        if target:
            parts.append("Ziel %.2f (%.2f %% entfernt, Gewinn dort %.0f $)" % (
                target, (target - cur) / cur * 100, (target - entry) * qty))
        lines.append(" · ".join(parts))
    lines.append("Konto %.0f $, heute %+.2f $" % (float(acc["equity"]), float(acc["equity"]) - float(acc["last_equity"])))
    return "\n".join(lines)


def cmd_report(a):
    """Stand an Discord; mit --every N alle N Minuten bis --until (holt dabei neue Fills)."""
    p = paths()
    base = guard(load_cfg(p))
    hh, mm = map(int, a.until.split(":"))
    ny = datetime.timezone(datetime.timedelta(hours=-4))
    while True:
        cmd_sync(a)
        text = report_text(base)
        if text:
            print(text)
            notify(text)
        else:
            print("Keine offene Position.")
        if not a.every:
            return 0
        now = datetime.datetime.now(ny)
        if now.time() >= datetime.time(hh, mm):
            return 0
        nxt = now + datetime.timedelta(minutes=a.every)
        time.sleep(max(60, (nxt - datetime.datetime.now(ny)).total_seconds()))


def cmd_say(a):
    """Freie Nachricht an Discord, z. B. Tageszusammenfassung oder Grund für keinen Trade."""
    print("An Discord geschickt." if notify(a.text) else "Nicht geschickt (kein DISCORD_WEBHOOK_URL oder Fehler).")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Autonomer Paper-Ausführer (nur Alpaca Paper).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    say = sub.add_parser("say")
    say.add_argument("text")
    for name in ("status", "place", "sync", "flatten", "report"):
        s = sub.add_parser(name)
        s.add_argument("--now", help='New Yorker Zeit, z. B. "2026-10-22 10:15"')
        s.add_argument("--today")
        if name == "place":
            s.add_argument("--index", type=int, required=True)
        if name == "flatten":
            s.add_argument("--symbol")
        if name == "report":
            s.add_argument("--every", type=float, help="Minuten zwischen Meldungen (ohne: einmal)")
            s.add_argument("--until", default="15:55", help="New Yorker Zeit, bis wann gemeldet wird")
    a = ap.parse_args(argv)
    try:
        return {"status": cmd_status, "place": cmd_place, "sync": cmd_sync, "flatten": cmd_flatten,
                "say": cmd_say, "report": cmd_report}[a.cmd](a)
    except (AutoError, T.TicketError) as e:
        print("Abgebrochen: %s" % e)
        return 2


if __name__ == "__main__":
    sys.exit(main())
