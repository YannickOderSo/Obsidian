---
typ: wissen
erstellt: 2026-10-22
aktualisiert: 2026-10-22
quelle: Recherche
tags:
  - trading
  - wissen
  - markt
---

# Handelszeiten und Sessions

Wann an der NYSE und der Nasdaq gehandelt wird, wie sich ein Handelstag in Abschnitte gliedert und was das in deutscher Zeit bedeutet, einschließlich der Wochen, in denen die Zeitumstellung in den USA und der EU auseinanderfällt. Dazu die Feiertage und verkürzten Tage für den Rest von 2026 und für 2027.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Der Handelstag in New York

Die reguläre Sitzung (Core Session) läuft an NYSE und Nasdaq von **9:30 bis 16:00 New York Zeit (ET)**. Davor und danach gibt es Extended Hours mit deutlich weniger Liquidität.

| Abschnitt | Zeit ET | Was passiert |
| --- | --- | --- |
| Overnight (Alpaca) | 20:00–4:00 (So–Fr) | Alpaca bietet eine eigene Overnight-Session an, nur Limit-Orders mit `extended_hours` |
| Pre-Market | 4:00–9:30 | Alpaca nimmt Extended-Hours-Orders ab 4:00; NYSE Arca handelt ab 4:00, NYSE (Tapes B/C) ab 7:00; dünnes Orderbuch, breite Spreads |
| Pre-Opening NYSE | ab 6:30 | Orders für die Eröffnungsauktion können eingegeben werden |
| Opening-Informationen | ab 8:00 | NYSE veröffentlicht sekündlich Imbalance-Daten bis zur Eröffnung |
| Eröffnungsauktion | 9:30 | Der Designated Market Maker eröffnet jede NYSE-Aktie in einer Auktion; Nasdaq hat den Opening Cross |
| Erste 15–30 Minuten | 9:30–10:00 | Höchstes Volumen und höchste Schwankung des Tages, breiteste Spreads; hier entsteht die Opening Range |
| Vormittag | 10:00–11:30 | Trends des Morgens laufen weiter oder scheitern |
| Mittagsflaute | ca. 11:30–14:00 | Weniger Volumen, engere Ranges, mehr Fehlsignale (siehe Evidenz unten) |
| Power Hour | 15:00–16:00 | Volumen steigt wieder, institutionelle Orders zum Schluss |
| MOC/LOC-Annahmeschluss NYSE | 15:50 | Danach nur noch Orders, die eine Imbalance ausgleichen; Imbalance-Daten jede Sekunde |
| Schlussauktion | 16:00 | Schlusskurs entsteht in der Auktion (NYSE Closing Auction, Nasdaq Closing Cross) |
| After-Hours | 16:00–20:00 | Earnings kommen oft hier; wieder dünnes Buch |

> [!info] Wie groß sind die Auktionen?
> Die Schlussauktion ist ein großer Teil des Tagesvolumens: BMLL beziffert sie für 2024 auf rund 9 % des gehandelten Werts eines typischen Tages (an Index-Rebalancing- und Verfallstagen etwa 20 %), State Street nennt für Dezember 2025 rund 15 % des US-Tagesvolumens. Die Zahlen messen Unterschiedliches (Notional vs. Stück, Zeitraum), die Größenordnung ist aber klar.

### Evidenz zum Tagesverlauf

- **Gut belegt:** Volumen und Kursschwankung sind über den Tag U-förmig verteilt, hoch zu Beginn und am Ende, niedrig zur Mittagszeit. Admati/Pfleiderer (1988) erklären die Bündelung theoretisch, Jain/Joh (1988) zeigen für die NYSE deutliche Unterschiede im Volumen je Tagesstunde.
- **Gut belegt:** Die Spreads sind direkt nach der Eröffnung am breitesten und fallen danach (McInish/Wood 1992, umgekehrtes J). Das ist ein guter Grund, nicht in den ersten Minuten mit Market-Orders einzusteigen.
- **Folklore:** Feste Regeln wie „zwischen 11:30 und 14:00 nie handeln“ oder „die Power Hour bestätigt den Trend des Tages“ sind Händlerweisheit, keine belegte Regel. Die Mittagsflaute ist nur die Mitte des U.

## Umrechnung in deutsche Zeit

Normalerweise liegt New York **6 Stunden** hinter Deutschland. Die USA stellen aber am zweiten Sonntag im März auf Sommerzeit um und am ersten Sonntag im November zurück, die EU am letzten Sonntag im März und im Oktober. In den Wochen dazwischen sind es nur **5 Stunden**.

