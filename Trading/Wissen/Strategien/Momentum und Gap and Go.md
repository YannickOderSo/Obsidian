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

# Momentum und Gap and Go

Gap and Go heißt: Eine Aktie eröffnet deutlich über dem Vortagesschluss (Gap), meist wegen einer Nachricht, und man kauft, wenn sie über ihr Pre-Market-Hoch weiterläuft. Die Strategie ist in Kursen für Kleinanleger sehr verbreitet. Gute, unabhängige Studien zu genau dieser Regel gibt es aber kaum, und gerade bei kleinen Aktien sind die Risiken groß.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Begriffe

| Begriff | Bedeutung |
| --- | --- |
| Gap (Kurslücke) | Eröffnungskurs ≠ Vortagesschluss. Gap up: Eröffnung darüber. |
| Pre-Market | Handel vor 9:30 New York, ab 4:00 möglich. Dünnes Volumen, breite Spreads. Siehe [[Handelszeiten und Sessions]] |
| Pre-Market-Hoch (PMH) | höchster Kurs vor 9:30, gilt als erste Marke des Tages |
| Float | frei handelbare Aktien. „Low Float“ heißt in der Praxis grob unter 20 Mio. Aktien |
| Katalysator | der Grund für das Gap: Earnings, Prognose, FDA, Übernahme, Auftrag. Siehe [[Katalysatoren]] |
| Gap Fill | der Kurs fällt im Tagesverlauf bis zum Vortagesschluss zurück, die Lücke ist „geschlossen“ |
| Relatives Volumen | Volumen heute im Vergleich zum üblichen Volumen, siehe [[Volumen und relatives Volumen]] |

## Die Regeln, wie sie gelehrt werden

Die bekannteste Form stammt aus der Retail-Szene, vor allem von Ross Cameron (Warrior Trading) mit seinen „Five Pillars“. Die genauen Schwellen sind **nur aus Drittquellen** belegt (Scanner und Indikatoren, die sich auf ihn berufen). Die folgenden Zahlen sind deshalb Richtwerte, keine geprüfte Regel:

| Kriterium | Typischer Wert laut Drittquellen |
| --- | --- |
| Kursanstieg | mindestens +10 % gegenüber Vortagesschluss |
| Relatives Volumen | mindestens 5x |
| Katalysator | frische Nachricht, manuell geprüft |
| Preis | etwa $1 bis $20 |
| Float | unter 10 Mio. (manche: 20 Mio.) |
| Pre-Market-Volumen | z. B. mindestens 50.000 Aktien |

Ablauf in der klassischen Form:

1. Vor 9:30 die Gapper scannen, nach Katalysator und Volumen sortieren, 2 bis 4 Kandidaten behalten.
2. Pre-Market-Hoch, Pre-Market-Tief, Vortagesschluss und Vortageshoch markieren.
3. Einstieg, wenn der Kurs nach 9:30 über das Pre-Market-Hoch steigt, oft in den ersten Minuten.
4. Stop unter einem nahen Tief (z. B. Tief der ersten Kerze oder unter dem PMH nach dem Ausbruch).
5. Schnelle Teilgewinne, weil die Bewegung oft früh ausläuft.

Eine seriösere Variante für liquide Aktien beschreibt etwa StockMarketWatch: Gaps von 3 bis 10 % bei großen Werten, Pre-Market-Volumen in **Dollar** prüfen (200.000 Aktien zu $5 sind nur etwa $1 Mio.), Nachrichten nach Qualität ordnen (angehobene Jahresprognose wiegt mehr als ein EPS-Beat), Gaps ohne Nachricht meiden.

## Evidenz

> [!warning] Dünn belegt
> Für die Gap-and-Go-Regel mit Float, Pre-Market-Hoch und 5x Volumen haben wir **keine unabhängige Studie** gefunden. Die Zahlen kommen aus Kursen, Scannern und Einzelfällen. Wer verkauft, zeigt die Gewinner.

