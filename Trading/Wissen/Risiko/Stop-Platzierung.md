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

# Stop-Platzierung

Der Stop markiert den Punkt, an dem die Idee hinter dem Trade widerlegt ist. Diese Notiz vergleicht die üblichen Arten, ihn zu setzen, sagt, was davon belegt und was Folklore ist, und erklärt, wie `/trader-exit` es macht.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Grundsatz

Ein guter Stop beantwortet die Frage: **Wo ist mein Setup falsch?** Nicht: Wie viel will ich verlieren? Der Verlust in Dollar wird danach über die Stückzahl gesteuert ([[Positionsgröße]]). Wer den Stop nach dem Geldbeutel setzt, landet oft mitten im normalen Rauschen und wird ausgestoppt, obwohl die Idee noch stimmt.

Drei Regeln aus `/trader-exit`, die unabhängig vom Verfahren gelten:

1. Stop und Ziel stehen **vor** dem Einstieg fest.
2. Ein Stop wird **nie** weiter vom Einstieg weggeschoben, wenn der Trade läuft.
3. Ein zu enger Stop wird abgelehnt: Risiko unter 0,05 % des Preises gilt als „zu eng für den Spread“.

## Die Verfahren

| Verfahren | Wo der Stop liegt | Stärken | Schwächen | In `/trader-exit` |
| --- | --- | --- | --- | --- |
| **Range-Mitte** | Mitte der Opening Range | enger als das Range-Tief, mehr Aktien je $50 | wird öfter von normalem Rücklauf erwischt | `or-mid` (Standard für ORB) |
| **Strukturell** | unter dem Range-Tief, unter einem Swing-Tief, unter Unterstützung | logisch begründet: darunter ist das Muster kaputt | oft weit weg → wenige Aktien; Niveaus sind für alle sichtbar | `or-low` oder `price:X` |
| **ATR-basiert** | k × ATR unter dem Einstieg | passt sich der aktuellen Schwankung an | ATR ist rückblickend; k ist frei gewählt | `atr:K` |
| **Prozent** | x % unter dem Einstieg | einfach | ignoriert Volatilität und Chart völlig | `pct:X` |
| **Zeit-Stop** | raus zu einer Uhrzeit oder nach x Minuten ohne Bewegung | begrenzt das Risiko von Nachrichten und Schlussauktion | kein Preisniveau | `flat_by` 15:55 (fest) |
| **Trailing** | zieht mit dem Kurs nach oben | sichert Gewinne bei Trends | wird im Rauschen früh ausgelöst | nicht unterstützt |

### Range-Mitte und Range-Tief beim ORB

Beim [[Opening Range Breakout]] ist die Logik: Fällt der Kurs nach dem Ausbruch zurück tief in die Range, war der Ausbruch ein Fehlausbruch. `or-mid` setzt den Stop auf (Range-Hoch + Range-Tief) ÷ 2, abgerundet auf den Cent. Im TSLA-Beispiel: (362,18 + 354,47) ÷ 2 = 358,325 → **358,32**, Risiko 5,86 je Aktie. Mit `or-low` (354,47) wäre das Risiko 9,71 je Aktie, also nur 5 statt 8 Aktien für $50. Welcher Stop besser ist, ist eine empirische Frage pro Setup; die Time Machine kann beide Varianten durchspielen (aber Achtung Mehrfachtests, siehe [[Backtesting und Overfitting]]).

### ATR-Stop

