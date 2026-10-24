---
typ: wissen
erstellt: 2026-10-23
aktualisiert: 2026-10-24
quelle: Recherche
tags:
  - trading
  - wissen
  - funded
---

# Prop-Firms für Futures

Futures-Prop-Firms sind der größte und am stärksten automatisierungsfreundliche Teil des Marktes, aber nicht bei allen Anbietern und nicht in jeder Kontostufe. Hier stehen Plattformen, Bot-Regeln (Prüfung und Funded/Live getrennt), Preise, Regeln, Auszahlung und Deutschland, dazu die Übertragung des ORB-Setups auf Micro-Futures. Teil von [[Funded Accounts]], baut auf [[Prop-Firms und Bot-Architektur]] auf.

> [!warning] Stand und Grenzen
> Abgerufen am 2026-10-23/24. Die Seiten von Apex, Take Profit Trader (AGB), Lucid (Startseite) und Tradeify (Help Center direkt) blockierten den Abruf (HTTP 403); was dort steht, kommt aus Suchergebnissen oder Ratgebern und ist so gekennzeichnet. Preise ändern sich fast monatlich durch Aktionen. Keine Kaufempfehlung, keine Anlage- oder Rechtsberatung.

## Kurz gesagt

- **Nur zwei Anbieter erlauben einen eigenen Bot laut eigener Hilfeseite ausdrücklich:** Topstep (über die TopstepX-API, nur in Combine und Express Funded) und Lucid Trading. My Funded Futures erlaubt „automated trading strategies tailored to their own specific settings“. Tradeify erlaubt eigene Bots mit Eigentumsnachweis per Video.
- **Verboten oder praktisch verboten:** Alpha Futures (laut Drittquellen, die die Regel wörtlich zitieren), Apex (laut Drittquellen), Take Profit Trader (laut Drittquellen).
- **Topstep verbietet VPS, VPN und entfernte Server für Orders.** Eine Claude-Code-Cloud-Sitzung ist ein entfernter Server. Der heutige Aufbau des Autopiloten wäre dort **nicht regelkonform**.
- **Deutschland bei Topstep:** Combine und Express Funded ja, **kein Live Funded Account**, Auszahlungen insgesamt bis $200.000.
- **ORB passt technisch gut auf MES/MNQ:** 1 MES = $5 je Indexpunkt, 1 MNQ = $2 je Punkt. Das Risiko lässt sich in kleinen Schritten dosieren.

## Begriffe

- **Evaluation / Combine / Test:** die gekaufte Prüfung auf einem simulierten Konto.
- **Funded (Sim-Funded, XFA, PA):** nach bestandener Prüfung; meist weiterhin **simuliert**, Auszahlungen sind vertragliche Prämien.
- **Live:** echtes Konto bei einem Futures-Broker (FCM), Kapital der Firma. Dort gelten oft andere Regeln, auch für Bots.
- **EOD-Trailing-Drawdown:** Die Verlustgrenze rückt nur nach dem Tagesschluss nach oben, gemessen am höchsten Schlusssaldo. **Intraday-Trailing** zieht schon bei offenen Gewinnen mit und ist strenger.

## Bot-Regeln im Vergleich

| Firma | Evaluation | Funded (simuliert) | Live | Cloud/VPS | Quelle |
| --- | --- | --- | --- | --- | --- |
| **Topstep** | erlaubt | erlaubt (XFA) | **nicht möglich**: API nur für Simulation | **verboten** (VPS, VPN, entfernte Server für Orders) | offiziell |
| **Lucid Trading** | erlaubt | erlaubt | nicht eigens geregelt | nicht erwähnt | offiziell (Hilfeseite); älterer LucidDirect-Vertrag (Mai 2025) verlangt vorherige schriftliche Erlaubnis |
| **My Funded Futures** | erlaubt | erlaubt | erlaubt, „must abide by CME guidelines“ | nicht erwähnt | offiziell |
| **Tradeify** | erlaubt, eigener Bot | erlaubt | nicht geprüft | Live-Video „enabling the code on your own PC“ kann verlangt werden | offiziell (über Suche/Intercom-Spiegel) |
| **Apex Trader Funding** | laut Drittquellen uneinheitlich | laut Drittquellen **verboten** | verboten | – | Drittquellen, offizielle Seite gesperrt |
| **Take Profit Trader** | laut Drittquellen verboten | laut Drittquellen verboten | – | – | Drittquellen, AGB gesperrt |
| **Alpha Futures** | **verboten** | **verboten** | – | VPS nur für die Plattform, nicht für Bots (Drittquelle) | Drittquellen zitieren: „The use of AI, bots, and other automated trading mechanisms is strictly prohibited across all account types.“ |

