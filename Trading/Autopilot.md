---
typ: ablauf
erstellt: 2026-10-22
aktualisiert: 2026-10-22
tags:
  - trading
---

# Autopilot (Paper)

Ablauf der geplanten Läufe im autonomen Paper-Experiment ([[2026-10-22 Autonomes Paper Trading]]). Limits in [[Trading/Regeln]], Lehren in [[Gedächtnis/Erkenntnisse/Trading]]. Alle Befehle in der Wurzel des Vaults, `S=.claude/skills`, `A=.claude/scripts/paper_auto.py`. Zeiten New York.

## Immer zuerst

1. `git pull` auf dem Arbeitszweig, [[Gedächtnis/Erkenntnisse/Trading]] und die eigenen Regeln lesen.
2. `python3 $A status`. Ist heute kein Handelstag (Feiertag, Wochenende), nichts tun außer einer Zeile in der Tagesnotiz.
3. Blockiert die Umgebung eine Datenquelle: nichts nachbauen, Lauf mit Vermerk beenden (Adressen im README, „In einer Cloud-Sitzung“).

## 9:22 Vorbereitung

1. `python3 $S/trader-scanner/scan.py daily` (bei Zeitnot `--limit 300`), dann `python3 $S/trader-news/news.py`.
2. Watchlist auf höchstens 5 Kandidaten eingrenzen: klares Setup, genug Volumen, keine Ergebnisse heute, keine schlechten News. Gründe kurz in die Tagesnotiz.
3. Noch in diesem Lauf `watch_wide.py` (siehe Setups) im Hintergrund starten, `--skip` mit den Werten, die heute Zahlen melden oder vorbörslich stark fallen. Er wartet bis zur ersten Kerze nach 9:45 und meldet jedes frische Signal. Grund: Am 2026-10-22 fielen alle 40 Signale der 60 Charts zwischen 9:30 und 10:10; ein Start erst um 10:25 verpasst sie.

## Setups (fest, seit 2026-10-22)

Varianten vorher festgelegt und im Journal getrennt gezählt, damit die Statistik zeigt, was trägt. Nicht bei einem Signal so lange Parameter probieren, bis die Time Machine passt.

| Setup | Einstieg | Stop-Varianten (beide in der Time Machine) | Ziel |
| --- | --- | --- | --- |
| `orb` | erste 5-Min-Kerze, die über dem Hoch der ersten 15 Minuten schließt | Mitte (`or-mid`) und Tief (`or-low`) des Eröffnungsbereichs | 2R |
| `vortageshoch` | erste 5-Min-Kerze, die über dem Hoch des Vortags schließt (`entry.py --setup level --level H`) | dieselben zwei | 2R |

- Gekauft wird höchstens eine Variante je Signal, die mit dem höheren positiven Ø R. Welche, steht im Journal (Setup und Stop-Regel).
- Hat ein Wert die Marke heute schon genommen und wieder verloren, ist das kein Signal mehr (gescheiterter Ausbruch).
- Nach dem 9:52-Lauf beobachtet `python3 .claude/scripts/watch_wide.py --from-watchlist trader/watchlist.full.json --top 60 --skip <Zahlen heute> --seen <SYM:setup schon bewertet> --until 15:30` im Hintergrund die liquidesten 60 Setups (Ausbruch, Bull Flag, über dem 20-Tage-Schnitt, RSI 45 bis 72) auf beide Setups. Ein frisches Signal beendet ihn und weckt den Lauf: News prüfen, bewerten, danach mit erweitertem `--seen` neu starten.
- **Jeden Handelstag von der Eröffnung bis 15:30** (Ende des Einstiegsfensters; Wunsch des Nutzers 2026-10-22). Hintergrundprozesse enden hier nach höchstens 2 Stunden: Bei jeder Beendigung vor 15:30 sofort neu starten, mit denselben Argumenten und dem bisherigen `--seen`.

## 9:52 und 10:47 Einstieg

Nur wenn heute weniger als 3 Trades und das Tagesverlustlimit nicht erreicht.

1. `python3 $S/trader-scanner/scan.py orb --watchlist trader/watchlist.json`, dann `python3 $S/trader-entry/entry.py watchlist`.
2. Je ausgelöstem Kandidat (bester zuerst): `entry.py check SYM --write`, `exit.py plan --write`, `timemachine.py run --until 15:55 --write`.
3. **Abwägen** (Regel „Risiko abwägen statt ausreizen“):
   - Durchschnitts-R der Time Machine ≤ 0 oder Ziel-Quote < Stop-Quote: kein Trade.
   - knapp positiv oder News unklar: halbes Risiko (Kopie der Config mit `max_loss_per_trade_usd` 500 als `trader/config.halb.json`, `size.py --config trader/config.halb.json --write`).
   - klar positiv: `size.py --write`.
4. `python3 $S/trader-risk/check.py`. Nur bei PASS: `python3 $A place --index 1`.
5. `python3 $S/trading-journal/journal.py write`; im Abschnitt Reflexion kurz festhalten, **warum** und mit welchem Risiko.

## Zwischendurch

`python3 $A sync` holt Fills (Einstieg, Stop, Ziel) ins Protokoll; danach `journal.py write`, bei Stop oder Ziel `journal.py close --exit PREIS`.

## 15:47 Schluss

1. `python3 $A sync`, dann `python3 $A flatten` (streicht die Bracket-Beine, verkauft den Rest), `python3 $A sync`.
2. Jeden offenen Trade schließen: `journal.py close --exit PREIS` (Grund `flat`, wenn glattgestellt).
3. Reflexion je Trade: Was war der Plan, was ist passiert, stimmte die Abwägung? `journal.py stats --write`.
4. Erst ein **Muster** über mehrere Trades kommt nach [[Gedächtnis/Erkenntnisse/Trading]]; daraus abgeleitete Regeln nach [[Trading/Regeln]] (Limits in der Config nur mit dem Nutzer).
5. Committen und pushen.

## Discord

Orders, Fills und Glattstellungen meldet `paper_auto.py` selbst, wenn `DISCORD_WEBHOOK_URL` in der Umgebung steht (nie in den Vault). Zusätzlich mit `python3 $A say "…"`: nach 9:22 die Kandidaten, nach jedem Einstiegslauf die Entscheidung mit Grund (auch „kein Trade, weil …“), nach 15:47 die Tageszusammenfassung (Trades, R, Tages-P&L, Kontostand).
