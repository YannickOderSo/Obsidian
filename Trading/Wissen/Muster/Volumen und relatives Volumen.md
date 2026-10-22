---
typ: wissen
erstellt: 2026-10-22
aktualisiert: 2026-10-22
quelle: Recherche
tags:
  - trading
  - wissen
  - muster
---

# Volumen und relatives Volumen

Volumen ist die Zahl der gehandelten Aktien. Für Day Trader zählt weniger die absolute Zahl als das **relative Volumen** (RVOL): Wird heute ungewöhnlich viel gehandelt, verglichen mit dem, was um diese Uhrzeit normal ist? Diese Notiz erklärt RVOL, den typischen Verlauf des Volumens über den Tag und was Studien zum Volumen am Ausbruch zeigen.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Der Tagesverlauf: die U-Kurve

Das Volumen ist über den Handelstag nicht gleich verteilt:

- **Eröffnung:** Am meisten Umsatz kurz nach 9:30, inklusive Eröffnungsauktion. Jain und Joh (1988) fanden an der NYSE ein signifikantes U-Muster: hoch zur Eröffnung, flacher über Mittag, wieder höher zum Schluss.
- **Mittag:** Das Tal. Spreads sind meist breiter, Bewegungen zäher.
- **Schluss:** Der Umsatz steigt in den letzten 30 Minuten wieder stark, mit einer Spitze kurz vor 16:00 (IEX 2024). Die Schlussauktion allein machte 2024 an einem typischen Tag etwa 9 % des US-Tagesumsatzes aus, an Index- und Verfallstagen etwa 20 % (BMLL, 2025).
- **Erklärung:** Theorie (Admati und Pfleiderer 1988): Informierte und uninformierte Händler bündeln ihren Handel zur gleichen Zeit, weil es dann am billigsten ist.

Folgen für Day Trading im Vault-Zeitfenster (Einstiege 9:45 bis 15:30, flat bis 15:55):

- Die ersten 15 Minuten, aus denen die Opening Range entsteht, haben das höchste Volumen des Tages. Jede spätere Kerze wirkt dagegen „dünn“.
- Um 15:55 raus heißt: kurz vor der Schlussauktion, in einer Phase mit hohem Umsatz. Das ist für einen Ausstieg eher günstig.
- Einstiege über Mittag treffen auf das Volumentief. Siehe [[Handelszeiten und Sessions]].

## Relatives Volumen (RVOL)

Zwei gängige Definitionen:

| Variante | Formel | Wofür |
| --- | --- | --- |
| Tages-RVOL | Volumen heute / Ø Tagesvolumen der letzten N Tage (N oft 10, 14, 20 oder 30) | nach Börsenschluss, für Tagesscans |
| RVOL zur Uhrzeit | kumuliertes Volumen heute bis jetzt / Ø kumuliertes Volumen bis zur gleichen Uhrzeit an den letzten N Tagen | während der Sitzung |

Die zweite Variante ist die richtige für den Handelstag, weil sie die U-Kurve berücksichtigt. TradingViews Indikator „Relative Volume at Time“ rechnet genau so: Er sucht in den letzten N Sitzungen die Kerzen mit demselben Abstand zur Eröffnung und teilt das aktuelle durch deren Durchschnitt (standardmäßig kumuliert).

### Beispielrechnung (Zahlen angenommen)

Ein Wert handelt im Schnitt 2,0 Mio. Aktien am Tag. An normalen Tagen sind bis 10:00 im Schnitt 400.000 Stück umgesetzt. Heute sind es um 10:00 schon 1,2 Mio.

| Rechnung | Ergebnis | Aussage |
| --- | --- | --- |
| naiv: 1,2 Mio. / 2,0 Mio. | 0,6 | wirkt unauffällig, ist aber falsch verglichen |
| zur Uhrzeit: 1,2 Mio. / 0,4 Mio. | **3,0** | dreimal so viel wie um diese Zeit üblich |

