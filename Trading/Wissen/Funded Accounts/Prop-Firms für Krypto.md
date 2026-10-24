---
typ: wissen
erstellt: 2026-10-23
aktualisiert: 2026-10-23
quelle: Recherche
tags:
  - trading
  - wissen
  - funded
---

# Prop-Firms für Krypto

Krypto-Prop-Firms, bei denen ein Bot über die API einer Börse oder eine eigene Schnittstelle handeln darf: wie die Anbindung funktioniert, was erlaubt ist, Preise, Regeln, Auszahlung, Deutschland. Dazu die Frage, ob das zu einem Aktien-ORB-Bot passt. Hub: [[Funded Accounts]].

> [!warning] Stand 2026-10-23, keine Empfehlung
> Auch hier ist alles **simuliert**: Bei HyroTrader steht wörtlich „There is no real-capital stage at any point“, auch das Funded-Konto ist ein Demokonto. Bezahlt wird eine Gebühr oder Kaution, ausgezahlt ein Vertragsanteil am simulierten Gewinn. Krypto-Prop-Firms sitzen meist in den VAE, auf den Britischen Jungferninseln oder in Hongkong und sind nicht reguliert. Keine Anlage-, Rechts- oder Steuerberatung, kein Affiliate-Link.

## Kurzüberblick

| Anbieter | Anbindung | Eigener Bot / KI-Agent | Gebühr 100k | Tagesverlust / Gesamt | Deutschland |
| --- | --- | --- | --- | --- | --- |
| **HyroTrader** | eigenes **Bybit- oder BloFin-Demokonto per Börsen-API**, oder Hyro-Plattform mit **MCP-Server und Agent-Token** | **ja**, „as long as the strategy is your own“, KI-Agenten ausdrücklich erlaubt | 2-Step $579 (Kaution, mit erster Auszahlung zurück) | 5 % / 10 % (2-Step) | erlaubt (nicht auf der Sperrliste) |
| **Velotrade** | DXtrade-API (REST und WebSocket) | laut eigenem Blog ja, ohne Freigabe | nicht bestätigt | 3–5 % / statisch | nicht bestätigt |
| **Kraken Prop / Breakout** | in Kraken Pro bzw. Breakout-Terminal | **nicht bestätigt** | nicht bestätigt (ab ~$20) | ≈ 3–6 % statisch (laut Kraken) | nicht bestätigt |
| **Bitfunded** | eigene Plattform (nicht bestätigt) | laut Ratgebern ja, mit Auflagen | $799 (laut Startseite, Modell unklar) | laut Ratgebern 5 % / 10 % | nicht bestätigt |
| **Crypto Fund Trader** | laut Ratgeber MT5, Match-Trader, Bybit | **nicht bestätigt** | nicht bestätigt | laut Ratgebern 4–5 % / 6–10 % | nicht bestätigt |

Nur HyroTrader ließ sich vollständig aus offiziellen Seiten belegen. Für die anderen gilt: Seite gesperrt oder nur per JavaScript lesbar, Angaben aus Ratgebern oder eigener Werbung, vor einem Kauf selbst prüfen.

## HyroTrader

Betreiber: HYRO TECHNOLOGIES FZ-LLC (Ras Al Khaimah, VAE), Funded-Konten über HYROTRADER TECHNOLOGIES LTD (Britische Jungferninseln), Kartenzahlung für EWR-Kunden über Hyro Finance (Bratislava). Gestartet 2023.

### So funktioniert die Anbindung

