---
typ: wissen
erstellt: 2026-10-22
aktualisiert: 2026-10-22
quelle: Recherche
tags:
  - trading
  - wissen
  - news
---

# Earnings-Saison

Viermal im Jahr legen die US-Firmen in wenigen Wochen ihre Quartalszahlen vor. Das sind die größten planbaren Kurssprünge einzelner Aktien. Die Notiz erklärt den Ablauf, die Lücken (Gaps), die implizierte Bewegung, die Post-Earnings-Announcement Drift und warum wir nie über einen Earnings-Termin hinweg halten.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]] · Verwandt: [[Katalysatoren]], [[Makro-Termine]], [[Marktlage Oktober 2026]]

## Ablauf einer Saison

| Phase | Wann (Faustregel) | Was passiert |
| --- | --- | --- |
| Quartalsende | 31.3., 30.6., 30.9., 31.12. (bei vielen Firmen) | Bücher werden geschlossen |
| Terminankündigung | meist 2–4 Wochen vorher | Pressemitteilung auf der Investor-Relations-Seite: Datum, Uhrzeit, Webcast |
| Auftakt | etwa zwei Wochen nach Quartalsende | große US-Banken eröffnen traditionell die Saison |
| Hauptwochen | etwa 3. bis 6. Woche nach Quartalsende | die meisten S&P-500-Firmen, darunter die großen Tech-Werte |
| Nachzügler | bis rund 8 Wochen danach | z. B. Nvidia (anderes Geschäftsjahr), Einzelhändler |
| Pflichtfrist 10-Q | 40 Tage (große und „accelerated“ Filer), 45 Tage (kleine) | geprüfte Quartalszahlen bei der SEC; 10-K: 60/75/90 Tage |

Die Phasen außer der 10-Q-Frist sind Erfahrungswerte, keine Regel. Den genauen Termin nennt nur die Firma selbst in ihrer Ankündigung, nicht die SEC.

### Ein Bericht im Detail

| Schritt | Vor Börsenbeginn (BMO) | Nach Börsenschluss (AMC) |
| --- | --- | --- |
| Pressemitteilung + 8-K Item 2.02 | meist zwischen 6:00 und 8:00 ET (12:00–14:00 MEZ) | meist ab 16:00 ET (22:00 MEZ) |
| Telefonkonferenz (Call) | kurz danach, oft vor 9:30 ET | meist 16:30–17:30 ET |
| erste Reaktion | Vorbörse, Gap zur Eröffnung | nachbörslich, Gap am nächsten Morgen |
| reguläre Reaktion | ab 9:30 ET am selben Tag | ab 9:30 ET am Folgetag |

Die Uhrzeiten sind typische Werte. Microsoft zum Beispiel veröffentlicht am 28.10.2026 nach Börsenschluss, der Call beginnt um 14:30 Pacific (17:30 ET). Zur Zeitverschiebung siehe [[Makro-Termine]] und [[Handelszeiten und Sessions]].

## Was der Markt vergleicht

- **Konsens:** Durchschnitt der Analystenschätzungen für Gewinn je Aktie (EPS) und Umsatz. „Beat“ heißt über, „Miss“ unter dem Konsens.
- **Guidance:** der Ausblick für das nächste Quartal oder Jahr. Er ist oft wichtiger als die abgelaufenen Zahlen.
- **Qualität:** Kommt der Gewinn aus dem Geschäft oder aus Einmaleffekten? `/trader-analyst` markiert, wenn der Nettogewinn über dem operativen Gewinn liegt.

> [!info] Fast alle schlagen die Erwartung
> Laut FactSet übertrafen im Schnitt der letzten fünf Jahre 78 % der S&P-500-Firmen die EPS-Schätzung, über zehn Jahre 77 %. Analysten senken ihre Schätzungen vor den Zahlen gern etwas, deshalb ist ein „Beat“ der Normalfall und kein Grund zum Kaufen. In der laufenden Saison (Stand 16.10.2026, 9 % berichtet) lagen 84 % über der Schätzung, aber nur um 2,6 % im Schnitt statt der üblichen 7,5 %.

