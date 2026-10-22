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

# VWAP-Strategien

Der VWAP (Volume Weighted Average Price) ist der volumengewichtete Durchschnittspreis eines Handelstags. Day Trader nutzen ihn als Trendfilter und als Marke für Einstiege. Die Notiz erklärt, warum Institutionen auf ihn schauen, welche drei Long-Setups üblich sind und was die Evidenz hergibt.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Definition

VWAP = Summe aus (Preis × Volumen) aller Trades ÷ Summe des Volumens, gerechnet ab der Eröffnung. Chartprogramme nähern das auf Bars an; die genaue Rechnung unterscheidet sich je Plattform. Der VWAP beginnt jeden Tag neu. Er ist deshalb ein reines Intraday-Werkzeug und taugt wenig für dünn gehandelte Aktien.

| Eigenschaft | Folge |
| --- | --- |
| startet bei 9:30 neu | am Morgen springt er stark, nachmittags bewegt er sich kaum noch |
| gewichtet nach Volumen | Kurse mit viel Umsatz zählen mehr |
| mit oder ohne Pre-Market | die Studie unten rechnet ohne Pre- und After-Market. Vor dem Vergleich klären, welcher VWAP gemeint ist |

## Warum Institutionen auf den VWAP schauen

- **Ausführungs-Benchmark**: Pensionsfonds und Fonds lassen große Orders oft über den Tag verteilt „zum VWAP“ ausführen. Wer besser als der VWAP kauft, hat gut ausgeführt. Die erste VWAP-Ausführung wird James Elkins (Abel Noser) 1984 für den Pensionsfonds von Ford zugeschrieben. Berkowitz, Logue und Noser haben den VWAP 1988 im *Journal of Finance* als Maß für Transaktionskosten an der NYSE beschrieben.
- **Anteil**: Zarattini und Aziz schreiben, VWAP-Orders machten rund 50 % des Handels institutioneller Anleger aus. Die Zahl stammt aus ihrer Literaturangabe, wir konnten sie nicht unabhängig prüfen.
- **Kritik**: Der VWAP ist als Benchmark leicht zu „spielen“ und bei einzelnen Trades zu grob.

Daraus folgt die verbreitete Trader-Logik: Liegt der Kurs über dem VWAP, haben die Käufer des Tages im Schnitt Gewinn, und Institutionen, die „unter VWAP“ kaufen wollen, stützen Rücksetzer. Das ist eine plausible Erzählung, kein Gesetz.

## Drei Long-Setups

### 1. VWAP als Filter

Nur long, wenn der Kurs über dem VWAP liegt. Das ist kein eigenes Signal, sondern ein Filter für andere Setups (ORB, Pullback). Aziz beschreibt: Eine Aktie, die nach einem Fehlausbruch unter den VWAP fällt, bleibt oft darunter. Eine, die darüber gedrückt wurde, bleibt oft darüber.

### 2. VWAP-Reclaim

1. Die Aktie fällt unter den VWAP (oft nach einem starken Start).
2. Ein Bar **schließt** wieder über dem VWAP, idealerweise mit mehr Volumen als die Bars des Rücksetzers.
3. Strengere Variante: auf einen Retest warten (Kurs berührt den VWAP, schließt darüber) und erst über dem Hoch dieser Kerze kaufen.
4. Stop unter dem Tief des VWAP-Tests.

Laut Scanz gilt: Je länger der Kurs unter dem VWAP lag, desto seltener hält der Reclaim. An Seitwärtstagen pendelt der Kurs um den VWAP, und Reclaims scheitern reihenweise.

### 3. Pullback zum VWAP

1. Aktie im Aufwärtstrend über dem VWAP.
2. Rücksetzer bis an den VWAP, der dort hält (Kerze schließt darüber).
3. Einstieg über dem Hoch der Abprallkerze.
4. Stop knapp unter dem VWAP oder unter dem Tief der Abprallkerze. TradeZella nennt z. B. etwa 0,2 % unter dem VWAP.

Verwandt mit dem Pullback an EMAs: [[Pullback im Trend]].

## Evidenz

### Zarattini und Aziz (2023): VWAP Trend Trading

Die bekannteste Studie testet die einfachste Regel: ab 9:31 long, wenn QQQ über dem VWAP liegt, short darunter. Ausstieg, sobald eine 1-Minuten-Kerze auf der anderen Seite schließt, sonst zum Handelsschluss. Zeitraum 2. Januar 2018 bis 28. September 2023.

| Kennzahl | VWAP-Strategie QQQ | QQQ Buy and Hold |
| --- | --- | --- |
| Gesamtrendite (netto Kommission) | 671 % ($25.000 → $192.656) | 126 % |
| max. Drawdown | 9,4 % | 37 % |
| Sharpe | 2,1 | 0,7 |
| Trades | 21.967 | 1 |
| Trefferquote je Trade | 17,0 % | – |
| Gewinn : Verlust je Trade | 5,67 | – |

- Mit dem 3-fach gehebelten TQQQ kamen sie auf 8.242 %, mit einem Drawdown von 36 %.
- Gleitende Durchschnitte (9 bis 200 Perioden) als Filter schnitten im selben Test schlechter ab als der VWAP.