Die Average True Range stammt von J. Welles Wilder (1978). True Range ist das Maximum aus Hoch − Tief, |Hoch − Vortagesschluss| und |Tief − Vortagesschluss|; Wilder glättete sie über 14 Perioden ([Wikipedia: Average true range](https://en.wikipedia.org/wiki/Average_true_range)). `/trader-exit` rechnet etwas anders: einfacher Durchschnitt der True Range der **letzten 14 Fünf-Minuten-Bars** der Sitzung bis zum Einstieg, ohne Wilder-Glättung; der erste Bar des Tages zählt nur Hoch − Tief, ohne Übernacht-Gap. Bei weniger als 14 Bars mittelt es alle und sagt das. Das ist eine Intraday-ATR, nicht die übliche Tages-ATR.

Beispiel: ATR(14) auf 5-Min-Bars = 0,80, Einstieg 50,00, `atr:1.5` → Stop 48,80, Risiko 1,20 → 41 Aktien für $50.

### Zeit-Stops

Unser fester Zeit-Stop ist **flat bis 15:55 New York**: kein Halten über Nacht, kein Übernacht-Gap. Weitere Zeit-Stops („raus, wenn nach 30 Minuten nichts passiert“) sind verbreitete Praktikerregeln; belastbare Studien dazu für unsere Setups kenne ich nicht. Wer so eine Regel will, sollte sie vorher festlegen und im Journal prüfen.

### Trailing Stops

Alpaca kennt `trailing_stop`-Orders (mit `trail_price` oder `trail_percent`), aber derzeit **nur als Einzelorder, nicht als Stop-Teil einer Bracket-Order** ([Alpaca: Orders](https://docs.alpaca.markets/docs/orders-at-alpaca)). Unsere Kette arbeitet mit Bracket-Orders, also ohne Trailing. Ob Trailing bei Day Trades hilft, ist nicht allgemein belegt.

## Was die Forschung zu Stops sagt

- **Stops kosten bei reinem Zufall Rendite.** Kaminski und Lo zeigen: Folgen Kurse einem Random Walk, senken einfache Stop-Loss-Regeln die erwartete Rendite immer; einen Mehrwert bringen sie nur bei Momentum oder Regimewechseln ([CXO Advisory zum Arbeitspapier](https://www.cxoadvisory.com/?p=1809), [Kaminski & Lo 2014, Journal of Financial Markets](https://dspace.mit.edu/handle/1721.1/114876)). Für uns heißt das: Der Stop ist vor allem **Risikobegrenzung**, kein Renditebringer.
- **Stop-Orders ballen sich an runden Zahlen.** Osler fand in den Orderbüchern einer großen Devisenbank: Stop-Kauforders liegen gehäuft knapp über runden Zahlen, Stop-Verkaufsorders knapp darunter ([Osler 2001, NY Fed Staff Report 125](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr125.html)). Werden sie ausgelöst, beschleunigen sie die Bewegung („price cascades“, [Osler 2002, Staff Report 150](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr150.html)). Die Daten stammen aus dem Devisenmarkt; dass es bei Aktien ähnlich ist, ist plausibel, aber nicht dieselbe Evidenz.

> [!info] Stop-Jagd: was dran ist
> Dass „Market Maker gezielt Stops jagen“, ist als Absicht kaum nachweisbar. Belegt ist der Mechanismus: Viele Stops an offensichtlichen Stellen (knapp unter runden Zahlen, unter dem Tagestief, unter dem Range-Tief) werden zusammen ausgelöst und verstärken den Ausschlag ([Osler](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr150.html)). Praktische Folge: Einen Stop nicht genau auf eine runde Zahl oder das exakte Tief legen, sondern mit etwas Abstand. `/trader-exit` rundet den Stop ohnehin nach unten (weg vom Einstieg).

## Gaps und schnelle Märkte

- Ein Stop wird bei Alpaca zur **Market-Order**, sobald auf dem konsolidierten Tape zum Stop-Preis oder darunter gehandelt wird. Der Fill kann deutlich schlechter sein; bei Halts steigt dieses Risiko ([Alpaca: Orders](https://docs.alpaca.markets/docs/orders-at-alpaca), [Investor.gov](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14)).
- Eine **Stop-Limit**-Order schützt vor dem schlechten Fill, kann aber gar nicht ausgeführt werden; nach einem Gap bleibt sie als Limit-Order stehen, und man ist weiter im Trade ([Alpaca](https://docs.alpaca.markets/docs/orders-at-alpaca)).
- Stop- und Stop-Limit-Orders laufen bei Alpaca nicht im vor- und nachbörslichen Handel. Für uns egal, da wir 9:45–15:55 handeln und flat gehen.
- **Intraday-Halts** (LULD, Nachrichten) können einen Kurs von über dem Stop auf weit darunter springen lassen. Siehe [[Handelsstopps und LULD]].

> [!warning] Der Stop ist keine Garantie
> Das sagt `/trader-exit` bei jedem Plan einmal. Der Max-Verlust von $50 ist der Verlust **am Stop-Preis**. Ein Positionsdeckel (75 % des Budgets) verhindert, dass ein sehr enger Stop zu einer riesigen Position führt, die ein Gap dann richtig teuer macht.

## Checkliste für einen Stop

- [ ] Liegt der Stop dort, wo das Setup widerlegt ist (nicht dort, wo $50 „passen“)?
- [ ] Mehr als normales Rauschen entfernt (ATR als Maß)?
- [ ] Nicht exakt auf einer runden Zahl oder dem offensichtlichen Tief?
- [ ] Erlaubt er bei $50 noch mindestens eine sinnvolle Stückzahl und ein CRV ≥ 1?
- [ ] Gibt es heute Earnings oder Makro-Daten, die einen Sprung über den Stop wahrscheinlich machen ([[Earnings-Saison]], [[Makro-Termine]])?

## Im Vault

- **`/trader-exit`**: Stop-Regeln `or-mid` (Standard für ORB), `or-low`, `price:X`, `pct:X`, `atr:K`; rundet den Stop nach unten auf den Cent; Ziel standardmäßig 2R; lehnt Stops ≥ Einstieg und Risiko < 0,05 % des Preises ab; ein Level-Setup (z. B. [[Breakout aus 20-Tage-Hoch]]) braucht einen Stop, den der Nutzer nennt.
- **`/trader-timemachine`** prüft Bar für Bar zuerst den Stop, dann das Ziel; ein Bar, der beides berührt, zählt als Stop (vorsichtig). Ein Gap über den Stop zählt als −1R (optimistisch).
- **`/trader-budget`** verkleinert nie den Stop, um mehr Aktien zu kaufen; **`/trader-risk`** blockt jede Entry-Order ohne Stop (`require_stop: true`).
- **`/trader-alerts`** meldet Stop, Ziel und 15:55 als Erinnerung; die Bracket-Order beim Broker ist der eigentliche Stop.
- Grenze: Kein Trailing, kein Zeit-Stop außer 15:55, keine Prüfung, ob der Stop auf einer runden Zahl liegt.

## Quellen

- `.claude/skills/trader-exit/SKILL.md` und `exit.py` (Funktion `atr_of`), `trader-timemachine/SKILL.md`
- [Alpaca Docs: Orders at Alpaca](https://docs.alpaca.markets/docs/orders-at-alpaca) – Stop-Auslösung, Stop-Limit nach Gap, Trailing nur als Einzelorder
- [Investor.gov: Stop, Stop-Limit und Trailing-Stop-Orders](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14)
- [Wikipedia: Average true range](https://en.wikipedia.org/wiki/Average_true_range) – Definition nach Wilder (1978)
- [Kaminski & Lo: When do stop-loss rules stop losses? (MIT DSpace)](https://dspace.mit.edu/handle/1721.1/114876) und [CXO Advisory: Zusammenfassung](https://www.cxoadvisory.com/?p=1809)
- [Osler (2001): Currency Orders and Exchange-Rate Dynamics, NY Fed Staff Report 125](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr125.html)
- [Osler (2002): Stop-Loss Orders and Price Cascades in Currency Markets, NY Fed Staff Report 150](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr150.html)
- Beispiel ATR-Stop: eigene Rechnung
