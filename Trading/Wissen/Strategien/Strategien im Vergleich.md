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

# Strategien im Vergleich

Die sechs Long-Strategien aus diesem Ordner nebeneinander: Idee, Regeln, was die Quellen zur Trefferquote sagen, ob sie zu unseren Limits passen und welcher Skill sie abdeckt. Am Ende steht eine Lernempfehlung, mit welcher **einen** Strategie man das Üben beginnt. Das ist keine Anlageberatung.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Überblick: Regeln

| Strategie | Idee | Zeitfenster | Einstieg | Stop | Ziel |
| --- | --- | --- | --- | --- | --- |
| [[Opening Range Breakout]] | Ungleichgewicht der Eröffnung setzt sich fort | erstes Signal ab 9:50 (15-Min-Range) | 5-Min-Bar schließt über dem Range-Hoch | Range-Mitte oder -Tief | 2R |
| [[Momentum und Gap and Go]] | Nachricht + Gap + Volumen treiben weiter | klassisch direkt nach 9:30 | über dem Pre-Market-Hoch | Tief der Ausbruchskerze | 2R oder schnelle Teilgewinne |
| [[VWAP-Strategien]] | Käufer des Tages im Plus, Institutionen stützen den VWAP | ganzer Tag | Schluss zurück über dem VWAP oder Abprall daran | unter dem Test-Tief / VWAP | 2R oder Tageshoch |
| [[Pullback im Trend]] | im Trend nach Rücksetzer günstiger einsteigen | meist ab 10:00 | über dem Hoch der Wendekerze an EMA 9/20 | unter dem höheren Tief | 2R oder Tageshoch |
| [[Mean Reversion und Oversold Bounce]] | starke Verluste laufen teilweise zurück | Original: Schluss bis mehrere Tage | RSI(2) < 5–10 über SMA 200 | Connors: keiner | Schluss über SMA 5 |
| [[Breakout aus 20-Tage-Hoch]] | neue Hochs ziehen Trends nach sich | Original: Wochen bis Monate | über dem 20-Tage-Hoch | Turtle: 2 × Tages-ATR | 10-Tage-Tief (Trailing) |

## Überblick: Evidenz, Limits, Skills

| Strategie | Trefferquote laut Quellen | Evidenz | passt zu unseren Limits? | Skill |
| --- | --- | --- | --- | --- |
| Opening Range Breakout | 17–27 % je Trade bei den besten Aktien (Studie: Stop 10 % ATR, Halten bis Schluss); QQQ-Variante etwa 24 % | **mittel**: zwei Papers, große Stichprobe, aber ohne Spread/Slippage und ohne Out-of-Sample; Nachrechnung auf Indizes netto ≈ 0 | **ja**, 15-Min-Range passt zu 9:45; 5-Min-Variante der Studie nicht | `/trader-scanner orb`, `/trader-entry`, `/trader-exit` (vollständig) |
| Gap and Go | keine belastbare Zahl gefunden | **schwach**: nur Kurse und Einzelfälle; Index-Studie: Gaps setzen sich eher fort | **eingeschränkt**: Einstieg vor 9:45 verboten, Scanner ab $5, Handelsstopps sprengen das $50-Limit | kein Gap-Scanner; `/trader-news`, `/trader-entry --setup level` |
| VWAP | 17 % je Trade (QQQ, long und short, Halten bis Schluss) | **mittel bis schwach**: ein Paper, ein Markt, Kosten zu niedrig; Reclaim/Pullback bei Aktien unbelegt | **teilweise**: ab 9:45 statt 9:31, nur long, VWAP selbst ablesen | kein VWAP im Skill; `/trader-entry --setup level` |
| Pullback im Trend | keine Zahl gefunden | **schwach**: Erfahrungswissen; MA-Regeln allgemein nach Kosten ohne Vorteil | **ja**, Zeitfenster passt; Level manuell | `/trader-entry --setup level`, `/trader-exit --stop price:X` |
| Mean Reversion (RSI 2) | etwa 71 % (S&P 500, 2016–2026, mehrtägig) | **gut** für Umkehr über Wochen (brutto), **mittel** für RSI(2) auf Indizes, **keine** für Intraday | **schlecht**: Original hält über Nacht und ohne Stop | Scanner `oversold`, `oversold_bounce` (RSI 14, ohne SMA-200-Filter) |
| 20-Tage-Breakout | 43,9 % bei Trendfolge auf Allzeithochs (Monate) | **gut** für Trendfolge über Monate, **keine** für Intraday | **teilweise**: Level-Setup geht, aber flat bis 15:55 schneidet den Trend ab | Scanner `breakout_20d`, `reclaim_ma20`; `/trader-entry --setup level` |

