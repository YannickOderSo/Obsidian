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

# Unterstützung und Widerstand

Unterstützung (Support) ist ein Preisbereich, an dem ein Rückgang oft stoppt, Widerstand (Resistance) einer, an dem ein Anstieg oft stoppt. Für Day Trading sind diese Levels der Kern fast jedes Setups: Sie liefern den Einstieg (Ausbruch über ein Level), den Stop (unter einem Level) und das Ziel (am nächsten Level). Anders als bei vielen Mustern gibt es hier echte Belege für einen Mechanismus.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Warum Levels wirken können (belegt)

| Befund | Quelle | Was es heißt |
| --- | --- | --- |
| Von Banken veröffentlichte Support-/Resistance-Levels sagten im Devisenmarkt Unterbrechungen von Intraday-Trends voraus; die Güte schwankte stark je nach Firma und Währung | Osler (2000), Fed New York | Levels sind nicht beliebig, aber nicht jedes Level ist gleich gut |
| Rund 9.700 Stop- und Take-Profit-Orders einer Großbank häuften sich an runden Zahlen: Take-Profits genau darauf, Stop-Losses knapp dahinter | Osler (2003), Journal of Finance | Erklärt beides: Umkehr am Level (Take-Profits) und Beschleunigung nach dem Durchbruch (ausgelöste Stops) |
| Support- und Resistance-Levels fallen mit Spitzen der Orderbuch-Tiefe zusammen | Kavajecz und Odders-White (2004), Review of Financial Studies | Technische Levels finden Liquidität, die schon im Orderbuch liegt |
| Über 100 Mio. US-Aktientrades: auffällig viele Käufe 1 Cent unter runden Zahlen, Verkäufe 1 Cent darüber; am stärksten bei ganzen Dollar, dann halben | Bhattacharya, Holden und Jacobsen (2012), Management Science | Runde Zahlen sind echte Ankerpunkte, auch bei Aktien |
| Die Nähe zum 52-Wochen-Hoch sagt künftige Renditen besser voraus als die vergangene Rendite | George und Hwang (2004), Journal of Finance | Ein markantes Hoch wirkt als Anker (Monate, nicht Minuten) |

Die Belege kommen vor allem aus dem Devisenmarkt und aus Orderbuchdaten. Dass ein Day Trader mit Levels nach Kosten Geld verdient, zeigt keine dieser Studien.

## Arten von Levels im Day Trading

| Level | Was es ist | Belege |
| --- | --- | --- |
| Horizontales Level | frühere Hochs und Tiefs, an denen der Kurs mehrfach gedreht hat | Mechanismus belegt (Orderbuch, Order-Häufung); wie viele Berührungen nötig sind, ist Konvention |
| Runde Zahlen | ganze Dollar ($50, $100), halbe Dollar | gut belegt (Osler 2003, Bhattacharya u. a. 2012) |
| Vortageshoch / -tief / -schluss | Hoch, Tief und Schluss der letzten regulären Sitzung | weit verbreitete Praxis; eigene Studie für US-Aktien nicht gefunden |
| Pre-Market-Hoch / -Tief | Extrempunkte vor 9:30 New York | Praxis-Konvention; Handel vorbörslich ist dünn, Preise tragen Information, sind aber weniger effizient (Barclay und Hendershott 2003) |
| Opening Range | Hoch und Tief der ersten 15 Minuten | Grundlage des ORB, siehe [[Opening Range Breakout]] |
| VWAP | volumengewichteter Durchschnittspreis des Tages, wandert mit | Benchmark großer Händler, siehe [[Indikatoren]] und [[VWAP-Strategien]] |
| 20-Tage-Hoch | höchster Schluss der letzten 20 Sitzungen | siehe [[Breakout aus 20-Tage-Hoch]] |

## Rollenwechsel (Polarity)

Ein durchbrochener Widerstand wird zur Unterstützung und umgekehrt. Das ist eine der ältesten Regeln der Chartanalyse. Belegt ist vor allem, dass der Kurs **zurückkommt**: Nach Ausbrüchen aus Chartformationen kehrt er laut Bulkowski in etwa 60 bis 70 % der Fälle innerhalb von 30 Tagen zum Ausbruchsniveau zurück (Throwback). Ob das Level dann hält, ist nicht allgemein belegt; Bulkowski findet sogar, dass Formationen mit Throwback danach schlechter laufen.

Für die Praxis heißt das:

- Ein Retest des Ausbruchslevels ist normal und kein Zeichen, dass der Trade falsch ist.
- Ein Stop **genau** am Level wird beim Retest oft abgeholt. Etwas Abstand (Zone statt Linie) oder ein Stop unter dem nächsten Tief ist robuster. Siehe [[Stop-Platzierung]].

## Levels zeichnen: Faustregeln

1. **Zonen statt Linien.** Ein Level ist ein Bereich von einigen Cent bis zu einem Bruchteil der Tagesspanne, keine exakte Zahl.
2. **Schlusskurse zählen mehr als Dochte.** Ein Docht über das Level ist ein Test, ein Schluss darüber ein Ausbruch.
3. **Wenige, deutliche Levels.** Wer zehn Linien zeichnet, findet immer eine, die „gehalten“ hat. Das ist Rückschaufehler.
4. **Runde Zahlen nicht als exakten Stop nehmen.** Weil Stops sich knapp hinter runden Zahlen häufen (Osler), schießt der Kurs dort oft kurz durch. Ein Stop bei $99,99 unter $100 liegt mitten in diesem Gedränge.
5. **Was liegt über dem Einstieg?** Ein Long-Trade, dessen 2R-Ziel hinter dem Vortageshoch liegt, muss zwei Hürden nehmen.