Übliche Praxis-Schwellen: RVOL über 1,5 oder 2 gilt als „in Bewegung“, über 3 bis 5 als außergewöhnlich, meist wegen einer Nachricht. Das sind Konventionen, keine geprüften Grenzwerte.

## Was Studien zeigen

| Befund | Quelle | Einordnung |
| --- | --- | --- |
| Ungewöhnlich hohes Volumen an einem Tag oder in einer Woche geht im Folgemonat mit höheren Renditen einher, ungewöhnlich niedriges mit niedrigeren (High-Volume Return Premium) | Gervais, Kaniel und Mingelgrin (2001), Journal of Finance | gut belegt, aber Horizont ein Monat, nicht ein Tag; Erklärung: mehr Aufmerksamkeit |
| Opening Range Breakout nur auf „Stocks in Play“ (hohes relatives Volumen, Top 20 nach RVOL) brachte im Backtest 2016–2023 weit mehr als auf allen Aktien | Zarattini, Barbon und Aziz (2024), Working Paper | einzelne, nicht begutachtete Studie, mit Hebel bis 4x und Leerverkäufen; für Long-only mit $5.000 nicht übertragbar, aber ein Hinweis, dass RVOL als Filter zählt |
| Ob das Volumen in einer Formation steigt oder fällt, brachte kaum zusätzliche Information | Lo, Mamaysky und Wang (2000) | das klassische „Volumen muss bestätigen“ ist in dieser großen Studie schwach |
| Hohes Ausbruchsvolumen (über dem 30-Tage-Schnitt) half bei Dreiecken, Keilen und Rechteck-Tops; **niedriges** half bei High and Tight Flags, Doppelböden (Adam & Adam) und Rechteck-Bottoms; kein Unterschied bei Cup with Handle und inverser Kopf-Schulter | Bulkowski, „Breakout Day Volume“ (Tageschart) | „Ausbruch nur mit Volumen“ gilt nicht für jede Formation |
| Intraday-Momentum der ersten halben Stunde für die letzte halbe Stunde ist an Tagen mit hohem Volumen stärker | Gao, Han, Li und Zhou (2018), Journal of Financial Economics | Index-ETF (SPY), nicht einzelne Aktien; Effekt klein (R² etwa 2 %) |

> [!warning] Volumen bestätigt, es sagt nicht voraus
> Hohes relatives Volumen zeigt, dass ein Wert Aufmerksamkeit hat, meist wegen einer Nachricht. Es sagt nicht, in welche Richtung es geht. Ein Wert mit RVOL 5 nach schlechten Zahlen fällt oft weiter. Erst Katalysator und Richtung prüfen, siehe [[Katalysatoren]] und [[News richtig lesen]].

## Volumen am Ausbruch: Praxisregeln

1. **Ausbruchskerze über dem Schnitt:** Viele verlangen das 1,5- bis 2-Fache des durchschnittlichen Volumens der letzten Kerzen. Konvention, nicht geprüft.
2. **Volumen in der Konsolidierung fallend:** Bei Flaggen und Dreiecken fällt es laut Bulkowski in 74 bis 86 % der Fälle ohnehin. Ein fallendes Volumen ist also normal, kein Gütesiegel.
3. **Uhrzeit bedenken:** Eine Ausbruchskerze um 11:30 mit dem halben Volumen der 9:30-Kerze kann für 11:30 trotzdem stark sein.
4. **Sonderfälle ausfiltern:** Index-Umschichtungen, großer Verfall (dritter Freitag), Earnings. Dann ist hohes Volumen mechanisch und kein Zeichen von Interesse.

## Im Vault

