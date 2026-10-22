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

# Indikatoren

Die sechs gängigsten technischen Indikatoren mit Formel, Standardwerten, Nutzen im Day Trading und typischen Fallen: gleitende Durchschnitte (SMA/EMA), VWAP, RSI, ATR, MACD und Bollinger Bands. Alle sind Rechnungen aus Kurs (und teils Volumen) der Vergangenheit; sie wissen nichts, was der Chart nicht schon zeigt.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Überblick

| Indikator | Formel (kurz) | Standard | Misst | Im Day Trading brauchbar für |
| --- | --- | --- | --- | --- |
| SMA | Summe der letzten n Schlüsse / n | 20, 50, 200 (Tag) | Trend, geglättet | Trendrichtung im Tageschart, Level |
| EMA | (Schluss − EMA vorher) × 2/(n+1) + EMA vorher | 9, 20 (intraday üblich) | Trend, schneller | Trend im 5-Minuten-Chart |
| VWAP | Σ(typischer Preis × Volumen) / ΣVolumen, ab 9:30 | täglich neu | fairer Durchschnittspreis des Tages | Bezugslinie: über/unter VWAP |
| RSI | 100 − 100 / (1 + Ø Gewinn / Ø Verlust) | 14, Grenzen 70/30 | Schwung, überkauft/überverkauft | Filter, nicht Signal |
| ATR | Ø der True Range | 14 | Schwankungsbreite, keine Richtung | Stop-Abstand, Positionsgröße |
| MACD | EMA 12 − EMA 26; Signal = EMA 9 davon | 12/26/9 | Trend und Schwung | wenig; viele Fehlsignale intraday |
| Bollinger Bands | SMA 20 ± 2 Standardabweichungen | 20, 2 | Schwankung um den Schnitt | Phasen enger Spanne (Squeeze) erkennen |

## Gleitende Durchschnitte (SMA, EMA)

- **SMA:** einfacher Durchschnitt der letzten n Schlusskurse. Beispiel 5er-SMA aus 11, 12, 13, 14, 15 = 13.
- **EMA:** gewichtet neuere Kurse stärker. Multiplikator 2/(n+1), beim 20er also 9,52 %. Start mit dem SMA der ersten n Werte; je mehr Vorlauf, desto genauer.
- **Verzögerung:** Beide hinken dem Kurs hinterher, längere mehr. Der EMA dreht früher als der SMA.
- **Evidenz:** Brock, Lakonishok und LeBaron (1992) fanden mit einfachen Durchschnitts- und Ausbruchsregeln im Dow Jones 1897–1986 deutlich bessere Renditen nach Kaufsignalen. In den folgenden zehn Jahren (1987–1996) war die beste Regel nicht mehr signifikant (Sullivan, Timmermann, White 1999), und schon geringe Handelskosten heben den Vorteil auf (Bajgrowicz, Scaillet 2012). Siehe [[Evidenz zu technischer Analyse]].
- **Day Trading:** Im Tageschart zeigt der 20er oder 50er, ob der Wert im Aufwärtstrend ist (Long-only: lieber mit dem Trend). Im 5-Minuten-Chart nutzen viele 9er und 20er EMA als „Trendschiene“; dafür gibt es keine belastbare Studie.

## VWAP

- **Formel:** VWAP = Σ(typischer Preis × Volumen) / Σ Volumen, typischer Preis = (Hoch + Tief + Schluss) / 3, kumuliert ab der Eröffnung.
- **Nur intraday:** setzt jeden Tag neu an, ist für Tagescharts nicht definiert.
- **Wer ihn nutzt:** Institutionen als Maßstab für ihre Ausführung: Kauf unter VWAP gilt als gut ausgeführt. Deshalb schauen viele auf ihn.
- **Fallen:** In den ersten Minuten springt er stark (wenige Daten). Später reagiert er kaum noch, weil das ganze Tagesvolumen drin steckt. Er ist kein Kursziel und kein Stop an sich.
- **Day Trading:** Häufige Praxis: Long nur, wenn der Kurs über VWAP liegt; Rücksetzer an VWAP als Einstieg. Siehe [[VWAP-Strategien]].

## RSI (Relative Strength Index)