> [!note] Überall gleich
> HFT, Ausnutzen simulierter Fills, Hedging über mehrere Konten und Microscalping sind bei allen Anbietern verboten. Für Fehler des eigenen Codes haftet immer der Trader („Traders are fully responsible for any software errors“, Lucid; „no exceptions are made for errant trades or malfunctions“, Topstep).

## Topstep

**Plattform und API:** Eigene Plattform **TopstepX** (betrieben von ProjectX Trading LLC). Die **TopstepX-API** (ProjectX Gateway) kostet $29 im Monat, mit Code „topstep“ $14,50, abgerechnet als „Sim2Funded Solutions“. Ein Schlüssel gilt für alle berechtigten Konten.

Offizielle Regeln zur API (Help Center):
- „Live funded accounts cannot trade through the ProjectX API“, das Gateway ist für die Simulation gebaut.
- VPS, VPN und entfernte Server sind laut Nutzungsbedingungen für das Handeln verboten. Ein privater Server ist nur für Arbeiten ohne Orders erlaubt (Daten, Backtests, Protokoll, Nur-Lese-Dashboard); er darf keine Orders platzieren, ändern, stornieren oder weiterleiten.
- Kein Sandbox-Konto; zum Testen ein Practice-Konto. Kein technischer Support für eigenen Code.
- HFT verboten, ebenso „scalping algorithms designed to exploit unrealistic SIM fills“ und volles Positionslimit direkt in große News.

Technik (offizielle API-Doku): REST unter `https://api.topstepx.com`, Echtzeit über SignalR/WebSocket (`rtc.topstepx.com/hubs/user` und `/hubs/market`). Anmeldung mit Benutzername und API-Schlüssel, Token 24 Stunden gültig. Ordertypen Limit, Market, Stop, TrailingStop; Stop-Loss und Take-Profit als Bracket in Ticks, wenn im Konto „Auto OCO Brackets“ eingestellt ist. Grenzen: 50 Anfragen je 30 Sekunden für historische Bars, 200 je 60 Sekunden für alles andere. Details: [[Schnittstellen für Bots]].

**Trading Combine** (Produktseite und Help Center):

| Konto | Preis/Monat | Gewinnziel | Max Loss Limit (EOD-trailing) | Daily Loss Limit | Max. Kontrakte |
| --- | --- | --- | --- | --- | --- |
| 50K | $49 (oder $85, je nach Option) | $3.000 | $2.000 | $1.000 | 5 Mini / 50 Micro |
| 100K | $99 (oder $129) | $6.000 | $3.000 | $2.000 | 10 / 100 |
| 150K | $199 | $9.000 | $4.500 | $3.000 | 15 / 150 |

- Nach Bestehen einmalig $149 Aktivierung für das Express Funded Account (XFA), außer im Pfad „No Activation Fee“.
- Konsistenz in der Combine: bester Tag unter 55 % des Gewinnziels (Help Center; ältere Ratgeber nennen 50 %). Wird sie verfehlt, steigt das Ziel, das Konto ist nicht verloren.
- Handelstag 17:00 CT bis 15:10 CT (= 16:10 New York); bis dahin flat.

**Express Funded Account:** Max Loss Limit wie oben, nachziehend vom höchsten Tagesschlusssaldo. Auszahlung „Standard“: fünf Gewinntage von je mindestens $150, dann bis 50 % des Saldos, höchstens $5.000; „Consistency“-Variante: drei Handelstage und 40 %-Regel, höchstens $6.000. Gewinnanteil 90/10. Bis 5 XFAs gleichzeitig.

**Deutschland:** Laut Help Center gehört Deutschland zu „Countries Eligible for an XFA — Not LFA“: Combine und XFA ja, Auszahlungen bis insgesamt $200.000, **kein Live Funded Account**; manche könnten stattdessen für einen „Pro Account“ in Frage kommen.

## Lucid Trading

