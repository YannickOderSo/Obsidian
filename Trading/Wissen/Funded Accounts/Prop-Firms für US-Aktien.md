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

# Prop-Firms für US-Aktien

Welche Prop-Firms 2026 überhaupt US-Aktien anbieten (echte Aktien in einer Simulation oder Aktien-CFDs), was sie kosten, welche Regeln gelten und ob ein eigener Bot dort laufen darf. Teil von [[Funded Accounts]], baut auf [[Prop-Firms und Bot-Architektur]] auf.

> [!warning] Stand und Grenzen
> Regeln und Preise ändern sich oft, teils monatlich. Alles hier ist am 2026-10-23/24 abgerufen, offizielle Seiten zuerst. Was nur auf Ratgeber- oder Affiliate-Seiten stand, ist so gekennzeichnet. Keine Kaufempfehlung, keine Anlage- oder Rechtsberatung.

## Kurz gesagt

- **Nur wenige Firmen handeln echte US-Aktien.** Die bekannteste ist **Trade The Pool** (Schwestermarke von The5ers). Die großen CFD-Firmen (FTMO, FundedNext, SabioTrade) bieten Aktien nur als **CFD** und oft nur eine kleine Auswahl großer Werte.
- **Kein Anbieter nutzt Alpaca.** Der Autopilot (`paper_auto.py`, REST an Alpaca) lässt sich nirgends direkt anschließen. Es bräuchte eine neue Schnittstelle: MetaTrader 5, die Plattform des Anbieters oder einen Webhook-Dienst.
- **Vollautomatik ist bei Aktien die Ausnahme.** Trade The Pool erlaubt sie nur als Beta über SignalStack und mit Vorbehalt, SabioTrade nur mit schriftlicher Erlaubnis, FundedNext nur unter $50.000 Kontogröße. FTMO und The5ers erlauben eigene EAs auf MetaTrader, dort gibt es aber nur Aktien-CFDs (bei FTMO wenige, bei The5ers unklar).
- **Kein Anbieter erlaubt ausdrücklich einen Bot aus einer Cloud-Sitzung.** Das muss vor jedem Kauf schriftlich geklärt werden, siehe [[Bot an Prop-Firm anbinden]].

## Überblick

| Firma | Was wird gehandelt | Plattform | Eigener Bot erlaubt? | Deutschland |
| --- | --- | --- | --- | --- |
| Trade The Pool | echte US-Aktien und ETFs (simuliert) | TraderEvolution (Desktop Windows, Web, Mobil) | **unklar/widersprüchlich**: AGB verbieten eigene algorithmische Software, Programmbedingungen nennen Automatisierung über SignalStack als „Beta“ mit Genehmigungsvorbehalt | nicht ausgeschlossen (nicht auf der Liste der verbotenen Länder), nicht ausdrücklich bestätigt |
| FTMO | Aktien-CFDs (Auswahl, Liste auf der Symbolseite) neben Forex, Indizes usw. | MT4, MT5, cTrader, DXtrade | **ja**, EAs und algorithmisches Handeln erlaubt, mit Grenzen (Serverlast, keine verbotenen Praktiken) | ja (Sitz Prag); Länderliste nicht eigens geprüft |
| FundedNext | 20 Aktien-CFDs (14 US, 6 EU), Hebel 1:2 | MT4, MT5, cTrader, Match-Trader | **nur unter $50.000** und nur auf MT4/MT5, gegen Zusatzgebühr; ab $50.000 nur manuell | nicht geprüft |
| The5ers | eigenes Programm: Forex, Metalle, Indizes; Aktien laut Startseite über die Schwester Trade The Pool. Die Seite „Asset Specifications“ hat einen Reiter „Stocks“, Inhalt nicht lesbar | MT5 (laut Drittquellen) | **ja**, EAs mit eigenem Quellcode; verboten u. a. fremde EAs mit gleichen Trades, HFT, zu viele Serveranfragen | nicht geprüft |
| SabioTrade | CFDs auf Aktien, ETFs, Forex u. a. („250+ Werte“), Aktien-Hebel bis 1:20 | eigene Plattform auf Basis von QuadCode, kein MT4/MT5 | **nein ohne schriftliche Erlaubnis** („Bots, copiers, or API trading without written permission“ verboten); EAs nur für Signale | Seite leitete auf die US-Version um, EU-Bedingungen nicht geprüft |
| PropShop Trader | ca. 100 US-Aktien und Futures | nur Tickblaze | laut Ratgeber erlaubt, **nicht bestätigt** | nicht geprüft |
| Zimtra | echter Direktzugang zu US-Börsen mit **eigener Einlage**, kein Challenge-Modell | nicht geprüft | nicht bestätigt | laut Werbung für internationale Trader; Sitz Kaimaninseln |

