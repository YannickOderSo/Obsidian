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

# Prop-Firms für CFD und Forex

Die bekannten „Funded Account“-Anbieter für Forex und CFDs im Vergleich: Plattformen, was sie bei Bots erlauben, Preise, Verlustregeln, Auszahlung, Deutschland und ob es CFDs auf US-Aktien gibt. Baut auf [[Prop-Firms und Bot-Architektur]] auf, Hub: [[Funded Accounts]].

> [!warning] Stand 2026-10-23, keine Empfehlung
> Regeln und Preise ändern sich bei diesen Anbietern fast monatlich (FTMO hat z. B. am 12.10.2026 die Best-Day-Regel ersetzt, Blueberry am 08.10.2026 die Bot-Regeln). Vor jedem Kauf die verlinkte Seite des Anbieters lesen. Alle Konten sind **simuliert** (Demo-Geld); bezahlt wird eine Gebühr für die Prüfung, ausgezahlt ein Anteil am simulierten Gewinn. Keine Anlage-, Rechts- oder Steuerberatung, kein Affiliate-Link.

## Kurzüberblick

| Anbieter | Plattformen | Eigener Bot erlaubt? | US-Aktien-CFDs | Deutschland |
| --- | --- | --- | --- | --- |
| **FTMO** | MT4, MT5, cTrader, TradingView | **ja**, „algorithmic trading or EAs“ ausdrücklich erlaubt | Kategorie „Stocks“ vorhanden, Liste und Zeiten öffentlich nicht bestätigt | ja (nicht auf der Sperrliste) |
| **The5ers** (High Stakes) | MT5 (Hedge) | **ja, mit Auflagen**: eigener Quellcode, keine Fremd-EAs | **nein** im High-Stakes-Programm (FX, Metalle, Indizes, Öl, Krypto) | ja (nicht auf der Sperrliste) |
| **FundedNext** (Stellar) | MT4, MT5, cTrader, Match-Trader | **nur unter $50.000**, nur MT4/MT5, nur mit kostenpflichtigem EA-Add-on | **ja**: 14 US- und 6 EU-Aktien, Hebel 1:2 | ja (nicht auf der Sperrliste) |
| **FXIFY** | MT5, DXtrade, TradingView (laut Startseite) | laut Startseite „EAs Allowed“; Ratgeber: vorher Freigabe nötig (nicht bestätigt) | laut Startseite „Stocks“, Hebel 2:1 | ja; USA gesperrt |
| **E8 Markets** | laut Ratgebern MT4, MT5, cTrader, Match-Trader, TradeLocker | laut Ratgebern ja (offizielle Seite für uns nicht abrufbar) | nicht bestätigt | nicht bestätigt |
| **FundingPips** | laut Ratgebern MT5, cTrader, Match-Trader | laut Ratgebern nur **selbst geschriebene** EAs mit Nachweis | nicht bestätigt | nicht bestätigt |
| **Blueberry Funded** | MT5, TradeLocker | **ja, nur eigener Code und nur nach schriftlicher Zustimmung** des Supports | **nein** (keine Aktien in der Hebeltabelle) | ja; USA und Australien gesperrt |

„Nicht bestätigt“ heißt: Die Seite des Anbieters war aus der Recherche-Umgebung nicht abrufbar (Cloudflare-Sperre bei E8, FundingPips, Teilen von FXIFY), und es gibt nur Ratgeber-Angaben, die sich teils widersprechen.

## Hintergrund: MetaQuotes und die Prop-Firms (2024)

Im Februar 2024 verloren mehrere Prop-Firms und die Broker dahinter den Zugang zu MetaTrader. Auslöser war, dass sie **US-Kunden** bedienten; laut einer nicht offiziell bestätigten Mail von MetaQuotes braucht MT5 für US-Kunden eine Regulierung durch FINRA oder NFA. True Forex Funds stellte den Betrieb vorübergehend ein, Eightcap beendete das Prop-Geschäft, BlackBull musste sich von FundingPips trennen. Viele Anbieter wichen auf **DXtrade, Match-Trader, TradeLocker und cTrader** aus oder sperrten US-Kunden. Die Spuren sieht man bis heute:

- The5ers schreibt in den AGB: MetaQuotes-Plattformen „are strictly prohibited from being used by residents of the United States“.
- FundedNext lässt US-Kunden nur über Match-Trader handeln und verwarnt, wer sich mit US-IP-Adresse an einem MetaQuotes-Server anmeldet.
- FTMO bedient US-Kunden über die verbundene Firma `ftmo.oanda.com` (FTMO hat 2025 die Übernahme von OANDA bekanntgegeben).

Für Yannick in Deutschland ändert das wenig: MT5 ist verfügbar. Es erklärt aber, warum die Plattformwahl bei Prop-Firms politisch ist und sich kurzfristig ändern kann. Ratgeber-Zahlen wie „80 Firmen geschlossen“ sind nicht belegt.

## Je Anbieter

### FTMO

| Punkt | Stand laut ftmo.com |
| --- | --- |
| Modelle | 2-Step (Challenge + Verification) und 1-Step |
| Preise 2-Step | 10k €89 · 25k €250 · 50k €345 · 100k €540 (Aktion €439) · 200k €1.080, einmalig, mit der ersten Auszahlung erstattet |
| Preise 1-Step | 10k €79 · 25k €199 · 50k €319 · 100k €499 (Aktion €399) · 200k €999; die Seite führt daneben eine „non-refundable“-Gebühr, ob die 1-Step-Gebühr erstattet wird: nicht bestätigt |
| Ziel | 2-Step: 10 % dann 5 %; 1-Step: 10 % |
| Tagesverlust | 2-Step 5 %, 1-Step 3 % vom Startkapital; Basis ist der **Kontostand um 00:00 CE(S)T**, geprüft wird gegen die **Equity** (inkl. offener Verluste, Swaps, Gebühren) |
| Maximalverlust | 2-Step 10 % **statisch**; 1-Step 10 % **nachziehend am Tagesende** (steigt mit dem höchsten Tagesschluss, fällt nie) |
| Mindesttage | 2-Step 4 Handelstage; 1-Step keine |
| Consistency | nur 1-Step: bester Tag ≤ 50 % des Gesamtgewinns (Bestellungen ab 12.10.2026); Überschreiten ist kein Verstoß, man muss weiter handeln |
| News | Standard-FTMO-Account: keine Orderausführung 2 Min. vor bis 2 Min. nach u. a. Zinsentscheid Fed, NFP, CPI, BIP; **gilt nicht in der Challenge**, nicht für Swing-Konten |
| Wochenende | Standard-Account: keine Positionen über Marktpausen > 2 Std. (also kein Wochenende); Swing-Konto ohne Einschränkung |
| Auszahlung | 2-Step 80 %, mit Skalierung bis 90 %; 1-Step 90 %. Antrag ab dem 14. Tag nach dem ersten Trade, Bearbeitung 1–2 Werktage |
| Deutschland | erlaubt (nicht in der Länder-Sperrliste) |

**Bots:** In der FAQ steht wörtlich, man dürfe handeln „whether it's discretionary trading, algorithmic trading or EAs“. Bedingungen: Die Strategie muss im echten Markt reproduzierbar sein; Server-Grenzen 200 offene Orders und 2.000 Positionen pro Tag; die Seite zu verbotenen Praktiken nennt mehr als 2.000 Server-Anfragen pro Tag als „Hyperaktivität“. Verboten sind u. a. das Ausnutzen von Preis- oder Feed-Fehlern, „software, artificial intelligence, ultra-high-speed tools, or mass data entry that might manipulate“, gleichzeitige Gegenpositionen über mehrere Konten, Gap-Trading vor großen News und Fremdzugriff auf das Konto. Bei **gekauften EAs** warnt FTMO, dass andere dieselben Trades machen und man an der Kapitalobergrenze scheitern kann.

**US-Aktien:** „Stocks“ ist als Instrumentklasse genannt, die Liste auf der Symbolseite lädt aber erst im Browser. Welche US-Werte und zu welchen Zeiten: **nicht bestätigt**, im Terminal unter „Spezifikation“ prüfen. Üblich bei Aktien-CFDs ist die reguläre Börsenzeit 15:30–22:00 MEZ.

