---
typ: wissen
erstellt: 2026-10-22
aktualisiert: 2026-10-22
quelle: Recherche
tags:
  - trading
  - wissen
  - risiko
---

# Drawdown und Risk of Ruin

Ein Drawdown ist der Rückgang vom bisherigen Höchststand des Kontos, Risk of Ruin die Wahrscheinlichkeit, eine Verlustgrenze zu erreichen, von der man sich nicht erholt. Diese Notiz zeigt mit Tabellen und Simulationen, warum normale Verlustserien länger sind, als man denkt, und was das für $50 je Trade bei $5.000 heißt.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Begriffe

- **Drawdown** = (Höchststand − aktueller Stand) ÷ Höchststand.
- **Max Drawdown** = der größte Drawdown über einen Zeitraum.
- **Ruin** = ein vorher festgelegter Punkt, an dem man aufhört, z. B. −50 % oder „Konto leer“. Bei Fixed-Fractional-Größen (immer x % des Kontos) wird das Konto rechnerisch nie ganz null; deshalb braucht Risk of Ruin immer eine **Schwelle**.

## Erholungstabelle

Nach einem Verlust von *d* braucht man *d* ÷ (1 − *d*) Gewinn, um zurückzukommen:

| Verlust | nötiger Gewinn zur Erholung | bei $5.000 Start |
| --- | --- | --- |
| −5 % | +5,3 % | $4.750 → $5.000 |
| −10 % | +11,1 % | $4.500 |
| −20 % | +25,0 % | $4.000 |
| −25 % | +33,3 % | $3.750 |
| −30 % | +42,9 % | $3.500 |
| −40 % | +66,7 % | $3.000 |
| −50 % | +100 % | $2.500 |
| −60 % | +150 % | $2.000 |
| −75 % | +300 % | $1.250 |
| −90 % | +900 % | $500 |

Eigene Rechnung. Die Asymmetrie ist der Kern des Risikomanagements: Kleine Verluste sind leicht aufzuholen, große kaum.

## Verlustserien sind normal

Wahrscheinlichkeit, **mindestens einmal** eine Serie von *k* oder mehr Verlusten in Folge zu erleben (exakt gerechnet, unabhängige Trades):

**Verlustquote 50 %** (z. B. 1R-Ziel mit 50 % Treffern)

| Trades | ≥ 3 | ≥ 4 | ≥ 5 | ≥ 6 | ≥ 8 | ≥ 10 |
| --- | --- | --- | --- | --- | --- | --- |
| 20 | 78,7 % | 47,8 % | 25,0 % | 12,2 % | 2,7 % | 0,6 % |
| 50 | 98,3 % | 82,7 % | 55,2 % | 31,5 % | 8,4 % | 2,0 % |
| 100 | 100 % | 97,3 % | 81,0 % | 54,6 % | 17,0 % | 4,4 % |
| 250 | 100 % | 100 % | 98,6 % | 86,8 % | 38,4 % | 11,2 % |

**Verlustquote 65 %** (z. B. 2R-Ziel mit 35 % Treffern, etwa Break-even)

| Trades | ≥ 3 | ≥ 4 | ≥ 5 | ≥ 6 | ≥ 8 | ≥ 10 |
| --- | --- | --- | --- | --- | --- | --- |
| 20 | 96,5 % | 82,0 % | 60,6 % | 41,0 % | 16,4 % | 6,1 % |
| 50 | 100 % | 99,0 % | 92,4 % | 77,8 % | 42,3 % | 19,1 % |
| 100 | 100 % | 100 % | 99,5 % | 95,7 % | 69,0 % | 36,8 % |
| 250 | 100 % | 100 % | 100 % | 100 % | 95,2 % | 70,0 % |

**Erwartete längste Verlustserie** (Simulation, 20.000 Läufe, Seed 19):

