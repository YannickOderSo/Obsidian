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

# Breakout aus 20-Tage-Hoch

Gekauft wird, wenn der Kurs über das Hoch der letzten 20 Handelstage steigt. Das ist der Kern der Donchian-Kanäle und des Systems 1 der „Turtles“. Trendfolge mit Ausbrüchen ist auf Wochen und Monate gut belegt. Als Day Trade, der um 15:55 endet, ist sie eine ganz andere Strategie.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Begriffe

| Begriff | Bedeutung |
| --- | --- |
| Donchian-Kanal | obere Linie = höchstes Hoch der letzten n Tage, untere = tiefstes Tief. Benannt nach Richard Donchian |
| 20-Tage-Hoch (intraday) | höchstes **Hoch** der letzten 20 Tage |
| 20-Tage-Schlusshoch | höchster **Schlusskurs** der letzten 20 Tage. Liegt meist darunter, wird also öfter überschritten |
| N | bei den Turtles der 20-Tage-ATR (durchschnittliche Tagesspanne), Maß für Volatilität |
| Reclaim des 20-Tage-Durchschnitts | Schluss gestern unter dem 20-Tage-Durchschnitt, heute darüber. Kein Ausbruch, aber eine verwandte Trendmarke |

## Die Turtle-Regeln (System 1 und 2)

Richard Dennis brachte 1983 Anfängern ein Regelwerk bei. Die Regeln, wie sie Curtis Faith später veröffentlichte, laut Sekundärquellen:

| Regel | System 1 | System 2 |
| --- | --- | --- |
| Einstieg long | Kurs über dem Hoch der letzten 20 Tage | Kurs über dem Hoch der letzten 55 Tage |
| Filter | Signal überspringen, wenn der letzte System-1-Ausbruch ein Gewinner war | keiner |
| Stop | 2 N unter dem Einstieg | 2 N |
| Ausstieg | Kurs unter dem Tief der letzten 10 Tage | Kurs unter dem Tief der letzten 20 Tage |
| Größe | 1 Einheit = 1 % des Kapitals Risiko bei 2 N Abstand | dito |
| Aufstocken | je ½ N im Gewinn eine Einheit mehr, höchstens 4 | dito |

Die Turtles handelten Futures (Rohstoffe, Anleihen, Währungen), keine Einzelaktien, und hielten Trends über Wochen. System 1 lieferte mehr Signale, aber auch mehr Fehlausbrüche.

## Evidenz

### Gut belegt: Trendfolge und Nähe zum Hoch über Monate

- **George und Hwang (2004, *Journal of Finance*)**: Wie nah eine Aktie an ihrem 52-Wochen-Hoch notiert, erklärte 1963 bis 2001 einen großen Teil der Momentum-Gewinne und sagte künftige Renditen besser voraus als die vergangene Rendite. Horizont: sechs Monate, kein Intraday. Folgestudien fanden den Effekt in Schwellenländer-Indizes nicht.
- **Wilcox und Crittenden (2005)**: Long-only-Trendfolge auf über 24.000 US-Aktien über 22 Jahre, inklusive später delisteter Firmen: Kauf am Allzeithoch, Ausstieg über einen ATR-basierten Trailing-Stop. Ergebnis: positive Erwartung.
- **Zarattini, Pagani und Wilcox (2025)**: dieselbe Idee auf allen liquiden US-Aktien von 1950 bis Oktober 2024, über 66.000 Trades. **Trefferquote 43,9 %**, durchschnittlicher Gewinner +1,90R, durchschnittlicher Verlierer −0,70R. Weniger als 7 % der Trades brachten den Großteil des Gewinns, gewinnende Trades liefen im Schnitt 370 Tage. Die Kernzahlen hielten auch außerhalb der ursprünglichen Stichprobe (2005 bis 2024). Das Portfolio kam 1991 bis 2024 brutto auf 15,0 % pro Jahr; wegen hoher Umschlagskosten war die Grundversion laut den Autoren für Konten unter $1 Mio. nicht tragfähig.

### Kaum belegt: Ausbruch über das 20-Tage-Hoch als Day Trade

Alle Belege oben beruhen darauf, Gewinner **lange laufen zu lassen**. Ein Day Trade, der den Ausbruch um 10:30 kauft und um 15:55 verkauft, schneidet genau diesen Teil ab. Für die Intraday-Version haben wir **keine Studie** gefunden. Verwandt ist höchstens die ORB-Evidenz: Ausbrüche bei Aktien mit hohem Volumen liefen im Schnitt etwas besser ([[Opening Range Breakout]]).

> [!warning] Fehlausbrüche
> Ein Ausbruch über eine viel beachtete Marke zieht Käufer an, aber auch Verkäufer, die dort Gewinne mitnehmen. Fällt der Kurs zurück unter die Marke, ist das ein „Failed Breakout“. Die Turtles nahmen viele kleine Verluste in Kauf, um die seltenen großen Trends zu erwischen. Im Day Trade fehlt die Zeit für den großen Trend. Siehe [[Unterstützung und Widerstand]].