### „Beat“ und trotzdem Minus: Beispiele aus dieser Woche

Laut der Marktzusammenfassung von Capp Notes für den 21.10.2026:

- Lam Research: Zahlen über Erwartung, Ausblick angehoben, nachbörslich trotzdem rund −6,3 %
- AT&T: Erwartung übertroffen, Ausblick angehoben, −6,45 % im regulären Handel
- Lithia Motors: bereinigter Gewinn $10,34 statt erwarteter $9,79, trotzdem −10,15 %
- Netflix: schwächere Gewinnprognose fürs vierte Quartal, −5,31 % auf ein 52-Wochen-Tief

Die Lehre: Die Richtung der Reaktion lässt sich aus der Schlagzeile „beats estimates“ nicht ablesen. Siehe [[News richtig lesen]].

## Gaps und implizierte Bewegung

Weil Zahlen außerhalb der Handelszeit kommen, öffnet die Aktie oft mit einer Lücke. Wie groß der Markt den Sprung erwartet, zeigt der Optionsmarkt:

**Implizierte Bewegung (Expected Move) ≈ 0,85 × Preis des At-the-Money-Straddles** (Call + Put zum Kurs, erster Verfall nach dem Termin). Der Faktor 0,85 ist eine Faustregel für etwa eine Standardabweichung, kein exaktes Ergebnis.

Beispiel: Aktie $100, Straddle für den Freitag nach den Zahlen kostet $8,00 → erwartete Bewegung ≈ $6,80 oder ±6,8 %. In etwa zwei Dritteln der Fälle bleibt der Sprung laut dieser Faustregel kleiner, in einem Drittel größer, und in welche Richtung, sagt der Straddle nicht.

> [!tip] Wir handeln keine Optionen
> `allow_options` ist bei uns aus. Den Straddle-Preis kann man sich trotzdem bei einem Broker oder Datendienst ansehen, als Maß dafür, wie viel Unruhe der Markt erwartet. Die Skills holen diese Zahl nicht.

## Post-Earnings-Announcement Drift (PEAD)

| Studie | Befund |
| --- | --- |
| Ball & Brown (1968) | Kurse laufen nach der Meldung noch länger in Richtung der Gewinnüberraschung. Erste Beschreibung der Drift. |
| Bernard & Thomas (1989) | Drift nach guten und schlechten Überraschungen über mindestens 60 Handelstage; Long-Short nach Überraschungsdezilen war in 41 von 48 Quartalen positiv (Stichprobe ab 1974). Deutung: verzögerte Reaktion, nicht Risikoprämie. |
| Bernard & Thomas (1990) | Ein Teil der Drift fällt in die Tage um die **nächsten** Zahlen: Anleger unterschätzen, wie sich Gewinne von Quartal zu Quartal fortsetzen. |
| Frazzini & Lamont (2007) | Aktien steigen im Schnitt rund um ihre Earnings-Termine (Earnings Announcement Premium), verbunden mit dem Volumensprung und Käufen kleiner Anleger. |
| Kettell, McInnis & Zhao (2022) | Spanne zwischen höchster und niedrigster Überraschungsgruppe fiel von etwa 5 % (1980er/90er) auf 3 % oder weniger (späte 2010er). |
| Martineau (2022), „Rest in Peace PEAD“ | Für Aktien außer Microcaps seit etwa 2006 keine Drift mehr; Preise passen sich heute am Tag der Meldung an. |
| Hirshleifer, Peng & Wang (2025); Dickerson, Julliard & Mueller (2025) | Finden weiter Drift, aber ohne Microcaps auszuschließen. |
| Subrahmanyam (2025, Working Paper) | Nachrechnung 2001–2024: t-Wert 2,18 mit allen Aktien, 1,43 ohne Microcaps (nicht signifikant). Streit liegt vor allem am Studiendesign. |

