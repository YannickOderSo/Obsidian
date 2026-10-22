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

# Pullback im Trend

Ein Pullback-Trade kauft in einem bestehenden Aufwärtstrend nach einem kurzen Rücksetzer, statt dem Kurs am Hoch hinterherzulaufen. Typische Marken sind die EMA 9 und EMA 20, der VWAP oder das letzte höhere Tief. Die Idee ist alt und überall verbreitet. Für genau diese Regeln gibt es aber kaum harte Evidenz.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Idee

Ein Trend ist eine Folge von höheren Hochs und **höheren Tiefs**. Wer im Rücksetzer kauft, bekommt einen besseren Preis und kann den Stop knapp unter das letzte höhere Tief legen. Gelingt der Trade, ist das Chance-Risiko-Verhältnis besser als beim Kauf am Ausbruch. Scheitert er, zeigt der Bruch des höheren Tiefs früh, dass der Trend vorbei sein könnte.

## Bausteine

| Baustein | Übliche Regel |
| --- | --- |
| Trend erkennen | Kurs über EMA 20, EMA 9 über EMA 20, beide steigen; höhere Hochs und höhere Tiefe; Kurs über dem VWAP |
| Trendstärke (optional) | ADX(14) über 30 und steigend (Raschke/Connors „Holy Grail“) |
| Rücksetzer | einige Bars gegen den Trend; Faustregel aus der Praxis: mit weniger Volumen als die Aufwärtsbars (nicht belegt) |
| Unterstützung | EMA 9 (schnelle Trends), EMA 20 (stärkere Marke), VWAP, altes Ausbruchsniveau |
| Einstieg | über dem Hoch der ersten Kerze, die wieder nach oben dreht (nicht in die fallende Kerze hinein) |
| Stop | unter dem Tief des Rücksetzers bzw. unter dem letzten höheren Tief; Aziz: einige Cent unter dem gleitenden Durchschnitt |
| Ziel | altes Hoch des Tages, 2R, oder nachziehen, bis die EMA 9 oder 20 bricht |

> [!info] EMA kurz erklärt
> Der exponentielle gleitende Durchschnitt (EMA) gewichtet die letzten Kurse stärker als ein einfacher Durchschnitt (SMA) und reagiert deshalb schneller. Auf dem 5-Minuten-Chart deckt die EMA 20 etwa die letzten 100 Minuten ab. Mehr in [[Indikatoren]].

### Varianten aus der Literatur

- **Aziz, „Moving Average Trend Trade“**: Eine Aktie mit hohem Volumen („Stock in Play“) bildet am späten Vormittag einen Trend entlang der EMA 9. Gekauft wird, wenn die EMA 9 oder 20 als Unterstützung hält und die Aktie über dem VWAP bleibt. Der Stop liegt knapp unter dem Durchschnitt, gehalten wird, bis die EMA bricht. Die EMA 20 gilt ihm als stärkere Marke.
- **Raschke/Connors, „Holy Grail“** (*Street Smarts*, 1995): ADX(14) über 30 als Zeichen eines starken Trends, Rücksetzer bis an den 20er-Durchschnitt, Kaufauftrag über dem Hoch der Kerze, die ihn berührt. Sekundärquellen sind sich uneinig, ob ein SMA oder EMA gemeint ist.
- **Bull Flag** ist ein Sonderfall: steiler Anstieg, dann eine enge, leicht fallende Konsolidierung. Siehe [[Bull Flag]].

## Evidenz

> [!warning] Überwiegend Erfahrungswissen
> Eine wissenschaftliche Studie zu „Kauf am Rücksetzer an die EMA 9/20 im Intraday-Chart“ haben wir **nicht gefunden**. Die Regeln stammen aus Büchern und Blogs, belegt meist mit ausgewählten Beispielcharts. Wer so etwas codiert, berichtet oft ernüchternde Ergebnisse.

Was die Forschung in der Nähe sagt:

- **Gleitende-Durchschnitt-Regeln allgemein**: Brock, Lakonishok und LeBaron (1992) fanden auf rund 100 Jahren Dow-Jones-Daten Erfolge einfacher Durchschnitts-Regeln. Sullivan, Timmermann und White (1999) prüften solche Regeln in großer Zahl mit einer Korrektur für Data Snooping. Bajgrowicz und Scaillet (2008) zeigten im selben Rahmen: Ein Anleger hätte die künftig besten Regeln nicht im Voraus auswählen können, und nach Transaktionskosten verschwindet der Vorteil ganz. Das betrifft Tagesdaten des Dow, nicht Intraday-Pullbacks. Siehe [[Evidenz zu technischer Analyse]] und [[Backtesting und Overfitting]].
- **Intraday-Trend vs. Durchschnitt**: Im VWAP-Paper von Zarattini und Aziz schnitten Trendregeln mit einfachen Durchschnitten (9 bis 200 Perioden, 1-Minuten-Bars, QQQ) schlechter ab als die VWAP-Regel. Kürzere Durchschnitte hatten höhere Trefferquoten, aber kleinere Gewinne je Treffer. Siehe [[VWAP-Strategien]].
- **Intraday-Momentum**: Morgen-Bewegungen im S&P-500-ETF setzen sich bis zur letzten halben Stunde leicht fort (Gao, Han, Li, Zhou 2018). Das spricht dafür, an Trendtagen mit dem Trend zu handeln, sagt aber nichts über die beste Einstiegsmarke.