- **Bot:** Hilfeseite „Other Trading Activities“: „Automated trading systems and trade copiers are permitted“, müssen alle Regeln einhalten, Trader haftet für Fehler. Verboten: HFT, Microscalping, Hedging. Der LucidDirect-Vertrag vom 19.05.2025 verlangt dagegen eine vorherige schriftliche Erlaubnis für Automatisierungssoftware: **Widerspruch, vor dem Kauf klären.**
- **News:** Im Plan LucidDaily ist Handel zu „red folder news“ ein harter Verstoß; Flex, Pro und Direct erlauben News.
- **Handelszeit:** Positionen bis 16:45 New York schließen, sonst automatisches Glattstellen. LucidLive: bis 16:45 (Tradovate) bzw. 16:15 (Rithmic).
- **Plattformen:** offiziell bestätigt nur Tradovate und Rithmic für LucidLive.
- **LucidFlex 50K (Ratgeber, nicht offiziell geprüft):** etwa $140–149 einmalig, $2.000 EOD-trailing, kein Daily Loss Limit, 50 %-Konsistenz nur in der Prüfung, 90/10.
- **Deutschland:** laut Ratgeber „most of Europe“ unterstützt, nicht offiziell bestätigt.

## My Funded Futures (MFFU)

- **Bot (offiziell):** „Traders may make use of automated trading strategies tailored to their own specific settings“, solange sie nicht die günstigen Fills der Simulation ausnutzen. „High-frequency Trading is not allowed“. Live: „must abide by CME guidelines“. Kein Gerät darf mit einem anderen Trader geteilt werden. Copy-Trading zwischen eigenen Konten erlaubt.
- **News (offiziell):** Bei Tier-1-Daten (FOMC, Protokoll, Arbeitsmarktbericht, CPI) muss alles **2 Minuten vorher** flach sein, auch Limit-Orders; frühestens 2 Minuten danach wieder rein (Beispiel 8:30 → 8:28 bis 8:32). Gilt für Rapid und Pro Sim Funded; Evaluations und Builder dürfen. Termine: [[Makro-Termine]].
- **Builder 50K (offiziell):** $153 Listenpreis (Aktionen bis $92), keine Aktivierungsgebühr, Ziel $3.000, $2.000 EOD-trailing (Variante $1.500), Daily Loss Limit $1.000 als Pause, keine Konsistenz in der Prüfung, 4 Mini / 40 Micro. Auszahlung 80/20, bester Tag ≤ 50 % je Zyklus, mindestens $500, höchstens $2.000 je Zyklus, nach 5 Sim-Auszahlungen Wechsel ins Live-Konto.
- **Plattform, Deutschland:** nicht geprüft.

## Tradeify

- **Bot (offizielle Richtlinie, über Intercom-Spiegel gelesen):** „Personal bots are allowed as long as they are not high-frequency trading (HFT) bots.“ Nachweis: „You must be able to prove that you are the sole owner of the bot or strategy“, und „We will also require a live video of you enabling the code on your own PC.“ Derselbe Bot bei mehreren Firmen ist gegen die Richtlinie.
- **Microscalping (nur Funded):** mehr als die Hälfte der Trades und des Gewinns muss aus Trades über 10 Sekunden kommen; sonst keine Auszahlung (kein Kontoverlust).
- **News:** keine Regel.
- **Plattformen:** Tradovate, WealthCharts, Rithmic/Tradesea (Startseite).
- **Preise und Regeln:** Die Startseite zeigte Platzhalter („Lorem ipsum“) und für alle Größen denselben Preis ($251 statt $359); Pläne Growth, Select, Lightning. **Nicht verlässlich, vor Kauf prüfen.** Gewinnanteil laut Startseite 90 %.

## Apex Trader Funding

Offizielle Seiten nicht abrufbar (HTTP 403). Nach Drittquellen (Stand Aug.–Okt. 2026):
- „Apex prohibits automation and algorithms“ laut aktueller Liste verbotener Aktivitäten; halbautomatisch (ATM-Strategien, Alarme mit Aufsicht) wird meist als zulässig beschrieben. Quellen widersprechen sich.
- Wahl zwischen EOD- und Intraday-Trailing; 50K: Ziel $3.000, $2.000 Drawdown, EOD-Daily-Loss $1.000; einmalige Gebühr (50K etwa $249 intraday bzw. $490 EOD laut einer Quelle); 30 Tage Zeit; bis zu sechs Auszahlungen je Konto, bester Tag ≤ 50 %.
- Plattformen laut Ratgebern Rithmic, Tradovate, WealthCharts (nicht bestätigt).

## Take Profit Trader

