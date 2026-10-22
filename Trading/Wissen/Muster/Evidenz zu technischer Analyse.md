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

# Evidenz zu technischer Analyse

Was die Forschung über Chartmuster, Indikatoren und Handelsregeln weiß: Einige Muster tragen statistisch Information, aber Gewinne nach Kosten sind selten, schwinden mit der Zeit und verschwinden oft, wenn man ehrlich zählt, wie viele Regeln probiert wurden. Diese Notiz fasst die wichtigsten Studien zusammen und sagt, was davon für Day Trading mit $5.000 übrig bleibt.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Die Studien im Überblick

| Studie | Daten | Befund |
| --- | --- | --- |
| Brock, Lakonishok, LeBaron (1992) | Dow Jones täglich 1897–1986; 26 Regeln (gleitende Durchschnitte, Ausbruch aus einer Handelsspanne) | Kaufsignale brachten höhere und ruhigere Renditen als Verkaufssignale, Renditen nach Verkaufssignalen waren negativ; nicht mit vier gängigen Zufallsmodellen vereinbar |
| Sullivan, Timmermann, White (1999) | dieselben Daten plus 1987–1996; 7.846 Regeln | 1897–1986 schlugen einige Regeln den Markt auch nach Korrektur für Data Snooping. 1987–1996 nicht mehr: Die beste Regel war nur mit etwa 12 % Irrtumswahrscheinlichkeit besser, also nicht signifikant |
| Lo, Mamaysky, Wang (2000) | US-Aktien 1962–1996, zehn Formationen per Computer erkannt | Formationen liefern „zusätzliche Information“ über die Renditeverteilung, vor allem bei Nasdaq-Werten (alle 10 signifikant, bei NYSE/AMEX 5 von 10). Ausdrücklich kein Nachweis von Gewinnen |
| Savin, Weller, Zvingelis (2007) | S&P 500 und Russell 2000, 1990–1999 | Kopf-Schulter als alleinige Strategie kaum profitabel, sagt aber Überrenditen von etwa 5–7 % p. a. voraus |
| Park, Irwin (2007) | Überblick über 95 moderne Studien | 56 positiv, 20 negativ, 19 gemischt. Gewinne vor allem bis Anfang der 1990er. Die meisten Studien haben Mängel: Data Snooping, nachträgliche Auswahl der Regeln, schlecht geschätzte Risiken und Kosten |
| Marshall, Cahan, Cahan (2008) | 5-Minuten-Daten des S&P-500-ETF (SPDR) 2002–2003; 7.846 Regeln | **Intraday:** keine Regel profitabel nach Korrektur für Data Snooping, schon vor Kosten |
| Bajgrowicz, Scaillet (2012) | Dow Jones 1897–2011, neue Methode (False Discovery Rate) | Die künftig besten Regeln ließen sich vorab nie auswählen. Schon geringe Kosten heben selbst die Gewinne in der Stichprobe vollständig auf |
| Duvinage, Mazza, Petitjean (2013) | 30 Dow-Werte, 5-Minuten-Kerzen 2010–2011 | Kerzenmuster schlagen nach Kosten und Snooping-Korrektur Kaufen und Halten nicht; siehe [[Kerzenmuster]] |
| Moskowitz, Ooi, Pedersen (2012) | 58 Futures (Aktienindizes, Währungen, Rohstoffe, Anleihen) | Zeitreihen-Momentum: Die Rendite der letzten 1–12 Monate setzt sich fort, für jedes untersuchte Instrument |
| Neely, Rapach, Tu, Zhou (2014) | US-Aktienmarkt, monatlich | Technische Indikatoren (Durchschnitte, Momentum, Volumen) sagen die Marktrendite so gut voraus wie makroökonomische Größen, beide ergänzen sich |
| Gao, Han, Li, Zhou (2018) | S&P-500-ETF 1993–2013 | Die Rendite der ersten halben Stunde sagt die der letzten halben Stunde voraus; klein (R² etwa 2 %), stärker an volatilen Tagen mit hohem Volumen |

## Data Snooping: warum so viele Regeln „funktionieren“

Wer viele Regeln an denselben Daten testet, findet zwangsläufig welche, die gut aussehen. Beispiel aus Marshall, Cahan und Cahan: Von 7.846 Regeln waren vor der Korrektur 163 auf dem 5-%-Niveau signifikant. Rein zufällig wären bei 7.846 voneinander unabhängigen Tests etwa 392 zu erwarten (7.846 × 5 %). Die „Treffer“ sind also nicht mehr, als der Zufall liefert. (Die Regeln hängen untereinander zusammen, die Rechnung ist nur eine Veranschaulichung.)