## Trade The Pool

Die einzige größere Firma, die nur Aktien und ETFs anbietet. Gehört zur The5ers-Gruppe.

**Programme und Preise** (Programmseite, Preise in USD, je Kontogröße zwei Preise ohne klare Beschriftung, vermutlich regulär und reduziert):

| Programm | Kontogröße (Kaufkraft intraday) | Preis |
| --- | --- | --- |
| Day (MAX oder FLEX) | $5.000 / $25.000 / $50.000 / $100.000 / $200.000 | $59/$47 · $120/$97 · $285/$230 · $545/$435 · $1.475/$1.100 |
| Swing | $2.000 / $10.000 / $20.000 / $40.000 | $87/$69 · $420/$297 · $670/$447 · $1.240/$800 |
| Edge | $50.000 / $100.000 | einmalig $156 / $266 |

Über Nacht sinkt die Kaufkraft der Day-Konten stark (z. B. $100.000 → $16.000).

**Regeln** (Programmbedingungen und FAQ):

| Regel | Wert |
| --- | --- |
| Gewinnziel | Day 6 %, Swing 15 % (netto nach simulierten Gebühren) |
| Tagesverlust („Daily Pause“) | Day 2 % oder 1 %, Swing 3 %; gerissen heißt: alle Positionen werden geschlossen, Pause bis zum nächsten Handelstag (kein Kontoverlust) |
| Maximalverlust | Day 4 % oder 3 %, Swing 7 %; statisch. Bei Gewinn von 3 × Tageslimit rückt die Grenze auf den Startsaldo |
| Konsistenz | beste Position höchstens 30 % des Gewinns (MAX in der Prüfung), 50 % bei FLEX |
| Mindestzahl | MAX Day 20 Positionen, FLEX Day 10, Swing 5 |
| Zeitlimit | MAX Day 60 Tage, FLEX unbegrenzt; 14 Tage ohne Handel beenden MAX/FLEX |
| Mindestbewegung | jede Position braucht mindestens **10 Cent** Unterschied zwischen Ein- und Ausstieg |
| Mindesthaltezeit | 30 Sekunden (MAX/FLEX), sonst 60 Sekunden |
| Volumen | Order höchstens 5 % des Volumens der letzten 1-Minuten-Kerze; Aktie muss am Tag über 200.000 Stück gehandelt haben |
| Schluss | Day-Konten werden ab **10 Minuten vor Börsenschluss** (15:50 NY) automatisch glattgestellt |
| Earnings, Dividenden | keine Haltepositionen über Nacht bei Earnings; vor dem Ex-Tag schließen |
| News | keine Sperre, nur Warnung vor breiten Spreads |
| Gebühren | simuliert 0,5 Cent je Aktie, mindestens $0,75 je Order |

**Auszahlung:** MAX und FLEX 70 % für den Trader, Edge 80 %. Frühestens 14 Tage nach Start oder letzter Auszahlung, mindestens $300 Gewinn; FLEX braucht zusätzlich drei Tage mit je 0,5 % Gewinn. Überweisung, Krypto, Guthaben, Karte.

**Bot und Schnittstelle:**

> [!danger] Widerspruch in den eigenen Bedingungen
> - **AGB, Abschnitt 11.1:** „The User may not use any custom, algorithmic, or other automated trading software“.
> - **Programmbedingungen:** „Support for automated trading, including the specific integration with SignalStack, is currently in a beta state.“ Ziel höchstens **2 Anfragen pro Minute**, die Firma behält sich die Genehmigung jedes Algorithmus vor und kann die Erlaubnis jederzeit entziehen.
> - **FAQ:** externe Kopier-Software ist „strictly prohibited“.
>
> Laut Programmbedingungen gehen bei Widerspruch die Nutzungsbedingungen (AGB) vor. Ohne schriftliche Genehmigung ist ein eigener Bot hier also **nicht erlaubt**.

