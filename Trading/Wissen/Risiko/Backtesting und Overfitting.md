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

# Backtesting und Overfitting

Ein Backtest spielt eine Regel auf vergangenen Daten durch. Er ist unverzichtbar und zugleich die bequemste Art, sich selbst zu täuschen. Diese Notiz erklärt die typischen Fehler, was Bailey und López de Prado dazu gezeigt haben, und wo die Time Machine stark und wo sie schwach ist.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## In-Sample und Out-of-Sample

- **In-Sample (IS)**: die Daten, auf denen man die Regel entwickelt und ihre Parameter wählt.
- **Out-of-Sample (OOS)**: Daten, die bei der Entwicklung **nicht** angefasst wurden. Nur dort zeigt sich, ob die Regel etwas Echtes gefunden hat.
- **Walk-Forward**: wiederholt auf einem Fenster entwickeln, auf dem nächsten testen, weiterschieben.

**Overfitting** heißt: Die Regel beschreibt das Rauschen der IS-Daten statt eines wiederkehrenden Musters. Sie sieht im Backtest gut aus und versagt danach.

Bailey, Borwein, López de Prado und Zhu warnen, dass klassische Hold-out-Verfahren bei Investment-Backtests unzuverlässig und ungenau sind. Ein naheliegender Grund: Wer nach einem enttäuschenden OOS-Test die Regel anpasst und erneut testet, hat den OOS-Teil damit zu In-Sample gemacht ([The Probability of Backtest Overfitting, Journal of Computational Finance](https://papers.ssrn.com/abstract=2326253)).

## Die typischen Fehler

| Fehler | Was passiert | Beispiel bei uns |
| --- | --- | --- |
| **Look-ahead-Bias** | Der Test nutzt Informationen, die zum Zeitpunkt der Entscheidung noch nicht bekannt waren | Einstieg auf dem Hoch eines Bars, das erst am Bar-Ende feststeht; Tages-ATR inklusive heute |
| **Survivorship-Bias** | Nur Aktien, die heute noch existieren, werden getestet; Pleiten und Delistings fehlen | Universum aus der heutigen Symbol-Liste von Nasdaq Trader auf Jahre zurück angewendet |
| **Selektions- / Mehrfachtest-Bias** | Viele Varianten probiert, die beste behalten | `or-mid` und `or-low`, 1R/2R/3R, 10 Ticker durch die Time Machine, den besten nehmen |
| **Data Snooping** | Dieselben Daten werden immer wieder für neue Ideen benutzt | jede Woche ein neuer Filter auf denselben 60 Tagen |
| **Kosten vergessen** | Spread, Slippage, Gebühren fehlen | enge Stops, bei denen Kosten 0,2R ausmachen ([[R-Multiple und Erwartungswert]]) |
| **Regimewechsel** | Die Testphase war ein besonderer Markt | 60 Tage Aufwärtstrend, dann Seitwärtsphase |
| **Zu wenige Trades** | Zufall sieht aus wie Können | 20 Signale, 12 Treffer = 60 %, Intervall ±22 Punkte |

**Survivorship-Bias** ist seit Brown, Goetzmann, Ibbotson und Ross (1992) als ernstes Problem in Performance-Studien bekannt: Wer nur Überlebende betrachtet, findet scheinbare Muster, die es nicht gibt ([Review of Financial Studies 5(4)](https://ideas.repec.org/a/oup/rfinst/v5y1992i4p553-80.html)).

## Mehrfachtests: warum der beste Backtest lügt

Probiert man viele Varianten aus und behält die beste, ist deren Ergebnis systematisch zu gut, auch wenn **keine** Variante einen echten Vorteil hat.

- **Minimum Backtest Length.** Bailey, Borwein, López de Prado und Zhu zeigen: Mit 5 Jahren Daten sollte man **höchstens etwa 45 unabhängige Varianten** probieren; sonst findet man fast sicher eine mit einer Sharpe Ratio von 1 im Backtest, deren erwartete Sharpe Ratio danach null ist. Bei nur 2 Jahren Daten reichen schon **7 Varianten** dafür. Faustformel für die nötige Länge in Jahren: MinBTL < 2 · ln(N) ÷ E[max SR]². Ohne Angabe, wie viele Varianten probiert wurden, lässt sich ein Backtest nicht beurteilen ([„Pseudo-Mathematics and Financial Charlatanism“, Notices of the AMS 2014](https://carmamaths.org/jon/backtest.pdf)).
- **Probability of Backtest Overfitting (PBO)**: ein Verfahren (CSCV, kombinatorisch symmetrische Kreuzvalidierung), das schätzt, wie wahrscheinlich die IS-beste Variante OOS unterdurchschnittlich ist ([Bailey et al., SSRN](https://papers.ssrn.com/abstract=2326253); R-Paket [pbo](https://packages.oit.ncsu.edu/cran/web/packages/pbo/readme/README.html)).
- **Deflated Sharpe Ratio**: korrigiert eine Sharpe Ratio um die Zahl der Versuche und um nicht normalverteilte Renditen ([Bailey & López de Prado 2014, SSRN](https://papers.ssrn.com/abstract=2460551)).
- **Höhere Hürde.** Harvey, Liu und Zhu argumentieren, dass ein neuer Faktor wegen der vielen Tests in der Forschung eine t-Statistik über **3,0** statt 2,0 braucht, und dass viele veröffentlichte Ergebnisse vermutlich falsch sind ([„… and the Cross-Section of Expected Returns“, NBER](https://www.nber.org/papers/w20592)).
- **Technische Regeln nach Korrektur.** Sullivan, Timmermann und White testeten tausende technische Handelsregeln auf 100 Jahren Dow-Jones-Daten mit Whites „Reality Check“; nach Korrektur für Data Snooping hielt die beste Regel in späteren Daten keinen signifikanten Vorteil ([Journal of Finance 1999, LSE-Repositorium](https://researchonline.lse.ac.uk/id/eprint/119144)). Mehr dazu in [[Evidenz zu technischer Analyse]].

> [!warning] Unser eigenes Mehrfachtest-Problem
> Wer an einem Morgen zehn Ticker und je drei Stop-Varianten durch die Time Machine schickt und dann den Trade mit den besten Quoten nimmt, hat 30 Tests gemacht. Die beste Quote ist dann zum Teil Glück. Besser: Stop- und Zielregel **vorher** festlegen (Standard `or-mid`, 2R) und nur prüfen, ob dieser eine Plan ein Münzwurf ist.

## Monte-Carlo: was es kann und was nicht

Monte-Carlo-Simulation zieht viele zufällige Pfade aus einer angenommenen oder aus Daten geschätzten Verteilung. Das zeigt die **Streuung** möglicher Ergebnisse. Es kann aber nichts zeigen, was nicht in den Annahmen steckt.

Grenzen eines einfachen Bootstraps (Ziehen einzelner Beobachtungen mit Zurücklegen):

- **Abhängigkeiten gehen verloren.** Renditen haben kaum lineare Autokorrelation, aber ausgeprägte **Volatilitäts-Cluster**: Große Bewegungen folgen auf große Bewegungen. Auf sehr kurzen Intraday-Skalen (etwa 20 Minuten) gibt es zudem Mikrostruktur-Effekte ([Cont 2001, Quantitative Finance](https://ideas.repec.org/a/taf/quantf/v1y2001i2p223-236.html)). Wer Bars verschiedener Tage zufällig mischt, mischt ruhige und hektische Tage und unterschätzt Trends innerhalb eines Tages.
- **Fette Ränder** (seltene extreme Bewegungen) kommen nur vor, wenn sie in der Stichprobe waren.
- **Neues fehlt**: Earnings, Halts, Makro-Daten, die in den 60 Tagen nicht vorkamen, kommen auch in 10.000 Replays nicht vor.
- **Viele Replays ≠ viel Information.** 10.000 Pfade aus 60 Tagen enthalten nur die Information dieser 60 Tage. Die Zahl der Replays verkleinert den Simulationsfehler, nicht den Schätzfehler.

## Die Time Machine im Licht dieser Punkte

`/trader-timemachine` baut den Rest des Tages 10.000-mal aus den 5-Minuten-Bars der Aktie der letzten 60 Tage nach (nur volle Sitzungen, Bar aus derselben Tageszeit ± 2 Bars, skaliert auf den aktuellen Kurs) und spielt die Regel zusätzlich auf jeder vergangenen Sitzung durch.

| Punkt | Wie die Time Machine es macht | Bewertung |
| --- | --- | --- |
| Look-ahead | nutzt nie einen noch offenen Bar, mischt den heutigen Tag nicht in den Pool | gut |
| Stop und Ziel im selben Bar | zählt als Stop | vorsichtig, gut |
| Gap über den Stop | zählt als −1R | **optimistisch**: echte Fills können schlechter sein |
| Tageszeit | Bars aus ähnlicher Uhrzeit (Eröffnung ist anders als Mittag) | gut |
| Abhängigkeiten | jeder Bar unabhängig gezogen, aus beliebigen Tagen | **schwach**: Trendtage und Volatilitäts-Cluster gehen verloren |
| Datenmenge | 60 Tage, mindestens 20 volle Sitzungen | **klein**: ein Marktregime |
| Historie | dieselbe Regel auf jeder vergangenen Sitzung | echt, aber wenige Signale (TSLA-Beispiel: 33 in 59 Sitzungen) |
| Ereignisse | Earnings, News, Halts nur, wenn sie in den 60 Tagen vorkamen | **Lücke**, deshalb vorher `/trader-news` |
| Kosten | keine Kosten, kein Spread | **optimistisch** |
| Reproduzierbarkeit | fester Seed (19), gleicher Plan → gleiche Zahlen | gut |

Das Skill sagt selbst: eine Simulation, keine Vorhersage. Die **Historie** ist der ehrlichere Teil, aber mit 30 Signalen liegt das Intervall einer Trefferquote bei etwa ±18 Punkten. Im TSLA-Beispiel lagen die Replays bei 53,6 % Ziel-zuerst unter den getroffenen (nötig: 50 %), die Historie bei 13 Ziel zu 15 Stop und −0,062R. Beides zusammen heißt: **kein erkennbarer Vorteil**, und genau das sagt das Urteil „Close to a coin flip“.

> [!tip] So nutzt man die Time Machine sinnvoll
> - Als **Plausibilitätscheck** für einen vorher festgelegten Plan, nicht als Suchmaschine für den besten Plan.
> - `--until 15:55` verwenden, damit „neither“ unserem Flat-Zeitpunkt entspricht.
> - Die echte Prüfung ist das **Journal**: `/trading-journal stats` vergleicht die Quoten der Time Machine mit den tatsächlichen Ergebnissen. Das ist echtes Out-of-Sample.

## Checkliste für jeden Backtest

- [ ] Regel und Parameter **vor** dem Test aufgeschrieben?
- [ ] Wie viele Varianten wurden insgesamt probiert? Notiert?
- [ ] Nur Informationen verwendet, die zum Entscheidungszeitpunkt bekannt waren?
- [ ] Universum inklusive später delisteter Aktien, oder Bias bewusst?
- [ ] Kosten und Slippage abgezogen?
- [ ] Genug Trades (Faustregel: mindestens 30 je Setup, besser 100+)?
- [ ] Out-of-Sample-Zeitraum oder Paper-Trading-Phase danach?
- [ ] Funktioniert es in verschiedenen Marktphasen, oder nur in einer?

## Im Vault

- **`/trader-timemachine`**: Monte-Carlo plus Historie für **einen** Plan, 60 Tage, 5-Minuten-Bars, Seed 19. Stark gegen Look-ahead, schwach bei Datenmenge, Abhängigkeiten, Kosten.
- **`/trader-scanner`**: Universum aus den aktuellen Verzeichnissen von Nasdaq Trader; als Live-Scanner richtig, für historische Tests auf Jahre zurück entstünde Survivorship-Bias.
- **`/trading-journal stats`**: der eigentliche Out-of-Sample-Test, Trade für Trade, mit Vergleich zu den Quoten der Time Machine. Unter etwa 30 geschlossenen Trades je Setup keine Schlüsse.
- Siehe auch [[Strategien im Vergleich]] und [[Evidenz zu technischer Analyse]] für die Frage, welche Setups überhaupt Belege haben.

## Quellen

- `.claude/skills/trader-timemachine/SKILL.md` (Pool, Replays, Historie, Urteil, Seed), `trader-scanner/SKILL.md`, `trading-journal/SKILL.md`
- [Bailey, Borwein, López de Prado, Zhu: Pseudo-Mathematics and Financial Charlatanism (Notices of the AMS 2014)](https://carmamaths.org/jon/backtest.pdf) – MinBTL, 45 Varianten bei 5 Jahren, 7 bei 2 Jahren
- [Bailey, Borwein, López de Prado, Zhu: The Probability of Backtest Overfitting (SSRN / Journal of Computational Finance)](https://papers.ssrn.com/abstract=2326253)
- [CRAN-Paket pbo](https://packages.oit.ncsu.edu/cran/web/packages/pbo/readme/README.html)
- [Bailey & López de Prado: The Deflated Sharpe Ratio (SSRN)](https://papers.ssrn.com/abstract=2460551)
- [Harvey, Liu, Zhu: … and the Cross-Section of Expected Returns (NBER w20592)](https://www.nber.org/papers/w20592)
- [Sullivan, Timmermann, White (1999): Data-Snooping, Technical Trading Rule Performance, and the Bootstrap](https://researchonline.lse.ac.uk/id/eprint/119144)
- [Brown, Goetzmann, Ibbotson, Ross (1992): Survivorship Bias in Performance Studies](https://ideas.repec.org/a/oup/rfinst/v5y1992i4p553-80.html)
- [Cont (2001): Empirical properties of asset returns – stylized facts and statistical issues](https://ideas.repec.org/a/taf/quantf/v1y2001i2p223-236.html)
- Intervall für Trefferquoten: eigene Rechnung (siehe [[R-Multiple und Erwartungswert]])