- **`/trader-scanner daily`:** Filtert auf mindestens 1 Mio. Stück Volumen der letzten Sitzung (`--min-volume`) und sortiert Treffer nach gehandeltem Wert (Kurs mal Volumen). Ein RVOL wird **nicht** berechnet. Während der Sitzung ist das Volumen das bisherige des Tages, darum den Tagesscan vor der Eröffnung oder nach dem Schluss laufen lassen.
- **`/trader-scanner orb`:** Prüft in Stufe 2 die am meisten gehandelten Kandidaten zuerst; ebenfalls kein RVOL.
- **`/trader-entry --min-volume-x 1.5`:** Vergleicht das Volumen der Auslöser-Kerze mit dem **Durchschnitt der Opening-Range-Kerzen**. Wegen der U-Kurve und der Eröffnungsauktion in der 9:30-Kerze ist das streng: Die Doku nennt schon 1,0 streng, im TSLA-Beispiel vom 19.10.2026 hatte die Auslöser-Kerze nur das 0,60-Fache. Das ist kein RVOL, sondern ein Vergleich mit dem lautesten Teil des Tages.
- **RVOL selbst bestimmen:** Kein Skill liefert es. Wer es nutzen will, liest es aus einem Chart-Tool ab und notiert es im Journal-Eintrag des Trades. Dann lässt sich nach einigen Wochen prüfen, ob Trades mit hohem RVOL bei dir besser laufen.
- **Time Machine:** Zieht für die Wiederholungen Kerzen derselben Tageszeit (±2 Kerzen) aus 60 Tagen. Die U-Kurve der Schwankung steckt damit drin, ein heute ungewöhnlich hohes Volumen nicht.

Verwandt: [[Bull Flag]], [[Chartformationen]], [[Opening Range Breakout]], [[Momentum und Gap and Go]], [[Spread Liquidität und Slippage]].

## Quellen

- Jain, Joh (1988), „The Dependence between Hourly Prices and Trading Volume“, Journal of Financial and Quantitative Analysis 23(3), 269–283: https://resolve.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/dependence-between-hourly-prices-and-trading-volume/C305DB5BFB5F2B2D803BB94449AF8B47 (U-Form laut Sekundärliteratur, Volltext nicht gelesen)
- Admati, Pfleiderer (1988), „A Theory of Intraday Patterns: Volume and Price Variability“, Review of Financial Studies 1(1), 3–40: https://www.gsb.stanford.edu/faculty-research/publications/theory-intraday-patterns-volume-price-variability
- IEX (22.05.2024), „It's 3:58 p.m. Do You Know Where the Volume Trades?“: https://www.iex.io/article/its-3-58-p-m-do-you-know-where-the-volume-trades
- BMLL (24.06.2025), „Into the Close: Unpacking U.S. Closing Auction Dynamics and the Impact of the Russell Reconstitution“: https://www.bmlltech.com/news/market-insight/into-the-close-unpacking-u-s-closing-auction-dynamics-and-the-impact-of-the-russell-reconstitution
- TradingView Hilfe, „Relative Volume at Time“: https://in.tradingview.com/support/solutions/43000705489-relative-volume-at-time/
- Gervais, Kaniel, Mingelgrin (2001), „The High-Volume Return Premium“, Journal of Finance 56(3), 877–919: https://ideas.repec.org/a/bla/jfinan/v56y2001i3p877-919.html
- Zarattini, Barbon, Aziz (2024), „A Profitable Day Trading Strategy For The U.S. Equity Market“, Swiss Finance Institute Research Paper: https://ideas.repec.org/p/chf/rpseri/rp2498.html; Details zu Filter (RVOL ≥ 100 %, Top 20), Hebel und Long/Short laut Zusammenfassung bei CXO Advisory: https://www.cxoadvisory.com/individual-investing/intraday-trading-of-overactive-stocks-via-opening-range-breakout/
- Lo, Mamaysky, Wang (2000), „Foundations of Technical Analysis“, Journal of Finance 55(4): https://www.nber.org/papers/w7613
- Bulkowski, „Breakout Day Volume“: https://thepatternsite.com/volbkout.html
- Gao, Han, Li, Zhou (2018), „Market Intraday Momentum“, Journal of Financial Economics 129, 394–414: https://www3.nd.edu/~zda/intramom.pdf
- Skills: `.claude/skills/trader-scanner/SKILL.md`, `.claude/skills/trader-entry/SKILL.md`, `.claude/skills/trader-timemachine/SKILL.md`