| Verlustquote | 50 Trades | 100 Trades | 250 Trades |
| --- | --- | --- | --- |
| 40 % | 3,9 | 4,6 | 5,6 |
| 50 % | 5,0 | 6,0 | 7,3 |
| 60 % | 6,5 | 7,9 | 9,6 |
| 65 % | 7,6 | 9,1 | 11,2 |

Eigene Rechnung. Die Größenordnung deckt sich mit der Faustregel von Schilling, nach der die längste Kopf-Serie in *n* fairen Münzwürfen etwa log₂(*n* ÷ 2) beträgt ([Schilling 1990, über MAA](https://maa.org/node/113688), [John D. Cook](https://www.johndcook.com/blog/2012/11/14/probability-of-long-runs/)).

> [!tip] Was das praktisch heißt
> Mit einem 2R-Setup und 35 % Treffern sind **acht Verluste in Folge** in 100 Trades wahrscheinlicher als nicht (69 %). Bei $50 je Trade sind das −$400 oder −8 %, ohne dass irgendetwas „kaputt“ ist. Wer das vorher weiß, ändert nicht nach fünf Verlusten panisch die Regeln.

## Risk of Ruin: Formeln

**Klassischer Gambler's Ruin.** Gewinn und Verlust gleich groß (1R gegen 1R), Trefferquote *p* > 0,5, *q* = 1 − *p*, Startkapital *u* Einheiten. Die Wahrscheinlichkeit, irgendwann alle *u* Einheiten zu verlieren, ist bei unbegrenztem Spiel **(q ÷ p)^u**. Sie folgt als Grenzfall aus der Ruin-Formel für zwei Spieler ([Wikipedia: Gambler's ruin](https://en.wikipedia.org/wiki/Gambler%27s_ruin)). Bei *p* ≤ 0,5 ist der Ruin auf Dauer sicher.

Mit unseren Zahlen: $5.000 ÷ $50 = **100 Einheiten** bis Konto leer, 50 Einheiten bis −50 %.

| Trefferquote bei 1:1 | Ruin bis −50 % (u = 50) | Konto leer (u = 100) |
| --- | --- | --- |
| 50 % oder weniger | auf Dauer sicher | auf Dauer sicher |
| 51 % | 13,5 % | 1,8 % |
| 52 % | 1,8 % | 0,03 % |
| 55 % | 0,004 % | ≈ 0 |

Eigene Rechnung. In Trading-Foren kursiert die Variante ((1 − Edge) ÷ (1 + Edge))^Einheiten, die Kaufman bzw. Vince zugeschrieben wird ([NexusFi](https://nexusfi.com/a/risk-management/risk-of-ruin)). Sie beruht auf denselben Annahmen: gleich große Gewinne und Verluste, feste Größe, unabhängige Trades. Echte Trades verletzen alle drei.

> [!warning] Die Formel ist zu optimistisch
> Sie kennt keine Kosten, keine Slippage, keine Gaps über den Stop, keine Verlustserien durch Marktphasen und vor allem **keinen Schätzfehler**: Wer 52 % Treffer „gemessen“ hat, kennt die wahre Quote nur auf ±10 Punkte genau (siehe [[R-Multiple und Erwartungswert]]). Liegt sie in Wahrheit bei 50 %, ist der Ruin auf Dauer sicher.

## Simulation mit unserem Konto

$5.000 Start, fester Max-Verlust $50 je Trade, 0,05R Kosten je Trade, 250 Trades (etwa ein Jahr mit einem Trade je Tag), 20.000 Läufe, Seed 19. Eigene Rechnung.

| Setup | Erwartung je Trade | Max-DD ≥ 10 % | Max-DD ≥ 20 % | Max-DD ≥ 50 % | Ende unter $5.000 | Median Ende |
| --- | --- | --- | --- | --- | --- | --- |
| 1R, 45 % Treffer | −0,15R | 99,8 % | 95,5 % | 28,3 % | 99,2 % | $3.075 |
| 1R, 50 % Treffer | −0,05R | 95,2 % | 59,3 % | 1,6 % | 79,7 % | $4.375 |
| 1R, 55 % Treffer | +0,05R | 65,6 % | 11,9 % | 0 % | 22,4 % | $5.575 |
| 2R, 35 % Treffer | 0,00R | 96,4 % | 58,1 % | 3,2 % | 50,3 % | $4.925 |
| 2R, 40 % Treffer | +0,15R | 71,4 % | 13,2 % | 0 % | 5,3 % | $6.875 |

Und dasselbe 1R-Setup mit 50 % bzw. 55 % Treffern, aber mit **Prozent-Risiko vom aktuellen Konto** statt $50 fest:

| Risiko je Trade | 50 %: Max-DD ≥ 50 % | 50 %: Median Ende | 55 %: Max-DD ≥ 50 % | 55 %: Median Ende |
| --- | --- | --- | --- | --- |
| 1 % | 0,1 % | $4.357 | 0 % | $5.540 |
| 2 % | 22,3 % | $3.703 | 1,2 % | $5.988 |
| 5 % | 92,9 % | $1.953 | 57,9 % | $6.509 |
| 10 % | 100 % | $401 | 99,2 % | $4.516 |

Lehren daraus:

1. **Ohne positiven Erwartungswert hilft kein Risikomanagement.** Es bestimmt nur, wie schnell das Geld weg ist.
2. **Selbst mit Vorteil** (55 % bei 1R) erlebt man mit 1 % Risiko in zwei von drei Jahren einen Drawdown von 10 % oder mehr.
3. **Zu großes Risiko zerstört auch einen echten Vorteil**: Bei 10 % je Trade endet das 55-%-Setup im Median unter dem Start. Das ist der Bereich jenseits des [[Kelly-Kriterium|Kelly-Anteils]].

Grenzen der Simulation: unabhängige Trades, nur zwei Ausgänge (keine Flat-Ausgänge um 15:55), feste Kosten, keine Gaps. Echte Ergebnisse streuen stärker.

## Im Vault

- **Max-Verlust je Trade** ($50 = 1 % bei Start) begrenzt jeden einzelnen Schritt; **Tageslimit** $150 und **3 Trades/Tag** begrenzen die Serie an einem Tag ([[Tageslimits und Regelwerk]]). Ein Wochen- oder Gesamt-Drawdown-Limit gibt es in `trader/config.json` nicht. Eine eigene Regel wie „bei −10 % ($500) Pause und Auswertung“ könnte der Nutzer in [[Trading/Regeln]] unter „Eigene Regeln“ festhalten; die Skills prüfen sie nicht.
- **`/trading-journal stats`** zeigt Trefferquote und R; den Drawdown muss man daraus selbst ablesen.
- **`/trader-timemachine`** simuliert einen einzelnen Trade, nicht die Folge vieler Trades. Für Serien und Drawdowns gelten die Tabellen hier.
- Paper Trading ist der richtige Ort, eine echte Verlustserie zu erleben, bevor echtes Geld dranhängt ([[Paper Trading bei Alpaca]]).

## Quellen

- [Wikipedia: Gambler's ruin](https://en.wikipedia.org/wiki/Gambler%27s_ruin) – Ruin-Formel für zwei Spieler
- [NexusFi: Risk of Ruin](https://nexusfi.com/a/risk-management/risk-of-ruin) – Trader-Formel und ihre Annahmen (Forum, Sekundärquelle)
- [Schilling (1990): The Longest Run of Heads, MAA](https://maa.org/node/113688) und [John D. Cook: Probability of long runs](https://www.johndcook.com/blog/2012/11/14/probability-of-long-runs/)
- [MacLean, Thorp, Ziemba (2010): Good and bad properties of the Kelly criterion](https://www.stat.berkeley.edu/~aldous/157/Papers/Good_Bad_Kelly.pdf) – zu großer Einsatz senkt Wachstum und erhöht Drawdowns
- Alle Tabellen (Erholung, Serien, Ruin, Simulation): eigene Rechnung in Python, Seed 19, reproduzierbar