**Ehrliches Fazit:** PEAD war eine der robustesten Anomalien. Für liquide, größere Aktien ist sie heute schwach oder weg, übrig bleibt sie am ehesten bei Microcaps, die teuer und schwer zu handeln sind. Für einen Day Trader ist sie ohnehin kaum nutzbar: Die Drift verteilt sich über Wochen, wir sind jeden Abend flat.

## Warum „über Earnings halten“ zu unseren Regeln nicht passt

1. **Flat bis 15:55.** Unsere Regeln verbieten Übernacht-Positionen. Eine Meldung nach Börsenschluss trifft uns also nie, solange wir uns daran halten.
2. **Ein Stop schützt nicht vor einem Gap.** Beispiel: 50 Aktien zu $80, Stop $79 (Risiko $50 = 1R). Zahlen enttäuschen, die Aktie öffnet bei $70. Der Stop füllt etwa bei $70: Verlust $500 = −10R, mehr als das Dreifache des Tageslimits von $150.
3. **Die Quoten der Time Machine gelten nicht.** `/trader-timemachine` simuliert aus den letzten 60 Tagen. Der Earnings-Tag ist ein Ausreißer, den diese 60 Tage nicht abbilden.
4. **Der Erwartungswert ist unklar.** Wie oben: 84 % Beats, aber die Kurse fallen trotzdem häufig. Ein Münzwurf mit fetten Rändern ist kein Setup mit positivem Erwartungswert. Siehe [[R-Multiple und Erwartungswert]].

### Was geht: der Tag nach den Zahlen

Am Tag nach einem Bericht ist die Aktie oft ein „Stock in Play“ mit hohem relativen Volumen, gut für einen [[Opening Range Breakout]] oder [[Momentum und Gap and Go]]. Die Spanne ist aber breit, also wird die Position klein:

| | Normaler Tag | Tag nach Earnings |
| --- | --- | --- |
| Opening Range (15 Min) | $53,00–$54,20 | $51,00–$53,60 |
| Einstieg (Schluss über Range-Hoch) | $54,30 | $53,70 |
| Stop (Range-Mitte, abgerundet) | $53,60 | $52,30 |
| Risiko je Aktie | $0,70 | $1,40 |
| Aktien bei $50 Max-Verlust | 71 → aber Positionsdeckel 75 % von $5.000 = $3.750 → **69** | **35** (Risiko $49) |
| Positionswert | $3.746,70 | $1.879,50 |
| Ziel 2R | $55,70 | $56,50 |

Die Zahlen sind ausgedacht und zeigen nur die Rechnung, wie `/trader-budget` sie macht. Siehe [[Positionsgröße]] und [[Stop-Platzierung]].

> [!warning] Zahlen vor Börsenbeginn
> Meldet eine Firma vor 9:30 ET, läuft der Tag selbst schon mit dem Gap. Unser Einstiegsfenster beginnt erst 9:45, die 15-Minuten-Range ist dann gebildet. Trotzdem: Der Call kann noch während der ersten Minuten laufen und den Kurs drehen.

## Die laufende Saison (Q3 2026, Stand 22.10.2026)

Momentaufnahme, Details in [[Marktlage Oktober 2026]]:

- FactSet (16.10.): 9 % der S&P-500-Firmen berichtet; Gewinnwachstum (blended) +29,0 % gegenüber Vorjahr, Umsatz +12,6 %; Energie, IT, Kommunikation und Grundstoffe führen; Gesundheit einziger Sektor mit Rückgang.
- Nächste große Termine: Microsoft 28.10. nach Börsenschluss (bestätigt), Alphabet voraussichtlich 28.10. (nicht von der Firma bestätigt), Amazon 29.10. nach Börsenschluss (Call 17:00 ET, bestätigt), Apple 2.11. nach Börsenschluss (bestätigt), Nvidia voraussichtlich 18.11. (nicht bestätigt).
- Die nächste Saison (Q4 2026) beginnt etwa Mitte Januar 2027.