Eine offene API für eigenen Code gibt es nicht. Der vorgesehene Weg ist SignalStack: Ein Dienst, der Webhooks (z. B. von TradingView-Alarmen) in Orders umsetzt. Laut Pressemitteilung vom August 2025 zwei Monate gratis, danach kostenpflichtig (Preisangaben widersprüchlich).

## FTMO

Großer CFD-Anbieter aus Prag. Aktien sind dabei („Stocks“ steht in der FAQ zu Instrumenten), die Liste steht auf der Symbolseite, die sich nicht auslesen ließ. Hebel und Handelszeiten für Aktien-CFDs: **nicht bestätigt**, im Terminal prüfen.

| Punkt | 2-Step | 1-Step |
| --- | --- | --- |
| Gewinnziel | 10 % (Phase 1), 5 % (Phase 2) | 10 % |
| Tagesverlust | 5 % | 3 % |
| Maximalverlust | 10 % statisch | 10 %, nachziehend am Tagesende |
| Konsistenz | keine | bester Tag ≤ 50 % des Gesamtgewinns (Bestellungen ab 12.10.2026) |
| Mindesthandelstage | 4 | keine |
| News | in Challenge/Verification frei; im FTMO-Konto keine Orders 2 Min. vor und nach ausgewählten Terminen (außer Swing) | gleich |

Preise: siehe [[Prop-Firms und Bot-Architektur]] (100k 2-Step etwa €540).

**Bot:** Die FAQ sagt: „we have no reason for limiting or restricting your trading strategy“, solange sie auf echten Konten nachbildbar ist und keine verbotene Praxis ist. Grenzen: 200 offene Orders, 2.000 Positionen am Tag; fremde EAs können zur Ablehnung führen (gleiche Trades bei anderen Kunden). Technisch heißt das: ein EA in MetaTrader 5 oder das Python-Paket für MT5, das ein laufendes MT5-Terminal unter Windows braucht. Details: [[Schnittstellen für Bots]].

## FundedNext

- **Aktien:** 20 CFDs (14 US, darunter AAPL, NVDA, TSLA, META, AMZN, GOOGL, MSFT und SPCX), Hebel 1:2, Kommission 0,004 % je Lot. Gilt für alle Challenge- und FundedNext-Konten, nicht für Labs, Free Trial, Competition.
- **Regeln:** Tagesverlust, Maximalverlust und Konsistenz gelten für Aktien genauso wie für alles andere.
- **Bot (Help Center, wörtlich):** EAs und Bots auf MT4/MT5 nur „for accounts below $50,000“, gegen eine nicht erstattbare Zusatzgebühr. „Traders on account sizes of $50,000 and above must trade manually“, auch Werkzeuge, die nur Stop, Ziel oder Stückzahl ändern, zählen als EA. Auf cTrader und Match-Trader nie. Jede Strategie höchstens $300.000 Kapital, keine EAs mit Telegram- oder WhatsApp-Anbindung, keine Bots „designed specifically to pass Prop firm challenges“.

## The5ers

- Eigenes Programm für Forex, Metalle und Indizes; Aktien verweist die Startseite an **Trade The Pool**. Ob einzelne Aktien-CFDs im eigenen MT5 liegen, war nicht lesbar (**nicht bestätigt**).
- **Verboten** (FAQ „Prohibited Trading Practices“): EAs, bei denen andere Trader dieselben Trades offen haben; EAs ohne eigenen Quellcode; Bots mit übermäßig vielen Serveranfragen; HFT und Tick-Scalping; Pending Orders um wichtige News („Bracketing“); viele gleichzeitige Trades. Folge: dauerhafte Sperre, keine Erstattung.
- Ein selbst geschriebener EA mit eigenem Quellcode wäre damit grundsätzlich möglich.

## SabioTrade

