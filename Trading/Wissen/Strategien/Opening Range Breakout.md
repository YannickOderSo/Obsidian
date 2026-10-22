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

# Opening Range Breakout

Der Opening Range Breakout (ORB) kauft, wenn eine Aktie über das Hoch der ersten Minuten des Handelstags ausbricht. Für ORB gibt es die besten Studien aller Strategien hier, und unsere Skills setzen sie von Anfang bis Ende um. Die Notiz zeigt, was die Studien wirklich zeigen und wo sich unsere Variante von ihnen unterscheidet.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Idee in einem Satz

In den ersten Minuten nach 9:30 New York treffen über Nacht angestaute Orders auf den Markt. Bricht der Kurs danach über die Spanne dieser Minuten (die **Opening Range**), deutet das auf einen Überhang an Käufern hin, der den Tag über anhalten kann. So begründen es Zarattini, Barbon und Aziz: Das Ungleichgewicht aus der Eröffnung soll sich in einen Intraday-Trend fortsetzen.

## Definition und Regeln

| Baustein | Übliche Varianten | Unsere Skills (Standard) |
| --- | --- | --- |
| Range-Länge | 5, 15, 30 oder 60 Minuten | 15 Minuten (9:30, 9:35, 9:40 als 5-Min-Bars) |
| Range-Hoch / -Tief | höchstes Hoch / tiefstes Tief der Range-Bars | dito |
| Einstieg | Stop-Order genau am Range-Hoch (Studie) oder Schlusskurs eines Bars über dem Hoch | erster **abgeschlossener** Bar, der **über** dem Range-Hoch schließt |
| Richtung | Studie: long nach grünem, short nach rotem Range-Bar | nur long |
| Stop | 10 % des 14-Tage-ATR (Studie), Range-Tief, Range-Mitte | Range-Mitte (`or-mid`), wahlweise `or-low`, `atr:K`, `pct:X` |
| Ziel | Studie: kein Ziel, Ausstieg zum Schluss (16:00) | 2R (wahlweise 1R oder Preis) |
| Spätester Ausstieg | Handelsschluss | flat bis 15:55 |

> [!info] Was „über dem Hoch schließen“ bedeutet
> Ein Docht über das Range-Hoch mitten im Bar zählt bei `/trader-entry` nicht. Erst wenn der 5-Minuten-Bar fertig ist und sein Schlusskurs über dem Hoch liegt, gilt das Signal. Das filtert manche Fehlausbrüche, macht den Einstieg aber später und teurer als die Stop-Order der Studie.

### Filter für „Stocks in Play“

Die wichtigste Erkenntnis der Studie von 2024: ORB auf beliebigen Aktien bringt fast nichts. Interessant wird es erst bei Aktien mit ungewöhnlich hohem Volumen in der Eröffnung. Die Filter der Studie:

1. Eröffnungskurs über $5
2. durchschnittliches Tagesvolumen der letzten 14 Tage mindestens 1.000.000 Aktien
3. 14-Tage-ATR über $0,50
4. **Relatives Volumen** der Opening Range mindestens 100 %, also Volumen der ersten n Minuten geteilt durch den Schnitt derselben n Minuten der letzten 14 Tage
5. davon nur die 20 Aktien mit dem höchsten relativen Volumen

Mehr zum relativen Volumen: [[Volumen und relatives Volumen]]. Ein Katalysator (Earnings, News) ist oft der Grund für hohes relatives Volumen: [[Katalysatoren]].

## Evidenz

### Toby Crabel (1990)

Crabels Buch *Day Trading with Short Term Price Patterns and Opening Range Breakout* gilt als frühe ausführliche Beschreibung. Seine Range war allerdings keine Spanne der ersten Minuten. Laut Zarattini, Barbon und Aziz kombinierte er die Volatilität der Vortage mit dem Eröffnungskurs, nutzte also keine Intraday-Daten für die Range, und testete das an Futures. Sekundärquellen nennen den Abstand zum Eröffnungskurs „Stretch“; das Original konnten wir nicht prüfen. Die heute übliche Variante misst die Range dagegen direkt in den ersten Minuten des Tages.

### Zarattini und Aziz (2023): ORB auf QQQ

- 5-Minuten-ORB auf QQQ und TQQQ, 2016 bis Februar 2023, long und short, Stop am anderen Ende des ersten 5-Minuten-Bars, Ziel 10R oder Schluss
- Annahmen: bis 4-facher Hebel, $0,0005 Kommission je Aktie, **kein Spread, kein Slippage**
- Trefferquote laut unabhängiger Nachrechnung etwa 24 % je Trade bei rund +0,13R im Schnitt (brutto)