- **Formel (Wilder):** RS = Ø Gewinn / Ø Verlust über n Perioden. Erste Durchschnitte einfach, danach geglättet: (Vorwert × 13 + aktueller Wert) / 14. RSI = 100 − 100 / (1 + RS).
- **Standard:** 14 Perioden, über 70 überkauft, unter 30 überverkauft. Wilder stellte ihn 1978 vor („New Concepts in Technical Trading Systems“).
- **Falle:** In starken Trends bleibt der RSI lange über 70 oder unter 30. Überkauft heißt dann Stärke, nicht Umkehr. Divergenzen gibt es in starken Trends viele, bevor es dreht.
- **Evidenz für „überverkauft dreht“:** Kurzfristige Umkehr gibt es in Aktien tatsächlich: Verlierer einer Woche erholten sich in der Folgewoche (Lehmann 1990), Verlierer eines Monats im Folgemonat (Jegadeesh 1990). Das betrifft Wochen bis Monate, nicht einen Day Trade, und Lo und MacKinlay (1990) erklären einen Teil anders. Siehe [[Mean Reversion und Oversold Bounce]].

## ATR (Average True Range)

- **True Range:** das Größte aus (Hoch − Tief), |Hoch − Schluss davor|, |Tief − Schluss davor|. So zählen Lücken mit.
- **ATR:** Durchschnitt der True Range, Standard 14, bei Wilder geglättet wie der RSI. Ebenfalls Wilder 1978.
- **Zeigt keine Richtung**, nur wie stark ein Wert normalerweise schwankt.
- **Day Trading:** der nützlichste Indikator für Risiko. Ein Stop enger als die normale Schwankung wird zufällig ausgelöst. Ein Stop von 1 bis 2 ATR (5-Minuten-ATR) unter dem Einstieg ist eine gängige Faustregel (Konvention, keine geprüfte Zahl). Siehe [[Stop-Platzierung]], [[Positionsgröße]].

### Beispielrechnung ATR-Stop

Wert bei $40,00, ATR der 5-Minuten-Kerzen $0,30. Stop 1,5 ATR = $0,45 unter dem Einstieg: $39,55.

| Rechnung | Ergebnis |
| --- | --- |
| Stücke nach Verlustlimit: $50 / $0,45 = 111 | 111 × $40 = $4.440, über dem Deckel |
| Positionsdeckel: $3.750 / $40 = 93,75 | **93 Aktien** = $3.720 |
| Risiko am Stop: 93 × 0,45 | $41,85 |
| Ziel 2R: 40,00 + 0,90 | $40,90 |

## MACD

- **Formel:** MACD-Linie = EMA 12 − EMA 26. Signallinie = EMA 9 der MACD-Linie. Histogramm = Differenz. Gerald Appel, späte 1970er.
- **Fallen:** Keine festen Grenzen für überkauft/überverkauft. Werte hängen vom Kurs ab, sind also zwischen Aktien nicht vergleichbar. Divergenzen sind in starken Trends häufig und unzuverlässig. Im 5-Minuten-Chart kreuzen sich die Linien oft.
- **Day Trading:** Er ist aus zwei EMAs gebaut, sagt also wenig, was die EMAs nicht schon zeigen. Als zusätzliches Signal meist überflüssig.

## Bollinger Bands

- **Formel:** Mitte = SMA 20; Bänder = SMA 20 ± 2 × Standardabweichung der letzten 20 Schlüsse. Von John Bollinger.
- **Inhalt:** Laut Bollinger liegen 88 bis 89 % der Kurse innerhalb der Bänder.
- **Squeeze:** Sehr enge Bänder zeigen eine ruhige Phase, nach der oft eine größere Bewegung kommt; die Richtung sagen sie nicht.
- **Falle:** Eine Berührung des oberen Bands ist ein „Tag“, kein Verkaufssignal. In Trends läuft der Kurs am Band entlang.

## Allgemeine Fallen

> [!warning] Mehr Indikatoren heißt nicht mehr Information
> - RSI, MACD, Bollinger und Durchschnitte rechnen alle aus denselben Schlusskursen. Wenn drei davon „bestätigen“, ist das meist dieselbe Information dreimal.
> - **Parameter-Fischen:** Wer RSI 9 statt 14 oder EMA 8 statt 9 nimmt, weil es im Chart besser aussah, betreibt Data Snooping. Siehe [[Backtesting und Overfitting]].
> - **Verzögerung:** Alle außer der ATR-Größe reagieren nach dem Kurs. Ein Signal kommt, wenn die Bewegung schon läuft.
> - **Ein Zeitrahmen:** Indikatoren auf 1-Minuten-Kerzen produzieren viel Rauschen. Im Vault gilt der 5-Minuten-Chart.

