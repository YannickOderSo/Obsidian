---
typ: entscheidung
erstellt: 2026-10-22
aktualisiert: 2026-10-22
quelle: Gespräch
tags:
  - entscheidung
  - trading
---

# Autonomes Paper Trading

## Entscheidung

[[Yannick]] lässt Claude auf dem Alpaca-Paper-Konto (100.000 $ Spielgeld) selbstständig handeln, die Trades dokumentieren und daraus lernen. Das Ja je Order entfällt nur im Paper-Betrieb; mit echtem Geld gilt es weiter.

- Orders nur über `.claude/scripts/paper_auto.py`: bricht ab, wenn `"paper"` nicht true ist oder der Endpunkt nicht `paper-api.alpaca.markets`.
- Jede Order braucht vorher ein PASS von `trader-risk` gegen die Limits in [[Trading/Regeln]].
- Limits: 1.000 $ Verlust je Trade als Obergrenze, 2.500 $ je Tag, CRV mindestens 1,5. Risiko wird je Setup abgewogen, nicht ausgereizt.
- Jeder Trade landet im Journal, Lehren in [[Gedächtnis/Erkenntnisse/Trading]].

## Warum

Experiment: Lernt ein Ablauf aus Scanner, Time Machine und Risikoprüfung über Wochen etwas, das sich in der Statistik zeigt? Mit Spielgeld kostet ein Fehler nichts.
