---
typ: wissen
erstellt: 2026-10-23
aktualisiert: 2026-10-23
quelle: Nutzer
tags:
  - trading
  - wissen
  - prop-firm
---

# Prop-Firms und Bot-Architektur

Geprüfte Einordnung der Gemini-Recherche von [[Yannick]] über LLM-Trading-Bots mit Obsidian-Gedächtnis bei Prop-Firms. Das Original steht unverändert in [[Gemini Prop-Trading-Bots]]. Hier steht, was davon stimmt, was nicht und was für dieses Setup gilt. Zurück zum Hub: [[Trading/Wissen/Übersicht]].

> [!warning] Keine Anlage- oder Steuerberatung
> Ein Wechsel von Paper Trading zu einer Prop-Firm ist eine Entscheidung von Yannick. Sie ist nicht gefallen. Bis dahin gilt [[Trading/Regeln]].

## Worum es geht

Eine Prop-Firm verkauft eine Prüfung (Challenge) auf einem simulierten Konto. Wer das Gewinnziel erreicht, ohne die Verlustgrenzen zu reißen, bekommt ein „Funded Account“ und einen Anteil der Gewinne (meist 80–90 %). Laut Gemini bestehen über 90 % die Prüfung nicht. Ein Ratgeber nennt 15–25 % beim ersten Versuch über große Firmen hinweg. Belastbare unabhängige Zahlen gibt es nicht.

## Prüfung der Kernaussagen

| Aussage im Original | Ergebnis der Prüfung (2026-10-23) |
| --- | --- |
| Obsidian als Markdown-Gedächtnis für einen LLM-Agenten | **passt**: so ist dieser Vault gebaut (siehe [[2026-10-21 Obsidian als Gedächtnis]]) |
| Risikolimits hart im Code, nicht als Prompt | **passt** und ist hier schon so: `/trader-risk` blockiert, bevor `/trader-broker` eine Order zeigt |
| FTMO 2-Step: Ziel 10 % / 5 %, Tagesverlust 5 %, Maximalverlust 10 % | **bestätigt** durch mehrere Drittquellen; FTMO-Seite selbst prüfen |
| FTMO 1-Step: Tagesverlust 3 % | **bestätigt** (Drittquellen); Maximalverlust 10 %, laut einer Quelle nachziehend am Tagesende |
| FTMO ersetzt im Oktober 2026 die Best-Day-Regel durch eine Consistency Rule (bester Tag ≤ 50 % des Gesamtgewinns) | **teils**: gilt laut Quellen nur für **1-Step** (neue Bestellungen ab 5. oder 12.10.2026, Quellen uneins), **nicht** für 2-Step. Das Rechenbeispiel ($6.000 von $10.000 → Gesamtgewinn muss auf $12.000) stimmt |
| Preise FTMO: 10k ~€155 … 100k ~€540 … 200k ~€1.080 | **teils veraltet**: 100k 2-Step €540 bestätigt; 10k wird 2026 eher mit €89 genannt |
| EAs bestehen zu 16 %, manuelle Trader zu 9 % | **nicht belegt**: keine Studie gefunden, Herkunft unklar; nicht verwenden |
| Apex Trader Funding ist am automatisierungsfreundlichsten | **eher falsch**: aktuelle Quellen sagen, Apex verbietet vollautomatisches Trading zumindest auf Funded- und Live-Konten, erlaubt nur halbautomatisch mit Aufsicht |
| FTMO erlaubt EAs, verbietet Fehlerausnutzung, HFT-/Latenz-Arbitrage und koordinierte Trades über Konten | **bestätigt** (FTMO-Seite zu verbotenen Praktiken); fremde EAs können an der Kapitalobergrenze scheitern |
| Equity statt Balance zählt für das Tageslimit | **plausibel** und bei FTMO üblich; offene Verluste zählen sofort |
| „Trade Randomization“: Preise zufällig verschieben, damit der Bot wie ein Mensch aussieht und Erkennungsalarme nicht anschlagen | **nicht übernehmen**: Das ist eine Umgehung der Betrugserkennung des Anbieters. Es kann gegen dessen Bedingungen verstoßen und zur Kontosperre führen |

## Was für dieses Setup gilt