### The5ers

| Punkt | Stand laut the5ers.com (High Stakes, 2-Step) |
| --- | --- |
| Preise | 2.5k $19 · 5k $35 · 10k $69 · 25k $176 · 50k $249 · 100k $405 (Seite zeigt diese als neue Preise, alte z. B. 100k $455) |
| Ziel | Schritt 1: 10 % (früher 8 %), Schritt 2: 5 % |
| Tagesverlust | 5 % vom **höheren Wert** aus Equity und Kontostand zu Tagesbeginn, Stichtag MT5-Serverzeit |
| Maximalverlust | 10 % (Art der Berechnung auf der Seite nicht genannt) |
| Mindesttage | 3 profitable Tage (je ≥ 0,5 % des Startkapitals) |
| News | keine Order 2 Min. vor bis 2 Min. nach High-Impact-News; Gewinne daraus werden abgezogen |
| Wochenende | erlaubt |
| Auszahlung | 80 % (mit Skalierung bis 100 %), erste nach 14 Tagen, dann alle 2 Wochen, ab $150 Gewinn; Wege laut Seite Krypto oder Rise |
| Plattform | MT5 Hedge, Hebel 1:100 |
| Deutschland | erlaubt (nicht unter „Forbidden Territory“) |

**Bots:** EAs sind grundsätzlich erlaubt. Die AGB („Trading Rules“) verbieten u. a.: Arbitrage, HFT „in which the majority of trades duration span is measured within a few seconds or less“, Bracketing um News, Copy-Trading mit anderen, „Expert advisors from a third party where other traders have the same trades open“, „Using an expert advisors from a provider where the trader does not own the source code“, Tick-Scalping, Hedge- und Reverse-Arbitrage sowie Software oder **KI**, die manipuliert oder einen „unfair advantage“ verschafft.

**US-Aktien:** Im High-Stakes-Programm nicht. The5ers verweist für US-Aktien auf die Schwesterfirma Trade The Pool, siehe [[Prop-Firms für US-Aktien]].

### FundedNext

| Punkt | Stand laut help.fundednext.com (Stellar 2-Step) |
| --- | --- |
| Preise | 6k $59,99 · 15k $119,99 · 25k $199,99 · 50k $299,99 · 100k $549,99 · 200k $999,99 |
| Ziel | 8 % dann 5 % |
| Tagesverlust | 5 % vom **Startkapital**, offene Verluste, Swaps und Gebühren zählen; Tagesgewinne erhöhen den Spielraum am selben Tag; Neustart 00:00 Serverzeit (GMT+2, Sommer GMT+3) |
| Maximalverlust | 10 %, Kontostand oder Equity nie unter 90 % des Startkapitals (statisch) |
| Mindesttage | 5 je Phase |
| Sonderregeln | „Quick Strike“: Gewinnanteil aus Trades unter 30 Sek. muss unter 30 % bleiben; dieselbe Strategie in Prüfung und Funded-Konto (kein Wechsel Bot ↔ manuell) |
| News | in der Prüfung frei; im Funded-Konto zählen Gewinne aus Trades 5 Min. vor bis 5 Min. nach High-Impact-News nur zu 40 % |
| Wochenende | erlaubt |
| Auszahlung | 80 % (Add-on 95 %), erster Zyklus 21 Tage, mit Add-on alle 14 Tage |
| Deutschland | erlaubt (nicht auf der Sperrliste) |

**Bots (wichtig):** Laut Help Center sind EAs und Bots **nur auf MT4/MT5, nur bei Kontogrößen unter $50.000 und nur mit dem kostenpflichtigen EA-Add-on** erlaubt. Ab $50.000 muss man „fully manually“ handeln, auch Tools, die nur Stop, Ziel oder Lotgröße setzen, gelten als EA. Auf cTrader und Match-Trader ist Automatisierung ganz verboten. Weitere Auflagen: jede Strategie höchstens $300.000 Kapital, keine identischen Trades über Konten, keine EAs mit Telegram- oder WhatsApp-Anbindung, keine „Pass-your-challenge“-EAs (mit namentlicher Verbotsliste). Verboten außerdem HFT, Latenz-Arbitrage, Tick-Scalping, Grid, Hyperaktivität und Copy-Trading zwischen Personen oder mit Cloud-Kopierern.