| Weg | Wie | Bots |
| --- | --- | --- |
| **Bybit** | Man eröffnet ein eigenes **Bybit-Demokonto**, erstellt dort einen API-Schlüssel (Lesen/Schreiben, Unified Account, ohne IP-Sperre) und trägt ihn bei HyroTrader ein. HyroTrader liest das Konto über die API mit. Orders gehen in die Demo-Umgebung von Bybit, nie ins echte Orderbuch. | Bot spricht direkt mit der **Bybit-Demo-API**. Je Challenge ein eigener Schlüssel; Schlüssel nicht ändern oder löschen, sonst Abbruch. |
| **BloFin** | wie Bybit, mit BloFin-Demokonto (80+ Paare) | Bot an die BloFin-Demo-API |
| **Hyro** (eigene Plattform) | kein Börsenkonto nötig; eigene Simulation auf Basis der Bybit-Kurse mit Gebühren und Slippage; Market, Limit, Stop-Loss, Take-Profit, Trailing Stop | **MCP-Server**: unter „Settings → Agent tokens“ ein Token erzeugen (2FA Pflicht), Lese- oder Handelsrecht wählen, Server und Token in einem MCP-fähigen KI-Assistenten eintragen. HyroTrader nennt Claude ausdrücklich. Nur für Challenges auf der Hyro-Plattform. Eine Schritt-für-Schritt-Anleitung ist laut FAQ „coming soon“. |
| Terminals | Tealstreet oder Tiger.com, API-Schlüssel erstellt HyroTrader | nicht für USA und Länder, in denen Bybit gesperrt ist |

Gehandelt werden nur **USDT-Perpetual-Futures** (Bybit 700+ Paare, Hebel bis 100x). Verboten: Spot, USDC-Perpetuals, COIN-M, Optionen und EUR/USD. Laut FAQ sind auf Bybit auch **tokenisierte Aktien**, Metalle und Öl als USDT-Paare erlaubt; welche Aktien und zu welchen Zeiten: **nicht bestätigt**.

### Bots und KI

- FAQ: „Can I use a trading bot or an AI agent? Yes, as long as the strategy is your own. You can automate it with a bot, a script or an AI agent, and we issue agent tokens for exactly that.“
- Verboten (AGB §10): jedes System, „bot, expert advisor, algorithm, script, application-programming-interface client, artificial-intelligence agent or agent token that executes a strategy that is not your own“, also gekaufte Bots mit fremder Strategie, Copy-Trading, Konto-Spiegelung, Signaldienste. Außerdem: Ausnutzen von Plattformfehlern, Latenz und Feed-Unterschieden; Strategien, die nur auf News-Veröffentlichungen zielen; Martingale; Hedging über mehrere Konten.
- Ein Ratgeber (April 2026) behauptet, in der Challenge seien Fremd-Bots verboten und eigene Bots erst ab 15 % Gewinn erlaubt. Die aktuellen offiziellen Seiten sagen das nicht; im Zweifel beim Support schriftlich nachfragen.

### Regeln und Preise

| | Zero-Step | One-Step | Two-Step |
| --- | --- | --- | --- |
| Ziel | 10 % | 10 % | 10 % + 5 % |
| Tagesverlust | 3 % | 4 % | 5 % |
| Maximalverlust | 5 % | 6 % | 10 % |
| Mindestdauer | 1 Tag | 5 Tage | 5 + 5 Tage |
| Verteilung | kein Trade > 50 % des Ziels | kein Tag > 40 % des Ziels | kein Tag > 40 % des Ziels |
| Bezahlung | Gebühr, nicht erstattbar | Kaution, mit 1. Auszahlung zurück | Kaution, mit 1. Auszahlung zurück |
| 5k / 10k / 25k / 50k | $89 / $169 / $379 / $629 | $69 / $129 / $299 / $499 | $59 / $119 / $249 / $379 |
| 100k / 200k | $949 / – | $749 / $1.299 | $579 / $969 |

- **Tagesverlust:** Tagesgrenze = Equity um **00:00 UTC** minus fester Prozentsatz vom Startkapital; offene Verluste und Gebühren zählen. Die Grenze steigt im Tagesverlauf nicht mit („static daily drawdown“).
- **Stop-Loss** nicht Pflicht, aber empfohlen. Höchstens 5 % des Startkapitals (inkl. Hebel) in Kleinwerten unter $100 Mio. Börsenwert.
- **News** erlaubt, nur keine reine News-Strategie. **Über Nacht und Wochenende** erlaubt. Konto schließt nach 30 Tagen ohne Trade.
- **Obergrenze:** $400.000 in Challenges, $200.000 in Funded-Konten je Person.
- **Auszahlung:** ab $100 Gewinn nach Aufteilung, jederzeit, in USDT oder USDC binnen 24 Std.; Anteil 80 %, bei One- und Two-Step nach Ermessen bis 90 %. Vorher alle Positionen schließen.
- **Länder:** Sperrliste in den AGB (u. a. Russland, Belarus, Iran, Nordkorea, Syrien, Kuba, Venezuela); **Deutschland, USA und UK stehen nicht drauf**. Wer Bybit nicht nutzen darf, soll die Hyro-Plattform nehmen. Ob ein Bybit-Demokonto aus Deutschland (dort ist Bybit EU zuständig) für die Challenge geht: **nicht bestätigt**. KYC erst nach bestandener Prüfung, bei HyroTrader, nicht bei Bybit.