- **Andere Welt:** Die Prop-Firms im Bericht handeln Forex, CFDs und Futures über MetaTrader 5, cTrader oder TradeLocker. Die Skills hier handeln US-Aktien über Alpaca, nur long. Ein Wechsel hieße neue Märkte, neue Schnittstelle und neue Regeln, nicht nur ein neues Konto.
- **Gleiche Grundregel:** Was der Bericht fordert (hartes Tageslimit, Stop vor dem Einstieg, kein Nachkaufen, Risiko vor jeder Order prüfen), gilt hier schon: [[Tageslimits und Regelwerk]], [[Positionsgröße]], [[Stop-Platzierung]].
- **Strengere Rechnung:** Bei Prop-Firms zählt der offene Verlust gegen das Tageslimit. Unser `/trader-risk` rechnet mit dem Verlust am Stop, also dem geplanten Maximum. Das ist vergleichbar, solange jede Position einen Stop beim Broker hat (Bracket-Order, siehe [[Ordertypen]]).
- **News-Sperren:** Viele Anbieter verbieten Trades in einem Fenster von 5–15 Minuten um FOMC, CPI und den Arbeitsmarktbericht. Termine: [[Makro-Termine]].
- **Nachweis zuerst:** Eine Prüfung zu kaufen ergibt erst Sinn, wenn das Journal einen Vorteil nach Kosten zeigt. Laut [[Strategien im Vergleich]] sind dafür etwa 30 Trades mit unveränderten Regeln nötig, besser mehr. Siehe auch [[Wie viele Day Trader gewinnen]] und [[Backtesting und Overfitting]].
- **Steuern:** Auszahlungen einer Prop-Firm sind wohl keine Kapitalerträge. Ratgeber tendieren zu gewerblichen oder sonstigen Einkünften, mit möglicher Gewerbeanmeldung. Das ist ungeklärt, vorher einen Steuerberater fragen. Siehe [[Steuern in Deutschland]].

## Offene Fragen

- Welcher Markt? Aktien wie bisher (wenige Prop-Firms, oft CFDs) oder Futures oder Forex (andere Handelszeiten, andere Skills nötig).
- Erlaubt der gewählte Anbieter einen vollautomatischen Bot mit Cloud-LLM? Vor dem Kauf in den aktuellen Regeln nachlesen und schriftlich bestätigen lassen.
- Ab welchem Journal-Ergebnis wäre eine Challenge überhaupt sinnvoll? Vorschlag zum Festlegen: Mindestzahl Trades und positiver Erwartungswert nach Kosten in R.

## Quellen

- Original: [[Gemini Prop-Trading-Bots]] (https://share.gemini.google/lyxULLZ2fPux)
- [FTMO: Introducing the 1-Step FTMO Challenge](https://ftmo.com/en/blog/introducing-the-1-step-ftmo-challenge/)
- [FTMO: Trading Objectives](https://ftmo.com/en/trading-objectives/)
- [FTMO (OANDA): Forbidden trading practices](https://ftmo.oanda.com/forbidden-trading-practices/)
- [FTMO (OANDA): Which instruments and strategies are allowed](https://ftmo.oanda.com/faq/which-simulated-instruments-can-i-trade-and-what-strategies-am-i-allowed-to-use/)
- [PropRuleGuard: FTMO Rules (Oct 2026)](https://propruleguard.com/firms/ftmo)
- [StonkJournal: FTMO Rules 2026](https://stonkjournal.com/articles/ftmo-review)
- [TradeTanto: FTMO Rules 2026, 1-Step & 2-Step](https://tradetanto.com/learn/ftmo-rules-evaluation-process)
- [ProptradingVibes: FTMO Preise 2026](https://proptradingvibes.com/de/blog/ftmo-account-sizes-pricing)
- [Traders Second Brain: Prop firm pass rate](https://traderssecondbrain.com/guides/prop-firm-pass-rate)
- [TradersPost: Apex Trader Funding Guide](https://blog.traderspost.io/article/apex-trader-funding-review)
- [PickMyTrade: 5 Prop Firm Automation Rules (2026)](https://blog.pickmytrade.io/5-prop-firm-automation-rules-before-you-run-a-bot-2026/)
- [CrossTrade: Apex Trader Funding and AI Workflows](https://crosstrade.io/learn/prop-firm-ai-trading/apex-trader-funding)
- [track360: Prop Trading Steuern Deutschland 2026](https://track360.io/de/blog/prop-trading-steuern-deutschland-2026)

Die meisten Quellen sind Drittanbieter-Ratgeber, einige verkaufen selbst Bots oder Prop-Konten. Regeln und Preise ändern sich oft, vor jeder Entscheidung die Seite des Anbieters prüfen.
