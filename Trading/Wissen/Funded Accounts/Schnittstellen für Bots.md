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

# Schnittstellen für Bots

Über welche Programmierschnittstellen sich Prop-Firm-Konten automatisiert handeln lassen, wie sie technisch funktionieren und wo die Firma den Zugang sperrt. Grundlage für [[Bot an Prop-Firm anbinden]]; Überblick im Hub [[Funded Accounts]], Einordnung in [[Prop-Firms und Bot-Architektur]].

> [!warning] Die Schnittstelle ist nicht die Erlaubnis
> Dass eine Plattform eine API hat, heißt nicht, dass die Prop-Firm sie für ihre Konten freischaltet oder vollautomatisches Handeln erlaubt. Das regeln die Bedingungen jeder einzelnen Firma, oft getrennt nach Prüfung, Funded- und Live-Konto. Vor einem Kauf die aktuellen Regeln lesen und die Nutzung schriftlich bestätigen lassen. Stand aller Angaben: Abruf 2026-10-23.

## Überblick

| Schnittstelle | Märkte | Protokoll | Anmeldung | Bracket/OCO serverseitig | Python | Dauerlaufender Prozess nötig? |
| --- | --- | --- | --- | --- | --- | --- |
| ProjectX Gateway API (TopstepX) | US-Futures | REST + SignalR über WebSocket | Benutzername + API-Key → Token (24 h) | ja, `stopLossBracket`/`takeProfitBracket` in Ticks, nur im Modus „Auto OCO Brackets“ | Community (`project-x-py`) | nein für REST; für Echtzeit-Updates ja |
| Tradovate API (jetzt unter NinjaTrader-Dokumentation) | US-Futures | REST + WebSocket | Name, Passwort, `cid`/`sec` → Token (~90 min, erneuerbar) | ja, `placeOSO` mit zwei Brackets = OCO | keine offizielle Bibliothek gefunden | nein für REST |
| Rithmic R\|Protocol API / R\|API+ | US-Futures | WebSocket + Protocol Buffers (4 „Plants“); R\|API+ als C++/.NET-Bibliothek | Rithmic-Benutzer, von Firma/FCM freigeschaltet; Conformance-Test | ja (Bracket-Orders laut Community-Bibliotheken) | Community (`async_rithmic`) | ja, stehende Verbindungen mit Heartbeat |
| NinjaTrader 8 (NinjaScript) | US-Futures | Desktop-Programm, Strategien in C# | Anmeldung in der Plattform; Verbindung über Rithmic oder Tradovate | ja (ATM-Strategien, Stop/Ziel als Orders) | keine (C#) | ja, Plattform muss laufen |
| MetaTrader 5 + Python-Paket | CFD, Forex | Interprozess-Kommunikation mit dem lokal laufenden MT5-Terminal | Login/Passwort/Server im Terminal | ja, `sl`/`tp` an der Order | offiziell (`MetaTrader5`, nur Windows) | ja, Terminal unter Windows |
| cTrader Open API | CFD, Forex | TCP oder WebSocket, Protobuf (Port 5035) oder JSON (5036) | OAuth 2.0 (App + Konto), Token ~30 Tage | ja, `stopLoss`/`takeProfit` bzw. relativ bei Market-Orders | offiziell (`ctrader-open-api`) | stehende Verbindung empfohlen |
| TradeLocker Public API | CFD, Forex, Krypto-CFD | REST | E-Mail, Passwort, Server → JWT | ja, `stopLoss`/`takeProfit` an der Order | offiziell (`tradelocker`) | nein (Abfragen) |
| DXtrade REST API | CFD, Forex | REST (Push separat) | Benutzer, Domain, Passwort → Session-Token | ja, Order-Gruppen IF-THEN mit OCO-Untergruppen | nur Community | nein, aber Session per `ping` halten |
| Match-Trader Platform API | CFD, Forex | REST, Marktdaten per WebSocket | Login → Token | nicht geprüft | nicht gefunden | nicht geprüft |
| Bybit API v5 | Krypto | REST + WebSocket | API-Key + HMAC-Signatur | ja, `takeProfit`/`stopLoss` an der Order | offiziell (`pybit`) | nein für REST |

Python-Bibliotheken: Versionen laut PyPI am 2026-10-23. „Offiziell“ heißt: vom Plattformbetreiber veröffentlicht.

## ProjectX Gateway API (TopstepX)

