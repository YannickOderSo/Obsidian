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

# Tageslimits und Regelwerk

Tageslimits begrenzen, wie viel an einem schlechten Tag verloren gehen kann, und nehmen Entscheidungen aus dem Moment, in dem man am schlechtesten entscheidet. Diese Notiz erklärt unsere Limits, wie `/trader-risk` sie prüft, was die Forschung zum Verhalten nach Verlusten sagt, und enthält eine Checkliste vor jedem Trade.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Unsere Limits

| Regel | Wert in `trader/config.json` | Wirkung |
| --- | --- | --- |
| Max-Verlust je Trade | `max_loss_per_trade_usd: 50` | 1R ≈ $50 |
| Max-Verlust je Tag | `max_daily_loss_usd: 150` | höchstens 3R Risiko am Tag |
| Max-Trades je Tag | `max_trades_per_day: 3` | höchstens 3 Einstiege |
| Max-Orders je Tag | `max_orders_per_day: 10` | inkl. Ausstiege und Korrekturen |
| Mindest-CRV | `min_reward_risk: 1.0` | Ziel mindestens 1R |
| Stop Pflicht | `require_stop: true` | keine Order ohne Stop |
| Einstiegsfenster | 09:45–15:30 New York | nicht in den ersten 15 Minuten, nicht kurz vor Schluss |
| Flat bis | 15:55 New York | kein Halten über Nacht |
| Optionen, Margin, Leerverkauf | aus | nur Aktien long, nur eigenes Geld |

Ändern darf diese Werte nur der Nutzer, dann auch [[Trading/Regeln]] nachziehen.

## Wie /trader-risk das Tageslimit zählt

Wichtig und strenger als bei vielen Tradern üblich: `/trader-risk` zählt **den vollen Max-Verlust jedes heute platzierten Einstiegs, egal ob der Trade gewonnen oder verloren hat**. Es ist also ein Limit für das **eingesetzte Risiko**, nicht für den realisierten Verlust.

- Drei volle Trades à $50 füllen die $150 aus, auch wenn alle drei gewonnen haben.
- Ein vierter Trade ist ohnehin durch `max_trades_per_day: 3` gesperrt.
- Kleinere Trades (z. B. $46,88 bei TSLA) lassen etwas Luft, aber nicht für einen vierten Einstieg.
- **Ausstiege werden nie blockiert.** Ein Verkauf, der nur eine Position schließt, bekommt höchstens eine Warnung, auch nach 15:30.

Ein Tag mit drei Verlusten hintereinander kostet also höchstens etwa $150 (plus Slippage). Wie oft passiert das? Bei unabhängigen Trades:

| Verlustquote je Trade | 3 Verluste an einem Tag (bei 3 Trades) | mind. ein solcher Tag in 20 Handelstagen |
| --- | --- | --- |
| 40 % | 6,4 % | 73 % |
| 50 % | 12,5 % | 93 % |
| 60 % | 21,6 % | 99 % |
| 65 % (2R-Setup) | 27,5 % | 100 % |

Eigene Rechnung. Ein „Max-Verlust-Tag“ ist also kein Ausnahmefall, sondern kommt fast jeden Monat. Das Limit sorgt dafür, dass er bei −3 % des Budgets endet.

## Warum Tageslimits: die Evidenz