## Beispielrechnung mit unseren Limits

Fiktive Aktie, Vortagesschluss $48,20, 20-Tage-Hoch (intraday) $48,90, 14-Tage-ATR $1,20. Ein 5-Min-Bar schließt um 10:40 bei $49,05.

| Stop-Variante | Stop | Risiko/Aktie | Aktien (Limit $50) | Position |
| --- | --- | --- | --- | --- |
| Turtle 2 N (2 × ATR) | $46,65 | $2,40 | 20 | $981 |
| 0,5 × Tages-ATR | $48,45 | $0,60 | 83 → Cap 76 | $3.728 |
| unter der Ausbruchsmarke | $48,75 | $0,30 | 166 → Cap 76 | $3.728 |

Der Turtle-Stop von 2 N ist für einen Tag viel zu weit: Bei einem 2R-Ziel von $53,85 müsste die Aktie an einem Tag fast 10 % steigen. Ein enger Stop direkt unter der Marke macht das Ziel erreichbar ($49,65 bei 2R), wird aber oft schon vom normalen Rauschen ausgelöst. Beides ist ein Kompromiss, den man im Journal messen sollte.

> [!info] ATR ist nicht gleich ATR
> Die Turtles nutzen die Tages-ATR. `/trader-exit --stop atr:K` rechnet die ATR auf den **Intraday-Bars** der Sitzung (14 Bars bis zum Einstieg). Die ist viel kleiner. „atr:2“ im Skill ist also kein Turtle-Stop.

## Im Vault

- **`/trader-scanner daily`** liefert vor der Eröffnung:
  - `breakout_20d`: Der **letzte Schlusskurs** liegt über allen Schlusskursen der 20 Sitzungen davor. Gemessen wird also auf Schlusskursen, nicht auf Hochs. Laut Skill-Doku feuert das öfter als ein Ausbruch über das Intraday-Hoch (Beispiel KO am 16.10.2026).
  - `reclaim_ma20`: gestern unter dem 20-Tage-Durchschnitt, heute darüber.
  - Wichtig: Der Ausbruch ist dann **schon gestern passiert**. Heute geht es um die Fortsetzung.
- **Das 20-Tage-Hoch steht nicht in der Watchlist.** `trader/watchlist.json` enthält Symbol, Setups, Schlusskurs, RSI und Volumen, aber nicht die Marke selbst. Das Level muss man am Chart ablesen (z. B. 20-Tage-Hoch inklusive gestern oder Vortageshoch).
- **`/trader-entry TICKER --setup level --level <Marke>`** wartet auf den ersten 5-Min-Bar, der über der Marke **schließt**. Mit `--min-volume-x` kann man zusätzlich Volumen verlangen.
- **`/trader-exit`** braucht bei einem Level-Setup einen eigenen Stop. Für einen Day Trade ist ein Stop unter der Ausbruchsmarke oder unter dem Tagestief üblicher als 2 N.
- **Flat bis 15:55** verhindert genau das, was Trendfolge laut Studien profitabel macht: Gewinner lange laufen lassen. Wer die Idee über Tage handeln will, braucht ein anderes Regelwerk. Das ist eine Entscheidung des Nutzers, nicht der Skills.
- Vergleich: [[Strategien im Vergleich]].

## Quellen

- MQL5: Automating Classic Market Methods (Part 5): The Original Turtle Trading Rules (N, 2N-Stop, 1 %, System 1/2, Ausstiege) – https://www.mql5.com/en/articles/23448
- TurtleTrader.com: Turtle Trading – Richard Dennis' Experiment (20- und 55-Tage-Ausbruch, Fehlausbrüche System 1) – https://www.turtletrader.com/turtle-trading/
- George, Hwang (2004): The 52-Week High and Momentum Investing, Journal of Finance 59, DOI 10.1111/j.1540-6261.2004.00695.x – Zusammenfassung bei CXO Advisory: https://www.cxoadvisory.com/1284/technical-trading/the-52-week-high-as-a-momentum-indicator-for-individual-stocks/
- Folgestudie Schwellenländer-Indizes (Malin, Bornholt 2010; Du 2008), Übersicht – https://experts.nau.edu/en/publications/the-52-week-high-and-momentum-investing-in-international-stock-in/
- Wilcox, Crittenden (2005): Does Trend Following Work on Stocks? – https://www.cis.upenn.edu/~mkearns/finread/trend.pdf
- Zarattini, Pagani, Wilcox (2025): Does Trend Following Still Work on Stocks? (Trefferquote 43,9 %, 1,90R/−0,70R, 370 Tage, Kosten) – https://concretumgroup.com/does-trend-following-still-work-on-stocks/ (Volltext: https://concretumgroup.com/wp-content/uploads/2026/02/Does-Trend-Following-Still-Work-on-Stocks.pdf)
- Skills im Vault: `.claude/skills/trader-scanner/SKILL.md` und `scan.py`, `trader-entry/SKILL.md`, `trader-exit/SKILL.md`