ProjectX ist die Plattform hinter TopstepX. Die offizielle Doku listet als Verbindungsadressen nur TopstepX (`api.topstepx.com`, Echtzeit `rtc.topstepx.com`). Ob und welche anderen Futures-Firmen ProjectX mit API anbieten: **nicht bestätigt**.

- **Protokoll:** REST mit JSON; Echtzeit über SignalR (WebSocket) mit einem User-Hub (`GatewayUserOrder`, `GatewayUserPosition`, `GatewayUserTrade`, `GatewayUserAccount`) und einem Market-Hub (Kurse, Trades, Orderbuch).
- **Anmeldung:** `POST /api/Auth/loginKey` mit `userName` (nicht die E-Mail) und `apiKey`. Das Token gilt 24 Stunden und wird als Bearer-Token mitgeschickt; ein fehlgeschlagener Login kommt trotzdem mit HTTP 200 und `success: false` zurück.
- **Order:** `POST /api/Order/place` mit `accountId`, `contractId`, `type` (1 Limit, 2 Market, 4 Stop, 5 Trailing Stop), `side` (0 Kauf, 1 Verkauf), `size` (Kontrakte). Stop und Ziel als `stopLossBracket`/`takeProfitBracket` mit **Abstand in Ticks**, nicht als Preis.
- **Falle:** Brackets funktionieren nur, wenn im Konto „Auto OCO Brackets“ eingestellt ist. Im Standardmodus „Position Brackets“ wird die Bracket abgelehnt, **die Einstiegsorder aber trotzdem angelegt**. Ein Bot muss das Ergebnis prüfen und darf nicht annehmen, dass ein Stop liegt.
- **Kontrakte:** `POST /api/Contract/search` liefert `id` (z. B. `CON.F.US.ENQ.U25`), `tickSize` und `tickValue` (Beispiel NQ: 0,25 Punkte, 5 $ je Tick).
- **Rate Limits:** 50 Anfragen je 30 Sekunden für historische Kerzen, 200 je 60 Sekunden für alles andere; darüber HTTP 429.
- **Zugang bei Topstep:** kostenpflichtiges Zusatzabo „TopstepX API Access“, 29 $/Monat (mit dem Code „topstep“ laut Topstep 50 % weniger). Eigene Bots sind laut Topstep erlaubt, HFT nicht. **Live-Funded-Konten dürfen nicht über die API handeln**; die API ist für die simulierte Umgebung gebaut. Keine Sandbox, zum Testen ein Practice-Konto.
- **VPS verboten:** Laut Topstep muss jede Handelsaktivität vom eigenen Gerät ausgehen; VPS, VPN und Remote-Server sind laut Nutzungsbedingungen verboten. Ein eigener Server darf Daten sammeln, testen und protokollieren, aber keine Orders senden („your server can watch and record, but it cannot trade“).

> [!important] Folge für eine Cloud-Sitzung
> Ein Bot, der aus einer Claude-Code-Cloud-Sitzung Orders an TopstepX schickt, sendet von einem fremden Server. Nach dem Wortlaut der Topstep-Hilfe ist das nicht erlaubt. Siehe [[Bot an Prop-Firm anbinden]].

## Tradovate API

Die Tradovate-Dokumentation liegt inzwischen unter `docs.ninjatrader.com/api` (Tradovate gehört zu NinjaTrader).

- **Protokoll:** REST (`demo.tradovateapi.com/v1`, `live.tradovateapi.com/v1`), Marktdaten über `md.tradovateapi.com`, Echtzeit über WebSocket. Die Hosts sollen aus der Anmeldeantwort gelesen, nicht fest eingetragen werden.
- **Anmeldung:** `accessTokenRequest` mit Name, Passwort, App-Angaben und API-Schlüssel (`cid`, `sec`). Token ca. 90 Minuten, etwa 15 Minuten vor Ablauf mit `renewAccessToken` verlängern. Eine gleichzeitige Client-Verbindung je Kunde, zwei Sessions je Nutzer (eine dritte schließt die älteste).
- **Bracket:** `POST /order/placeOSO` mit Einstiegsorder und `bracket1` (Pflicht) und `bracket2`; sind beide angegeben, sind sie als OCO verknüpft.
- **Rate Limits:** 5.000 Anfragen pro Stunde für angemeldete Nutzer; dazu Limits je Endpunkt und IP, z. B. `accesstokenrequest` 5 Fehlversuche/Stunde, `renewaccesstoken` 15/Stunde. Bei Überschreitung kommt eine „Penalty Ticket“-Antwort mit HTTP 200 (Wartezeit `p-time`), bei `p-captcha` eine Stunde Pause; ein Nutzerlimit ergibt HTTP 429.
- **Zugang:** Für einen eigenen API-Schlüssel nennen Tradovate-Forum und Anbieter ein Live-Konto mit mehr als 1.000 $ plus das Zusatzabo „API Access“. **Prop-Konten haben laut Nutzerberichten im Tradovate-Forum keinen direkten API-Zugang**; eine offizielle Aussage von Tradovate dazu wurde nicht gefunden. Drittanbieter (Webhook-Brücken) handeln Prop-Konten über eigene, bereits freigeschaltete Integrationen; das ist eine andere Lage als ein eigener Bot.
- **Python:** keine offizielle Bibliothek gefunden; das PyPI-Paket `tradovate` (0.0.1, 2022) ist ein privates Projekt.