> [!warning] Wie belastbar ist das?
> - **Kosten**: angesetzt nur $0,0005 Kommission je Aktie, kein Spread, kein Slippage. Die Autoren schreiben selbst, dass höhere Kommissionen das Ergebnis deutlich verschlechtern. Bei rund 22.000 Trades in knapp sechs Jahren zählt jeder Cent.
> - **Ein Markt, kein Out-of-Sample**: nur QQQ und TQQQ, ein Zeitraum. Eine Nachbildung auf QuantConnect kam auf ein anderes Endkapital (etwa $173.000), das Ergebnis hängt also an Details der Umsetzung.
> - **Volle Investition, auch short**: Jede Position nutzt 100 % des Kapitals, die Hälfte der Trades ist short. Beides geht bei uns nicht.
> - **Trefferquote 17 %**: Die Strategie lebt von wenigen großen Trendtagen. Das muss man psychisch aushalten: 8 von 10 Trades verlieren.
> - Die Autoren nennen es selbst „kein fertiges Handelssystem“.

Für den VWAP-Reclaim und den Pullback zum VWAP bei Einzelaktien haben wir **keine Studie mit Zahlen** gefunden. Die Regeln stammen aus Trader-Blogs und Büchern (Aziz, Scanz, Trade-Ideas, TradeZella). Die Zahlen oben gelten für den Index-ETF mit Short-Seite und Halten bis zum Schluss, nicht für einzelne Reclaim-Trades.

## Beispielrechnung mit unseren Limits

Fiktive Aktie: VWAP $39,80, Kurs fällt bis $39,60, ein 5-Min-Bar schließt bei $39,95 wieder über dem VWAP.

| Größe | Rechnung | Wert |
| --- | --- | --- |
| Stop unter dem Test-Tief | | $39,59 |
| Risiko je Aktie | 39,95 − 39,59 | $0,36 |
| Stückzahl nach Verlustlimit | floor(50 / 0,36) | 138 Aktien = $5.513 |
| Positions-Cap 75 % von $5.000 | floor(3.750 / 39,95) | **93 Aktien** |
| Max. Verlust am Stop | 93 × 0,36 | $33,48 |
| Ziel 2R | 39,95 + 0,72 | $40,67 |

> [!tip] Enge Stops treffen auf das Positions-Cap
> VWAP-Setups haben oft enge Stops. Dann begrenzt nicht das Verlustlimit von $50 die Größe, sondern das Positions-Cap von $3.750. `/trader-budget` sagt, welches Limit entschieden hat. Siehe [[Positionsgröße]].

## Im Vault

- **Kein Skill rechnet den VWAP.** `/trader-scanner` und `/trader-entry` arbeiten mit Range-Hoch oder einem festen Level, nicht mit einer Linie, die sich bewegt. VWAP-Setups muss man am Chart (z. B. TradingView oder Alpaca) selbst ablesen.
- **Halbautomatisch**: Den VWAP-Wert ablesen und mit `/trader-entry TICKER --setup level --level <VWAP>` auf einen Schlusskurs darüber warten. Weil der VWAP wandert, ist das nur eine Näherung. Kurz vor dem Signal neu ablesen.
- **`/trader-exit`**: Bei einem Level-Setup braucht es einen eigenen Stop (`price:X` unter dem Test-Tief). Ein Risiko unter 0,05 % des Kurses lehnt der Skill als zu eng ab.
- **Filter für ORB**: Ein ORB-Signal über dem VWAP ist in der Logik von Aziz stärker als eines darunter. Bei einem Ausbruch über das Range-Hoch liegt der Kurs fast immer schon über dem VWAP, weil der VWAP ein Durchschnitt der bisherigen Kurse ist. Als Zusatzfilter bringt er beim ORB also wenig; belegt ist ein Nutzen nicht.
- **Zeitfenster**: Die Studie steigt um 9:31 ein. Bei uns gehen Einstiege erst ab 9:45, und um 15:55 muss alles geschlossen sein. Die großen Trendtage der Studie laufen oft bis 16:00.
- Indikatoren allgemein: [[Indikatoren]]. Vergleich: [[Strategien im Vergleich]].

## Quellen

- Zarattini, Aziz (2023): Volume Weighted Average Price (VWAP): The Holy Grail for Day Trading Systems, SSRN 4631351 – https://ssrn.com/abstract=4631351 (Volltext: https://concretumgroup.com/wp-content/uploads/2026/02/Volume-Weighted-Average-Price.pdf)
- Concretum: Zusammenfassung des VWAP-Papers – https://concretumgroup.com/volume-weighted-average-price-vwap-the-holy-grail-for-day-trading-systems/
- QuantConnect: Nachbildung des VWAP-Papers (Backtest-Ergebnis) – https://www.quantconnect.com/terminal/cache/embedded_backtest_0cab7e083e99d5a372e02fe882bbf078.html
- Wikipedia: Volume-weighted average price (Formel, Elkins 1984, Berkowitz/Logue/Noser 1988) – https://en.wikipedia.org/wiki/Volume-weighted_average_price
- Plan Sponsor: VWAP: Benchmark Or Millstone? (Kritik am VWAP als Benchmark) – https://plansponsor.com/?p=44512
- Aziz, How to Day Trade for a Living (Zitate zu VWAP und EMA-Trend) – https://www.goodreads.com/work/quotes/52463925
- Scanz: VWAP Trading Strategy (Reclaim, Volumen, Seitwärtstage) – https://scanz.com/vwap-trading-strategy/
- Trade-Ideas: VWAP Trading Strategy (Reclaim, Stop unter dem Test-Tief) – https://www.trade-ideas.com/learning-center/trading-strategies/vwap-trading-strategy/
- TradeZella: VWAP Trading Strategy – 4 Setups (Pullback, Stop-Varianten) – https://www.tradezella.com/blog/vwap-trading-strategy
- Skills im Vault: `.claude/skills/trader-entry/SKILL.md`, `trader-exit/SKILL.md`, `trader-budget/SKILL.md`