Was nach dem Stand der Forschung am ehesten taugt: Trendfilter auf längeren Zeitskalen (siehe [[Evidenz zu technischer Analyse]]) und die ATR für Stop und Größe. Beides ist Risikosteuerung, keine Vorhersage.

## Im Vault

- **`/trader-scanner daily`:** nutzt **RSI 14 nach Wilder auf Tagesschlüssen** (`oversold`: RSI unter 30; `oversold_bounce`: gestern unter 30, heute höher geschlossen) und den **SMA 20** (`reclaim_ma20`: gestern unter, heute über dem 20-Tage-Schnitt). Die RSI-Rechnung steht in `scan.py` (`rsi`).
- **`/trader-exit --stop atr:K`:** ATR aus den **5-Minuten-Kerzen der Sitzung bis zur Einstiegskerze**, 14 Kerzen (bei weniger Kerzen der Schnitt aller). Im Code (`exit.py`, `atr_of`) ist es der einfache Durchschnitt der letzten 14 True Ranges, nicht Wilders Glättung; die erste Kerze des Tages zählt nur Hoch minus Tief, ohne Übernacht-Lücke. Ein ATR-Stop um 10:15 beruht also auf nur 9 Kerzen.
- **VWAP, EMA, MACD, Bollinger:** berechnet kein Skill. Wer sie nutzt, liest sie aus einem Chart-Tool ab und notiert den Wert im Journal-Eintrag.
- **Time Machine:** prüft nur die Quoten von Stop und Ziel; ob ein Indikator den Trade verbessert, misst sie nicht.

Verwandt: [[Volumen und relatives Volumen]], [[Unterstützung und Widerstand]], [[Pullback im Trend]], [[Strategien im Vergleich]].

## Quellen

- StockCharts ChartSchool, „Moving Averages – Simple and Exponential“: https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential
- StockCharts ChartSchool, „Volume-Weighted Average Price (VWAP)“: https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/volume-weighted-average-price-vwap
- StockCharts ChartSchool, „Relative Strength Index (RSI)“: https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/relative-strength-index-rsi
- StockCharts ChartSchool, „Average True Range (ATR)“: https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-atr-and-average-true-range-percent-atrp
- StockCharts ChartSchool, „MACD“: https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator
- StockCharts ChartSchool, „Bollinger Bands“: https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/bollinger-bands
- Brock, Lakonishok, LeBaron (1992), „Simple Technical Trading Rules and the Stochastic Properties of Stock Returns“, Journal of Finance 47(5), 1731–1764: https://ideas.repec.org/a/bla/jfinan/v47y1992i5p1731-64.html
- Sullivan, Timmermann, White (1999), „Data-Snooping, Technical Trading Rule Performance, and the Bootstrap“, Journal of Finance 54(5), 1647–1691: https://ideas.repec.org/p/fmg/fmgdps/dp303.html
- Bajgrowicz, Scaillet (2012), „Technical trading revisited: False discoveries, persistence tests, and transaction costs“, Journal of Financial Economics 106(3), 473–491: https://ideas.repec.org/a/eee/jfinec/v106y2012i3p473-491.html
- Lehmann (1990), „Fads, Martingales, and Market Efficiency“, Quarterly Journal of Economics 105(1), 1–28: https://www.nber.org/papers/w2533
- Jegadeesh (1990), „Evidence of Predictable Behavior of Security Returns“, Journal of Finance 45(3); Zusammenfassung zur kurzfristigen Umkehr bei Alpha Architect: https://alphaarchitect.com/quantitative-momentum-research-short-term-return-reversal/
- Lo, MacKinlay (1990), „When Are Contrarian Profits Due to Stock Market Overreaction?“, Review of Financial Studies 3(2), 175–205: https://web.mit.edu/Alo/www/Papers/lo-mackinlay-90b.html
- Skills: `.claude/skills/trader-scanner/scan.py` (`rsi`, `find_setups`), `.claude/skills/trader-exit/exit.py` (`atr_of`), `.claude/skills/trader-exit/SKILL.md`
