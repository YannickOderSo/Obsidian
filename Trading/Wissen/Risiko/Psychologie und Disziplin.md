---
typ: wissen
erstellt: 2026-10-22
aktualisiert: 2026-10-22
quelle: Recherche
tags:
  - trading
  - wissen
  - risiko
---

# Psychologie und Disziplin

Die meisten Fehler beim Day Trading sind keine Rechenfehler, sondern Verhaltensfehler: Verluste laufen lassen, Gewinne zu früh nehmen, nach einem Stop sofort wieder rein. Diese Notiz fasst die gut belegten Verzerrungen zusammen und sagt, welche Gegenmittel im Vault schon eingebaut sind.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Die wichtigsten Verzerrungen

| Verzerrung | Was passiert | Evidenz | Gegenmittel im Vault |
| --- | --- | --- | --- |
| Verlustaversion | Verluste schmerzen etwa doppelt so stark wie gleich große Gewinne freuen | stark (Experimente) | Stop vor Einstieg, Bracket-Order |
| Dispositionseffekt | Gewinner zu früh verkaufen, Verlierer zu lange halten | stark (Kontodaten) | festes Ziel und fester Stop, Stop nie verschieben |
| Revenge Trading | nach Verlust mehr Risiko, um „zurückzuholen“ | gut (Profi-Händler) | Tageslimit, Trade-Limit |
| FOMO | Kauf dessen, was gerade in den News ist oder schon gelaufen ist | gut (Kontodaten) | Signal nur auf abgeschlossenem Bar, frischer Kurs im Risk-Check |
| Overconfidence | eigene Fähigkeit überschätzen, zu viel handeln | stark (Kontodaten) | Time Machine, Journal-Statistik, Trade-Limit |
| Overtrading | Handel aus Langeweile oder Gewohnheit | stark (Kontodaten) | max. 3 Trades/Tag, Checkliste |

### Verlustaversion