**US-Aktien:** Seit 2026 gibt es **20 Aktien-CFDs** (14 US, 6 EU), auf allen Plattformen und Modellen, Hebel **1:2**, Kommission 0,004 % je Lot, dreifacher Swap freitags. Handelszeiten sind im Artikel nicht genannt (**nicht bestätigt**); als Spot-CFDs vermutlich nur zur regulären US-Börsenzeit.

### FXIFY

Die Seiten von FXIFY waren nur teilweise abrufbar. Laut Startseite (Abruf 2026-10-24): Programme mit One, Two und Three Phase, statischer oder nachziehender Drawdown, bis $400.000; Plattformen MT5, DXtrade und TradingView; „EAs Allowed“ sowie „Martingale & Grid Allowed“; „Trade Stocks“ mit Aktien-Hebel 2:1; Gewinnanteil bis 90 % (Futures bis 100 %); keine Konten für **Einwohner der USA**. Preis für 100k: auf der Startseite nicht genannt.

Ratgeber (PropFirmMap, Myfxbook, FundedTrading) widersprechen sich: teils „EAs voll erlaubt“, teils „nur nach schriftlicher Freigabe durch den Support“, auf DXtrade keine EAs, in Lightning- und Instant-Konten keine Bots. Verbotslisten nennen HFT, Latenz-Arbitrage, Gruppen-Hedging, Order-Spamming. **Nicht bestätigt**, vor einem Kauf schriftlich beim Support klären. FXIFY Futures (eigene Firma, eigenes Help Center) verbietet EAs laut Ratgeber derzeit ganz.

### E8 Markets

Offizielle Seiten für uns gesperrt, Angaben nur aus Ratgebern (Stand Mitte 2026): Plattformen MT4, MT5, cTrader, Match-Trader, TradeLocker; EAs und Bots erlaubt, solange nicht viele Nutzer dieselbe Strategie fahren; Latenz-Arbitrage verboten; Warnung, wenn mehr als 50 % der Trades unter einer Minute gehalten werden; im Funded-Konto keine High-Impact-News und eine 40-%-Best-Day-Regel. Drawdown je Produkt verschieden (E8 One intraday nachziehend, E8 Signature am Tagesende nachziehend, E8Pro V2 statisch, seit Juni 2026). 100k-Preis und Länderliste: **nicht bestätigt**.

### FundingPips

Offizielles Help Center für uns gesperrt, Angaben aus Ratgebern: 2-Step Standard 8 % / 5 %, Tagesverlust 5 %, Maximalverlust 10 %, 100k um $520–530; 2-Step Pro 3 % Tag / 6 % gesamt. Gewinnanteil je nach Auszahlungsrhythmus 60–100 %. **Bots:** nur **selbst geschriebene** EAs mit Nachweis (Quellcode, Versionsverlauf); gekaufte EAs nur als Trade- oder Risikomanager. FundingPips war 2024 vom Bruch BlackBull/MetaQuotes betroffen. US-Aktien und Deutschland: **nicht bestätigt**.

### Blueberry Funded

| Punkt | Stand laut help.blueberryfunded.com (Prime 2-Step) |
| --- | --- |
| Ziel | 8 % dann 6 % |
| Tagesverlust | 4 % vom Startkapital als fester Betrag; Startpunkt ist der höhere Wert aus Kontostand und Equity zu Tagesbeginn |
| Maximalverlust | 10 % statisch |
| Mindesttage | 3 aktive Tage je Auszahlungszyklus (Käufe ab 17.08.2026) |
| Consistency | keine bei Prime; andere Modelle: im Funded-Konto max. 1,5 % Verlust je Trade-Idee |
| News | kein Öffnen oder Schließen 2 Min. vor bis 2 Min. nach High-Impact-News, auch in der Prüfung, auch per Take-Profit |
| Wochenende | erlaubt (außer Flex 1-Step) |
| Auszahlung | 80 %, alle 14 Tage |
| Plattformen | MT5 und TradeLocker; DXtrade, Match-Trader, cTrader nicht |
| Länder | gesperrt u. a. **USA** und Australien; Deutschland erlaubt |
| Preise | auf der Startseite ohne JavaScript nicht lesbar: **nicht bestätigt** |