- Startseite (offiziell): PRO 80/20, PRO+ 90/10 (live, EOD-Drawdown), Auszahlung ab Tag 1, einmalig $130 für PRO, gescheiterter Test kostet „at MOST, $360“, bis 5 Funded-Konten. Plattformen u. a. NinjaTrader, TradingView, Tradovate, R|Trader, Quantower, MotiveWave, Routing über Rithmic und Tradovate.
- **Bot:** laut Drittquellen in PRO verboten; die AGB sprechen laut Suche von „discretionary traders, not automated trading robots“ (nicht selbst gelesen, 403). Copier und Automatisierung von Dritten auf eigenes Risiko.

## Alpha Futures

- **Bot:** laut zwei Drittquellen, die die Regelseite wörtlich zitieren, in **allen Kontoarten verboten**, auch „API-based trading without manual per-trade confirmation“. Erlaubt: Indikator mit Signalen, wenn der Mensch jede Order selbst setzt. Über 100 Trades am Tag unerwünscht.
- Pläne Standard, Advanced, Zero mit EOD-Trailing; Preise laut Ratgebern $79–139 für 50K (widersprüchlich). Plattformwechsel im Juli 2026 auf AlphaTrader, WealthCharts, Quantower, Deepcharts laut einer Quelle, nicht bestätigt.

## ORB auf Micro-Futures

**Kontraktwerte** (CME, über Ratgeber bestätigt; CME-Seite selbst nicht erreichbar):

| Kontrakt | Basis | $ je Indexpunkt | Tick | $ je Tick |
| --- | --- | --- | --- | --- |
| MES (Micro E-mini S&P 500) | S&P 500 | $5 | 0,25 | $1,25 |
| MNQ (Micro E-mini Nasdaq-100) | Nasdaq-100 | $2 | 0,25 | $0,50 |
| ES / NQ (E-mini) | gleich | $50 / $20 | 0,25 | $12,50 / $5,00 |

Der S&P 500 stand Anfang Oktober 2026 bei etwa 7.700–7.800 Punkten. Ein MES bewegt damit rund $39.000 Index-Gegenwert, obwohl nur eine kleine Margin hinterlegt ist.

**Übertragung der Regeln:**

| Bot heute (Aktien) | Futures-Version |
| --- | --- |
| Scanner über Tausende Aktien | entfällt: ein bis zwei feste Kontrakte (MES, MNQ) |
| 15-Min-Range ab 9:30 NY, Einstieg nach 5-Min-Schluss darüber | gleich, auf der regulären Sitzung (Futures handeln fast rund um die Uhr, die Range bezieht sich trotzdem auf 9:30–9:45) |
| Stop Range-Mitte, Ziel 2R | gleich, auf Ticks (0,25) gerundet; bei TopstepX als Bracket in Ticks |
| flat 15:55 NY | passt: Topstep 16:10, Lucid 16:45 |
| Einstiege bis 15:30 | gleich; plus News-Sperren (MFFU 2 Min. um Tier-1-Daten) |
| Yahoo-Kurse | Kurse aus der Plattform (Market Hub), nicht Yahoo |
| nur long | bleibt; Short wäre bei Futures leicht möglich, aber ein neues Setup ohne Journal |
| — | **neu:** Kontraktwechsel (Rollover) im März, Juni, September, Dezember |

**Beispiel: Risiko je Kontrakt** (Annahmen, keine Messung: Range und Kurse schwanken stark)

| | MES | MNQ |
| --- | --- | --- |
| angenommene 15-Min-Range | 12 Punkte | 60 Punkte |
| Stop an der Range-Mitte | 6 Punkte = **$30** | 30 Punkte = **$60** |
| plus je 1 Tick Slippage rein und raus | +$2,50 → $32,50 | +$1 → $61 |
| Stop am Range-Tief | 12 Punkte = $60 | 60 Punkte = $120 |
| Ziel 2R (Stop Mitte) | +12 Punkte = $60 | +60 Punkte = $120 |

Gebühren je Kontrakt sind nicht eingerechnet (bei den Anbietern nicht geprüft).

