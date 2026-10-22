---
typ: wissen
erstellt: 2026-10-22
aktualisiert: 2026-10-22
quelle: Recherche
tags:
  - trading
  - wissen
  - strategien
---

# Mean Reversion und Oversold Bounce

Mean Reversion setzt darauf, dass ein Kurs nach einem starken Fall wieder Richtung Durchschnitt zurückläuft. Der bekannteste Ansatz ist Larry Connors' RSI(2). Kurzfristige Umkehrungen sind wissenschaftlich gut belegt, aber vor allem über mehrere Tage und vor Kosten. Für einen Day Trade mit Stop und „flat bis 15:55“ passt das nur eingeschränkt.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Idee

Fällt eine Aktie in kurzer Zeit stark, ohne dass sich an der Firma viel geändert hat, verkaufen oft Leute, die schnell raus wollen oder müssen. Wer dann kauft, stellt Liquidität bereit und wird dafür im Schnitt mit einer Gegenbewegung bezahlt. So deutet Nagel (2012) die kurzfristige Umkehr: als Prämie für Liquidität, die in Krisen besonders hoch ist.

Gegen den Trend zu kaufen heißt aber auch, „in ein fallendes Messer zu greifen“. Ein Kurs, der wegen schlechter Nachrichten fällt, kann weiter fallen. Siehe [[Katalysatoren]].

## Maße für „überverkauft“

| Maß | Rechnung | übliche Schwelle |
| --- | --- | --- |
| RSI(14) nach Wilder | Verhältnis der Auf- zu Abwärtsbewegungen der letzten 14 Schlusskurse, 0 bis 100 | unter 30 |
| RSI(2) nach Connors | dasselbe mit nur 2 Perioden, reagiert extrem schnell | unter 10, strenger unter 5 |
| Abstand zum Durchschnitt | Kurs vs. 5-, 10- oder 20-Tage-Durchschnitt, in % oder in ATR | z. B. 2 ATR unter dem 20er |
| Serie von Verlusttagen | z. B. drei tiefere Schlusskurse in Folge | Connors-Varianten wie „R3“ |

Mehr zum RSI: [[Indikatoren]].

## Die RSI(2)-Regeln von Connors

So beschreibt StockCharts die Regeln (Connors und Alvarez, *Short Term Trading Strategies That Work*, 2008):

1. **Trendfilter**: Kurs über dem 200-Tage-Durchschnitt (SMA 200). Nur dann long.
2. **Signal**: RSI(2) unter 10; Connors fand unter 5 bessere Ergebnisse.
3. **Einstieg**: kurz vor Handelsschluss (Connors) oder am nächsten Morgen (flexibler, aber mit Gap-Risiko).
4. **Ausstieg**: Schlusskurs über dem 5-Tage-Durchschnitt (SMA 5).
5. **Stop**: Connors lehnt Stops ab. In seinen Tests verschlechterten Stops die Ergebnisse bei Aktien und Indizes. StockCharts warnt, dass das zu großen Verlusten und Drawdowns führen kann.

> [!warning] Zwei harte Konflikte mit unseren Regeln
> - **Haltedauer**: Der Ausstieg über dem SMA 5 kommt typischerweise nach einem bis mehreren Tagen. Unsere Regeln verlangen flat bis 15:55, keine Übernacht-Position.
> - **Kein Stop**: Bei uns ist ein Stop Pflicht (`require_stop`). Mit Stop ist es eine andere Strategie, und die Zahlen von Connors gelten dafür nicht.

## Evidenz

### Gut belegt: kurzfristige Umkehr im Querschnitt

- **Jegadeesh (1990)** und **Lehmann (1990)**: Aktien, die in einem Monat bzw. einer Woche am stärksten gefallen sind, entwickeln sich in der Folgeperiode im Schnitt besser als die Gewinner. Häufig zitiert werden für die Monatsstrategie rund 2 % pro Monat (1934 bis 1987), für die Wochenstrategie rund 1,8 % pro Woche, beides **brutto**.
- **Kosten fressen viel davon**: Mehrere Arbeiten (Kaul und Nimalendran 1990, Conrad, Kaul und Nimalendran 1991, Ball, Kothari und Wasley 1995) zeigen, dass ein Großteil der Wochen-Umkehr innerhalb des Geld-Brief-Spreads liegt. Avramov, Chordia und Goyal (2006) führen die Umkehr auf Handelsfriktionen zurück.
- **Nagel (2012)**: Die Rendite der Umkehrstrategie lässt sich mit dem VIX vorhersagen. Sie ist in Phasen von Marktstress am höchsten.

### Mittel belegt: RSI(2) auf Indizes