## Rithmic (R|Protocol API, R|API+)

Viele Futures-Prop-Firmen führen ihre Konten über Rithmic. Die Rithmic-Seiten sind per Skript kaum lesbar; die Angaben stammen aus der Produktseite (über die Suche) und von Brokern.

- **Varianten:** R|API+ als Bibliothek für C++ (Windows, macOS, Linux) und .NET (Windows); R|Protocol API über WebSocket und Google Protocol Buffers, damit in jeder Sprache nutzbar; R|Diamond für niedrige Latenz (Linux).
- **Aufbau:** vier getrennte WebSocket-Verbindungen („Plants“) für Kurse, Orders, Historie und Gewinn/Verlust, jede mit eigenem Login und Heartbeat. Ein Bot braucht also einen dauernd laufenden Prozess.
- **Zugang:** Entwicklerkit bei Rithmic anfordern, gegen das Testsystem bauen, **Conformance-Prüfung** bestehen, dann Produktionszugang. Die Firma bzw. der Clearer vergibt den Rithmic-Benutzer und entscheidet, ob er die API nutzen darf; Fehler wie „permission denied“ bedeuten laut Anbieterblog meist eine fehlende Freischaltung. Ob eine bestimmte Prop-Firm einem eigenen Programm den API-Zugang gibt: je Firma **nicht bestätigt**.
- **Python:** nur Community, z. B. `async_rithmic` (1.6.6, 2026-08-21, unterstützt Bracket-Orders) und das ältere `pyrithmic`.
- **Rate Limits:** keine öffentlichen Zahlen gefunden.

## NinjaTrader 8 (NinjaScript)

- **Was:** Desktop-Handelsplattform (Windows) mit eigenen Strategien in C# (NinjaScript). Kein Python. Die Plattform muss die ganze Zeit laufen.
- **Prop-Konten:** werden über die Verbindung „Rithmic for NinjaTrader Brokerage“ oder die Tradovate-basierte Verbindung „NinjaTrader“ eingebunden (laut Anbieterleitfaden je nach Firma verschieden).
- **Erlaubnis:** hängt an der Firma. Für Apex berichten mehrere Drittquellen, vollautomatisches Handeln sei auf Funded-Konten verboten, nur halbautomatisch unter Aufsicht erlaubt (siehe [[Prop-Firms und Bot-Architektur]]); eine offizielle Apex-Seite konnte nicht abgerufen werden (HTTP 403).
- **Für diesen Bot:** ein Umweg. Die Python-Skripte müssten Signale an eine NinjaScript-Strategie übergeben (Datei, Socket oder kommerzielle Brücke). Nur sinnvoll, wenn die Firma nichts anderes anbietet.

## MetaTrader 5 und das Python-Paket