## Weitere Anbieter (2026 aktiv, schwächer belegt)

### Velotrade

Laut eigener Seite: Multi-Asset-Prop-Firm (Krypto, Forex, Aktien wie TSLA, Indizes wie SPY, Rohstoffe) mit **DXtrade-API** (REST und WebSocket, Login wie am Desktop), „No additional fee, no application, no approval process“. Erlaubt: eigene Bots in Python oder JavaScript, Signal-Automatisierung, „AI-assisted trading“. Verboten: Grid, Arbitrage, Tick-Scalping, HFT, koordinierte Bots über Konten. Pläne mit 3–5 % Tagesverlust (Reset 00:30 UTC) und statischem Gesamtverlust (3–10 % je Plan), Anteil 80–90 %, ab etwa $40. Betreiber laut Blog Velotrade Re Limited, Hongkong. Wann das Prop-Angebot startete und welche Länder zugelassen sind: **nicht bestätigt**. Alle Angaben stammen aus der Werbung des Anbieters selbst.

### Kraken Prop und Breakout

Kraken hat Breakout im September 2025 übernommen und im Mai 2026 Kraken Prop in Kraken Pro gestartet. Laut Kraken: statischer Maximalverlust (Kraken Funded 3 %, Breakout je Plan ≈ 3–6 %), keine Consistency-Regel, keine Mindesttage, 80 % Anteil (90 % gegen Aufpreis), Auszahlung in USDC binnen etwa 24 Std.; Kraken nennt es selbst „an unregulated service“. Laut Ratgeber 60+ Perpetuals mit Hebel bis 5x. **Ob Bots oder die Kraken-API erlaubt sind, steht auf keiner gefundenen Seite**; die Seite von Breakout war gesperrt. Deutschland: nicht bestätigt.

### Bitfunded

Laut Startseite simulierte Krypto-Challenges bis $100.000 (Preise $79 bis $799, daneben eine zweite Preisreihe bis $1.399, Zuordnung unklar), 80/20-Aufteilung, Auszahlung binnen 24 Std. Laut Ratgebern Bots und API erlaubt, aber Stop-Loss binnen 5 Minuten Pflicht, kein Martingale, kein Copy-Trading; Drawdown je nach Quelle statisch oder am Tagesende nachziehend. **Nicht bestätigt.**

### Crypto Fund Trader

Laut Ratgebern MT5, Match-Trader und Bybit, auch Forex, Indizes und Aktien-CFDs; 4–5 % Tagesverlust. Bot-Regel und Preise **nicht bestätigt** (Startseite leitet nur weiter).

## Passt das zum Aktien-ORB-Bot?

> [!important] Eher nicht, außer als eigenes neues Projekt
> Der Bot ist für **US-Aktien während der New Yorker Börsenzeit** gebaut: Opening Range der ersten 15 Minuten ab 9:30 NY, Einstiege bis 15:30, glatt um 15:55 ([[Opening Range Breakout]]). Krypto-Perpetuals laufen **rund um die Uhr**, sieben Tage die Woche.