### Zarattini, Barbon und Aziz (2024): ORB auf Stocks in Play

Über 7.000 US-Aktien, 2016 bis 2023, $25.000 Startkapital, $0,0035 Kommission je Aktie, 1 % Risiko je Trade, Hebel bis 4x, long und short.

| Variante | Gesamtrendite | Rendite p. a. | Sharpe | max. Drawdown |
| --- | --- | --- | --- | --- |
| 5-Min-ORB, alle Aktien (Basis) | 29 % | 3,2 % | 0,48 | 13 % |
| 5-Min-ORB + rel. Volumen, Top 20 | 1.637 % | 41,6 % | 2,81 | 12 % |
| 15-Min-ORB + rel. Volumen | 272 % | 17,4 % | 1,43 | 11 % |
| 30-Min-ORB + rel. Volumen | 21 % | 2,3 % | 0,21 | 35 % |
| 60-Min-ORB + rel. Volumen | 39 % | 4,1 % | 0,40 | 21 % |
| S&P 500 Buy and Hold | 198 % | 14,2 % | 0,78 | 34 % |

- Durchschnittlicher Gewinn je Trade nach relativem Volumen: unter 100 % etwa −0,02R, über 100 % etwa +0,08R, über 3.000 % etwa +0,38R.
- Je Trade gewinnt nur eine Minderheit: Selbst bei den besten Einzelaktien liegt die Trefferquote je Trade meist bei 17 bis 27 %. Das Geld kommt aus wenigen großen Gewinnern, die bis zum Schluss laufen. Die „Hit Ratio“ von 48,4 % in der Tabelle der Studie meint nach unserem Verständnis den Portfolio-Tag, nicht den einzelnen Trade. Das Paper sagt das nicht ausdrücklich, deshalb unsicher.

> [!warning] Wie belastbar ist das?
> - **Keine Out-of-Sample-Prüfung.** Beide Papers testen nur einen Zeitraum. Die Autoren betreiben selbst ein Handels- und Ausbildungsgeschäft (Concretum, Bear Bull Traders).
> - **Kosten zu niedrig.** Spread und Slippage fehlen. Eine unabhängige Nachrechnung der QQQ-Regel auf fünf Index-CFDs (2015 bis Juni 2026) reproduziert das Brutto-Ergebnis, findet aber **nach Kosten keinen Markt, der sich von null unterscheidet**, vier von fünf leicht negativ. In 2015 bis 2017 war die Regel in allen Märkten negativ.
> - **Hebel bis 4x** macht aus +0,08R je Trade große Prozentzahlen. Wir handeln ohne Margin.
> - Eine Nachbildung auf QuantConnect kam laut Forum auf ein Sharpe von etwa 2,4. Das ist ein Forumsbeitrag, keine geprüfte Studie.
> - Der Vorteil schrumpft stark mit längerer Range: 30 und 60 Minuten waren kaum besser als nichts.

### Verwandte Evidenz

Gao, Han, Li und Zhou (2018, *Journal of Financial Economics*) fanden für den S&P-500-ETF: Die Rendite vom Vortagesschluss bis 10:00 sagt die Rendite der letzten halben Stunde voraus, besonders an volatilen Tagen und an Tagen mit Makro-News. Das stützt die Idee, dass sich Morgen-Impulse fortsetzen können. Der Effekt ist aber klein (R² um 2 % in einer frühen Fassung) und gilt für den Index, nicht für Einzelaktien.

## Beispielrechnung mit unseren Limits

Echtes Beispiel aus dem Skill (TSLA, 19.10.2026): Range 354,47 bis 362,18, Einstieg 364,18 um 10:15.

| Größe | Rechnung | Wert |
| --- | --- | --- |
| Stop `or-mid` | (362,18 + 354,47) / 2, abgerundet | $358,32 |
| Risiko je Aktie | 364,18 − 358,32 | $5,86 |
| Stückzahl (Limit $50) | floor(50 / 5,86) | 8 Aktien |
| Positionsgröße | 8 × 364,18 | $2.913 (unter Positions-Cap $3.750) |
| Max. Verlust am Stop | 8 × 5,86 | $46,88 |
| Ziel 2R | 364,18 + 2 × 5,86 | $375,90 |

Mit Stop `or-low` (354,47) wäre das Risiko $9,71 je Aktie, also nur 5 Aktien. Ein weiterer Stop heißt nicht mehr Risiko, sondern weniger Aktien: [[Positionsgröße]], [[Stop-Platzierung]].

> [!tip] Rechnung zur Trefferquote
> Bei 2R-Ziel und 1R-Verlust braucht man ohne Kosten mehr als 33,3 % Treffer, um im Plus zu sein (1 / (1 + 2)). Bei 1R-Ziel sind es 50 %. Spread und Slippage schieben die Schwelle nach oben. Siehe [[R-Multiple und Erwartungswert]].

