#!/usr/bin/env python3
"""Stündliche Marktanalyse für Discord (Paper-Autopilot).

Regelbasiert, ohne Claude: Indizes, Marktbreite der beobachteten Charts, stärkste und
schwächste Werte der letzten Stunde und der Verlauf der offenen Positionen, jeweils mit
Tagesänderung, Änderung in der letzten Stunde und Lage zum VWAP.

    python3 .claude/scripts/market_report.py                     # einmal, nur ausgeben
    python3 .claude/scripts/market_report.py --send --every 60 --until 16:00
"""

import argparse
import datetime
import json
import os
import sys
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paper_auto as P  # noqa: E402
import watch_wide as W  # noqa: E402

NY = W.NY
INDEX = [("SPY", "S&P 500"), ("QQQ", "Nasdaq 100"), ("DIA", "Dow"), ("IWM", "Russell 2000")]


def series(sym):
    url = "https://query1.finance.yahoo.com/v8/finance/chart/%s?interval=5m&range=5d" % sym
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    r = json.load(urllib.request.urlopen(req, timeout=15))["chart"]["result"][0]
    q = r["indicators"]["quote"][0]
    rows = []
    for i, t in enumerate(r.get("timestamp") or []):
        if None in (q["close"][i], q["high"][i], q["low"][i]):
            continue
        rows.append((datetime.datetime.fromtimestamp(t, NY), q["high"][i], q["low"][i], q["close"][i],
                     q["volume"][i] or 0))
    return rows


def stats(sym, now):
    rows = series(sym)
    today = [r for r in rows if r[0].date() == now.date() and r[0].time() >= datetime.time(9, 30)]
    before = [r for r in rows if r[0].date() < now.date() and r[0].time() < datetime.time(16, 0)]
    if not today or not before:
        return None
    prev_close, last = before[-1][3], today[-1][3]
    hour_ago = [r for r in today if r[0] <= now - datetime.timedelta(minutes=60)]
    ref = hour_ago[-1][3] if hour_ago else today[0][3]
    pv = sum((r[1] + r[2] + r[3]) / 3 * r[4] for r in today)
    vol = sum(r[4] for r in today)
    vwap = pv / vol if vol else None
    return {"sym": sym, "last": last, "day": (last / prev_close - 1) * 100, "hour": (last / ref - 1) * 100,
            "hi": max(r[1] for r in today), "lo": min(r[2] for r in today), "vwap": vwap}


def vw(s):
    if not s["vwap"]:
        return ""
    return "über VWAP" if s["last"] >= s["vwap"] else "unter VWAP"


def mood(spy, breadth):
    if spy is None:
        return "keine Indexdaten"
    up_h, above = spy["hour"] > 0.05, spy["vwap"] and spy["last"] >= spy["vwap"]
    if up_h and above and breadth >= 0.55:
        return "Käufer haben die Oberhand: Index steigt in der letzten Stunde, über VWAP, Breite positiv."
    if spy["hour"] < -0.05 and not above and breadth <= 0.45:
        return "Verkäufer dominieren: Index fällt in der letzten Stunde, unter VWAP, Breite negativ."
    return "Gemischt: kein klarer Trend in der letzten Stunde, Ausbrüche eher vorsichtig behandeln."


def build(watch_syms, base):
    now = datetime.datetime.now(NY)
    idx = {}
    lines = ["🕐 **Marktanalyse %s NY**" % now.strftime("%H:%M"), "**Indizes**"]
    for sym, name in INDEX:
        try:
            s = stats(sym, now)
        except Exception:
            s = None
        if s:
            idx[sym] = s
            lines.append("• %s (%s): %+.2f %% heute, %+.2f %% letzte Stunde, %s" % (name, sym, s["day"], s["hour"], vw(s)))
    rows = []
    for sym in watch_syms:
        try:
            s = stats(sym, now)
        except Exception:
            s = None
        if s:
            rows.append(s)
    breadth = sum(1 for s in rows if s["day"] > 0) / len(rows) if rows else 0.5
    if rows:
        rows.sort(key=lambda s: s["hour"])
        lines.append("**Beobachtete Charts** (%d): %d im Plus, %d im Minus, %d über VWAP" % (
            len(rows), sum(1 for s in rows if s["day"] > 0), sum(1 for s in rows if s["day"] <= 0),
            sum(1 for s in rows if s["vwap"] and s["last"] >= s["vwap"])))
        lines.append("• stärkste Stunde: " + ", ".join("%s %+.2f %%" % (s["sym"], s["hour"]) for s in rows[::-1][:3]))
        lines.append("• schwächste Stunde: " + ", ".join("%s %+.2f %%" % (s["sym"], s["hour"]) for s in rows[:3]))
    try:
        positions = P.api(base, "GET", "positions")
    except Exception:
        positions = []
    if positions:
        lines.append("**Offene Positionen**")
        for p in positions:
            try:
                s = stats(p["symbol"], now)
            except Exception:
                s = None
            if not s:
                continue
            rng = (s["last"] - s["lo"]) / (s["hi"] - s["lo"]) * 100 if s["hi"] > s["lo"] else 50
            lines.append("• %s %.2f: %+.2f %% heute, %+.2f %% letzte Stunde, %s, steht bei %.0f %% der Tagesspanne "
                         "(%.2f bis %.2f), P&L %+.2f $" % (p["symbol"], s["last"], s["day"], s["hour"], vw(s), rng,
                                                          s["lo"], s["hi"], float(p["unrealized_pl"])))
    lines.append("**Einordnung:** " + mood(idx.get("SPY"), breadth))
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-watchlist", default=os.path.join(P.ROOT, "trader", "watchlist.full.json"))
    ap.add_argument("--top", type=int, default=60)
    ap.add_argument("--skip", default="")
    ap.add_argument("--send", action="store_true", help="an Discord schicken")
    ap.add_argument("--every", type=float, help="Minuten zwischen Analysen (ohne: einmal)")
    ap.add_argument("--until", default="16:00")
    a = ap.parse_args(argv)
    base = P.guard(P.load_cfg(P.paths()))
    skip = {s.strip().upper() for s in a.skip.split(",") if s.strip()}
    syms = W.pick(a.from_watchlist, a.top, skip)
    hh, mm = map(int, a.until.split(":"))
    while True:
        text = build(syms, base)
        print(text, flush=True)
        if a.send:
            P.notify(text)
        if not a.every:
            return 0
        now = datetime.datetime.now(NY)
        nxt = (now + datetime.timedelta(minutes=a.every)).replace(second=30, microsecond=0)
        if a.every == 60:
            nxt = nxt.replace(minute=0)
        if (nxt.hour, nxt.minute) > (hh, mm) or now.time() >= datetime.time(hh, mm):
            return 0
        time.sleep(max(60, (nxt - datetime.datetime.now(NY)).total_seconds()))


if __name__ == "__main__":
    sys.exit(main())