> [!info] Trefferquoten sind nicht vergleichbar
> Die Zahlen stammen aus verschiedenen Märkten, Zeiträumen und Regeln (mit oder ohne Short-Seite, Halten bis Schluss oder mehrere Tage). Eine niedrige Trefferquote ist nicht schlecht, wenn die Gewinner viel größer sind. Entscheidend ist der Erwartungswert in R. Siehe [[R-Multiple und Erwartungswert]].

## Break-even-Trefferquote je Ziel

Wie oft muss man treffen, um ohne Kosten bei null zu landen, wenn Verluste 1R kosten?

| Ziel | Break-even | passt zu |
| --- | --- | --- |
| 1R | 50 % | Mean Reversion |
| 1,5R | 40 % | Pullback, VWAP |
| 2R | 33,3 % | ORB (Standard in `/trader-exit`) |
| 3R | 25 % | Trendtage |

Formel: Break-even = 1 / (1 + Ziel in R). Spread, Slippage und Kommission heben die Schwelle. Bei engen Stops ist der Effekt größer, weil die Kosten einen größeren Teil von 1R ausmachen ([[Spread Liquidität und Slippage]]).

## Gemeinsame Muster

- **Volumen ist der beste Filter, den die Daten hergeben.** In der ORB-Studie war der Schnitt je Trade bei relativem Volumen unter 100 % negativ (−0,02R), darüber positiv (+0,08R), über 3.000 % deutlich höher (+0,38R). Siehe [[Volumen und relatives Volumen]].
- **Die Studien mit großen Zahlen hielten Gewinner bis zum Schluss oder Monate.** Feste Ziele bei 2R und flat bis 15:55 schneiden die seltenen großen Gewinner ab, von denen ORB, VWAP-Trend und Trendfolge leben.
- **Kosten entscheiden.** Mehrere Strategien, die brutto funktionieren, sind netto bei null oder darunter (ORB auf Indizes, technische Regeln auf dem Dow, kurzfristige Umkehr auf Wochenbasis).
- **Die Autoren der stärksten Day-Trading-Papers verkaufen Ausbildung oder Handelssysteme.** Das macht die Ergebnisse nicht falsch, aber es ist ein Grund, die Annahmen genau zu lesen.

## Lernempfehlung: mit einer Strategie anfangen

> [!tip] Empfehlung zum Üben (keine Anlageberatung)
> **Mit dem 15-Minuten-Opening-Range-Breakout anfangen, genau so, wie ihn die Skills umsetzen.**

Warum gerade diese:

1. **Ganz mechanisch.** Nur ORB läuft vollständig durch die Skill-Kette: `/trader-scanner orb` → `/trader-news` → `/trader-entry` → `/trader-exit` (Range-Mitte, 2R) → `/trader-timemachine` → `/trader-budget` → `/trader-risk` → `/trader-broker`. Jede Marke wird gerechnet, nicht geschätzt. So prüft das Journal die Regel und nicht das Bauchgefühl beim Einstieg.
2. **Beste verfügbare Evidenz**, mit klaren Grenzen: zwei Papers über viele Jahre und tausende Aktien. Die Schwächen (Kosten, kein Out-of-Sample, 15 Minuten schwächer als 5) sind bekannt und lassen sich im eigenen Journal überprüfen.
3. **Passt zu den Limits.** Das erste 15-Min-Signal kommt frühestens um 9:50, also nach 9:45. Der Stop an der Range-Mitte steht vor dem Einstieg fest, die Größe folgt aus $50 Risiko. Ein Trade pro Tag reicht.
4. **Klare Ungültigkeit.** Fällt der Kurs unter die Range-Mitte, war der Ausbruch falsch. Es gibt nichts zu interpretieren.
5. **Lehrt das Wichtigste zuerst**: auf einen abgeschlossenen Bar warten, Stop und Ziel vor dem Einstieg setzen, Größe aus dem Risiko rechnen, Verluste als normale 1R-Kosten akzeptieren.