- **Keine Eröffnung, keine Opening Range:** Das Setup lebt von der Eröffnungsauktion und dem Volumenschub um 9:30 NY. Bei Krypto gibt es keinen solchen Start. Man könnte eine Ersatz-Range um 00:00 UTC oder um den US-Handelsbeginn bauen, das wäre aber ein neues Setup und müsste von vorn getestet werden ([[Backtesting und Overfitting]]).
- **Andere Volatilität:** Bitcoin und vor allem Altcoins schwanken stärker und springen nachts und am Wochenende. Mit Hebel bis 100x reißt ein Stop an der Range-Mitte schnell das Tageslimit. Die Stop- und Zielabstände von `/trader-exit` und die Quoten der Time Machine aus 5-Minuten-Aktienbalken lassen sich nicht übertragen.
- **Andere Tagesgrenze:** HyroTrader rechnet den Tag ab 00:00 UTC, also 20:00 New Yorker Sommerzeit. Für einen Bot, der um 15:55 glattstellt, ist das unkritisch; für einen 24/7-Bot heißt es, dass ein Verlust kurz vor Mitternacht UTC und einer kurz danach auf zwei Tage fallen.
- **Daten und Skills:** Scanner, News (SEC-8-K, Yahoo), Earnings-Analyse und Pelosi-Tracker sind auf US-Aktien gebaut. Für Krypto bringen sie nichts.
- **Tokenisierte Aktien:** HyroTrader erlaubt auf Bybit auch tokenisierte Aktien als USDT-Paare. Das klingt passend, aber Liste, Handelszeiten, Liquidität und Kursbildung außerhalb der US-Börsenzeit sind **nicht bestätigt**; vor jeder Idee in diese Richtung zuerst prüfen, ob diese Perpetuals außerhalb der Börsenzeit überhaupt mit der Aktie mitlaufen.
- **Was technisch passt:** Die Anbindung ist hier am nächsten an dem, was der Bot heute tut. Bybit hat eine REST-API wie Alpaca, und der MCP-Weg von HyroTrader wäre sogar eine direkte Verbindung aus einer Claude-Sitzung. Mehr dazu in [[Schnittstellen für Bots]] und [[Bot an Prop-Firm anbinden]].

## Für diesen Bot

- Für den bestehenden ORB-Bot sind [[Prop-Firms für US-Aktien]] die naheliegende Wahl, danach [[Prop-Firms für Futures]] (Index-Futures zur US-Börsenzeit). Krypto ist ein eigenes Projekt mit neuem Setup, neuen Tests und neuem Journal.
- Wer das trotzdem testen will: HyroTrader ist der einzige Anbieter, bei dem Bots und KI-Agenten offiziell und ausdrücklich erlaubt und die Regeln vollständig öffentlich sind. Zuerst mit Paper-Daten über die Bybit-Demo-API oder die kostenlose Testversion üben; laut AGB darf die Testversion aber nicht zum „Kalibrieren“ verbotener Praktiken genutzt werden.
- **Agent-Token und API-Schlüssel sind Zugangsdaten.** Sie gehören nicht in den Vault, nicht in Notizen und nicht ins Git (siehe CLAUDE.md), sondern in die Umgebungsvariablen der Cloud-Umgebung.
- Eine Challenge kostet echtes Geld und Auszahlungen sind echtes Geld. Dafür gilt [[Trading/Regeln]]: Entscheidung und jede Order mit echtem Bezug nur mit ausdrücklichem Ja von Yannick. Ablauf und Kosten: [[Kauf und Ablauf einer Challenge]]; Steuern: [[Recht Steuern und Risiken]], [[Steuern in Deutschland]].
- Mit 5 Paper-Trades ist noch kein Vorteil belegt, für Aktien nicht und für Krypto erst recht nicht ([[Wie viele Day Trader gewinnen]]).

## Quellen

Abruf 2026-10-23/24. Offizielle Seiten zuerst; „Ratgeber“ sind Drittanbieter, oft mit Affiliate-Interesse; Velotrade-Blog ist Werbung des Anbieters.