## Im Vault

- **`/trader-analyst`** liest die gemeldeten Zahlen direkt aus SEC EDGAR (XBRL aus 10-Q/10-K plus das letzte 8-K mit Item 2.02) und vergleicht jedes Quartal mit dem Vorjahresquartal. Den **nächsten** Termin kennt die SEC nicht: Er kommt aus `/trader-news`-Schlagzeilen oder von der IR-Seite, mit Quelle.
- **`/trader-news`** taggt Meldungen mit `earnings` (Stichwörter oder 8-K Item 2.02) und markiert Item 2.02 als wichtig.
- **Vor jedem Trade fragen:** Berichtet die Firma heute nach Schluss oder morgen früh? Wenn ja, ist ein Day Trade bis 15:55 möglich, aber das Gap-Risiko darf nicht über Nacht mitgenommen werden. `/trader-alerts` erinnert an 15:55.
- **Journal:** Im [[Trading/Regeln|Regelwerk]] gibt es keine eigene Earnings-Regel. Wenn sich zeigt, dass Trades an Earnings-Tagen schlechter laufen, gehört das in [[Gedächtnis/Erkenntnisse/Trading]] und dann als eigene Regel ins Regelwerk.

## Quellen

- SEC: [Form 10-Q – Fristen nach Filer-Kategorie](https://www.sec.gov/answers/form10q.htm)
- FactSet: [S&P 500 Earnings Season Update: October 16, 2026](https://insight.factset.com/sp-500-earnings-season-update-october-16-2026); [Übersicht der Earnings-Artikel](https://insight.factset.com/topic/earnings)
- Capp Notes: [Closing Look – Wednesday, October 21, 2026](https://cappnotes.substack.com/p/closing-look-wednesday-october-21) (Reaktionen Lam Research, AT&T, Lithia, Netflix)
- Microsoft-Termin: [Microsoft announces quarterly earnings release date (finviz/PR Newswire)](https://finviz.com/news/400058/microsoft-announces-quarterly-earnings-release-date)
- Amazon-Termin: [Amazon.com to Webcast Third Quarter 2026 Financial Results Conference Call](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-to-Webcast-Third-Quarter-2026-Financial-Results-Conference-Call/default.aspx)
- Apple-Termin: [Apple to Report Q4 2026 Earnings on November 2 – MacRumors](https://www.macrumors.com/2026/10/06/apple-q4-2026-earnings-nov-2/)
- Alphabet/Nvidia (unbestätigt): [MarketBeat – Alphabet Q3 2026](https://www.marketbeat.com/earnings/reports/2026-10-28-alphabet-inc-stock/); [Wall Street Horizon – Nvidia](https://www.wallstreethorizon.com/nvidia-earnings-calendar)
- Implizierte Bewegung: [Barchart – Expected Move](https://www.barchart.com/stocks/quotes/AAPL%7C20250221%7C220.00C/expected-move); [Moomoo – Calculating Expected Move Using Option](https://www.moomoo.com/us/learn/calculating-expected-move-using-option)
- PEAD-Überblick (Ball & Brown 1968, Bernard & Thomas 1989/1990, Kettell et al. 2022): [Post-earnings-announcement drift – Wikipedia](https://en.wikipedia.org/wiki/Post%E2%80%93earnings-announcement_drift)
- Martineau (2022): [Rest in Peace Post-Earnings Announcement Drift – Critical Finance Review (PDF)](https://cfr.ivo-welch.info/published/papers/martineau2021rest.pdf)
- Gegenpositionen und Subrahmanyam: [Is Post-Earnings Announcement Drift a Thing Again? – UCLA Anderson Review (21.1.2026)](https://anderson-review.ucla.edu/is-post-earnings-announcement-drift-a-thing-again/)
- Frazzini & Lamont (2007): [The Earnings Announcement Premium and Trading Volume – NBER w13090](https://www.nber.org/papers/w13090)