| Zeitraum | Abstand | NYSE öffnet (DE) | Schluss (DE) |
| --- | --- | --- | --- |
| Normal (Sommer wie Winter) | 6 h | 15:30 | 22:00 |
| **25.10.–31.10.2026** | 5 h | **14:30** | **21:00** |
| ab 01.11.2026 | 6 h | 15:30 | 22:00 |
| **14.03.–27.03.2027** | 5 h | **14:30** | **21:00** |
| ab 28.03.2027 | 6 h | 15:30 | 22:00 |
| **31.10.–06.11.2027** | 5 h | **14:30** | **21:00** |
| ab 07.11.2027 | 6 h | 15:30 | 22:00 |

Berechnet mit der Zeitzonen-Datenbank (America/New_York gegen Europe/Berlin); die Umstellungstage sind der 8.3. und 1.11.2026 (USA), 29.3. und 25.10.2026 (EU), 14.3. und 7.11.2027 (USA), 28.3. und 31.10.2027 (EU).

> [!warning] Nächste Woche ist eine Sonderwoche
> Vom 26. bis 30. Oktober 2026 öffnet die NYSE schon um **14:30** deutscher Zeit, die Einstiegsregel 9:45 ET ist dann **14:45**, Flat by 15:55 ET ist **20:55**. Wer sich nach der deutschen Uhr richtet, liegt eine Stunde daneben. Die Skills rechnen intern in New York Zeit und sind davon nicht betroffen.

> [!warning] Unsicher ab 2027: Sommerzeit in den USA
> Das Repräsentantenhaus hat im Juli 2026 den Sunshine Protection Act (dauerhafte Sommerzeit) beschlossen, der Senat hat Anfang Oktober 2026 noch nicht abgestimmt, laut Mehrheitsführer Thune ohne Konsens. Für den 1. November 2026 wird die Uhr in den USA wie gewohnt zurückgestellt. Würde das Gesetz später in Kraft treten, läge New York im europäischen Winter dauerhaft 5 Stunden zurück. Auch in der EU ist die Abschaffung der Zeitumstellung seit Jahren blockiert. Die Tabelle oben vor jeder Umstellung kurz prüfen.

### Die wichtigsten Zeiten der Vault-Regeln in deutscher Zeit

| Regel (ET) | Normal | Sonderwoche |
| --- | --- | --- |
| Eröffnung 9:30 | 15:30 | 14:30 |
| Opening Range fertig, Einstiege ab 9:45 | 15:45 | 14:45 |
| Letzter Einstieg 15:30 | 21:30 | 20:30 |
| MOC-Annahmeschluss 15:50 | 21:50 | 20:50 |
| Flat by 15:55 | 21:55 | 20:55 |
| Schluss 16:00 | 22:00 | 21:00 |
| Verkürzter Tag: Schluss 13:00, Flat by 12:55 | 19:00 / 18:55 | (kein verkürzter Tag fällt in eine Sonderwoche) |

## Feiertage und verkürzte Tage

Laut nyse.com (abgerufen 2026-10-22). Die Liste in `trader-alerts` (gelesen 2026-10-13) stimmt damit überein.

### Rest 2026

| Datum | Was |
| --- | --- |
| Do 26.11.2026 | Thanksgiving, geschlossen |
| Fr 27.11.2026 | Verkürzt, Schluss 13:00 ET (19:00 DE) |
| Do 24.12.2026 | Verkürzt, Schluss 13:00 ET (19:00 DE) |
| Fr 25.12.2026 | Weihnachten, geschlossen |

### 2027

| Datum | Feiertag |
| --- | --- |
| Fr 01.01.2027 | New Year's Day |
| Mo 18.01.2027 | Martin Luther King Jr. Day |
| Mo 15.02.2027 | Washington's Birthday |
| Fr 26.03.2027 | Good Friday (Karfreitag; fällt in die Sonderwoche) |
| Mo 31.05.2027 | Memorial Day |
| Fr 18.06.2027 | Juneteenth (nachgeholt, 19.6. ist Samstag) |
| Mo 05.07.2027 | Independence Day (nachgeholt) |
| Mo 06.09.2027 | Labor Day |
| Do 25.11.2027 | Thanksgiving |
| Fr 24.12.2027 | Weihnachten (nachgeholt, 25.12. ist Samstag) |

Verkürzt 2027: nur **Fr 26.11.2027** (Schluss 13:00 ET). Am 31.12.2027 wird normal gehandelt, weil Neujahr 2028 auf einen Samstag fällt und nicht nachgeholt wird.