**Bots:** Seit Oktober 2026 auf allen Produkten erlaubt, aber nur, wenn der EA (1) selbst gebaut ist, (2) die eigene Strategie fährt und (3) **vor dem ersten Trade beim Support offengelegt und genehmigt** wurde. Gekaufte, gemietete und **in Auftrag gegebene** EAs sind verboten. Verboten außerdem HFT, Tick-Scalping, Latenz-, Reverse- und Hedge-Arbitrage, Emulatoren, Signal-Kopieren. Copy-Trading nur zwischen eigenen Konten. Keine Aktien-CFDs.

## Was das Regelwerk gemeinsam hat

- **Equity zählt:** Überall wird der Tagesverlust gegen Kontostand plus offene Verluste gerechnet. Ein Stop beim Broker ist Pflicht, sonst reißt ein Kurssprung das Limit, bevor der Bot reagiert.
- **Tagesgrenze nach Serverzeit:** FTMO 00:00 MEZ/MESZ, MT5-Firmen meist 00:00 GMT+2/+3. Für US-Aktien (15:30–22:00 MEZ) fällt jede Sitzung in einen Tag.
- **Immer verboten:** HFT, Latenz- und andere Arbitrage, Tick-Scalping, Ausnutzen von Feed-Fehlern, Copy-Trading mit fremden Konten, Kontoverwaltung durch Dritte, Gegenpositionen über Konten.
- **Fremd-EAs sind das Problem, nicht Bots an sich:** Fast alle verbieten oder deckeln gekaufte EAs, weil viele Kunden dieselben Trades machen. Eigener Code mit Nachweis ist die sichere Seite.
- **„KI“ in den AGB:** FTMO und The5ers verbieten Software „or artificial intelligence“, die manipuliert oder einen unfairen Vorteil verschafft. Ein LLM, das eine eigene Strategie ausführt, ist damit nicht ausdrücklich verboten, aber auch nicht ausdrücklich erlaubt. Vor dem Kauf schriftlich bestätigen lassen.

## Für diesen Bot

> [!important] Passt nur mit Umbau
> Der Bot handelt US-Aktien long per Opening Range Breakout über die REST-API von Alpaca ([[Opening Range Breakout]], [[Ordertypen]]). Keine der CFD-Firmen bietet eine solche REST-API; angebunden wird über MT5 (MQL5-EA oder das Python-Paket für ein laufendes Windows-Terminal) oder cTrader. Details: [[Schnittstellen für Bots]] und [[Bot an Prop-Firm anbinden]].