HyroTrader (offiziell):
- [Startseite mit Preisen](https://www.hyrotrader.com/), [Trading Rules](https://www.hyrotrader.com/trading-rules/), [Terms and Conditions](https://www.hyrotrader.com/terms-and-conditions/)
- FAQ: [Bot oder KI-Agent](https://www.hyrotrader.com/faq/getting-started/can-i-use-a-trading-bot-or-an-ai-agent/), [Bots in Challenge und Funded](https://www.hyrotrader.com/faq/hyrotrader-account/can-i-use-trading-bots-or-signal-bots-during-the-challenge-or-on-a-funded-account/), [Verbindung mit Claude](https://www.hyrotrader.com/faq/hyro-platform/how-can-i-connect-my-hyrotrader-challenge-to-claude/), [Prop-Firm für Trading-Agenten](https://www.hyrotrader.com/faq/hyro-platform/is-hyrotrader-a-prop-firm-for-trading-agents/), [Bybit-API einrichten](https://www.hyrotrader.com/faq/bybit-platform/how-to-correctly-set-up-bybit-api-and-why-am-i-getting-an-error-when-connecting-the-api/), [Wohin gehen Orders](https://www.hyrotrader.com/faq/platform/where-do-my-orders-actually-go/), [Plattformen](https://www.hyrotrader.com/faq/getting-started/which-platforms-can-i-use-for-trading/), [Tokenisierte Aktien](https://www.hyrotrader.com/faq/bybit-platform/can-i-trade-tokenized-stocks-metals-or-oil-on-hyrotrader/), [Risikoregeln](https://www.hyrotrader.com/faq/rules/what-are-the-risk-management-conditions-at-hyrotrader/), [Tagesverlust](https://www.hyrotrader.com/faq/rules/how-is-the-5-daily-drawdown-calculated/), [Art des Tagesverlusts](https://www.hyrotrader.com/faq/rules/what-is-the-difference-between-standard-trailing-and-swing-fixed-daily-drawdown/), [Verbotene Handlungen](https://www.hyrotrader.com/faq/trading-restrictions/what-are-prohibited-trading-actions/), [News](https://www.hyrotrader.com/faq/trading-restrictions/is-news-trading-allowed/), [Copy-Trading](https://www.hyrotrader.com/faq/trading-restrictions/is-copy-trading-allowed/), [Über Nacht](https://www.hyrotrader.com/faq/rules/do-i-have-to-close-my-positions-overnight/), [Länder](https://www.hyrotrader.com/faq/platform/which-countries-are-allowed-to-join-hyrotrader-can-i-join-from-the-usuk/), [Gewinnanteil](https://www.hyrotrader.com/faq/hyrotrader-account/how-much-is-the-profit-split/), [Auszahlung](https://www.hyrotrader.com/faq/hyrotrader-account/how-can-i-withdraw-my-profits/), [Kaution](https://www.hyrotrader.com/faq/getting-started/what-is-the-refundable-challenge-deposit/), [KYC bei Bybit](https://www.hyrotrader.com/faq/bybit-platform/do-i-need-to-complete-kyc-on-bybit-when-starting-the-verification-process-with-hyrotrader/)

Weitere Anbieter:
- [Velotrade: Startseite](https://velotrade.com/), [Velotrade-Blog: Algo and bot trading](https://velotrade.com/blog/algo-bot-trading-crypto-prop-firm) (Werbung des Anbieters)
- [Kraken: Best crypto prop firms 2026](https://www.kraken.com/learn/best-crypto-prop-firms) (Werbung von Kraken), [Business Wire: Kraken completes acquisition of Breakout](https://www.businesswire.com/news/home/20250904012956/en), [Yahoo Finance: Kraken Prop](https://finance.yahoo.com/markets/crypto/articles/kraken-prop-inside-funded-trader-183521927.html)
- [Bitfunded: Startseite](https://www.bitfunded.com/)

Ratgeber (Drittanbieter):
- [ProptradingVibes: HyroTrader prohibited strategies](https://proptradingvibes.com/blog/hyrotrader-prohibited-strategies), [FundedTrading: HyroTrader](https://fundedtrading.com/de/propfirm/hyrotrader/)
- [TheTrustedProp: Bitfunded](https://thetrustedprop.com/prop-firms/bitfunded)
- [Lunefi: Crypto Fund Trader Rules](https://lunefi.com/blog/crypto-fund-trader-rules), [Velotrade-Vergleich CFT vs. E8](https://velotrade.com/prop-firms/compare/crypto-fund-trader-vs-e8-markets)
- [AirdropAlert: Breakout Review](https://airdropalert.com/blogs/breakout-prop-firm-review/), [ProptradingVibes: Breakout Max Drawdown](https://proptradingvibes.com/blog/breakout-max-drawdown)
