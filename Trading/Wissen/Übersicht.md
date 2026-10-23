---
typ: wissen
erstellt: 2026-10-22
aktualisiert: 2026-10-22
quelle: Recherche
tags:
  - trading
  - wissen
---

# Trading-Wissen

Nachschlagewerk zum Day Trading, recherchiert am 2026-10-22, jede Notiz mit Quellen. Es ergänzt [[Trading/Regeln]] und das Journal in [[Trading/Übersicht]]. Was sich aus eigenen Trades ergibt, gehört nicht hierher, sondern nach [[Gedächtnis/Erkenntnisse/Trading]].

> [!warning] Keine Anlageberatung
> Die Notizen fassen Studien und Regeln zusammen. Die meisten Day Trader verlieren Geld, siehe [[Wie viele Day Trader gewinnen]]. Geübt wird mit Paper Trading.

## Das Wichtigste in fünf Sätzen

1. Der Vorteil eines Setups ist klein oder unbewiesen. Darum kommt zuerst das Risiko: $50 je Trade (1 % des Budgets), Stop vor dem Einstieg, siehe [[Positionsgröße]] und [[Stop-Platzierung]].
2. Gestartet wird mit einer einzigen Strategie, dem 15-Minuten-[[Opening Range Breakout]], weil die Skills sie von Anfang bis Ende abdecken. Siehe [[Strategien im Vergleich]].
3. Kosten und Slippage fressen bei engen Stops schnell 0,1–0,2R, und Paper Trading zeigt sie nicht. Siehe [[R-Multiple und Erwartungswert]] und [[Paper Trading bei Alpaca]].
4. Lange Verlustserien sind normal und kein Beweis, dass die Strategie kaputt ist. Ein Urteil gibt es erst nach etwa 30 Trades mit unveränderten Regeln. Siehe [[Drawdown und Risk of Ruin]] und [[Backtesting und Overfitting]].
5. Vor jedem Tag die Termine prüfen ([[Makro-Termine]], [[Earnings-Saison]]) und bei jeder Aktie den Grund der Bewegung kennen ([[Katalysatoren]]).

## Strategien

- [[Strategien im Vergleich]]: Tabelle, Evidenz, womit anfangen
- [[Opening Range Breakout]] · [[Momentum und Gap and Go]] · [[VWAP-Strategien]]
- [[Pullback im Trend]] · [[Mean Reversion und Oversold Bounce]] · [[Breakout aus 20-Tage-Hoch]]

## Muster und Indikatoren

- [[Evidenz zu technischer Analyse]]: was nach Kosten übrig bleibt
- [[Bull Flag]] · [[Chartformationen]] · [[Kerzenmuster]]
- [[Unterstützung und Widerstand]] · [[Volumen und relatives Volumen]] · [[Indikatoren]]

## Risiko und Psychologie

- [[Positionsgröße]] · [[R-Multiple und Erwartungswert]] · [[Stop-Platzierung]]
- [[Drawdown und Risk of Ruin]] · [[Kelly-Kriterium]] · [[Tageslimits und Regelwerk]]
- [[Psychologie und Disziplin]] · [[Wie viele Day Trader gewinnen]] · [[Backtesting und Overfitting]]

## Markt und Regeln

- [[Handelszeiten und Sessions]] · [[Ordertypen]] · [[Spread Liquidität und Slippage]]
- [[Handelsstopps und LULD]] · [[Pattern Day Trader Regel]]
- [[Paper Trading bei Alpaca]] · [[Steuern in Deutschland]]

## News und Termine

- [[Katalysatoren]] · [[News richtig lesen]] · [[Earnings-Saison]]
- [[Makro-Termine]] · [[Saisonalität und Kalendereffekte]]
- [[Marktlage Oktober 2026]]: Momentaufnahme, veraltet schnell

## Prop-Firms und Automatisierung

- [[Prop-Firms und Bot-Architektur]]: geprüfte Einordnung der Gemini-Recherche von Yannick
- [[Gemini Prop-Trading-Bots]]: Original, ungeprüft

## Ablauf eines Trades mit Wissen

| Schritt | Skill | Nachlesen |
| --- | --- | --- |
| Setups finden | `/trader-scanner` | [[Opening Range Breakout]], [[Breakout aus 20-Tage-Hoch]], [[Bull Flag]] |
| Grund der Bewegung | `/trader-news` | [[Katalysatoren]], [[News richtig lesen]] |
| Einstieg | `/trader-entry` | [[Volumen und relatives Volumen]], [[Unterstützung und Widerstand]] |
| Stop und Ziel | `/trader-exit` | [[Stop-Platzierung]], [[R-Multiple und Erwartungswert]] |
| Quoten | `/trader-timemachine` | [[Backtesting und Overfitting]] |
| Größe | `/trader-budget` | [[Positionsgröße]] |
| Limits | `/trader-risk` | [[Tageslimits und Regelwerk]] |
| Order | `/trader-broker` | [[Ordertypen]], [[Paper Trading bei Alpaca]] |
| Journal | `trading-journal` | [[Psychologie und Disziplin]] |

## Offene Lücken in den Skills

Bei der Recherche aufgefallen, nicht geändert (Skills nur nach Rückfrage anfassen):

- Der Scanner kennt kein relatives Volumen, keinen VWAP, keine EMA und keine Pre-Market-Daten. Einen Gap-Scanner gibt es nicht.
- `oversold` nutzt RSI 14 statt RSI(2) und hat keinen Filter über dem 200-Tage-Durchschnitt.
- `bull_flag` prüft nur Tagesschlusskurse, weder Volumen noch Ausbruch.
- `trader-entry --min-volume-x` vergleicht mit den Bars der Opening Range, das ist kein RVOL.
- Die ATR in `trader-exit` ist ein einfacher Schnitt aus 5-Minuten-Bars, keine Wilder-Glättung.
- Die Time Machine rechnet ohne Kosten, mischt Bars verschiedener Tage und hat nur für `orb` eine Historie.
