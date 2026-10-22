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

# Bull Flag

Die Bull Flag ist eine kurze Pause nach einem steilen Anstieg: erst die Fahnenstange, dann eine enge, leicht fallende oder seitliche Flagge, dann (vielleicht) der Ausbruch nach oben. Diese Notiz beschreibt die klassischen Regeln, die Zahlen dazu und genau, was der Scanner im Vault unter `bull_flag` versteht.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Aufbau

| Teil | Klassische Regel (Tageschart, Bulkowski) | Übliche Praxis im Intraday-Chart | Scanner `bull_flag` |
| --- | --- | --- | --- |
| Fahnenstange | ungewöhnlich steiler Anstieg über mehrere Tage | schneller Lauf über wenige 1- oder 5-Minuten-Kerzen, meist mit Katalysator | Schlusskurs mehr als 10 % höher als 10 Sitzungen davor |
| Flagge | kleines Rechteck oder Kanal, oft gegen den Trend geneigt, unter 3 Wochen | 2 bis 10 Kerzen, flach oder leicht fallend, hält meist über VWAP | letzte 5 Schlusskurse innerhalb von 5 % |
| Volumen | fällt in der Flagge (bei 74 % der Aufwärtsausbrüche) | hoch in der Stange, niedrig in der Flagge, wieder hoch am Ausbruch | wird nicht geprüft |
| Ausbruch | Schluss über der oberen Flaggenlinie | erste Kerze, die über dem Flaggenhoch schließt | wird nicht geprüft |

Weitere Merkmale nach Bulkowski: Enge, saubere Flaggen laufen besser als lockere, die über ihre Linien stechen, Lücken haben oder zackig aussehen. Am besten liefen Flaggen, die gegen den Trend nach unten geneigt waren. Ausbruchsrichtung bei Flaggen auf dem Tageschart: 60 % nach oben, also auch 40 % nach unten.

Eine Faustregel aus Praxisquellen: Die Flagge soll höchstens etwa die Hälfte der Stange zurückgeben, idealerweise nur 10 bis 25 %. Das ist eine Konvention, keine geprüfte Zahl.

### Sonderfall High and Tight Flag

Bulkowskis „High and Tight Flag“ ist eine eigene, seltene Form: Der Kurs muss sich in höchstens zwei Monaten fast verdoppeln (mindestens +90 %), danach folgt eine Pause. Bestätigt ist sie erst mit einem Schluss über dem höchsten Punkt des Musters. Für Day Trading ist sie kaum relevant, aber sie zeigt, wie unterschiedlich „Flagge“ definiert wird.

## Was die Zahlen sagen

Bulkowskis Statistik für Flaggen (Tageschart, Bullenmarkt, „hunderte“ Fälle, Stand 2020):

| Kennzahl | Ausbruch nach oben |
| --- | --- |
| Ausbruch nach oben | 60 % |
| Break-even-Fehlerquote (weniger als 5 % Anstieg) | 44 % |
| Durchschnittlicher Anstieg (bis zum nächsten kleinen Hoch) | 9 % |
| Kursziel (Messregel) erreicht | 46 % |
| Rang | nicht gerankt |

Über die Jahrzehnte wurde es schlechter: Der durchschnittliche Anstieg nach Aufwärtsausbrüchen aus Flaggen lag in den 1990ern bei 14 %, in den 2000ern bei 12 %, in den 2010ern bei 6 % (Median 9 %, 7 %, 4 %). Wimpel (Pennants, die dreieckige Schwester) sind noch schwächer: 54 % Fehlerquote, 7 % Anstieg im Schnitt.

> [!warning] Die Flagge ist fast ein Münzwurf
> Fast jede zweite Flagge (44 %) schafft nach dem Ausbruch nicht einmal 5 %, und nur 46 % erreichen das Kursziel der Messregel. Ratgeber nennen oft „60 bis 70 % Erfolg“, ohne Quelle. Für die Intraday-Flagge auf 1- oder 5-Minuten-Charts gibt es keine belastbare öffentliche Studie, die ich gefunden habe.

Wichtige Einschränkungen dieser Zahlen:

- Bulkowski misst ab der Eröffnung am Tag nach dem Ausbruch bis zu einem Hoch, das man erst hinterher kennt. Das ist kein handelbares Ergebnis, Kosten und Stops fehlen.
- Die Stichprobe ist von Hand ausgewählt („perfect trades“), die Definition bleibt teils Ermessenssache.
- Ein Vergleich mit zufälligen Einstiegen im selben Markt wird auf den gelesenen Seiten nicht gezeigt. Im Bullenmarkt steigt auch ein zufälliger Kauf oft.