## Beispielrechnung

Annahme (frei gewählt): Ein Wert schloss gestern bei $100,80, Vortageshoch $102,40, Pre-Market-Hoch $101,80, runde Zahl $100 darunter.

| Größe | Rechnung | Ergebnis |
| --- | --- | --- |
| Einstieg | 5-Minuten-Schluss über dem Vortageshoch | $102,50 |
| Stop | unter dem Pre-Market-Hoch, mit Abstand | $101,70 |
| Risiko je Aktie | 102,50 − 101,70 | $0,80 |
| Stücke nach Verlustlimit | $50 / $0,80 = 62,5 | 62 Aktien = $6.355 |
| Positionsdeckel | 75 % von $5.000 = $3.750 / 102,50 = 36,6 | **36 Aktien** = $3.690 |
| Tatsächliches Risiko | 36 × 0,80 | $28,80 |
| Ziel 2R | 102,50 + 1,60 | $104,10 |

> [!tip] Bei teuren Aktien entscheidet der Deckel, nicht der Stop
> Ab etwa $50 je Aktie und einem Stop unter 1 % bindet bei $5.000 Budget meist der Positionsdeckel von $3.750. Dann ist das Risiko kleiner als $50, und ein weiter weg liegender, sinnvoller Stop kostet nichts extra. Das rechnet `/trader-budget` und sagt, welches Limit entschieden hat. Siehe [[Positionsgröße]].

## Typische Fallen

- **Fehlausbruch an runden Zahlen:** Der Kurs sticht über $100, löst Stops und Kauforders aus und fällt zurück. Auf den Schluss der Kerze warten.
- **Level aus dünnem Pre-Market:** Ein Pre-Market-Hoch aus wenigen tausend Stück ist ein schwaches Level.
- **Alte Levels überbewerten:** Ein Hoch von vor einem Jahr kennen weniger Marktteilnehmer als das von gestern. Belegt ist das nicht, aber Studien zu Ankerpunkten (52-Wochen-Hoch) betreffen Monate, nicht Intraday-Trades.
- **Alles ist ein Level:** Wenn fast jeder Preis irgendein Level ist, sagt keiner etwas.

## Im Vault

- **`/trader-scanner`:** `breakout_20d` nutzt den höchsten **Schlusskurs** der 20 Sitzungen davor, nicht das Intraday-Hoch. Das feuert öfter (Doku-Beispiel KO am 16.10.2026: über dem 20-Tage-Schlusshoch, nicht über dem 20-Tage-Hoch). Der ORB-Scan nutzt das Hoch der ersten 15 Minuten als Level.
- **`/trader-entry`:** `--setup level --level <Preis>` meldet die erste geschlossene Kerze über dem Level (nicht davor, nicht gleich). So lassen sich Vortageshoch, Pre-Market-Hoch oder runde Zahlen nutzen. Nur long, keine Einstiege vor 9:45 oder nach 15:30.
- **`/trader-exit`:** Für Level-Setups muss der Stop genannt werden (`--stop price:X`). Liegt der Stop unter einer runden Zahl, nicht direkt darunter setzen.
- **`/trader-alerts`:** `alerts.py add --symbol XYZ --above 102.40` oder `--below 100` meldet, wenn ein Level erreicht wird, je einmal.
- **Grenze:** Kein Skill liefert Vortageshoch oder Pre-Market-Levels fertig; Yahoo-Daten sind verzögert und kostenlos. Levels werden von Hand bestimmt und im Journal notiert.

Verwandt: [[Chartformationen]], [[Bull Flag]], [[Volumen und relatives Volumen]], [[Handelszeiten und Sessions]].

## Quellen

- Osler (2000), „Support for Resistance: Technical Analysis and Intraday Exchange Rates“, FRBNY Economic Policy Review 6(2): https://www.newyorkfed.org/medialibrary/media/research/epr/00v06n2/0007osle.html
- Osler (2003), „Currency Orders and Exchange Rate Dynamics: An Explanation for the Predictive Success of Technical Analysis“, Journal of Finance 58, 1791–1819; Staff Report 125: https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr125.html
- Kavajecz, Odders-White (2004), „Technical Analysis and Liquidity Provision“, Review of Financial Studies 17(4), 1043–1071: https://ideas.repec.org/a/oup/rfinst/v17y2004i4p1043-1071.html
- Bhattacharya, Holden, Jacobsen (2012), „Penny Wise, Dollar Foolish: Buy–Sell Imbalances On and Around Round Numbers“, Management Science 58(2), 413–431: https://pubsonline.informs.org/doi/10.1287/mnsc.1110.1364
- George, Hwang (2004), „The 52-Week High and Momentum Investing“, Journal of Finance 59, 2145–2176: https://academicnewsletter.sufe.edu.cn/info/361244
- Barclay, Hendershott (2003), „Price Discovery and Trading After Hours“, Review of Financial Studies 16(4), 1041–1073: https://ideas.repec.org/a/oup/rfinst/v16y2003i4p1041-1073.html
- Bulkowski, „Throwbacks“ und Glossar (Throwback-Definition, Raten je Formation): https://thepatternsite.com/throwbacks.html, https://thepatternsite.com/glossary.html
- Skills: `.claude/skills/trader-scanner/SKILL.md`, `.claude/skills/trader-entry/SKILL.md`, `.claude/skills/trader-exit/SKILL.md`, `.claude/skills/trader-alerts/SKILL.md`, `.claude/skills/trader-budget/SKILL.md`