- **Nach Verlusten steigt die Risikobereitschaft.** Coval und Shumway untersuchten über 1.000 Eigenhändler an der CBOT (Treasury-Futures, 1998): Wer vormittags verloren hatte, ging am Nachmittag mit etwa 16 % höherer Wahrscheinlichkeit überdurchschnittliches Risiko ein als wer vormittags gewonnen hatte ([Coval & Shumway 2005, Journal of Finance; Zusammenfassung CFA Institute](https://rpc.cfainstitute.org/research/cfa-digest/2005/11/do-behavioral-biases-affect-prices-digest-summary)). Das ist genau das Muster, das ein Tageslimit abschneidet.
- **Break-even-Effekt.** In Experimenten von Thaler und Johnson waren nach Verlusten Wetten besonders attraktiv, die eine Chance boten, wieder auf null zu kommen; nach Gewinnen stieg die Risikobereitschaft („House Money“) ([Thaler & Johnson 1990, Management Science](https://ideas.repec.org/a/inm/ormnsc/v36y1990i6p643-660.html)).
- **Disziplin sagt Erfolg voraus.** Bei Profi-Futures-Händlern am CME hatte ein Maß für Handelsdisziplin Vorhersagekraft für späteren Erfolg ([Locke & Mann 2005, Journal of Financial Economics](https://ideas.repec.org/a/eee/jfinec/v76y2005i2p401-444.html)).
- **Mehr Trades, mehr Verlierer.** In der SEBI-Studie zu indischen Intraday-Tradern (2022/23) stieg der Anteil der Verlierer von etwa 71 % auf 80 % bei denen mit mehr als 500 Trades im Jahr ([Taxscan zur SEBI-Studie](https://www.taxscan.in/7-out-of-10-individual-intraday-traders-in-equity-cash-segment-make-losses-says-sebi/422657)).
- **Branchenpraxis.** Prop-Firmen arbeiten mit harten Tagesverlustgrenzen, etwa 5 % des Kontos bei der klassischen FTMO-Challenge; die Regeln ändern sich und unterscheiden sich je Produkt ([LuxAlgo zu FTMO](https://www.luxalgo.com/prop-firms/ftmo/), Sekundärquelle). Unsere 3 % liegen darunter.

> [!info] Ehrlich zur Evidenz
> Dass Tageslimits die **Rendite** verbessern, ist nicht belegt. Belegt ist, dass Menschen nach Verlusten riskanter handeln und dass häufiges Handeln mit schlechteren Ergebnissen einhergeht. Ein Tageslimit ist deshalb vor allem eine **Schadensbegrenzung** gegen das eigene Verhalten.

## Pause nach Verlusten

`trader/config.json` hat keine eigene Regel „Pause nach X Verlusten“. Praktisch übernimmt das Trade-Limit die Rolle: Nach drei Trades ist Schluss. Mögliche eigene Regeln, die der Nutzer in [[Trading/Regeln]] unter „Eigene Regeln“ festhalten kann (die Skills prüfen sie nicht):

- Nach **zwei Verlusten in Folge** an einem Tag kein dritter Trade.
- Nach einem Trade, der gegen eine Regel verstoßen hat, Schluss für den Tag, egal wie er ausging.
- Nach einer Woche mit −$300 (−6 %) eine Pause von einem Tag und Auswertung im Journal.
- Kein neuer Einstieg innerhalb von 15 Minuten nach einem Stop (gegen [[Psychologie und Disziplin|Revenge Trading]]).

Das sind Vorschläge aus der Praxis, keine belegten Optimalwerte.

## Checkliste vor dem Trade

Vor jedem Einstieg, in dieser Reihenfolge (entspricht der Kette der Skills):

- [ ] **Setup**: Kommt der Kandidat aus `/trader-scanner` mit einem benannten Setup? Kein Einstieg aus Langeweile oder einem Tipp.
- [ ] **News**: `/trader-news` geprüft? Earnings heute oder morgen früh, ein Halt, ein 8-K? ([[Katalysatoren]], [[Earnings-Saison]])
- [ ] **Uhrzeit**: zwischen 9:45 und 15:30 New York? Ist heute ein Tag mit frühem Schluss?
- [ ] **Signal**: Hat `/trader-entry` auf einem **abgeschlossenen** Bar ausgelöst, oder will ich nur hinterherlaufen?
- [ ] **Plan**: Stop und Ziel aus `/trader-exit` stehen **vor** dem Einstieg; Stop dort, wo das Setup widerlegt ist ([[Stop-Platzierung]]).
- [ ] **Quoten**: `/trader-timemachine` gelaufen, Urteil ehrlich gelesen (Münzwurf heißt Münzwurf).
- [ ] **Größe**: `/trader-budget` gerechnet, Max-Verlust ≤ $50.
- [ ] **Limits**: `/trader-risk` sagt PASS; wie viel vom Tageslimit ist schon verbraucht?
- [ ] **Kopf**: Bin ich ruhig? Will ich einen Verlust zurückholen? Wenn ja: kein Trade.
- [ ] **Order**: Ticket von `/trader-broker` gelesen, Ja nur für genau diese Order.
- [ ] **Journal**: `/trading-journal write` nach jedem Schritt.

## Im Vault

- **`/trader-risk`** prüft hart: Stop vorhanden, Max-Verlust je Trade, CRV, Tagesverlust (Summe der Max-Verluste heutiger Einstiege), Trades je Tag, Einstiegsfenster und Börsenzeiten (inkl. Feiertage und frühe Schlüsse, Zeit in New York gerechnet), Positionsdeckel, Cash-Puffer, Duplikate, Orders je Tag. Ein BLOCK ist endgültig für diese Order.
- **`/trader-broker`** zeigt nur Orders, die heute PASS bekommen haben, und braucht ein ausdrückliches Ja für genau diese Order.
- **`pdt_guard`** ist aus; FINRA hat die $25.000-Mindestgrenze für Pattern Day Trader abgeschafft, Broker dürfen die Umstellung aber bis Oktober 2027 strecken (laut `trader-risk/SKILL.md`, Details in [[Pattern Day Trader Regel]]).
- Grenzen: Kein Wochen- oder Gesamt-Drawdown-Limit, keine „Pause nach X Verlusten“, keine Sperrzeit nach einem Stop. Das muss der Nutzer selbst halten oder als Regel ergänzen lassen.

## Quellen

- `.claude/skills/trader-risk/SKILL.md`, `trader-budget/SKILL.md`, `trader/config.json`, [[Trading/Regeln]]
- [Coval & Shumway (2005): Do Behavioral Biases Affect Prices? – CFA Institute Digest](https://rpc.cfainstitute.org/research/cfa-digest/2005/11/do-behavioral-biases-affect-prices-digest-summary) und [Deep Blue (Abstract)](https://deepblue.lib.umich.edu/handle/2027.42/115930?show=full)
- [Thaler & Johnson (1990): Gambling with the House Money and Trying to Break Even, Management Science](https://ideas.repec.org/a/inm/ormnsc/v36y1990i6p643-660.html)
- [Locke & Mann (2005): Professional trader discipline and trade disposition, JFE](https://ideas.repec.org/a/eee/jfinec/v76y2005i2p401-444.html)
- [Taxscan: SEBI-Studie zu Intraday-Tradern](https://www.taxscan.in/7-out-of-10-individual-intraday-traders-in-equity-cash-segment-make-losses-says-sebi/422657)
- [LuxAlgo: FTMO Prop Firm](https://www.luxalgo.com/prop-firms/ftmo/) – Tagesverlustgrenze 5 % (Sekundärquelle, Stand kann sich ändern)
- Wahrscheinlichkeiten für Verlusttage: eigene Rechnung