Kahneman und Tversky zeigten in der Prospect Theory (1979), dass Menschen Ergebnisse als Gewinne oder Verluste gegenüber einem Referenzpunkt bewerten, nicht als Endvermögen ([Econometrica 1979](https://doi.org/10.2307/1914185)). In der kumulativen Fassung von 1992 schätzten Tversky und Kahneman den Verlustaversions-Koeffizienten auf **λ ≈ 2,25**: Ein Verlust wiegt gut doppelt so schwer wie ein gleich großer Gewinn ([Journal of Risk and Uncertainty 1992](https://ideas.repec.org/a/kap/jrisku/v5y1992i4p297-323.html), Parameter nach [Wakker](https://personal.eur.nl/wakker/miscella/calculate.cpt.kobb/index.htm)). Der genaue Wert schwankt je nach Studie und Methode, die Richtung ist robust.

Im Trade heißt das: Ein laufender Verlust fühlt sich so schlecht an, dass man ihn lieber nicht realisiert („kommt schon zurück“).

### Dispositionseffekt

Shefrin und Statman nannten 1985 die Neigung, „Gewinner zu früh zu verkaufen und Verlierer zu lange zu reiten“, Dispositionseffekt ([Journal of Finance 1985](https://cir.nii.ac.jp/crid/1360011145247011968)). Odean belegte ihn 1998 mit 10.000 Konten eines US-Discount-Brokers (1987–1993): Anleger realisierten **14,8 %** ihrer Buchgewinne, aber nur **9,8 %** ihrer Buchverluste. Die verkauften Gewinner schnitten im folgenden Jahr im Schnitt um **3,4 Prozentpunkte besser** ab als die gehaltenen Verlierer; das Verhalten war also auch rückblickend nicht klug ([Odean 1998, Journal of Finance](https://faculty.haas.berkeley.edu/odean/papers%20current%20versions/areinvestorsreluctant.pdf)).

Selbst bei Profis: Vollzeit-Händler an Futures-Börsen hielten Verluste deutlich länger als Gewinne ([Locke & Mann 2005](https://ideas.repec.org/a/eee/jfinec/v76y2005i2p401-444.html)).

### Revenge Trading und Break-even-Effekt

„Revenge Trading“ ist ein Praktikerbegriff. Das Muster dahinter ist belegt: Eigenhändler an der CBOT, die vormittags verloren, gingen nachmittags mit rund 16 % höherer Wahrscheinlichkeit überdurchschnittliches Risiko ein ([Coval & Shumway 2005](https://rpc.cfainstitute.org/research/cfa-digest/2005/11/do-behavioral-biases-affect-prices-digest-summary)). In Experimenten wurden nach Verlusten besonders Wetten attraktiv, die eine Chance auf „wieder null“ boten ([Thaler & Johnson 1990](https://ideas.repec.org/a/inm/ormnsc/v36y1990i6p643-660.html)).

Typische Formen: sofort nach dem Stop wieder in dieselbe Aktie, größere Position „um es zurückzuholen“, Stop weglassen.

### FOMO und Aufmerksamkeit

Auch „FOMO“ ist Umgangssprache. Belegt ist: Privatanleger kaufen bevorzugt Aktien, die gerade Aufmerksamkeit erregen (in den News, ungewöhnlich hohes Volumen, extreme Tagesbewegung), und diese Käufe schneiden danach schlechter ab als die Aktien, die sie gleichzeitig verkaufen ([Barber & Odean 2008, „All That Glitters“, Review of Financial Studies](https://ideas.repec.org/a/oup/rfinst/v21y2008i2p785-818.html)). Für Day Trader ist das heikel, weil Scanner genau solche Aktien finden. Ein Ausbruch, der schon gelaufen ist, verschlechtert das CRV: Im TSLA-Beispiel fiel es durch 20 Minuten Warten von 1,0 auf 0,44.

### Overconfidence und Overtrading

- Die aktivsten 20 % von 66.465 Haushalten eines US-Discount-Brokers (1991–1996) erzielten **11,4 %** im Jahr, der Markt **17,9 %**; die Autoren führen das auf Overconfidence zurück ([Barber & Odean 2000, „Trading Is Hazardous to Your Wealth“](https://faculty.haas.berkeley.edu/odean/Papers%20current%20versions/Individual_Investor_Performance_Final.pdf)).
- Männer handelten 45 % mehr als Frauen; das Handeln kostete sie 2,65 Prozentpunkte Rendite im Jahr gegenüber 1,72 bei Frauen ([Barber & Odean 2001, „Boys Will Be Boys“](https://faculty.haas.berkeley.edu/odean/papers/gender/gender.html)).
- Anleger, die vom Telefon- auf Online-Handel wechselten, hatten vorher den Markt geschlagen, handelten danach mehr und lagen dann mehr als 3 % im Jahr hinter dem Markt ([Barber & Odean 2002, „Online Investors: Do the Slow Die First?“](https://ideas.repec.org/a/oup/rfinst/v15y2002i2p455-488.html)).
- Gervais und Odean modellieren, wie Händler durch Erfolge **lernen, überheblich zu werden**: Gewinne werden dem eigenen Können zugeschrieben, Verluste dem Pech; die Überheblichkeit ist früh in der „Karriere“ am größten ([Gervais & Odean 2001](https://faculty.haas.berkeley.edu/odean/papers/learning/learning.html)).
- Indische Intraday-Trader mit mehr als 500 Trades im Jahr waren zu 80 % Verlierer, gegenüber rund 71 % insgesamt ([SEBI-Studie, Taxscan](https://www.taxscan.in/7-out-of-10-individual-intraday-traders-in-equity-cash-segment-make-losses-says-sebi/422657)).

> [!warning] Gefahr der ersten Erfolge
> Drei gewonnene Paper-Trades in Folge beweisen nichts (siehe [[R-Multiple und Erwartungswert]] zum Standardfehler). Genau dann ist laut Gervais/Odean die Überheblichkeit am größten. Die Statistik im Journal ist das Gegengift.

## Besonderheit Paper Trading

Mit Spielgeld fehlt der echte Schmerz. In Experimenten von Holt und Laury stieg die Risikoscheu deutlich, wenn hohe Einsätze **echt** ausgezahlt wurden, bei nur hypothetischen hohen Einsätzen dagegen nicht ([Holt & Laury, AER; Nachfolgestudie 2005](https://econweb.ucsd.edu/~jandreon/Econ264/papers/Holt%20Laury%20AER%202005.pdf)). Daraus folgt nicht sicher, wie sich Day Trader verhalten, aber es ist plausibel: **Disziplin im Paper Trading ist leichter als mit echtem Geld.** Wer schon im Paper Trading Stops verschiebt, wird es mit echtem Geld erst recht tun.

## Gegenmittel, die wirken sollen

Die Verzerrungen sind gut belegt; wie gut einzelne Gegenmittel bei Privat-Tradern wirken, ist deutlich schwächer belegt. Die Liste folgt der Logik „Entscheidungen vorher treffen, wenn man ruhig ist“:

1. **Plan vor dem Einstieg** (Stop, Ziel, Größe), schriftlich. Im Trade nur noch ausführen.
2. **Bracket-Order beim Broker**: Stop und Ziel liegen als Orders im Markt; man muss im Moment nichts entscheiden.
3. **Stop nie weiter weg schieben.** Wer ihn anfassen will, darf ihn nur näher ziehen oder aussteigen.
4. **Harte Tages- und Trade-Limits**, technisch durchgesetzt statt per Willenskraft ([[Tageslimits und Regelwerk]]).
5. **Checkliste** vor jedem Trade, inklusive „Will ich gerade etwas zurückholen?“.
6. **Kleine, gleich große Risiken** ($50), damit kein einzelner Trade emotional wichtig wird.
7. **Journal mit Reflexion**, besonders bei Regelbrüchen.
8. **Ergebnis und Entscheidung trennen**: Ein Trade nach Plan, der am Stop endet, ist ein guter Trade; ein Regelbruch, der zufällig gewinnt, ein schlechter.

## Journal-Routine mit dem Skill trading-journal

| Wann | Was | Befehl |
| --- | --- | --- |
| nach `/trader-exit` | Trade anlegen (Status `geplant`) | `journal.py write` |
| nach Time Machine, Budget, Risk, Broker | ergänzen | `journal.py write` |
| Stop, Ziel oder 15:55 erreicht | schließen mit Ausstiegspreis | `journal.py close --exit PREIS` |
| direkt danach | **Reflexion** in eigenen Worten unter `## Reflexion`: Plan eingehalten? Was war anders? Wie fühlte ich mich vor dem Einstieg? | Claude fragt nach |
| Ende der Woche | Statistik, Time-Machine-Quoten gegen echte Ergebnisse | `journal.py stats --write` |
| wenn sich ein Muster zeigt | Erkenntnis nach `Gedächtnis/Erkenntnisse/Trading.md` mit Links auf die Trades | Skill `gedaechtnis` |

Sinnvolle Fragen für die Reflexion: Hätte ich diesen Trade auch ohne den letzten Verlust genommen? Habe ich nach dem Signal gekauft oder vorher? Habe ich irgendetwas am Plan geändert, nachdem ich drin war?

## Im Vault

- `/trader-exit` setzt Stop und Ziel **vor** dem Einstieg und verbietet, den Stop wegzuschieben; `/trader-budget` verkleinert nie den Stop für mehr Aktien.
- `/trader-risk` setzt Tageslimit, Trade-Limit und Einstiegsfenster technisch durch und misst das Risiko vom höheren Kurs, wenn der Preis schon gelaufen ist (Anti-FOMO).
- `/trader-timemachine` sagt „Close to a coin flip“, wenn es einer ist, gegen Overconfidence.
- `/trader-broker` braucht ein ausdrückliches Ja für genau eine Order, kein „mach mal“.
- `/trading-journal` hält Plan, Ergebnis und Reflexion fest; Muster wandern ins Gedächtnis.
- Grenze: Kein Skill erkennt Revenge Trading (z. B. Wiedereinstieg in dieselbe Aktie kurz nach einem Stop). Das muss in die Checkliste und die Reflexion.

## Quellen

- [Kahneman & Tversky (1979): Prospect Theory, Econometrica 47(2)](https://doi.org/10.2307/1914185)
- [Tversky & Kahneman (1992): Advances in Prospect Theory, Journal of Risk and Uncertainty](https://ideas.repec.org/a/kap/jrisku/v5y1992i4p297-323.html) und [Wakker: CPT-Parameter (λ = 2,25)](https://personal.eur.nl/wakker/miscella/calculate.cpt.kobb/index.htm)
- [Shefrin & Statman (1985): The Disposition to Sell Winners Too Early and Ride Losers Too Long](https://cir.nii.ac.jp/crid/1360011145247011968)
- [Odean (1998): Are Investors Reluctant to Realize Their Losses?](https://faculty.haas.berkeley.edu/odean/papers%20current%20versions/areinvestorsreluctant.pdf)
- [Locke & Mann (2005): Professional trader discipline and trade disposition](https://ideas.repec.org/a/eee/jfinec/v76y2005i2p401-444.html)
- [Coval & Shumway (2005): Do Behavioral Biases Affect Prices? – CFA Institute Digest](https://rpc.cfainstitute.org/research/cfa-digest/2005/11/do-behavioral-biases-affect-prices-digest-summary)
- [Thaler & Johnson (1990): Gambling with the House Money and Trying to Break Even](https://ideas.repec.org/a/inm/ormnsc/v36y1990i6p643-660.html)
- [Barber & Odean (2008): All That Glitters](https://ideas.repec.org/a/oup/rfinst/v21y2008i2p785-818.html)
- [Barber & Odean (2000): Trading Is Hazardous to Your Wealth](https://faculty.haas.berkeley.edu/odean/Papers%20current%20versions/Individual_Investor_Performance_Final.pdf)
- [Barber & Odean (2001): Boys Will Be Boys](https://faculty.haas.berkeley.edu/odean/papers/gender/gender.html)
- [Barber & Odean (2002): Online Investors: Do the Slow Die First?](https://ideas.repec.org/a/oup/rfinst/v15y2002i2p455-488.html)
- [Gervais & Odean (2001): Learning to Be Overconfident](https://faculty.haas.berkeley.edu/odean/papers/learning/learning.html)
- [Holt & Laury (2005): Risk Aversion and Incentive Effects: New Data without Order Effects](https://econweb.ucsd.edu/~jandreon/Econ264/papers/Holt%20Laury%20AER%202005.pdf) (fasst auch die Studie von 2002 zusammen)
- [Taxscan: SEBI-Studie zu Intraday-Tradern](https://www.taxscan.in/7-out-of-10-individual-intraday-traders-in-equity-cash-segment-make-losses-says-sebi/422657)
- `.claude/skills/trading-journal/SKILL.md` und die `trader-*`-Skills