- **Kaum US-Aktien:** Nur FundedNext hat bestätigt CFDs auf 14 US-Werte, mit Hebel 1:2 (auf $25.000 Konto also höchstens ~$50.000 Positionswert). FTMO und FXIFY nennen Aktien, Liste und Zeiten offen. Ein Scanner über Tausende US-Aktien wie bei `/trader-scanner` lässt sich dort nicht 1:1 handeln, nur die Handvoll vorhandener Symbole.
- **Bot-Regeln trennen die Anbieter:** FundedNext erlaubt Bots nur unter $50.000 mit Add-on. Blueberry verlangt vorherige Zustimmung und eigenen Code. FTMO und The5ers erlauben eigene EAs ohne Vorab-Freigabe. Der Code hier ist selbst geschrieben und im Git nachweisbar, das hilft bei Nachweispflichten.
- **Laufzeit:** Claude-Cloud-Sitzungen enden nach etwa 2 Stunden und sind kein Dauerprozess. Ein MT5-EA müsste auf einem eigenen Windows-Server (VPS) laufen, der Bot würde dann Signale liefern statt selbst Orders zu senden. Das ist ein anderer Aufbau als heute.
- **Limits passen:** $1.000 Risiko je Trade und $2.500 am Tag auf $100.000 liegen unter FTMO 2-Step (5 % = $5.000) und 1-Step (3 % = $3.000) und unter The5ers und FundedNext (5 %). Bei Blueberry Prime (4 % = $4.000) ebenfalls. Acht Trades am Tag sind weit unter jeder Hyperaktivitätsgrenze.
- **News:** CPI und Arbeitsmarktbericht kommen um 8:30 NY, also vor dem ersten Einstieg um 9:45. FOMC um 14:00 NY fällt in die Handelszeit; bei FTMO (Funded-Konto), The5ers und Blueberry wäre dann ein 2-Minuten-Fenster zu sperren, auch für Stops und Ziele. Termine: [[Makro-Termine]].
- **Glattstellen 15:55 NY** passt zu FTMOs Verbot, über Marktpausen zu halten.
- **Erst Nachweis, dann Kauf:** Mit 5 geschlossenen Paper-Trades ist kein Vorteil belegt ([[Wie viele Day Trader gewinnen]], [[Backtesting und Overfitting]]). Ablauf und Kosten: [[Kauf und Ablauf einer Challenge]]; Recht und Steuern: [[Recht Steuern und Risiken]], [[Steuern in Deutschland]]. Für echte US-Aktien sind [[Prop-Firms für US-Aktien]] die näherliegende Wahl, für rund um die Uhr [[Prop-Firms für Krypto]], für Index-Futures [[Prop-Firms für Futures]].
- Mit echtem Geld gilt weiter [[Trading/Regeln]]: keine Order ohne ausdrückliches Ja.

## Quellen

Abruf 2026-10-23/24. Offizielle Seiten zuerst; „Ratgeber“ sind Drittanbieter, oft mit Affiliate-Interesse.

