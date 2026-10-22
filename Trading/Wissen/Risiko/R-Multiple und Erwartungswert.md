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

# R-Multiple und Erwartungswert

R misst jeden Trade in Vielfachen des geplanten Risikos, der Erwartungswert sagt, ob eine Regel über viele Trades Geld bringt oder kostet. Diese Notiz erklärt beides mit unseren Zahlen und zeigt, wie Spread und Slippage ein knappes Setup ins Minus drehen.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## R: das geplante Risiko als Maßeinheit

**1R = Einstieg − Stop** (je Aktie) oder, in Dollar, Stückzahl × (Einstieg − Stop). Der Begriff „R-Multiple“ wurde vor allem durch Van K. Tharp verbreitet; der Durchschnitt aller R-Multiples einer Regel ist ihre **Expectancy** ([Van Tharp Institute](https://vantharp.com/Weekly_update/Weekly_273_May_31_2006.htm)).

| Ausgang | Rechnung | R |
| --- | --- | --- |
| Stop getroffen | (Stop − Einstieg) ÷ R | −1 |
| Ziel bei 2R | (Ziel − Einstieg) ÷ R | +2 |
| Flat um 15:55 bei halbem Weg zum 1R-Ziel | | +0,5 |
| Stop mit $0,50 Slippage, R = 5,86 | (−5,86 − 0,50) ÷ 5,86 | −1,09 |

Warum in R und nicht in Dollar oder Prozent? Weil R Trades vergleichbar macht: Ein $50-Verlust bei TSLA und ein $50-Verlust bei einer $8-Aktie sind beide −1R. So sieht man, ob eine **Regel** funktioniert, unabhängig von Preis und Stückzahl. Unser $50-Limit heißt: 1R ≈ $50 (bei Beispiel TSLA $46,88, siehe [[Positionsgröße]]).

## Erwartungswert

Für eine Regel mit Trefferquote *p*, durchschnittlichem Gewinn *G* und durchschnittlichem Verlust *V* (beide positiv in R):

> **E = p · G − (1 − p) · V**

Mit festem Ziel bei *k*R und Stop bei 1R vereinfacht sich das zu **E = p · k − (1 − p)**. Positiv heißt: Im Schnitt bringt jeder Trade E × R. Bei E = +0,1R und $50 Risiko sind das $5 je Trade, im Schnitt, mit großer Streuung.

**Break-even-Trefferquote** (E = 0): **p = V ÷ (G + V) = 1 ÷ (1 + k)**. Dieselbe Formel nutzt die Time Machine für ihr Urteil („1 in (1 + R)“).

| CRV (Ziel in R) | Break-even-Trefferquote ohne Kosten | mit 0,05R Kosten je Trade | mit 0,1R | mit 0,2R |
| --- | --- | --- | --- | --- |
| 0,5 | 66,7 % | | | |
| 1,0 | 50,0 % | 52,5 % | 55,0 % | 60,0 % |
| 1,5 | 40,0 % | | | |
| 2,0 | 33,3 % | 35,0 % | 36,7 % | 40,0 % |
| 3,0 | 25,0 % | 26,2 % | 27,5 % | 30,0 % |
| 4,0 | 20,0 % | | | |
| 5,0 | 16,7 % | | | |

Rechnung mit Kosten *c* (in R, je Round-Trip): Gewinn = k − c, Verlust = 1 + c, Break-even p = (1 + c) ÷ (k + 1). Eigene Rechnung.

> [!warning] Hohes CRV ist kein Vorteil an sich
> Ein 3R-Ziel braucht nur 25 % Treffer, wird aber auch seltener erreicht. Ob die Rechnung aufgeht, hängt allein davon ab, wie oft das Ziel **wirklich** vor dem Stop kommt. Ein weiteres Ziel verschiebt nur die Messlatte. Deshalb wiegt die Time Machine das R des Ziels schon in ihr Urteil ein, statt „Ziel zuerst“ und „Stop zuerst“ einfach zu vergleichen.

## Kosten und Slippage in R

Kosten zählen nicht in Dollar, sondern im Verhältnis zum Risiko. Dieselben 2 Cent Spread sind bei einem weiten Stop nichts und bei einem engen Stop ein großer Teil von R.

| Fall | R je Aktie | Spread + Slippage je Round-Trip | Kosten in R |
| --- | --- | --- | --- |
| TSLA, Stop an OR-Mitte | 5,86 | angenommen 0,04 | 0,007R |
| $20-Aktie, Stop 2 % | 0,40 | angenommen 0,03 | 0,075R |
| $10-Aktie, enger Stop | 0,10 | angenommen 0,02 | **0,2R** |

Die Spreads sind Annahmen zur Illustration, keine Messwerte. Sie hängen stark von Aktie, Uhrzeit und Volumen ab (siehe [[Spread Liquidität und Slippage]]). Bei 0,2R Kosten braucht ein 1R-Setup schon 60 % Treffer statt 50 %.

Weitere Kosten:

- **Regulatorische Gebühren** auf Verkäufe: SEC-Gebühr $20,60 je Million Dollar seit 4. April 2026 ([SEC](https://www.sec.gov/rules-regulations/fee-rate-advisories/2026-2)), FINRA TAF $0,000195 je Aktie seit 1. Januar 2026 ([Investrade](https://investrade.com/commissions-fees/)). Bei unseren Größen Cent-Beträge. Alpaca gibt sie weiter, verlangt aber keine Kommission ([Alpaca: Regulatory Fees](https://alpaca.markets/support/regulatory-fees)).
- **Slippage am Stop**: Ein Stop wird zur Market-Order und kann unter dem Stop-Preis gefüllt werden ([Alpaca: Orders](https://docs.alpaca.markets/docs/orders-at-alpaca)). Die Time Machine zählt einen Gap über den Stop trotzdem als −1R, ein echter Fill kann schlechter sein.
- **Paper Trading** simuliert weder Market Impact noch Slippage durch Latenz, Queue-Position oder Gebühren ([Alpaca: Paper Trading](https://docs.alpaca.markets/docs/paper-trading)). Paper-Ergebnisse überschätzen also das R echter Trades. Im Journal lohnt es sich, eine Kostenannahme (z. B. 0,05R je Trade) von der Paper-Statistik abzuziehen.

In der Praxis zeigt sich, wie stark Kosten wiegen: In der Studie der indischen Aufsicht SEBI zu Intraday-Tradern (Geschäftsjahr 2022/23) kamen bei den Verlierern zu den Handelsverlusten noch einmal 57 % an Handelskosten hinzu ([Taxscan zur SEBI-Studie](https://www.taxscan.in/7-out-of-10-individual-intraday-traders-in-equity-cash-segment-make-losses-says-sebi/422657)).

## Wie sicher ist eine Trefferquote?

Eine gemessene Trefferquote ist eine Schätzung mit Unsicherheit. Standardfehler bei wahrer Quote um 50 %: √(0,25 ÷ n).

| Anzahl Trades | Standardfehler | grobes 95-%-Intervall |
| --- | --- | --- |
| 20 | 11,2 Punkte | ±22 Punkte |
| 30 | 9,1 Punkte | ±18 Punkte |
| 50 | 7,1 Punkte | ±14 Punkte |
| 100 | 5,0 Punkte | ±10 Punkte |
| 250 | 3,2 Punkte | ±6 Punkte |

Eigene Rechnung (Normalapproximation der Binomialverteilung). Nach 30 Trades mit 55 % Treffern bei 1R ist also noch alles zwischen klar negativ und klar positiv möglich. Das Journal-Skill sagt aus demselben Grund: unter etwa 30 geschlossenen Trades je Setup keine Schlüsse.

> [!tip] Lieber Durchschnitts-R als Trefferquote
> Die Kennzahl, die zählt, ist das **durchschnittliche R je Trade nach Kosten**. Trefferquote und CRV sind nur die zwei Hälften davon. Trades, die bei „flat 15:55“ irgendwo zwischen Stop und Ziel enden, gehen mit ihrem echten R ein.

## Im Vault

- **`/trader-exit`** setzt das Ziel als Vielfaches von R (`2R` Standard, `1R`, `1.5R` oder Preis) und schreibt `risk_per_share` und `reward_risk` nach `trader/plan.json`.
- **`/trader-risk`** blockt, wenn (Ziel − Einstieg) ÷ (Einstieg − Stop) unter `min_reward_risk` (1,0) liegt, gemessen vom höheren Wert aus Plan und frischem Kurs. Ein davongelaufener Kurs verschlechtert das CRV, deshalb wurde im TSLA-Beispiel bei 366,48 ein CRV von 0,44 geblockt.
- **`/trader-timemachine`** gibt „Average R“ aus und urteilt mit der Break-even-Quote 1 ÷ (1 + R) über die Replays, die eine Seite getroffen haben. Im TSLA-Beispiel: 53,6 % Ziel-zuerst unter den getroffenen bei nötigen 50 % → „Close to a coin flip“; die echte Historie hatte −0,062R im Schnitt.
- **`/trading-journal`** speichert `ergebnis_r` je Trade (vom tatsächlichen Einstieg, wenn ein Fill erfasst ist) und rechnet in `Trading/Statistik.md` die Trefferquoten gegen die Quoten der Time Machine.
- Grenze: Kein Skill zieht Kosten oder Slippage vom R ab. Das muss man beim Lesen der Statistik selbst tun.

## Quellen

- [Van Tharp Institute: Weekly Update (R-Multiples, Expectancy)](https://vantharp.com/Weekly_update/Weekly_273_May_31_2006.htm)
- [Alpaca Docs: Orders at Alpaca](https://docs.alpaca.markets/docs/orders-at-alpaca) – Stop wird Market-Order, Fill kann schlechter sein
- [Alpaca Docs: Paper Trading](https://docs.alpaca.markets/docs/paper-trading) – was die Simulation nicht abbildet
- [Alpaca Support: Regulatory Fees](https://alpaca.markets/support/regulatory-fees) – SEC/FINRA-Gebühren werden weitergegeben
- [SEC Fee Rate Advisory 2026-2](https://www.sec.gov/rules-regulations/fee-rate-advisories/2026-2)
- [Investrade: Commissions & Fees](https://investrade.com/commissions-fees/) – FINRA TAF 2026 (Sekundärquelle)
- [Taxscan: 7 out of 10 individual intraday traders make losses, says SEBI](https://www.taxscan.in/7-out-of-10-individual-intraday-traders-in-equity-cash-segment-make-losses-says-sebi/422657) – Kosten als Anteil der Verluste
- `.claude/skills/trader-timemachine/SKILL.md`, `trader-exit/SKILL.md`, `trader-risk/SKILL.md`, `trading-journal/SKILL.md`
- Tabellen zu Break-even, Kosten und Standardfehler: eigene Rechnung