Was dabei ehrlich bleiben muss:

- Unsere Variante (nur long, Einstieg auf Schlusskurs, Stop Range-Mitte, Ziel 2R, flat 15:55) ist **nicht** die Variante der Studie. Ihre Zahlen gelten nicht für uns.
- Der Scanner sortiert nach Dollarvolumen, nicht nach relativem Volumen. Den wichtigsten Filter der Studie muss man selbst prüfen, etwa mit `/trader-entry --min-volume-x 1.5` oder einem Blick auf das Tagesvolumen. Das ist nur eine Annäherung.
- Wie viele Trades zeigen etwas? Bei 20 Trades und einer wahren Trefferquote von 33 % liegt die Standardabweichung der gemessenen Quote bei etwa 10,5 Prozentpunkten (√(0,33 × 0,67 / 20)). 20 Trades können also zufällig wie 23 % oder 43 % aussehen. Vor einem Urteil über die Strategie viele Trades mit **unveränderten** Regeln sammeln; die Journal-Doku nennt etwa 30 je Setup als Untergrenze. Siehe [[Backtesting und Overfitting]].
- Erst wenn die ORB-Routine sitzt, eine zweite Strategie dazunehmen. Naheliegend ist der [[Pullback im Trend]] über dem VWAP, weil er dieselben Werkzeuge (Level-Setup, eigener Stop) nutzt.

## Im Vault

- Jeder Trade kommt nach jedem Schritt ins Journal (`/trading-journal`). Die Skills kennen nur zwei Setup-Namen: `orb` und `level`. Pullback, VWAP, 20-Tage-Breakout und Gap and Go landen alle als `level` im Journal. Welche Strategie es war, deshalb in der Trade-Notiz selbst festhalten. `Trading/Statistik.md` rechnet Trefferquote, R und den Vergleich mit der Time Machine, trennt aber nicht automatisch nach Strategie.
- Die Journal-Skill-Doku sagt: unter etwa 30 geschlossenen Trades je Setup keine Schlüsse ziehen.
- Lehren aus dem Vergleich gehören nach [[Gedächtnis/Erkenntnisse/Trading]], eigene Regeln nach [[Trading/Regeln]] (Abschnitt „Eigene Regeln“).
- Weitere Grundlagen: [[Positionsgröße]], [[Stop-Platzierung]], [[Tageslimits und Regelwerk]], [[Psychologie und Disziplin]], [[Wie viele Day Trader gewinnen]].

## Quellen

Die Einzelbelege stehen in den verlinkten Notizen. Die wichtigsten:

- Zarattini, Barbon, Aziz (2024): A Profitable Day Trading Strategy For The U.S. Equity Market, SSRN 4729284 – https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4729284 (Volltext: https://concretumgroup.com/wp-content/uploads/2026/02/A-Profitable-Day-Trading-Strategy-For-The-U.S.-Equity-Market.pdf)
- Zarattini, Aziz (2023): Can Day Trading Really Be Profitable?, SSRN 4416622 – https://papers.ssrn.com/abstract=4416622
- MQL5-Blog: ORB-Paper auf fünf Indizes nachgerechnet, netto null – https://www.mql5.com/en/blogs/post/776235
- Zarattini, Aziz (2023): VWAP – The Holy Grail for Day Trading Systems, SSRN 4631351 – https://ssrn.com/abstract=4631351 (Volltext: https://concretumgroup.com/wp-content/uploads/2026/02/Volume-Weighted-Average-Price.pdf)
- Backtrex: RSI(2) auf dem S&P 500 (2016–2026) – https://backtrex.com/en/backtests/connors-rsi-2-sp-500
- StockCharts ChartSchool: RSI(2) – https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/rsi-2
- Zarattini, Pagani, Wilcox (2025): Does Trend Following Still Work on Stocks? – https://concretumgroup.com/does-trend-following-still-work-on-stocks/
- Plastun, Sibande, Gupta, Wohar (2020): Price gap anomaly in the US stock market – https://ideas.repec.org/p/pre/wpaper/201963.html
- Bajgrowicz, Scaillet (2008): Technical Trading Revisited – https://www.efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2008-Athens/papers/Bajgrowicz.pdf
- Skills im Vault: `.claude/skills/trader-*/SKILL.md`
