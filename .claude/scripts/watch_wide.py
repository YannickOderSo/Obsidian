#!/usr/bin/env python3
"""Breiter Beobachter für den Paper-Autopiloten: viele Charts, zwei feste Setups.

Prüft nach jedem 5-Minuten-Schluss für jedes Symbol
  orb           erste Kerze nach 9:45, die über dem Hoch der ersten 15 Minuten schließt
  vortageshoch  erste Kerze, die über dem Hoch des Vortags schließt (nur wenn heute
                noch keine Kerze darüber geschlossen hat und die Eröffnung darunter lag)
und meldet nur frische Signale (die gerade geschlossene Kerze). Bei einem Signal:
Ausgabe, trader/wide_hits.json schreiben, Exit 0. Um --until ohne Signal: Exit 1.
Kauft nichts.

    python3 .claude/scripts/watch_wide.py --symbols AAPL,DHR --until 11:30 [--seen COF:orb,MRK:orb]
    python3 .claude/scripts/watch_wide.py --from-watchlist trader/watchlist.full.json --top 40 --until 11:30
"""

import argparse
import datetime
import json
import os
import sys
import time
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
try:
    from zoneinfo import ZoneInfo
    NY = ZoneInfo("America/New_York")
except Exception:  # ohne Zeitzonendaten: Sommerzeit-Abstand
    NY = datetime.timezone(datetime.timedelta(hours=-4))


def bars(sym):
    url = "https://query1.finance.yahoo.com/v8/finance/chart/%s?interval=5m&range=5d" % sym
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    r = json.load(urllib.request.urlopen(req, timeout=15))["chart"]["result"][0]
    q = r["indicators"]["quote"][0]
    out = []
    for i, t in enumerate(r.get("timestamp") or []):
        if None in (q["open"][i], q["high"][i], q["low"][i], q["close"][i]):
            continue
        dt = datetime.datetime.fromtimestamp(t, NY)
        out.append({"t": dt, "o": q["open"][i], "h": q["high"][i], "l": q["low"][i], "c": q["close"][i]})
    return out


def signals(sym, now):
    b = bars(sym)
    today = now.date()
    td = [x for x in b if x["t"].date() == today and x["t"].time() >= datetime.time(9, 30)]
    prev_days = sorted({x["t"].date() for x in b if x["t"].date() < today})
    if not td or not prev_days:
        return []
    prev = [x for x in b if x["t"].date() == prev_days[-1]
            and datetime.time(9, 30) <= x["t"].time() < datetime.time(16, 0)]
    done = [x for x in td if x["t"] + datetime.timedelta(minutes=5) <= now]
    if len(done) < 4:
        return []
    last = done[-1]
    rng = done[:3]
    or_hi, or_lo = max(x["h"] for x in rng), min(x["l"] for x in rng)
    out = []
    after = done[3:]
    first = next((x for x in after if x["c"] > or_hi), None)
    if first is last:
        out.append({"symbol": sym, "setup": "orb", "time": last["t"].strftime("%H:%M"), "price": round(last["c"], 2),
                    "level": round(or_hi, 2), "or_high": round(or_hi, 2), "or_low": round(or_lo, 2)})
    pdh = max(x["h"] for x in prev) if prev else None
    if pdh and done[0]["o"] < pdh:
        first = next((x for x in done if x["c"] > pdh), None)
        if first is last:
            out.append({"symbol": sym, "setup": "vortageshoch", "time": last["t"].strftime("%H:%M"),
                        "price": round(last["c"], 2), "level": round(pdh, 2),
                        "or_high": round(or_hi, 2), "or_low": round(or_lo, 2)})
    return out


def tradable(min_free):
    """Ist nach der Reserve aus der Config noch genug Bargeld für einen Kauf frei? Im Zweifel ja."""
    if not min_free:
        return True
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import paper_auto as P
        cfg = P.load_cfg(P.paths())
        acc = P.api(P.guard(cfg), "GET", "account")
        free = float(acc["cash"]) - float(acc["equity"]) * float(cfg.get("cash_buffer_pct", 10)) / 100
        return free >= min_free
    except Exception:
        return True


def pick(path, top, skip):
    d = json.load(open(path))
    keep = {"breakout_20d", "bull_flag", "reclaim_ma20"}
    hits = [h for h in d["hits"] if set(h.get("setups", [])) & keep and 45 <= (h.get("rsi") or 0) <= 72
            and h["symbol"] not in skip]
    hits.sort(key=lambda h: -(h.get("price", 0) * h.get("volume", 0)))
    return [h["symbol"] for h in hits[:top]]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbols")
    ap.add_argument("--from-watchlist")
    ap.add_argument("--top", type=int, default=40)
    ap.add_argument("--skip", default="", help="Symbole, die nicht beobachtet werden (z. B. Zahlen heute)")
    ap.add_argument("--seen", default="", help="SYM:setup, schon bewertet")
    ap.add_argument("--until", default="11:30")
    ap.add_argument("--min-free", type=float, default=5000,
                    help="Signale nur melden, wenn nach der Reserve so viel Bargeld frei ist (0: immer)")
    ap.add_argument("--out", default=os.path.join(ROOT, "trader", "wide_hits.json"))
    a = ap.parse_args(argv)
    skip = {s.strip().upper() for s in a.skip.split(",") if s.strip()}
    syms = [s.strip().upper() for s in a.symbols.split(",")] if a.symbols else pick(a.from_watchlist, a.top, skip)
    seen = {s.strip() for s in a.seen.split(",") if s.strip()}
    hh, mm = map(int, a.until.split(":"))
    print("Beobachte %d Charts bis %s NY: %s" % (len(syms), a.until, " ".join(syms)), flush=True)
    while True:
        now = datetime.datetime.now(NY)
        if now.time() >= datetime.time(hh, mm):
            print("%s: bis %s kein frisches Signal." % (now.strftime("%H:%M"), a.until))
            return 1
        found = []
        for s in syms:
            try:
                found += [x for x in signals(s, now) if "%s:%s" % (x["symbol"], x["setup"]) not in seen]
            except Exception as e:  # ein Chart ohne Daten hält die anderen nicht auf
                print("  %s: %s" % (s, str(e)[:80]), flush=True)
        if found and not tradable(a.min_free):
            for x in found:
                seen.add("%s:%s" % (x["symbol"], x["setup"]))
                print("%s: Signal %s %s ohne freies Bargeld, nur notiert." % (
                    now.strftime("%H:%M"), x["symbol"], x["setup"]), flush=True)
            found = []
        if found:
            json.dump({"at": now.isoformat(), "hits": found}, open(a.out, "w"), indent=2)
            for x in found:
                print("SIGNAL %s %s %s: Schluss %.2f über %.2f (Eröffnungsbereich %.2f bis %.2f)" % (
                    x["time"], x["symbol"], x["setup"], x["price"], x["level"], x["or_low"], x["or_high"]))
            return 0
        print("%s: %d Charts geprüft, kein frisches Signal." % (now.strftime("%H:%M"), len(syms)), flush=True)
        nxt = now.replace(second=20, microsecond=0) + datetime.timedelta(minutes=5 - now.minute % 5)
        time.sleep(max(30, (nxt - datetime.datetime.now(NY)).total_seconds()))


if __name__ == "__main__":
    sys.exit(main())