Was es an belastbarer Forschung gibt:

- **Gaps setzen sich im Index eher fort, als dass sie sich schließen.** Plastun, Sibande, Gupta und Wohar (2020) untersuchten Dow, S&P 500 und Nasdaq von 1928 bis 2018. Am Gap-Tag lief der Kurs eher in Richtung des Gaps weiter. Der Effekt war vorübergehend, und die verbreitete Annahme „Gaps werden immer gefüllt“ fanden sie nicht bestätigt. Das gilt für Indizes, nicht für kleine Einzelaktien.
- **Gap-Fill-Quoten hängen an der Definition.** Tastylive fand bei rund 350.000 großen Gaps in 100 liquiden Werten, dass große Gaps nach 15 bis 45 Tagen in mehr als der Hälfte der Fälle gefüllt waren. Das ist mehrtägig, nicht intraday. Eine belastbare Quote „so oft wird ein Gap am selben Tag gefüllt“ für Einzelaktien haben wir nicht gefunden.
- **Stocks in Play.** Die ORB-Studie von Zarattini, Barbon und Aziz zeigt: Aktien mit sehr hohem relativem Volumen (oft nach News) liefern im Schnitt bessere Ausbrüche als normale Aktien. Das stützt die Idee hinter Gap and Go (Aktien mit Nachrichten handeln), nicht aber die konkrete Regel. Siehe [[Opening Range Breakout]].
- **Intraday-Momentum.** Gao, Han, Li und Zhou (2018) fanden, dass die Rendite bis 10:00 (inklusive Übernacht-Gap) die letzte halbe Stunde beim S&P-500-ETF vorhersagt. Auch das gilt für den Index, und der Effekt ist klein.

## Risiken

> [!warning] Was bei Gappern schiefgeht
> - **Gap Fill / Fade**: Gaps ohne klare Nachricht laufen häufig zurück. Der Vortagesschluss ist dann das naheliegende Ziel der Verkäufer.
> - **Handelsstopps (LULD)**: Low-Float-Aktien springen oft aus dem Preisband und werden für mindestens 5 Minuten gestoppt. Während des Stopps kommt man nicht raus, und der Kurs nach der Wiederaufnahme kann weit vom Stop entfernt sein. Siehe [[Handelsstopps und LULD]].
> - **Verwässerung**: Kleine Firmen nutzen Kurssprünge für Kapitalerhöhungen (Offerings). Dann kippt der Kurs oft schnell. Vorher die Filings auf SEC EDGAR prüfen.
> - **Pump and Dump / Ramp and Dump**: SEC und FINRA warnen vor Kampagnen über Social Media und Messenger, die kleine Aktien hochtreiben und dann verkaufen. FINRA nennt ungewöhnliche Kurssprünge kurz nach dem Börsengang kleiner, oft ausländischer Firmen.
> - **Spread und Slippage**: Im Pre-Market und bei kleinen Aktien sind Spreads breit, ein Stop kann deutlich schlechter ausgeführt werden. Siehe [[Spread Liquidität und Slippage]].

## Beispielrechnung mit unseren Limits

Fiktive Aktie, nur zur Rechnung: Vortagesschluss $8,00, Eröffnung $10,00 (+25 %), Pre-Market-Hoch $10,50. Ein 5-Min-Bar schließt um 9:55 bei $10,55 über dem PMH.

| Größe | Rechnung | Wert |
| --- | --- | --- |
| Stop (Tief der Ausbruchskerze) | angenommen | $10,15 |
| Risiko je Aktie | 10,55 − 10,15 | $0,40 |
| Stückzahl | floor(50 / 0,40) | 125 Aktien |
| Position | 125 × 10,55 | $1.319 |
| Ziel 2R | 10,55 + 0,80 | $11,35 |