Dasselbe passiert im Kleinen jedem Trader:

- Parameter so lange drehen (RSI 9 statt 14, Stop 1,3 ATR statt 1,5), bis die letzten Wochen gut aussehen.
- Im Chart nur die Formationen sehen, die funktioniert haben.
- Nach drei Gewinnen eine Regel für „bewiesen“ halten.

Siehe [[Backtesting und Overfitting]].

## Kosten: der stille Gegner

Auch ohne Kommission kosten Spread und Slippage bei jedem Trade. Rechnung in R:

| Annahme | Wert |
| --- | --- |
| Risiko je Aktie (Stop-Abstand) | $0,45 |
| Kosten je Aktie, hin und zurück (halber Spread zweimal plus Slippage, angenommen) | $0,03 |
| Kosten in R | 0,03 / 0,45 = 0,067 R |
| nötige Trefferquote bei Ziel 1R ohne Kosten | 50 % |
| nötige Trefferquote mit Kosten: (1 + 0,067) / 2 | **53,3 %** |

Je enger der Stop, desto teurer: Bei $0,15 Stop-Abstand sind dieselben $0,03 schon 0,2 R, und die nötige Trefferquote bei 1R steigt auf 60 %. Siehe [[Spread Liquidität und Slippage]] und [[R-Multiple und Erwartungswert]].

## Was übrig bleibt

> [!tip] Am besten belegt
> 1. **Trend und Momentum über Wochen bis Monate** (Zeitreihen-Momentum, technische Indikatoren als Ergänzung zu Makrodaten). Das ist kein Day Trading, aber ein Grund, im Tageschart lieber mit dem Trend zu handeln.
> 2. **Levels haben einen Mechanismus:** Orders häufen sich an runden Zahlen und an Support/Resistance, das Orderbuch ist dort tiefer. Siehe [[Unterstützung und Widerstand]].
> 3. **Aufmerksamkeit und Volumen:** Ungewöhnlich hohes Volumen geht mit späteren Renditen einher (Monatshorizont). Siehe [[Volumen und relatives Volumen]].
> 4. **Kleine Intraday-Effekte gibt es** (Momentum der ersten halben Stunde im Index), aber sie sind klein im Verhältnis zu Kosten.

> [!warning] Schwach oder nicht belegt
> - Klassische Chartformationen als eigenständige, profitable Strategie: Information ja, Gewinne nach Kosten kaum nachgewiesen. Die Erfolgsquoten von Bulkowski messen Bewegungen bis zu einem nachträglich bekannten Hoch, ohne Stop und Kosten. Siehe [[Chartformationen]].
> - Kerzenmuster an großen US-Aktien: nach Kosten nichts. Siehe [[Kerzenmuster]].
> - Intraday-Regeln am S&P-500-ETF: nach Snooping-Korrektur nichts (2002–2003).
> - Die Wirkung schwindet: Park und Irwin sehen Gewinne vor allem bis Anfang der 1990er; Bulkowskis Formationen liefen in den 2010ern deutlich schwächer als in den 1990ern. Was bekannt wird, wird weggehandelt.

Eine Ausnahme mit Vorbehalt: Zarattini, Barbon und Aziz (2024) berichten für einen 5-Minuten-Opening-Range-Breakout auf Aktien mit sehr hohem relativem Volumen sehr hohe Backtest-Gewinne 2016–2023. Das ist ein nicht begutachtetes Arbeitspapier, mit Hebel und Leerverkäufen, und genau die Art Ergebnis, die nach Veröffentlichung oft schrumpft. Siehe [[Opening Range Breakout]].

Was technische Analyse auch ohne Vorhersagekraft leistet: Sie gibt **feste Punkte für Einstieg, Stop und Ziel**. Der Nutzen liegt dann in der Disziplin und der Risikosteuerung, nicht in der Prognose. Ob ein Trader damit gewinnt, entscheidet vor allem die Verlustbegrenzung. Siehe [[Wie viele Day Trader gewinnen]], [[Psychologie und Disziplin]].

## Im Vault