- Einmalgebühr (US-Seite): $20.000 für $139, $50.000 für $339, $100.000 für $549, $200.000 für $1.079, $1 Mio. für $6.889.
- Regeln: Ziel 10 %, Tagesverlust 5 % (vom Vortagesschluss), Maximalverlust 6 % nachziehend ab dem Höchststand (offene Verluste zählen), Konsistenz: ein Tag höchstens 55 % des Gewinnziels, sonst steigt das Ziel. Kein Zeitlimit, 30 Tage ohne Trade können das Konto beenden.
- Gewinnanteil 80–90 %, Auszahlung alle 7 Tage.
- **Bot:** EAs nur „to detect signals and entry/exit points only“. „Bots, copiers, or API trading without written permission“ sind verboten.
- Die Seite leitete beim Abruf auf `sabiotrade.us` um. Für Kunden in der EU können Bedingungen abweichen.

## Weitere Anbieter (nur Drittquellen)

- **PropShop Trader:** Aktien- und Futures-Konten auf Tickblaze; Ratgeber nennen Algorithmen und Kopierer als erlaubt, Aktienkonten mit $25.000 und $50.000. Nicht auf der Firmenseite geprüft.
- **The Trading Pit, Finotive Funding, TakeCap:** werden in Affiliate-Listen als „Stocks“-Firmen geführt; Art (CFD oder echt) und Bot-Regeln nicht geprüft.
- **Zimtra:** kein Prüfungsmodell, sondern ein Prop-Konto mit eigener Einlage und echtem Börsenzugang (4–20 Uhr NY). API und Einlagehöhe nicht bestätigt. Das ist eher ein Broker-Modell mit Hebel als ein „Funded Account“.

## Passt das ORB-Setup?

| Bot-Regel ([[Opening Range Breakout]]) | Trade The Pool (Day) | Aktien-CFDs (FTMO, FundedNext) |
| --- | --- | --- |
| US-Aktien, long, intraday | passt | passt nur bei den wenigen Werten im Angebot; Scanner findet oft kleinere Aktien, die es als CFD nicht gibt |
| flat um 15:55 NY | **zu spät**: Zwangsglattstellung ab 15:50 → Bot muss bis ~15:45 flat sein | CFD-Handelszeiten nicht bestätigt |
| max. $2.500 Verlust am Tag (Paper $100.000) | **zu hoch**: Daily Pause 2 % = $2.000 beim $100k-Konto, Maximalverlust 4 % = $4.000 | FTMO 1-Step 3 % = $3.000, 2-Step 5 %; Gesamtgrenze 10 % |
| max. $1.000 je Trade | zu hoch: TTP empfiehlt 30 % des Tageslimits = $600 | vier volle Verlusttrades = 4 % → bei 1-Step über dem Tageslimit |
| bis 8 Trades/Tag | erlaubt, aber 10-Cent-Regel: Kleingewinne/-verluste unter 10 Cent zählen nicht als gültige Position | erlaubt |
| Bracket (Stop + Ziel) | TraderEvolution hat Stop-Orders; Automatik nur über SignalStack | MT5 kann Stop und Ziel je Order |
| Ziel 2R | kollidiert evtl. mit Konsistenz (ein großer Gewinner > 30 % des Gewinns) | FTMO 1-Step: bester Tag ≤ 50 % |

Fazit: Das Setup passt fachlich am besten zu **Trade The Pool**, technisch aber am schlechtesten, weil eigener Code dort nicht freigegeben ist. Bei den CFD-Firmen ist der Bot technisch möglich (MT5), aber die Auswahl an Aktien ist sehr klein und der Scanner müsste auf diese Liste beschränkt werden.

## Für diesen Bot