Was das Beispiel nicht zeigt: Bei einem Spread von $0,05 auf beiden Seiten und einem Stop, der im schnellen Markt 10 Cent tiefer gefüllt wird, verliert man statt $50 schnell $70 oder mehr. Ein Handelsstopp kann den Verlust noch weiter vergrößern. Das Tageslimit von $150 ist dann nach zwei Trades fast weg.

## Im Vault

- **Zeitfenster passt nicht zur klassischen Form**: Einstiege erst ab 9:45 New York. Der typische Gap-and-Go-Einstieg in den ersten Minuten nach 9:30 ist damit ausgeschlossen. Möglich ist nur eine spätere Variante: der Ausbruch über das Pre-Market-Hoch oder über die 15-Minuten-Range nach 9:45.
- **Kein Gap-Scanner**: `/trader-scanner` hat kein Setup für Gaps, Float oder Pre-Market-Volumen. Der `daily`-Scan arbeitet auf Schlusskursen, der `orb`-Scan auf 5-Min-Bars ab 9:30 (Pre-Market ist nicht enthalten). Standard-Mindestpreis ist $5, also fallen viele typische Low-Float-Gapper ($1 bis $5) heraus.
- **`/trader-news`** zeigt Schlagzeilen und 8-K-Filings und wie weit eine Aktie vom Vortagesschluss entfernt ist. Damit lässt sich der Katalysator prüfen. Siehe [[News richtig lesen]].
- **`/trader-entry --setup level --level <PMH>`** kann auf einen Schlusskurs über dem Pre-Market-Hoch warten. Das PMH muss man selbst nennen, die Skills lesen keine Pre-Market-Daten.
- **`/trader-exit`** braucht bei einem Level-Setup einen eigenen Stop (`price:X`, `pct:X` oder `atr:K`).
- **`/trader-risk`** blockt keine Low-Float-Aktien automatisch. Wer sie meiden will, trägt Ticker in `blocked` ein. Das ist eine Änderung an `trader/config.json` und nur auf Wunsch des Nutzers.
- Die ORB-Kette ist für Gapper mit hohem Volumen meist die sauberere Wahl: [[Opening Range Breakout]]. Vergleich: [[Strategien im Vergleich]].

## Quellen

- StockMarketWatch: Finding Premarket Gappers (Kriterien, Float, Halts, Katalysator-Rangfolge) – https://stockmarketwatch.com/edu/trading-strategies/day-trading/finding-premarket-gappers
- TraderDaddy Pro Premarket Gappers (Scanner-Schwellen nach Cameron-Kriterien, Drittquelle) – https://mcpservers.org/servers/www-traderdaddy-pro-premarket-gappers
- Warrior Trading Blog (erwähnt die „Five Pillars of Stock Selection“) – https://www.warriortrading.com/?p=68640
- Plastun, Sibande, Gupta, Wohar (2020): Price gap anomaly in the US stock market: the whole story, North American Journal of Economics and Finance – https://ideas.repec.org/p/pre/wpaper/201963.html und https://repository.up.ac.za/handle/2263/78336
- Tastylive Market Measures: Edge in Trading Gaps (2016) – https://www.tastylive.com/shows/market-measures/episodes/edge-in-trading-gaps-08-22-2016
- LuxAlgo: Gap Fill (Fill-Quoten hängen an Definitionen) – https://www.luxalgo.com/library/concept/gap-fill.md
- Zarattini, Barbon, Aziz (2024): A Profitable Day Trading Strategy For The U.S. Equity Market – https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4729284
- Gao, Han, Li, Zhou (2018): Market intraday momentum – https://profiles.wustl.edu/en/publications/market-intraday-momentum/
- SEC Investor Alert: Pump-and-Dumps and Market Manipulations – https://www.sec.gov/files/investor/alerts/ia_pumpanddump.htm
- FINRA: Ramp-and-Dump Schemes – https://www.finra.org/investors/insights/ramp-and-dump-schemes
- Skills im Vault: `.claude/skills/trader-scanner/SKILL.md`, `trader-entry/SKILL.md`, `trader-news/SKILL.md`