**Rechnung für ein Topstep-50K-Konto:** Max Loss $2.000, Daily Loss $1.000. Wer je Trade z. B. 10 % des Max Loss riskiert ($200), handelt bei 6 Punkten Stop **6 MES** (6 × $32,50 = $195). Das bisherige Bot-Limit von $1.000 je Trade wäre hier die Hälfte des gesamten Kontopuffers; acht Trades am Tag passen nicht unter ein Tageslimit von $1.000, wenn jeder $200 riskiert. Die Limits in `trader/config.json` gelten für das Paper-Konto und werden nicht ohne Yannicks Auftrag geändert; ein eigener Satz Limits für ein Prop-Konto wäre eine neue Entscheidung. Siehe [[Positionsgröße]], [[Tageslimits und Regelwerk]], [[Drawdown und Risk of Ruin]].

## Regulierung (kurz)

- Futures sind in den USA von der **CFTC** beaufsichtigt; Broker (FCM) und Vermittler müssen bei der **NFA** registriert sein. Wer ein echtes Live-Konto bekommt, handelt über einen solchen Broker.
- Prüfungen und Sim-Funded-Konten sind **Simulationen**. Ein eigener Rechtsrahmen für Retail-Prop-Firms ist in den USA nach den gefundenen Quellen **nicht erlassen**. Die Frage, ob Prüfungsgebühren als Anteil an einem Commodity Pool gelten, gilt als offen.
- Präzedenzfall: Die CFTC verklagte 2023 die Mutter von My Forex Funds; das Gericht sanktionierte später die CFTC wegen ihres Vorgehens (laut Sekundärquellen über $3 Mio.). Berichte über eine CFTC-Konsultation zu Prop-Firms ab 01.08.2026 und eine freiwillige Registrierung von Topstep und Apex: **nicht bestätigt**.
- Registrierung einer Firma lässt sich in NFA BASIC (nfa.futures.org) nachsehen. Für Deutschland: [[Recht Steuern und Risiken]], [[Steuern in Deutschland]].

## Für diesen Bot

- **Topstep wäre der einzige Anbieter mit offizieller API, aber nicht aus der Cloud.** Die Regel „VPS, VPNs, and remote servers“ verboten schließt Orders aus einer Claude-Code-Cloud-Sitzung aus. Regelkonform wäre nur: Order-Teil läuft auf Yannicks eigenem Rechner; Cloud nur für Analyse, Journal und Backtests (laut Topstep erlaubt, solange sie keine Orders platziert oder weiterleitet). Vor dem Kauf schriftlich bei Topstep bestätigen lassen. Siehe [[Bot an Prop-Firm anbinden]].
- **Tradeify** verlangt ggf. ein Video vom Start des Codes „on your own PC“: ebenfalls lokal gedacht. **Lucid** und **MFFU** erwähnen Server nicht; nachfragen.
- **Mit Deutschland als Wohnsitz** endet Topstep beim simulierten XFA; echtes Kapital gibt es dort nicht, nur Prämien bis $200.000.
- **Umbau nötig:** neue Broker-Anbindung (ProjectX statt Alpaca), Kurse aus der Plattform, Kontraktwechsel, Tick-Rundung, und `/trader-risk` müsste Max Loss (EOD-trailing), Daily Loss, Konsistenz, News-Sperren und Flat-Zeit des Anbieters hart prüfen.
- **Neues Setup heißt neuer Nachweis.** Das Journal hat 5 Aktien-Trades; für MES/MNQ gibt es keine. Erst Backtest und Paper-Phase mit genau diesen Regeln, siehe [[Backtesting und Overfitting]] und [[Wie viele Day Trader gewinnen]]. Topstep bietet dafür ein Practice-Konto.
- **Repo-Regel bleibt:** Keine Order mit echtem Geld ohne Yannicks ausdrückliches Ja. Ein vollautonomer Bot auf einem bezahlten Konto ist eine eigene Entscheidung von Yannick, nicht Teil dieser Recherche. Siehe [[Trading/Regeln]].

## Quellen

Abgerufen am 2026-10-23 und 2026-10-24.