- **Die Time Machine ist ein Null-Modell.** Sie zieht für 10.000 Wiederholungen zufällige 5-Minuten-Kerzen derselben Tageszeit aus den letzten 60 Tagen. Ein Muster oder Indikator hat darin keine Wirkung. Was sie zeigt, folgt aus Schwankung, Stop- und Zielabstand. Wenn ein Setup wirklich einen Vorteil hat, müsste die echte Trefferquote im Journal **über** den Quoten der Time Machine liegen. Das vergleicht der Skill `trading-journal` in `Trading/Statistik.md`.
- **Die Historie der Time Machine ist klein.** Sie läuft nur für `orb` und nur über etwa 60 Tage. Im Doku-Beispiel (TSLA) waren es 33 Fälle: 13 Ziel, 15 Stop, 5 weder noch. Bei rund 33 Fällen und einer Quote um 40 % liegt der Zufallsfehler bei etwa ±17 Prozentpunkten (95 %). Daraus lässt sich wenig schließen.
- **Der Scanner** sagt „passt zur Regel“, nie „kaufen“. Das passt zur Forschung: Eine Regel ist ein Filter, kein Vorteil.
- **Eigene Statistik:** Nach 30, 50, 100 Trades im Journal prüfen, ob ein Setup die Quoten der Time Machine schlägt, und nicht vorher die Regeln wechseln. Paper Trading bleibt Standard (`"paper": true`).

Verwandt: [[Indikatoren]], [[Bull Flag]], [[Strategien im Vergleich]], [[Backtesting und Overfitting]].

## Quellen

- Brock, Lakonishok, LeBaron (1992), „Simple Technical Trading Rules and the Stochastic Properties of Stock Returns“, Journal of Finance 47(5), 1731–1764: https://ideas.repec.org/a/bla/jfinan/v47y1992i5p1731-64.html
- Sullivan, Timmermann, White (1999), „Data-Snooping, Technical Trading Rule Performance, and the Bootstrap“, Journal of Finance 54(5), 1647–1691; Arbeitspapier mit Volltext: https://www.fmg.ac.uk/sites/default/files/2020-11/dp303.pdf
- Lo, Mamaysky, Wang (2000), „Foundations of Technical Analysis“, Journal of Finance 55(4), 1705–1765: https://www.nber.org/papers/w7613
- Savin, Weller, Zvingelis (2007), „The Predictive Power of ‚Head-and-Shoulders‘ Price Patterns in the U.S. Stock Market“, Journal of Financial Econometrics 5(2): https://ideas.repec.org/a/oup/jfinec/v5yi2p243-265.html
- Park, Irwin (2007), „What Do We Know About the Profitability of Technical Analysis?“, Journal of Economic Surveys 21(4), 786–826: https://ideas.repec.org/a/bla/jecsur/v21y2007i4p786-826.html
- Marshall, Cahan, Cahan (2008), „Does intraday technical analysis in the U.S. equity market have value?“, Journal of Empirical Finance 15(2), 199–210: https://ideas.repec.org/a/eee/empfin/v15y2008i2p199-210.html; Zahlen (163 von 7.846) laut CXO Advisory: https://cxoadvisory.com/technical-trading/technical-analysis-anathema-to-the-academic-world
- Bajgrowicz, Scaillet (2012), „Technical trading revisited: False discoveries, persistence tests, and transaction costs“, Journal of Financial Economics 106(3), 473–491: https://ideas.repec.org/a/eee/jfinec/v106y2012i3p473-491.html
- Duvinage, Mazza, Petitjean (2013), Quantitative Finance 13(7); Zusammenfassung: https://cxoadvisory.com/technical-trading/testing-japanese-candlesticks-intraday-on-liquid-stocks
- Moskowitz, Ooi, Pedersen (2012), „Time Series Momentum“, Journal of Financial Economics 104, 228–250: https://papers.ssrn.com/abstract=2089463
- Neely, Rapach, Tu, Zhou (2014), „Forecasting the Equity Risk Premium: The Role of Technical Indicators“, Management Science 60(7), 1772–1791: https://files.stlouisfed.org/files/htdocs/wp/2010/2010-008.pdf
- Gao, Han, Li, Zhou (2018), „Market Intraday Momentum“, Journal of Financial Economics 129, 394–414: https://www3.nd.edu/~zda/intramom.pdf
- Zarattini, Barbon, Aziz (2024), „A Profitable Day Trading Strategy For The U.S. Equity Market“, Swiss Finance Institute Research Paper: https://ideas.repec.org/p/chf/rpseri/rp2498.html
- Bulkowski, „Chart Pattern Performance over Decades“: https://thepatternsite.com/TimePerformance.html
- Skills: `.claude/skills/trader-timemachine/SKILL.md`, `.claude/skills/trader-scanner/SKILL.md`, `.claude/skills/trading-journal/`