- **Was:** Das Paket `MetaTrader5` (MetaQuotes, 5.0.6231 vom 2026-09-27) spricht über Interprozess-Kommunikation mit einem **lokal laufenden MT5-Terminal**. Auf PyPI gibt es nur Windows-Pakete (x86-64). Unter Linux geht es nur über Umwege wie Wine oder eine Windows-Maschine; das ist nicht offiziell unterstützt.
- **Ablauf:** `initialize()`, `login()`, `order_send()` mit `volume` (in Lots), `sl`, `tp`, `deviation`, `magic` (Kennung des Bots), `positions_get()`.
- **Stop beim Broker:** Stop-Loss und Take-Profit liegen auf dem Server und lösen auch bei geschlossenem Terminal aus; ein Trailing Stop dagegen läuft im Terminal und endet mit ihm (laut MetaTrader-4-Hilfe, für MT5 nicht eigens geprüft).
- **Rate Limits:** keine öffentlichen Zahlen; Firmen setzen eigene Grenzen gegen übermäßig viele Anfragen (je Firma prüfen).
- **Prop-Firmen:** MT5 ist bei CFD/Forex-Firmen verbreitet; FTMO erlaubt Expert Advisors grundsätzlich (siehe [[Prop-Firms und Bot-Architektur]]). VPN/VPS sind bei FTMO allgemein erlaubt, aber man soll sich nicht aus den USA in MetaTrader oder cTrader anmelden und keine US-Geolokation über VPN/VPS verwenden.

## cTrader Open API

- **Protokoll:** TCP oder WebSocket; Protobuf über Port 5035, JSON über Port 5036; getrennte Hosts `live.ctraderapi.com` und `demo.ctraderapi.com` (ein Live-Host nimmt keine Demo-Konten an und umgekehrt).
- **Anmeldung:** OAuth 2.0. Die eigene Anwendung wird im Open-API-Portal registriert (`clientId`, `clientSecret`, Redirect-URI), der Kontoinhaber stimmt zu. Access Token ca. 30 Tage (2.628.000 s), Refresh Token ohne Ablauf. In der Verbindung erst `ProtoOAApplicationAuthReq`, dann `ProtoOAAccountAuthReq`.
- **Order:** `ProtoOANewOrderReq`, `volume` in 0,01 Einheiten (1000 = 10,00 Einheiten). Absolutes `stopLoss`/`takeProfit` ist **bei Market-Orders nicht erlaubt**; dort `relativeStopLoss`/`relativeTakeProfit` (in 1/100000 Preiseinheiten) verwenden.
- **Rate Limits:** 50 Anfragen pro Sekunde je Verbindung, 5 pro Sekunde für historische Daten.
- **Python:** offiziell `ctrader-open-api` (Spotware, OpenApiPy, 0.9.2 von 2024-06).
- **Prop-Firmen:** ob die Firma cTrader-Konten für fremde Open-API-Apps freigibt, ist **je Firma zu klären**; nicht bestätigt für eine bestimmte Firma.

## TradeLocker Public API

- **Protokoll:** REST, Basis `demo.tradelocker.com/backend-api/` bzw. `live.tradelocker.com/backend-api/`. Kein Streaming in der öffentlichen Referenz gefunden, also Abfragen (Polling).
- **Anmeldung:** `/auth/jwt/token` mit E-Mail, Passwort und Servername der Firma → Access- und Refresh-Token (JWT). Jede `/trade/`-Anfrage braucht zusätzlich `accNum` im Header.
- **Order:** `POST /trade/accounts/{accountId}/orders` mit `qty`, `routeId`, `side`, `validity` (Market = IOC, Limit/Stop = GTC), `type`, `tradableInstrumentId`; dazu `stopLoss`/`stopLossType` (absolute, offset, trailingOffset) und `takeProfit`/`takeProfitType`. Ein Freitextfeld kennzeichnet Bot-Orders.
- **Rate Limits:** je Route, abzufragen über `/trade/config`; mehr Spielraum über das TradeLocker Developer Program (`tl-developer-api-key`).
- **Python:** offiziell `tradelocker` (0.56.2 von 2024-12, Python ≥ 3.11).
- **Prop-Firmen:** viele CFD-Firmen bieten TradeLocker; ob sie die API für eigene Bots erlauben, steht in deren Regeln (**je Firma prüfen**).

## DXtrade REST API

- **Protokoll:** REST; Push-Benachrichtigungen in einem eigenen Dokument (WebSocket).
- **Anmeldung:** `POST …/login` mit `username`, `domain`, `password` → `sessionToken` mit Inaktivitäts-Timeout; Header `Authorization: DXAPI <token>`; `ping` verlängert die Session.
- **Order:** `POST …/accounts/<account code>/orders` nimmt Einzelorders und Order-Gruppen; `contingencyType: IF-THEN` (Einstieg löst Folgeorders aus) mit `ocoSubgroups` für Stop und Ziel. Die Spezifikation widerspricht sich bei der Kombination von OCO und IF-THEN; vor Gebrauch auf Demo testen.
- **Python:** nur Community-Code. **Rate Limits:** nicht gefunden.
- **Prop-Firmen:** die Firma betreibt den DXtrade-Server und entscheidet, ob die REST-API für Kunden offen ist (nicht bestätigt).