Deutsche Feiertage spielen keine Rolle: Am Ostermontag, 1. Mai oder 3. Oktober ist die NYSE offen.

## Was sich ändern könnte

- **23/5-Handel:** Nasdaq und NYSE Arca planen für den **6. Dezember 2026** einen Handel von Sonntag 21:00 bis Freitag 20:00 ET mit einer Stunde Pause. Die SEC hat den Nasdaq-Antrag im April 2026 genehmigt, Teile hängen aber noch an weiteren Genehmigungen und an der Bereitschaft des SIP. Das Datum ist ein Ziel, keine Zusage. Für die Regeln des Vaults ändert das nichts, gehandelt wird nur in der regulären Sitzung.

## Im Vault

- `trader-alerts` (`alerts.py clock`) kennt NYSE-Zeiten, Feiertage 2026/2027 und verkürzte Tage und rechnet die Sommerzeit selbst. Für andere Jahre sagt es, dass die Liste unbekannt ist.
- `trader-risk` sperrt neue Einstiege vor 9:45 und nach 15:30 ET, am Wochenende, an Feiertagen und auf verkürzten Tagen drei Stunden früher. Ausstiege sind nie gesperrt.
- `trader-exit` schiebt Flat by an verkürzten Tagen auf 12:55; ein Einstieg nach Flat by wird abgelehnt.
- `trader-entry` und `trader-scanner` bauen die Opening Range aus den Bars 9:30, 9:35 und 9:40. Die 15-Minuten-Wartezeit lässt die breitesten Spreads der Eröffnung vorbeiziehen.
- Grenze: Die Skills arbeiten nur in der regulären Sitzung. Pre-Market-Kurse und Gaps sieht man über `/trader-news` und die Kurse, gehandelt wird dort nicht. Siehe [[Momentum und Gap and Go]], [[Opening Range Breakout]], [[Makro-Termine]] und [[Saisonalität und Kalendereffekte]].

## Quellen

- NYSE: Holidays and Trading Hours – https://www.nyse.com/markets/hours-calendars
- NYSE: Opening and Closing Auctions Fact Sheet (2024) – https://www.nyse.com/publicdocs/nyse/markets/nyse/NYSE_Opening_and_Closing_Auctions_Fact_Sheet.pdf
- Nasdaq Trader: Opening and Closing Crosses – https://nasdaqtrader.com/Cross
- Alpaca Docs: Orders at Alpaca (Extended Hours, Overnight) – https://docs.alpaca.markets/docs/orders-at-alpaca
- BMLL: Into the Close – U.S. Closing Auction Dynamics (2025) – https://www.bmlltech.com/news/market-insight/into-the-close-unpacking-u-s-closing-auction-dynamics-and-the-impact-of-the-russell-reconstitution
- State Street Global Advisors: Closing time – How passive investing is reshaping equity market microstructure – https://www.ssga.com/us/en/institutional/insights/how-passive-investing-reshaping-microstructure
- Admati, Pfleiderer (1988): A Theory of Intraday Patterns: Volume and Price Variability, Review of Financial Studies 1(1) – https://doi.org/10.1093/rfs/1.1.3
- Jain, Joh (1988): The Dependence between Hourly Prices and Trading Volume, JFQA 23(3), S. 269–283 – https://ideas.repec.org/r/cup/jfinqa/v23y1988i03p269-283_01.html
- McInish, Wood (1992): An Analysis of Intraday Patterns in Bid/Ask Spreads for NYSE Stocks, Journal of Finance 47(2) – https://doi.org/10.1111/j.1540-6261.1992.tb04408.x
- timeanddate.com: USA beginnt Sommerzeit 2026 – https://www.timeanddate.com/news/time/usa-start-dst-2026.html
- TIME (07.10.2026): Most Americans Want to Stop Changing the Clocks. Here's Why Senators Are Hesitating – https://time.com/article/2026/10/07/senate-permanent-daylight-saving-time-sunshine-protection-act/
- Congressional Research Service: Daylight Saving Time – https://www.congress.gov/crs-product/R45208
- Harvard Law School Forum (21.10.2026): NYSE Arca and Nasdaq to Launch Extended Trading – https://corpgov.law.harvard.edu/2026/10/21/nyse-arca-and-nasdaq-to-launch-extended-trading-what-companies-should-consider/
- Nasdaq: 23/5 Trading Information Hub – https://www.nasdaq.com/products/north-american-markets/market-structure-policy/24-hour-trading-hub