Siehe [[Evidenz zu technischer Analyse]] und [[Chartformationen]].

## Einstieg, Stop, Kursziel

1. **Einstieg:** Schluss einer Kerze über dem Flaggenhoch (bei der klassischen Variante über der oberen Trendlinie). Ein Docht darüber reicht nicht. Aggressiver: Kauf schon in der Flagge; das gibt ein besseres CRV, aber mehr Fehlsignale.
2. **Stop:** unter dem Tief der Flagge. Enger (unter der Flaggenmitte) heißt mehr Stücke, aber mehr Ausstopper durch normales Wackeln. Siehe [[Stop-Platzierung]].
3. **Kursziel (Messregel):** Höhe der Stange messen, nach Bulkowski mit der Trefferquote (46 %) multiplizieren und auf das Flaggentief aufschlagen. Die volle Stangenhöhe ab Ausbruch ist das optimistische Ziel. Im Day Trading ist ein festes Ziel in R ehrlicher, weil die volle Stange bis 15:55 selten erreicht wird.
4. **Volumen:** Am Ausbruch sollte das Volumen steigen. Bulkowskis Auswertung zu hohem Ausbruchsvolumen nennt die normale Flagge allerdings gar nicht, und für die High and Tight Flag lief geringes Ausbruchsvolumen sogar besser. Volumen ist hier ein Hinweis, kein Beweis. Siehe [[Volumen und relatives Volumen]].

### Beispielrechnung mit den Limits

Annahme (frei gewählt, keine echte Aktie): Ein Wert läuft am Vormittag von $36,00 auf $40,00 (Stange $4,00). Die Flagge pendelt zwischen $39,20 und $39,80.

| Größe | Rechnung | Ergebnis |
| --- | --- | --- |
| Einstieg | 5-Minuten-Kerze schließt bei $39,85 über $39,80 | $39,85 |
| Stop | unter dem Flaggentief | $39,15 |
| Risiko je Aktie | 39,85 − 39,15 | $0,70 |
| Stücke nach Verlustlimit | $50 / $0,70 = 71,4 | 71 Aktien |
| Positionswert | 71 × 39,85 | $2.829 (unter dem Deckel von $3.750 = 75 % von $5.000) |
| Ziel 2R | 39,85 + 2 × 0,70 | $41,25 |
| Ziel Messregel (Bulkowski) | 39,20 + 4,00 × 0,46 | $41,04 |
| Verlust am Stop | 71 × 0,70 | $49,70 (plus Slippage) |

Bei 2R muss der Trade ohne Kosten in gut einem Drittel der Fälle (1 von 3) das Ziel vor dem Stop erreichen, um bei null zu landen. Siehe [[R-Multiple und Erwartungswert]].

> [!tip] Vor dem Einstieg prüfen
> - Gibt es einen Grund für die Stange (News, Earnings)? Ohne Katalysator ist die Flagge oft nur Rauschen. Siehe [[Katalysatoren]].
> - Ist das relative Volumen hoch? Siehe [[Volumen und relatives Volumen]].
> - Liegt direkt über dem Ausbruch ein Widerstand (Vortageshoch, runde Zahl)? Dann ist das Ziel verbaut. Siehe [[Unterstützung und Widerstand]].
> - Ist der Stop weiter weg als $50 / Stückzahl erlaubt? Dann weniger Stücke, nie einen engeren Stop erzwingen.

## Typische Fallen

- **Tiefe Flagge:** Gibt die Flagge mehr als die Hälfte der Stange ab, ist es eher eine Umkehr als eine Pause.
- **Später Ausbruch:** Je länger die Flagge, desto schwächer der Schwung. Bulkowski: Flaggen sind kürzer als drei Wochen, sonst Rechteck. Intraday kommt dazu, dass das Volumen zur Mittagszeit typischerweise am niedrigsten ist (siehe [[Volumen und relatives Volumen]]); ob Flaggen dort schlechter laufen, ist nicht untersucht, aber plausibel.
- **Fehlausbruch:** Die Ausbruchskerze schließt knapp drüber, die nächste fällt zurück in die Flagge. Bei Flaggen bricht laut Bulkowski 40 % nach unten aus.
- **Rückblick-Fehler:** Im fertigen Chart sieht man nur die Flaggen, die funktioniert haben. Ein gutes Journal zählt auch die anderen.