## Typische Fehler

- Ausbruch auf dünnem Volumen kaufen: Laut Studie lag genau dort der Schnitt unter null.
- Zu spät kaufen: Ein Signal, das schon mehrere Bars alt ist, ist ein anderer Trade, denn Einstieg und Risiko haben sich verschoben.
- Stop nach dem Einstieg weiter weg schieben. Das verbietet auch `/trader-exit`.
- Am ersten Ausbruch eines Tages ohne Plan nachkaufen, wenn er scheitert.

## Im Vault

- **`/trader-scanner orb`** (nach 9:50): sucht in allen oder ausgewählten Aktien den ersten 5-Min-Bar, der über dem 15-Min-Range-Hoch schließt. Er filtert nur nach Preis (Standard ab $5) und optional Volumen. **Relatives Volumen wie in der Studie berechnet er nicht.** Die Treffer sind nach gehandeltem Dollarvolumen sortiert, nicht nach relativem Volumen.
- **`/trader-entry TICKER`** (Setup `orb`): meldet waiting, triggered oder expired und schreibt `trader/entry.json`. Mit `--min-volume-x 1.5` muss der Ausbruchs-Bar das 1,5-fache Volumen der Range-Bars haben. Das ist ein Volumenfilter innerhalb des Tages, kein Vergleich mit den letzten 14 Tagen.
- **`/trader-exit`**: Stop `or-mid`, Ziel 2R, flat bis 15:55.
- **`/trader-timemachine`**: prüft den Plan an 60 Tagen 5-Min-Bars derselben Aktie. Das ist kein Ersatz für eine Studie über viele Aktien.
- **Zeitfenster**: Einstiege erst ab 9:45. Der 5-Minuten-ORB der Studie löst oft schon vor 9:45 aus und passt deshalb nicht zu unseren Regeln. Der 15-Minuten-ORB passt, weil sein erstes Signal frühestens um 9:50 kommt. Er war in der Studie aber deutlich schwächer (Sharpe 1,43 statt 2,81).
- **Unterschiede zur Studie**: nur long, Einstieg auf Schlusskurs statt Stop-Order, Stop an der Range-Mitte statt bei 10 % ATR, festes 2R-Ziel statt Halten bis zum Schluss, kein Hebel. Die Zahlen der Studie gelten deshalb **nicht** für unsere Variante. Ob sie trägt, zeigt erst das eigene Journal ([[Backtesting und Overfitting]]).
- Vergleich mit den anderen Strategien: [[Strategien im Vergleich]].

## Quellen

- Zarattini, Barbon, Aziz (2024): A Profitable Day Trading Strategy For The U.S. Equity Market, SSRN 4729284 – https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4729284 (Volltext: https://concretumgroup.com/wp-content/uploads/2026/02/A-Profitable-Day-Trading-Strategy-For-The-U.S.-Equity-Market.pdf)
- Concretum: Zusammenfassung des Papers – https://concretumgroup.com/a-profitable-day-trading-strategy-for-the-u-s-equity-market/
- Universität St. Gallen, Eintrag zum Paper – https://www.alexandria.unisg.ch/entities/publication/ab50f49b-4d5c-4aa8-aaa1-af7a4c131008
- CXO Advisory: Zusammenfassung Stocks in Play ORB (Filter, Regeln) – https://www.cxoadvisory.com/?p=45379
- Zarattini, Aziz (2023): Can Day Trading Really Be Profitable?, SSRN 4416622 – https://papers.ssrn.com/abstract=4416622
- CXO Advisory: Zusammenfassung QQQ-ORB (Regeln, Annahmen ohne Spread) – https://www.cxoadvisory.com/?p=44210
- MQL5-Blog: The opening-range breakout paper, replicated on five indices: gross reproduced, net zero – https://www.mql5.com/en/blogs/post/776235
- QuantConnect-Forum: Opening Range Breakout for Stocks in Play (Nachbildung) – https://www.quantconnect.com/forum/discussion/18444/opening-range-breakout-for-stocks-in-play/
- Crabel (1990): Day Trading with Short Term Price Patterns and Opening Range Breakout (Buchdaten) – https://www.goodreads.com/book/show/2306346
- Gao, Han, Li, Zhou (2018): Market intraday momentum, Journal of Financial Economics – https://profiles.wustl.edu/en/publications/market-intraday-momentum/
- Skills im Vault: `.claude/skills/trader-scanner/SKILL.md`, `trader-entry/SKILL.md`, `trader-exit/SKILL.md`, `trader-budget/SKILL.md`