## Match-Trader Platform API

- Match-Trader hat eine „Platform API (for traders use)“: REST für Login, Token-Erneuerung, Konto, Positionen und Orders, Marktdaten per WebSocket (STOMP). Referenz bei Theneo (`app.theneo.io/match-trade/platform-api`), per Skript nicht vollständig lesbar.
- Laut Match-Trade-Dokumentation kann der Betreiber diese API auf seinem Server **abschalten**. Bei einer Prop-Firm mit Match-Trader ist also offen, ob sie überhaupt erreichbar ist. Bracket-Unterstützung und Rate Limits: **nicht geprüft**.

## Börsen-API: Bybit

- **Protokoll:** REST und WebSocket. Anmeldung mit API-Key und HMAC-Signatur (Header `X-BAPI-API-KEY`, `X-BAPI-SIGN`, `X-BAPI-TIMESTAMP`, `X-BAPI-RECV-WINDOW`).
- **Order:** `POST /v5/order/create` mit `takeProfit`/`stopLoss` direkt an der Order; bei Perpetuals `tpslMode` Full oder Partial.
- **Rate Limits:** 600 Anfragen je 5 Sekunden je IP; `order/create` etwa 10–20 je Sekunde je Konto; Fehler 10006 bei Überschreitung, HTTP 403 bei IP-Sperre (10 Minuten warten).
- **Python:** offiziell `pybit` (bybit-exchange, 5.17.0 von 2026-07).
- **Prop-Firmen:** Krypto-Firmen wie HyroTrader lassen den Bot direkt an die Bybit-Demo-API anbinden; laut HyroTrader-FAQ sind Bots erlaubt, wenn die Strategie die eigene ist (kein Copy-Trading, keine fremden Signale). Siehe [[Prop-Firms für Krypto]].

## Was überall gleich ist

- **Stop beim Broker:** Alle Plattformen außer NinjaTrader-Strategien ohne ATM können Stop und Ziel als echte Orders beim Server ablegen. Nur das schützt bei einem Ausfall des Bots. Ein Stop, den der Bot selbst überwacht, ist kein Stop.
- **Einheiten:** Aktien in Stück; Futures in Kontrakten und Ticks; CFD/Forex in Lots oder Einheiten, oft mit Mindestschritt 0,01. Der Budget-Schritt muss das je Plattform umrechnen.
- **Geheimnisse:** Schlüssel und Passwörter gehören in Umgebungsvariablen, nie in den Vault (Regel aus `CLAUDE.md`).
- **Vor dem Kauf klären:** API-Zugang für genau diesen Kontotyp (Prüfung, Funded, Live)? Vollautomatisch erlaubt? Von welchem Rechner bzw. Standort aus (VPS, Cloud, Land)?

## Für diesen Bot

- Der heutige Bot spricht REST mit Alpaca und handelt US-Aktien. **Keine** der Prop-Plattformen oben handelt echte US-Aktien wie Alpaca; es sind Futures, CFDs oder Krypto. Siehe [[Prop-Firms für US-Aktien]].
- Am nächsten am heutigen Aufbau (Python, REST, Bracket in einer Anfrage): **TradeLocker**, **Bybit**, **cTrader Open API** und **ProjectX**. MT5 verlangt ein Windows-Terminal; Rithmic und NinjaTrader verlangen dauernd laufende Verbindungen bzw. eine Desktop-Plattform.
- **Standort ist ein Ausschlusskriterium:** Topstep verbietet Orders von VPS und Remote-Servern; FTMO will keine Anmeldung mit US-Geolokation in MetaTrader oder cTrader. Eine Claude-Code-Cloud-Sitzung läuft auf fremden Servern mit unbekanntem Standort. Das vor allem anderen klären.
- Wie der Umbau im Einzelnen aussähe: [[Bot an Prop-Firm anbinden]].

## Quellen

Abgerufen 2026-10-23.