Offizielle Seiten:
- [Topstep Help: TopstepX API Access](https://help.topstep.com/en/articles/11187768-topstepx-api-access)
- [Topstep Help: Trading Combine Parameters](https://help.topstep.com/en/articles/8284197-trading-combine-parameters)
- [Topstep Help: Prohibited Trading Strategies](https://help.topstep.com/en/articles/10305426-prohibited-trading-strategies-at-topstep)
- [Topstep Help: Am I eligible to trade with Topstep?](https://help.topstep.com/en/articles/8284116-am-i-eligible-to-trade-with-topstep)
- [Topstep: Express Funded Account Rules](https://www.topstep.com/express-funded-account-rules)
- [Topstep: Topstep Prop (Preise)](https://www.topstep.com/topstep-prop)
- [ProjectX Gateway API: Connection URLs](https://gateway.docs.projectx.com/docs/getting-started/connection-urls/), [Rate Limits](https://gateway.docs.projectx.com/docs/getting-started/rate-limits/), [Authenticate](https://gateway.docs.projectx.com/docs/getting-started/authenticate/authenticate-api-key/), [Place an Order](https://gateway.docs.projectx.com/docs/api-reference/order/order-place/), [Retrieve Bars](https://gateway.docs.projectx.com/docs/api-reference/market-data/retrieve-bars/)
- [Lucid Support: Other Trading Activities](https://support.lucidtrading.com/en/articles/11404728-other-trading-activities)
- [Lucid Support: Allowed Trading Times](https://support.lucidtrading.com/en/articles/11404729-allowed-trading-times)
- [Lucid: LucidDirect Account Agreement (19.05.2025, PDF)](https://lucidtrading.com/wp-content/uploads/2025/05/LucidDirect-Account-Agreement-5-19.pdf) (nur über Suche gesehen)
- [MFFU Help: Fair Play and Prohibited Trading Practices](https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices)
- [MFFU Help: News Trading Policy](https://help.myfundedfutures.com/en/articles/8230009-news-trading-policy)
- [MFFU Help: Builder Plan 50k](https://help.myfundedfutures.com/en/articles/14290805-builder-plan-50k-a-comprehensive-guide)
- [Tradeify Help: Guidelines for Traders](https://intercom.help/tradeify/en/articles/10468318-guidelines-for-traders) und [Tradeify: Startseite](https://tradeify.co/)
- [Take Profit Trader: Startseite](https://takeprofittrader.com/) ([AGB](https://takeprofittrader.com/terms) nicht abrufbar)
- [CME: Micro E-mini S&P 500 Contract Specs](https://www.cmegroup.com/markets/equities/sp/micro-e-mini-sandp-500.contractSpecs.html) (beim Abruf nicht erreichbar), [CME Fact Card Micro E-mini Options](https://www.cmegroup.com/markets/equities/files/micro-e-mini-sandp-and-nasdaq-100-options-fact-card.pdf)

Ratgeber und Affiliate-Seiten (nur ergänzend, viele verkaufen Automatisierung oder erhalten Provision):
- [ProptradingVibes: Apex Trader Funding Rules Overview](https://proptradingvibes.com/blog/apex-trader-funding-rules-overview)
- [TradersPost: Apex Trader Funding Guide](https://blog.traderspost.io/article/apex-trader-funding-review) (Automatisierungsanbieter)
- [PickMyTrade: Apex Funded Automation Rules 2026](https://blog.pickmytrade.trade/apex-funded-automation-rules-2026/) (Automatisierungsanbieter)
- [Propvator: Alpha Futures Automated Trading](https://propvator.com/blog/alpha-futures-automated-trading/)
- [PickMyTrade: Alpha Futures FAQ](https://pickmytrade.trade/prop-firm-faq/alpha-futures-faq/)
- [TradersPost: Alpha Futures Pricing](https://blog.traderspost.io/article/alpha-ticks-pricing-evaluation-guide)
- [FundedTrading: Alpha Futures](https://fundedtrading.com/propfirm/alpha-futures/) (Affiliate)
- [TradersPost: Take Profit Trader](https://blog.traderspost.io/article/automate-take-profit-trader-with-traderspost)
- [ProptradingVibes: LucidFlex](https://proptradingvibes.com/blog/lucid-trading-lucidflex-account)
- [ProptradingVibes: Lucid Restricted Countries](https://proptradingvibes.com/blog/lucid-trading-restricted-countries)
- [NinjaTrader: What are MES futures?](https://ninjatrader.com/Futures/Blogs/What-are-Micro-E-mini-S-P-500-Futures-MES)
- [Tapeboard: Stock Market Today, 2.10.2026](https://tapeboard.com/blog/market-pulse-2026-10-02)
- [NexusFi: Prop Firm Regulatory Status](https://nexusfi.com/a/prop-firms/prop-firm-regulatory-status) (Forum)
- [track360: Prop Firm Regulation Roundup Q3 2026](https://www.track360.io/blog/prop-firm-regulation-news-roundup-q3-2026)
- [DayTradingToolkit: Prop Firm Regulation](https://daytradingtoolkit.com/market-insights/prop-firm-regulation-funded-traders-guide)