Fazit: Pullback-Regeln sind ein vernünftiges Werkzeug, um im Trend günstiger einzusteigen und den Stop eng zu setzen. Dass die EMA 9 oder 20 eine „magische“ Unterstützung ist, ist nicht belegt.

## Beispielrechnung mit unseren Limits

Fiktive Aktie im Aufwärtstrend seit dem Morgen. Um 11:20 fällt sie an die EMA 20 (5-Min) bei $25,10 zurück. Das letzte höhere Tief liegt bei $24,95. Der nächste Bar dreht und schließt bei $25,30.

| Größe | Rechnung | Wert |
| --- | --- | --- |
| Einstieg (über dem Hoch der Wendekerze) | | $25,30 |
| Stop (unter dem höheren Tief) | | $24,89 |
| Risiko je Aktie | 25,30 − 24,89 | $0,41 |
| Stückzahl | floor(50 / 0,41) = 121; Cap floor(3.750 / 25,30) = 148 | 121 Aktien |
| Position | 121 × 25,30 | $3.061 |
| Max. Verlust am Stop | 121 × 0,41 | $49,61 |
| Ziel 2R | 25,30 + 0,82 | $26,12 |

> [!tip] Ziel mit dem Tageshoch abgleichen
> Liegt das Tageshoch schon bei $25,60, ist ein 2R-Ziel bei $26,12 nur mit einem neuen Hoch erreichbar. Dann lieber 1R bzw. das Tageshoch als Ziel prüfen, solange das Mindest-CRV von 1,0 erfüllt ist. Siehe [[R-Multiple und Erwartungswert]] und [[Unterstützung und Widerstand]].

## Häufige Fehler

- „Rücksetzer“ kaufen, die in Wahrheit Trendwenden sind: Bricht das letzte höhere Tief, ist der Trend nach der eigenen Definition vorbei.
- In die fallende Kerze kaufen statt auf die Wendekerze zu warten.
- Seitwärtsmärkte: Wenn EMA 9 und EMA 20 flach liegen und sich ständig kreuzen, gibt es keinen Trend, den man zurücksetzen sehen könnte.
- Zu spät am Tag: Nach 15:00 bleibt wenig Zeit bis zum Flat-Zeitpunkt 15:55.

## Im Vault

- **Kein Pullback-Setup im Scanner.** `/trader-scanner daily` hat `reclaim_ma20` (Schlusskurs gestern unter dem 20-Tage-Durchschnitt, heute darüber). Das ist ein Tages-Signal, ein Rücksprung über den Durchschnitt nach einem Rücksetzer, aber kein Intraday-Pullback an die EMA. Für Aktien mit Tagestrend ist es ein möglicher Startpunkt der Watchlist.
- **Einstieg halbautomatisch**: Das Hoch der Wendekerze selbst ablesen und mit `/trader-entry TICKER --setup level --level <Hoch>` auf einen Schlusskurs darüber warten. Die Skills rechnen keine EMA.
- **Stop**: `/trader-exit --stop price:<unter dem höheren Tief>`. Der Skill rundet nach unten auf den Cent und lehnt ein Risiko unter 0,05 % des Kurses als zu eng ab.
- **Zeitfenster**: Pullbacks entstehen typischerweise nach dem ersten Schub, also oft nach 10:00. Das passt gut zu „Einstiege 9:45 bis 15:30“.
- **`/trader-timemachine`** prüft auch Level-Pläne. Die Quoten basieren auf den 60 letzten Tagen der Aktie, nicht auf der Pullback-Situation.
- Vergleich: [[Strategien im Vergleich]].

## Quellen

- Aziz, How to Day Trade for a Living (Zitate: EMA 9/20 als Unterstützung, VWAP halten, Stop knapp unter dem Durchschnitt) – https://www.goodreads.com/work/quotes/52463925 und https://www.goodreads.com/author/show/15708710.Andrew_Aziz
- Trading Setups Review: The Holy Grail Trading Setup (Raschke/Connors, ADX > 30, Rücksetzer an den 20er-Durchschnitt) – https://tradingsetupsreview.com/the-holy-grail-trading-setup
- Capital.com: Holy Grail trading strategy (ADX und 20er-Durchschnitt, SMA- oder EMA-Variante) – https://capital.com/en-gb/learn/trading-strategies/holy-grail-trading-strategy
- Sullivan, Timmermann, White (1999): Data-Snooping, Technical Trading Rule Performance, and the Bootstrap, Journal of Finance – https://www.fmg.ac.uk/publications/discussion-papers/data-snooping-technical-trading-rule-performance-and-bootstrap
- Bajgrowicz, Scaillet (2008): Technical Trading Revisited: Persistence Tests, Transaction Costs, and False Discoveries (EFMA 2008) – https://www.efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2008-Athens/papers/Bajgrowicz.pdf
- Zarattini, Aziz (2023): VWAP – The Holy Grail for Day Trading Systems (Vergleich mit SMA-Regeln) – https://concretumgroup.com/wp-content/uploads/2026/02/Volume-Weighted-Average-Price.pdf
- Gao, Han, Li, Zhou (2018): Market intraday momentum – https://profiles.wustl.edu/en/publications/market-intraday-momentum/
- Skills im Vault: `.claude/skills/trader-scanner/SKILL.md`, `trader-entry/SKILL.md`, `trader-exit/SKILL.md`