Offizielle Dokumentation:
- [ProjectX Gateway: Authenticate (API key)](https://gateway.docs.projectx.com/docs/getting-started/authenticate/authenticate-api-key/)
- [ProjectX Gateway: Rate Limits](https://gateway.docs.projectx.com/docs/getting-started/rate-limits/)
- [ProjectX Gateway: Place an Order](https://gateway.docs.projectx.com/docs/api-reference/order/order-place/)
- [ProjectX Gateway: Search Contracts](https://gateway.docs.projectx.com/docs/api-reference/market-data/search-contracts/)
- [ProjectX Gateway: Real Time API](https://gateway.docs.projectx.com/docs/realtime/)
- [ProjectX Gateway: Connection URLs](https://gateway.docs.projectx.com/docs/getting-started/connection-urls/)
- [Topstep Help Center: TopstepX API Access](https://help.topstep.com/en/articles/11187768)
- [NinjaTrader/Tradovate API: Authentication](https://docs.ninjatrader.com/api/authentication)
- [NinjaTrader/Tradovate API: placeOSO](https://docs.ninjatrader.com/api/rest-api-endpoints/orders/place-oso)
- [Tradovate Partner Docs: Rate Limits](https://partner.tradovate.com/overview/core-concepts/rate-limits)
- [Tradovate Partner Docs: Penalty Tickets](https://partner.tradovate.com/overview/core-concepts/penalty-tickets)
- [Rithmic: API Suite](https://www.rithmic.com/products/api-suite)
- [MQL5: Python-Integration MetaTrader 5](https://www.mql5.com/en/docs/python_metatrader5)
- [MQL5: order_send](https://www.mql5.com/en/docs/python_metatrader5/mt5ordersend_py)
- [PyPI: MetaTrader5](https://pypi.org/project/MetaTrader5/)
- [MetaTrader 4 Hilfe: Trailing Stop](https://www.metatrader4.com/en/trading-platform/help/positions/trailing)
- [cTrader Open API: Getting Started](https://help.ctrader.com/open-api/)
- [cTrader Open API: Proxies/Endpoints](https://help.ctrader.com/open-api/proxies-endpoints/)
- [cTrader Open API: Account Authentication](https://help.ctrader.com/open-api/account-authentication/)
- [cTrader Open API: Messages](https://help.ctrader.com/open-api/messages/)
- [TradeLocker Public API: Getting Started](https://public-api.tradelocker.com/docs/getting-started)
- [TradeLocker Public API: Place a new order](https://public-api.tradelocker.com/reference/placeorder)
- [GitHub: tradelocker-python](https://github.com/tradelocker/tradelocker-python/)
- [DXtrade REST API Spezifikation](https://demo-xt.dx.trade/dxweb/specs/DX_REST_API.html)
- [Match-Trade Docs: Match-Trader API Documentation](https://docs.match-trade.com/docs/match-trader-api-documentation/)
- [Bybit API v5: Rate Limit](https://bybit-exchange.github.io/docs/v5/rate-limit)
- [Bybit API v5: Place Order](https://bybit-exchange.github.io/docs/v5/order/create-order)
- [GitHub: bybit-exchange/pybit](https://github.com/bybit-exchange/pybit)
- [FTMO FAQ: Can I travel or use VPN/VPS?](https://ftmo.com/en/faq/can-i-travel-or-use-vpn-vps/)
- [HyroTrader FAQ: Trading bots](https://www.hyrotrader.com/faq/hyrotrader-account/can-i-use-trading-bots-or-signal-bots-during-the-challenge-or-on-a-funded-account/)

Community-Bibliotheken und Foren (keine offiziellen Aussagen):
- [project-x-py (TexasCoding)](https://github.com/TexasCoding/project-x-py)
- [async_rithmic (rundef)](https://github.com/rundef/async_rithmic)
- [Tradovate Community: Prop Account API Access](https://community.tradovate.com/t/prop-account-api-access/10430)
- [Tradovate Community: API Access Requirements](https://community.tradovate.com/t/api-access-requirements/7769)

Ratgeber und Anbieter, die selbst Automatisierung verkaufen (nur als Hinweis):
- [Ironbeam: Rithmic API](https://www.ironbeam.com/rithmic-api-futures-trading/) (Broker)
- [PickMyTrade: Rithmic Access Denied](https://blog.pickmytrade.io/rithmic-access-denied-api-access-level-error-fix/) (Anbieter einer Webhook-Brücke)
- [CrossTrade: NinjaTrader 8 Prop Firm Connection Guide](https://crosstrade.io/blog/ninjatrader-8-prop-firm-connection-guide) (Anbieter einer Brücke)
- [TradersPost: Apex Trader Funding Guide](https://blog.traderspost.io/article/apex-trader-funding-review) (Anbieter einer Brücke)