- **Kein Weg ohne Umbau.** Alle Anbieter brauchen eine andere Schnittstelle als Alpaca. Der Autopilot müsste eine zweite Broker-Anbindung bekommen, und `/trader-risk` müsste die Regeln des Anbieters (Daily Pause, 10-Cent-Regel, Flat-Zeit 15:45, Konsistenz) hart prüfen. Siehe [[Bot an Prop-Firm anbinden]].
- **Cloud ist ein Problem.** MT5 läuft als Windows-Programm, nicht in einer Claude-Code-Cloud-Sitzung, die nach etwa zwei Stunden neu startet. Ob ein Anbieter Orders von einem Cloud-Server akzeptiert, ist bei keinem der Aktien-Anbieter ausdrücklich geregelt (bei Topstep im Futures-Bereich ausdrücklich verboten, siehe [[Prop-Firms für Futures]]). Vor dem Kauf schriftlich fragen.
- **Repo-Regel bleibt:** Mit echtem Geld, und eine bezahlte Challenge ist echtes Geld, keine Order ohne Yannicks ausdrückliches Ja. Ein vollautonomer Bot auf einem gekauften Konto widerspricht der heutigen Regel in `CLAUDE.md`; das wäre eine eigene Entscheidung von Yannick.
- **Limits wären enger.** Für ein $100k-Konto bei Trade The Pool hieße das z. B. höchstens $600 Risiko je Trade und $2.000 am Tag statt $1.000 und $2.500. Vorher im Paper-Konto mit diesen Limits testen, siehe [[Tageslimits und Regelwerk]].
- **Erst Nachweis, dann Kauf:** fünf Trades reichen nicht; siehe [[Wie viele Day Trader gewinnen]] und [[Backtesting und Overfitting]].
- Kein Anbieter hier unterliegt der [[Pattern Day Trader Regel]], weil alles simuliert ist. Steuern: [[Steuern in Deutschland]], [[Recht Steuern und Risiken]].

## Quellen

Abgerufen am 2026-10-23 und 2026-10-24.

Offizielle Seiten:
- [Trade The Pool: Startseite](https://tradethepool.com/)
- [Trade The Pool: Program Terms](https://tradethepool.com/program-terms/)
- [Trade The Pool: The Program (FAQ, Preise)](https://tradethepool.com/the-program/)
- [Trade The Pool: Terms and Conditions](https://tradethepool.com/terms-and-conditions/)
- [FTMO: Trading Objectives](https://ftmo.com/en/trading-objectives/)
- [FTMO: Which instruments can I trade and what strategies am I allowed to use?](https://ftmo.com/en/faq/which-instruments-can-i-trade-and-what-strategies-am-i-allowed-to-use/)
- [FTMO: Can I trade news?](https://ftmo.com/en/faq/can-i-trade-news/)
- [FTMO: Symbols](https://ftmo.com/en/symbols/) (Inhalt nicht auslesbar)
- [FundedNext Help: Can I trade stocks with FundedNext?](https://help.fundednext.com/en/articles/16859574-can-i-trade-stocks-with-fundednext)
- [FundedNext Help: Does FundedNext allow EAs/Indicators?](https://help.fundednext.com/en/articles/8020763-does-fundednext-allow-eas-indicators)
- [The5ers: Startseite](https://the5ers.com/), [Asset Specifications](https://the5ers.com/asset-specifications/), [Prohibited Trading Practices](https://the5ers.com/faqs/prohibited-trading-practices/)
- [SabioTrade (US-Seite): Startseite](https://sabiotrade.us/), [Trading Rules](https://sabiotrade.us/trading-rules)
- [SignalStack Help: TradingView Alerts](https://help.signalstack.com/kb/signal-source-integrations/tradingview-alerts-f07455cf99ed63bd)

Ratgeber und Affiliate-Seiten (nur ergänzend, teils mit Provision oder eigenem Bot-Angebot):
- [FundedTrading: Best Stocks Prop Firm](https://fundedtrading.com/best-stocks-prop-firm/) (Affiliate)
- [PropFirmMap: Stocks Prop Firms](https://propfirmmap.com/best/stocks-prop-firms)
- [FXEmpire: Trade The Pool](https://fxempire.com/prop-firms/tradethepool)
- [TradersPost: Trade The Pool](https://traderspost.io/connections/trade-the-pool) (Anbieter von Automatisierung)
- [Propvator: The5ers Instruments](https://propvator.com/blog/the5ers-instruments/)
- [FundedTrading: SabioTrade](https://fundedtrading.com/propfirm/sabiotrade/) (Affiliate)
- [FundedTrading: PropShop Trader](https://fundedtrading.com/propfirm/propshop-trader/) (Affiliate)
- [Trustpilot: Zimtra](https://at.trustpilot.com/review/zimtra.com)