Offiziell:
- FTMO: [Trading Objectives](https://ftmo.com/en/trading-objectives/), [Preise (Startseite)](https://ftmo.com/en/), [Instrumente und Strategien](https://ftmo.com/en/faq/which-instruments-can-i-trade-and-what-strategies-am-i-allowed-to-use/), [Forbidden Trading Practices](https://ftmo.com/en/forbidden-trading-practices/), [Plattformen](https://ftmo.com/en/faq/which-platforms-can-i-use-for-trading/), [News](https://ftmo.com/en/faq/can-i-trade-news/), [Overnight/Wochenende](https://ftmo.com/en/faq/can-i-hold-positions-overnight-or-over-the-weekend/), [Auszahlung](https://ftmo.com/en/faq/how-do-i-withdraw-my-profits/), [Wer darf teilnehmen](https://ftmo.com/en/faq/who-can-join-ftmo/), [Handelszeiten (FTMO/OANDA)](https://ftmo.oanda.com/faq/what-are-the-trading-hours-and-where-can-i-check-them/)
- The5ers: [High Stakes](https://the5ers.com/high-stakes/), [Terms and Conditions](https://the5ers.com/terms-and-conditions/)
- FundedNext: [Stellar 2-Step](https://help.fundednext.com/en/articles/17255124-stellar-2-step-challenge), [Is EA allowed](https://help.fundednext.com/en/articles/8020763-is-ea-allowed-in-fundednext), [Prohibited Strategies](https://help.fundednext.com/en/articles/8020351-what-are-the-restricted-prohibited-trading-strategies), [Strategie-Wechsel](https://help.fundednext.com/en/articles/8388896-are-there-any-restrictions-on-my-trading-strategy), [HFT](https://help.fundednext.com/en/articles/11982271-does-fundednext-allow-hft-high-frequency-trading), [Copy Trading](https://help.fundednext.com/en/articles/8019805-what-is-the-copy-trading-rule-at-fundednext), [Plattformen](https://help.fundednext.com/en/articles/8019808-which-platforms-can-i-use-for-trading-at-fundednext), [Länder](https://help.fundednext.com/en/articles/8020080-are-any-countries-restricted-on-fundednext-cfds), [Aktien](https://help.fundednext.com/en/articles/16859574-can-i-trade-stocks-with-fundednext), [Tagesverlust](https://help.fundednext.com/en/articles/8019811-how-can-i-calculate-the-daily-loss-limit), [Serverzeit](https://help.fundednext.com/en/articles/8019672-what-is-fundednext-s-server-time), [News](https://help.fundednext.com/en/articles/10701447-is-news-trading-allowed-at-fundednext), [Wochenende](https://help.fundednext.com/en/articles/11982358-does-fundednext-allow-holding-trades-over-the-night-weekend)
- FXIFY: [Startseite](https://fxify.com/), [FAQ](https://fxify.com/faqs/all-faqs/) (nur Vorschau lesbar)
- Blueberry Funded: [Bots und EAs](https://help.blueberryfunded.com/en/articles/9550892-do-you-allow-bots-and-ea-expert-advisor-trading), [Verbotene Strategien](https://help.blueberryfunded.com/en/articles/9714626-prohibited-strategies-after-march-12-2026), [Copy Trading](https://help.blueberryfunded.com/en/articles/9550602-am-i-allowed-to-copy-trade), [Länder](https://help.blueberryfunded.com/en/articles/9550574-are-any-countries-restricted-from-purchasing-an-evaluation), [Prime](https://help.blueberryfunded.com/en/articles/12136509-what-is-the-prime-challenge), [Prime Drawdown](https://help.blueberryfunded.com/en/articles/12136586-what-are-the-drawdown-limits-on-a-prime-account), [Prime Auszahlung](https://help.blueberryfunded.com/en/articles/12136624-prime-reward-structure), [News](https://help.blueberryfunded.com/en/articles/9715375-do-you-allow-news-trading), [Wochenende](https://help.blueberryfunded.com/en/articles/9550589-can-i-hold-positions-over-the-weekend-and-overnight), [Plattformen](https://help.blueberryfunded.com/en/articles/10741972-platform-downloads), [Hebel](https://help.blueberryfunded.com/en/articles/9550888-what-leverage-does-blueberry-funded-offer), [1,5-%-Regel](https://help.blueberryfunded.com/en/articles/14072474-1-5-risk-per-trade-idea-rule)

Presse zu MetaQuotes 2024:
- [Finance Magnates: True Forex Funds stalls operations](https://www.financemagnates.com/forex/after-the-my-forex-funds-fiasco-true-forex-funds-stalls-operations/)
- [Finance Magnates: Prop firms cutting US clients, new platforms](https://financemagnates.com/forex/prop-trading-firms-renaissance-cutting-us-clients-integrating-new-trading-platforms)
- [FinanceFeeds: BlackBull und Funding Pips](https://financefeeds.com/blackbull-denies-losing-metaquotes-license-after-funding-pips-closure/)

Ratgeber (Drittanbieter, teils Affiliate):
- [TradeTanto: FTMO Rules 2026](https://tradetanto.com/learn/ftmo-rules-evaluation-process), [PropFirmMap: FTMO Review 2026](https://propfirmmap.com/blog/ftmo-review-2026-trustpilot-rating-safety-grade-challenge-prices)
- [FundedTrading: Prop firms for EA trading](https://fundedtrading.com/prop-firms-for-expert-advisors-ea-trading/), [FundedTrading: E8 Markets Review](https://fundedtrading.com/prop-trading-firm/e8-markets-review), [FundedTrading: True Forex Funds shutdown](https://fundedtrading.com/de/true-forex-funds-shutdown/)
- [PropFirmMap: FXIFY Review 2026](https://propfirmmap.com/blog/fxify-review-2026-a-plus-safety-grade-trustpilot-challenge-prices), [Myfxbook: FXIFY](https://www.myfxbook.com/de/prop-firms/fxify)
- [PropFirmMap: E8 Markets](https://propfirmmap.com/firms/e8-markets), [ProptradingVibes: E8 Drawdown](https://proptradingvibes.com/blog/e8-markets-drawdown-rules)
- [PickMyTrade: FundingPips Review](https://blog.pickmytrade.io/fundingpips-review-rules-payouts-automation/), [ProptradingVibes: FundingPips-Regeln 2026](https://proptradingvibes.com/de/blog/fundingpips-rules), [NYC Servers: FundingPips Review](https://newyorkcityservers.com/blog/fundingpips-review)