## Im Vault

- **Scanner (`/trader-scanner daily`):** Der Setup-Name ist `bull_flag`. Die Regel steht in `.claude/skills/trader-scanner/scan.py` (`find_setups`) und nutzt nur Tagesschlusskurse, weil Yahoos Spark-Endpunkt keine Hochs und Tiefs liefert:
  - Stange: `c[-6] / c[-16] - 1 > 0,10`, also mehr als 10 % Anstieg vom Schluss vor 15 Sitzungen bis zum Schluss vor 5 Sitzungen.
  - Flagge: `(max(c[-5:]) - min(c[-5:])) / letzter Schluss < 0,05`, die letzten 5 Schlüsse liegen in einem Band von unter 5 %.
  - Nicht geprüft: Volumen, Neigung der Flagge, wie tief die Flagge unter dem Stangenhoch liegt (der Abstand zwischen `c[-6]` und der Flagge zählt nicht), ob ein Ausbruch stattfand. Filter vorher: Kurs ab $5, Vortagesvolumen ab 1 Mio. Stück.
  - Beispiel aus der Skill-Doku: Am 19.10.2026 meldete der Scan CCL und RCL als Flagge (Schlüsse bis 16.10.).
  - Ein Treffer heißt „passt zur Regel“, nicht „kaufen“.
- **Einstieg (`/trader-entry`):** Eine Flagge ist kein Opening Range Breakout. Sinnvoll ist `--setup level --level <Flaggenhoch>`; der Skill meldet die erste geschlossene Kerze über dem Level, frühestens ab 9:45. Optional `--min-volume-x`, siehe [[Volumen und relatives Volumen]] zur Tücke dieses Vergleichs.
- **Stop (`/trader-exit`):** Für ein Level-Setup gibt es keinen Standard-Stop, er muss genannt werden, zum Beispiel `--stop price:39.15` (unter der Flagge) oder `--stop atr:1.5`. Ziel `2R` oder `price:X`.
- **Time Machine:** Für Level-Setups gibt es nur die 10.000 Zufalls-Wiederholungen, keine Historie der eigenen Regel (die kennt nur `orb`). Die Wiederholungen ziehen zufällige Kerzen derselben Tageszeit; ein Vorteil des Musters steckt darin nicht.
- **Budget und Risiko:** `/trader-budget` rechnet die Stücke wie oben, `/trader-risk` prüft $50 je Trade, $150 je Tag, 3 Trades, CRV ≥ 1,0 und das Zeitfenster.
- **Journal:** Im Trade-Eintrag festhalten, ob die Flagge sauber war (Tiefe, Dauer, Volumen), damit [[Backtesting und Overfitting|die eigene Statistik]] später etwas aussagt.

Verwandt: [[Breakout aus 20-Tage-Hoch]], [[Momentum und Gap and Go]], [[Pullback im Trend]], [[Chartformationen]].

## Quellen

- Thomas Bulkowski, „Flags“, ThePatternSite (Statistik Stand 27.08.2020): https://thepatternsite.com/flags.html
- Thomas Bulkowski, „High and Tight Flags“, ThePatternSite: https://thepatternsite.com/htf.html
- Thomas Bulkowski, „Pennants“, ThePatternSite: https://thepatternsite.com/pennants.html
- Thomas Bulkowski, „Chart Pattern Performance over Decades“ (Stand 2019/2020): https://thepatternsite.com/TimePerformance.html
- Thomas Bulkowski, „Breakout Day Volume“: https://thepatternsite.com/volbkout.html
- Thomas Bulkowski, Glossar (Break-even-Fehlerquote, Ultimate High): https://thepatternsite.com/glossary.html
- CMC Markets, „Bull Flag Pattern: Complete Trading Guide“ (Praxisregeln Rücklauf 10–25 %, Volumen; nennt 60–70 % ohne Beleg): https://www.cmcmarkets.com/en/technical-analysis/bull-flag-pattern
- Scanner-Regel: `.claude/skills/trader-scanner/SKILL.md` und `scan.py` (Funktion `find_setups`)
- Einstieg, Stop, Time Machine: `.claude/skills/trader-entry/SKILL.md`, `.claude/skills/trader-exit/SKILL.md`, `.claude/skills/trader-timemachine/SKILL.md`
