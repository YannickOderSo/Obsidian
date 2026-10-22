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

# Kelly-Kriterium

Das Kelly-Kriterium berechnet, welchen Anteil des Kontos man je Wette einsetzen muss, um das Konto langfristig am schnellsten wachsen zu lassen. Diese Notiz zeigt die Formel, rechnet sie mit unseren Setups durch und erklärt, warum Praktiker nur einen Bruchteil davon nehmen und wir mit 1 % deutlich darunter liegen.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Herkunft

John L. Kelly Jr. veröffentlichte 1956 bei den Bell Labs „A New Interpretation of Information Rate“ ([Bell System Technical Journal, archive.org](https://archive.org/details/bstj35-4-917)). Kern: Wer wiederholt mit einem Vorteil wettet, maximiert das langfristige Wachstum, indem er den **Erwartungswert des Logarithmus** seines Vermögens maximiert. Edward O. Thorp übertrug das auf Blackjack und die Börse ([Thorp: The Kelly Criterion in Blackjack, Sports Betting and the Stock Market](https://sites.oxy.edu/lengyel/M330/thorp/paper.htm)).

## Die Formel für einen Trade mit festem Stop und Ziel

Trefferquote *p*, Verlustquote *q* = 1 − *p*, Gewinn-Verlust-Verhältnis *b* (Ziel in R, Stop = 1R):

> **f\* = p − q ÷ b**

*f\** ist der Anteil des Kontos, der **am Stop verloren** gehen darf, also genau das „Risiko je Trade“ aus [[Positionsgröße]]. Wachstum je Trade: g(f) = p · ln(1 + b·f) + q · ln(1 − f).

| Setup | p | b | Kelly f\* | in $ bei $5.000 |
| --- | --- | --- | --- | --- |
| 1R-Ziel, 50 % Treffer | 0,50 | 1 | **0 %** | $0, kein Vorteil |
| 1R-Ziel, 55 % | 0,55 | 1 | 10,0 % | $500 |
| 1R-Ziel, 60 % | 0,60 | 1 | 20,0 % | $1.000 |
| 2R-Ziel, 35 % | 0,35 | 2 | 2,5 % | $125 |
| 2R-Ziel, 40 % | 0,40 | 2 | 10,0 % | $500 |
| 1,5R-Ziel, 45 % | 0,45 | 1,5 | 8,3 % | $417 |

Eigene Rechnung, ohne Kosten. Mit Kosten sinkt *f\** weiter; ein Setup an der Break-even-Grenze hat Kelly = 0.

## Wachstum bei Bruchteilen von Kelly

Beispiel *p* = 0,55, *b* = 1, *f\** = 10 %. Wachstum relativ zu vollem Kelly und Vielfaches des Kontos nach 250 Trades (idealisiert, ohne Kosten):

| Anteil von Kelly | Risiko je Trade | relatives Wachstum | Faktor nach 250 Trades |
| --- | --- | --- | --- |
| ¼ Kelly | 2,5 % | 44 % | ×1,73 |
| ½ Kelly | 5 % | 75 % | ×2,56 |
| 1 × Kelly | 10 % | 100 % | ×3,50 |
| 1,5 × Kelly | 15 % | 75 % | ×2,54 |
| **2 × Kelly** | 20 % | **≈ 0 %** | ×0,97 |
| 2,5 × Kelly | 25 % | negativ | ×0,19 |

Eigene Rechnung. Das bestätigt zwei bekannte Eigenschaften ([MacLean, Thorp, Ziemba 2010](https://www.stat.berkeley.edu/~aldous/157/Papers/Good_Bad_Kelly.pdf)):

- **Halbes Kelly bringt etwa drei Viertel des Wachstums** bei deutlich kleineren Schwankungen.
- **Bei doppeltem Kelly fällt das Wachstum auf etwa null** (im stetigen Modell genau auf den risikolosen Zins), darüber wird es negativ. Mehr als Kelly lohnt sich nie: mehr Risiko *und* weniger Wachstum.

> [!warning] Auch volles Kelly tut weh
> Die Faktoren oben sind Mediane eines idealen Modells. Die Wege dorthin sind brutal: Bei vollem Kelly fällt das Vermögen mit 50 % Wahrscheinlichkeit irgendwann auf die Hälfte des Starts ([David Aldous, UC Berkeley](https://www.stat.berkeley.edu/~aldous/Top_Ten/slide_10.pdf)). Die Simulation in [[Drawdown und Risk of Ruin]] zeigt dasselbe: 10 % je Trade bei einem 55-%-Setup führt fast sicher zu einem Drawdown über 50 %.

## Warum Bruchteil-Kelly: der Schätzfehler

Kelly setzt voraus, dass *p* und *b* bekannt sind. Beim Trading sind sie **geschätzt**, aus wenigen Trades oder einem Backtest. MacLean, Thorp und Ziemba schreiben, die Rechnung reagiere extrem empfindlich auf Fehler im geschätzten Mittelwert; um sicher zu sein, solle man die Einsätze verkleinern, und Praktiker reduzieren das Risiko stark, wenn der Drawdown wächst ([Good and bad properties](https://www.stat.berkeley.edu/~aldous/157/Papers/Good_Bad_Kelly.pdf)).

Beispiel: Man glaubt an 55 % Treffer bei 1R und setzt deshalb 10 % (volles Kelly) oder 5 % (halbes Kelly). Was nach 250 Trades passiert, wenn die **wahre** Quote niedriger ist (idealisiert, ohne Kosten, eigene Rechnung):

| wahre Trefferquote | volles Kelly (10 %) | halbes Kelly (5 %) | 1 % je Trade |
| --- | --- | --- | --- |
| 55 % (Schätzung stimmt) | ×3,50 | ×2,56 | ×1,27 |
| 53 % | ×1,28 | ×1,55 | ×1,15 |
| 52 % | ×0,78 | ×1,21 | ×1,09 |
| 51 % | ×0,47 | ×0,94 | ×1,04 |
| 50 % | ×0,29 | ×0,73 | ×0,99 |
| 48 % | ×0,10 | ×0,44 | ×0,89 |

Schon wenn die wahre Quote 3 Punkte unter der Schätzung liegt, **verliert** volles Kelly Geld, während kleinere Einsätze noch wachsen. Und 3 Punkte sind weniger als der Standardfehler einer Trefferquote aus 100 Trades (5 Punkte, siehe [[R-Multiple und Erwartungswert]]).

> [!tip] Faustregeln
> - Kelly ist eine **Obergrenze**, kein Ziel.
> - Ohne nachgewiesenen Vorteil über viele Trades ist die ehrliche Kelly-Schätzung **null**.
> - „Fractional Kelly“ tauscht Wachstum gegen Sicherheit ([MacLean, Thorp, Ziemba](https://www.stat.berkeley.edu/~aldous/157/Papers/Good_Bad_Kelly.pdf)). Welcher Bruchteil (oft wird halbes Kelly genannt) richtig ist, ist eine Abwägung, keine Formel.

## Weitere Grenzen

- **Kelly geht von unabhängigen, gleichartigen Wetten aus.** Trades am selben Tag in ähnlichen Aktien sind korreliert.
- **Feste Ausgänge**: Unsere Trades enden nicht nur bei +bR oder −1R, sondern oft „flat um 15:55“ irgendwo dazwischen, und Slippage macht −1R manchmal zu −1,1R.
- **Lange Horizonte**: Der Vorteil von Kelly zeigt sich erst über sehr viele Wetten. MacLean, Thorp und Ziemba nennen ein Münzbeispiel, bei dem zwei Millionen Würfe nötig sind, um mit 84 % Wahrscheinlichkeit einen Vorsprung von 1,1 % gegenüber 1,0 % Vorteil zu sehen.

## Im Vault

- Unser Risiko je Trade ist fest $50, also **1 % des Budgets**. Das ist ein Zehntel von Kelly für ein 55-%-1R-Setup und weniger als Kelly für jedes Setup mit ernsthaftem Vorteil. Für ein Setup ohne nachgewiesenen Vorteil ist Kelly null; dann begrenzen die $50 nur, wie teuer das Lernen wird.
- **`/trader-timemachine`** liefert Quoten aus Simulation und Historie. Die eignen sich **nicht** als *p* für Kelly: Die Replays sind eine Simulation aus 60 Tagen, die Historie umfasst oft nur 20 bis 40 Signale (siehe [[Backtesting und Overfitting]]).
- **`/trading-journal stats`** liefert nach genügend Trades (Faustregel ab 30 je Setup, besser deutlich mehr) eine echte Trefferquote und ein durchschnittliches R. Erst dann ist eine Kelly-Rechnung überhaupt sinnvoll, und auch dann mit Abschlag.
- `max_loss_per_trade_usd` ändert nur der Nutzer in `trader/config.json`; kein Skill passt die Größe an Kelly an.

## Quellen

- [Kelly (1956): A New Interpretation of Information Rate, Bell System Technical Journal 35(4)](https://archive.org/details/bstj35-4-917)
- [Thorp: The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market](https://sites.oxy.edu/lengyel/M330/thorp/paper.htm)
- [MacLean, Thorp, Ziemba (2010): Good and bad properties of the Kelly criterion](https://www.stat.berkeley.edu/~aldous/157/Papers/Good_Bad_Kelly.pdf) – Wachstum null bei 2 × Kelly, Empfindlichkeit gegen Schätzfehler, Zeitbedarf
- [David Aldous: Kelly-Strategie, Folie 10 (UC Berkeley)](https://www.stat.berkeley.edu/~aldous/Top_Ten/slide_10.pdf) – 50 % Chance, bei vollem Kelly zwischenzeitlich auf die Hälfte zu fallen
- Tabellen zu f\*, Bruchteilen und Schätzfehler: eigene Rechnung