- Ein Backtest (Backtrex) der Long- und Short-Regeln auf dem S&P 500, Oktober 2016 bis Oktober 2026, mit 0,02 % Kommission je Seite: **73 Trades in zehn Jahren, Trefferquote 71 %**, Profit-Faktor 1,43, Gesamtrendite +18,1 % gegenüber +255 % für Kaufen und Halten. Durchschnittlicher Gewinn 1,22 %, durchschnittlicher Verlust 2,10 %.
- Auf Nasdaq 100 und DAX war die Regel ebenfalls positiv, aber schwächer als Kaufen und Halten. Auf EUR/USD war sie negativ.
- Das typische Profil: **hohe Trefferquote, kleine Gewinne, seltene große Verluste.** Genau das Gegenteil von ORB und VWAP-Trend.
- LuxAlgo betont: Die Tests von Connors sind Geschichte einer Stichprobe, kein Naturgesetz. Eine unabhängige wissenschaftliche Prüfung von RSI(2) auf Einzelaktien haben wir nicht gefunden.

### Schwach belegt: Oversold Bounce als Day Trade

Für „Aktie ist auf Tagesbasis überverkauft, heute intraday kaufen und bis 15:55 schließen“ haben wir **keine Studie** gefunden. Die Umkehr-Evidenz bezieht sich auf Wochen und Monate oder auf mehrtägige RSI(2)-Trades.

## Beispielrechnung mit unseren Limits

Fiktive Aktie: gestern RSI(14) bei 27, heute im Plus (Setup `oversold_bounce`). Gestern Hoch $61,40. Ein 5-Min-Bar schließt um 10:20 bei $61,50 über dem Vortageshoch.

| Größe | Rechnung | Wert |
| --- | --- | --- |
| Stop (unter dem Tagestief) | | $60,70 |
| Risiko je Aktie | 61,50 − 60,70 | $0,80 |
| Stückzahl | floor(50 / 0,80) = 62; Cap floor(3.750 / 61,50) = 60 | **60 Aktien** (Cap entscheidet) |
| Max. Verlust am Stop | 60 × 0,80 | $48,00 |
| Ziel 1R | 61,50 + 0,80 | $62,30 |

> [!tip] Warum hier 1R statt 2R
> Mean Reversion lebt von häufigen kleinen Gewinnen. Ein fernes Ziel widerspricht der Idee: Der Kurs soll nur zurück Richtung Durchschnitt laufen. 1R erfüllt das Mindest-CRV von 1,0, braucht aber über 50 % Treffer nach Kosten. Ob das intraday gelingt, ist offen. Siehe [[R-Multiple und Erwartungswert]].

## Im Vault

- **`/trader-scanner daily`** hat zwei passende Setups, beide auf **RSI 14 (Wilder)**, nicht auf RSI(2):
  - `oversold`: RSI 14 unter 30.
  - `oversold_bounce`: RSI 14 war gestern unter 30, heute schloss höher.
  Ein Trendfilter über dem SMA 200 wie bei Connors fehlt. Viele Treffer sind deshalb Aktien im Abwärtstrend, also genau die, die Connors ausschließt.
- **Der Daily-Scan läuft auf Schlusskursen.** Vor der Eröffnung zeigt `oversold_bounce` also die Bewegung von gestern. Heute kann das schon vorbei sein.
- **Einstieg**: Es gibt keinen eigenen Mean-Reversion-Trigger. Möglich ist `/trader-entry --setup level --level <z. B. Vortageshoch>` oder ein ORB auf einem überverkauften Wert. Beides macht aus der Umkehr-Idee einen Ausbruch.
- **Stop ist Pflicht** (`/trader-exit` mit `price:X`, `pct:X` oder `atr:K`), anders als bei Connors.
- **`/trader-news` zuerst**: Wer fällt, fällt oft aus gutem Grund. Prüfen, ob eine Gewinnwarnung, ein Offering oder eine Klage dahintersteht ([[News richtig lesen]]).
- Für das Swing-Original (mehrere Tage halten) sind unsere Skills nicht gebaut. Vergleich: [[Strategien im Vergleich]].

## Quellen

- StockCharts ChartSchool: RSI(2) (Connors-Regeln, SMA 200, Ausstieg SMA 5, Haltung zu Stops) – https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/rsi-2
- Backtrex: Does the RSI(2) strategy work on the S&P 500? (Backtest 2016–2026) – https://backtrex.com/en/backtests/connors-rsi-2-sp-500
- Backtrex: Connors RSI(2) auf dem Nasdaq 100 – https://backtrex.com/en/backtests/connors-rsi-2-nasdaq-100
- LuxAlgo: RSI 2 (Schwellen, Connors und Alvarez 2008, Vorbehalte) – https://www.luxalgo.com/library/concept/rsi-2/
- Nagel (2012): Evaporating Liquidity, Review of Financial Studies 25(7) – https://ideas.repec.org/a/oup/rfinst/v25y2012i7p2005-2039.html
- EFMA 2011 (Braga), Arbeitspapier zur kurzfristigen Umkehr mit Literaturüberblick zu Kosten (Kaul/Nimalendran, Conrad et al., Ball et al., Avramov et al.) – https://efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2011-Braga/papers/0259_update.pdf
- Alpha Architect: Short-Term Return Reversal (Jegadeesh 1990, Lehmann 1990) – https://alphaarchitect.com/quantitative-momentum-research-short-term-return-reversal/
- Skills im Vault: `.claude/skills/trader-scanner/SKILL.md` und `scan.py` (Funktion `find_setups`)
