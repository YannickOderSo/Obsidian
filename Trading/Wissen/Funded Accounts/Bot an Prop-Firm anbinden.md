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

# Bot an Prop-Firm anbinden

Umbauplan für genau diesen Bot (Skills `trader-*` plus Autopilot `paper_auto.py`), falls er einmal ein Prop-Firm-Konto statt des Alpaca-Paper-Kontos handeln soll. Ein Plan, kein Code; die Schnittstellen selbst stehen in [[Schnittstellen für Bots]], der Rahmen in [[Funded Accounts]].

> [!warning] Erst die Entscheidung, dann der Umbau
> Die Repo-Regel gilt: **mit echtem Geld keine Order ohne Yannicks ausdrückliches Ja für genau diese Order.** Autonom handelt der Bot nur Paper (Entscheidung vom 2026-10-22, nur für das Alpaca-Paper-Konto). Eine Challenge kostet echtes Geld, und ein Funded-Konto zahlt echtes Geld aus, auch wenn die Orders simuliert sind. Ob der Bot dort selbstständig handeln darf, entscheidet allein Yannick, und diese Entscheidung ist **nicht gefallen**. Bis dahin heißt „anbinden“: Der Bot schlägt vor, Yannick sagt je Order Ja.

## Ausgangslage

| Heute | Bei einer Prop-Firm |
| --- | --- |
| US-Aktien über Alpaca, nur long, Bracket per REST an `paper-api.alpaca.markets` | meist Futures (ProjectX, Tradovate, Rithmic), CFD/Forex (MT5, cTrader, TradeLocker, DXtrade, Match-Trader) oder Krypto (Bybit); echte US-Aktien nur bei wenigen Firmen, siehe [[Prop-Firms für US-Aktien]] |
| Stückzahl, Preise in Cent | Kontrakte und Ticks, oder Lots mit Schrittweite |
| eigene Limits: 1.000 $ je Trade, 2.500 $ je Tag, 8 Trades | Limits der Firma: Tagesverlust auf Equity inkl. offener Verluste, nachziehender Maximalverlust, Konsistenz, eventuell News-Sperren, eigene Tagesgrenze |
| Cloud-Sitzungen nach Zeitplan, Hintergrundprozesse enden nach etwa 2 Stunden | Firma legt fest, **von wo** Orders kommen dürfen (Topstep: kein VPS, kein Remote-Server) |

## Was bleibt, was sich ändert

| Baustein | Bleibt? | Was sich ändert |
| --- | --- | --- |
| `trader-scanner` | teilweise | Bei Futures gibt es keine Tausende Werte zu durchsuchen, sondern eine feste Liste (z. B. Micro-E-mini S&P 500 und Nasdaq-100). Der Tagesscan entfällt, der ORB-Scan bleibt. Bei Aktien-CFDs: nur Werte aus der Instrumentenliste der Firma |
| `trader-news` | ja | SEC-8-Ks passen nur zu Einzelaktien; für Index-Futures zählen Makro-Termine ([[Makro-Termine]]), die gleichzeitig die News-Sperre der Firma füttern |
| `trader-entry` | ja | Datenquelle: Kerzen vom Broker (z. B. ProjectX `History/retrieveBars`) statt Yahoo, weil Yahoo-Futures-Kurse verzögert und nicht der Handelspreis sind. Die Regel (15-Min-Range, 5-Min-Schluss darüber) bleibt |
| `trader-exit` | ja | Stop und Ziel auf die **Tick-Größe** runden statt auf Cent; bei ProjectX zusätzlich in Tick-Abstand umrechnen |
| `trader-timemachine` | ja | braucht historische Kerzen des gehandelten Instruments; ein Index-Future verhält sich anders als eine Einzelaktie, alte Quoten nicht übertragen |
| `trader-budget` | umbauen | Stückzahl → Kontrakte oder Lots; Verlust je Kontrakt = Ticks bis Stop × Tick-Wert + Gebühren; Höchstzahl Kontrakte der Firma |
| `trader-risk` | erweitern | Prop-Regeln als zusätzliche harte Prüfungen (unten) |
| `trader-broker` / `paper_auto.py` | ersetzen | Broker-Adapter je Plattform statt Alpaca-REST |
| `trading-journal` | ja | Felder für Kontrakte, Tick-Wert, Gebühren, Stand der Prop-Regeln (Abstand zu Tageslimit und Maximalverlust) |
| Discord-Meldungen | ja | zusätzlich Warnungen bei Annäherung an Prop-Grenzen |

## Umrechnung: Symbol, Tick, Größe

- **Symbol:** eine Zuordnungstabelle `trader/instruments.json`, z. B. Signal `MNQ` → Kontrakt-ID der Plattform für den laufenden Monat. Bei ProjectX liefert `Contract/search` die `id`, `tickSize` und `tickValue`; Kontrakte laufen aus (Rollover), die Tabelle muss den aktiven Monat kennen. Bei CFD-Plattformen heißen Symbole je Firma anders: nie raten, immer aus der Instrumentenliste der Plattform lesen.
- **Tick-Größe:** Preise auf ganze Ticks runden, Stop **vom Einstieg weg** (long: abrunden), Ziel zum Einstieg hin. Beispiel aus der ProjectX-Doku: NQ 0,25 Punkte = 5 $ je Tick. Werte nie fest im Code, immer von der Plattform holen.
- **Größe:**

```
risiko_je_kontrakt = ticks(einstieg - stop) * tick_wert + gebuehr_rundreise
kontrakte = floor(min(max_verlust_trade, prop_rest_tag * anteil) / risiko_je_kontrakt)
kontrakte = min(kontrakte, max_kontrakte_der_firma)
wenn kontrakte < 1: kein Trade (wie heute: Stop zu weit = Absage, kein kleinerer Stop)
```

- **CFD/Forex:** Lots statt Kontrakte; Mindestgröße und Schrittweite aus den Instrumentdaten (cTrader `volume` in 0,01 Einheiten, MT5 `volume` in Lots).

## Prop-Regeln als harte Prüfungen in trader-risk

Heute rechnet `trader-risk` das Tageslimit als Summe der Verluste am Stop aller heutigen Einstiege. Prop-Firmen rechnen anders: auf **Equity**, also inklusive offener Verluste, und laufend. Neue Prüfungen, jede führt zu BLOCK (Ausstiege bleiben wie heute immer erlaubt):

| Prüfung | Rechnung | Beispiel aus den Regeln |
| --- | --- | --- |
| Tageslimit auf Equity | Equity jetzt − Summe(Verlust bis Stop aller offenen Positionen) − Verlust am Stop der neuen Order − Puffer > Tagesgrenze | FTMO: Grenze täglich um 0:00 CE(S)T aus dem Kontostand neu berechnet; Equity = Kontostand + offene Gewinne/Verluste ± Swaps − Kommissionen |
| Nachziehender Maximalverlust | dieselbe Rechnung gegen die aktuelle Untergrenze; die Untergrenze täglich (oder je Trade) neu von der Firma holen | Topstep: Maximum Loss Limit zieht mit dem Tagesschluss-Kontostand nach, wird aber in Echtzeit inkl. offener Verluste überwacht; Erreichen = sofortige Liquidation |
| Konsistenz | bester Tag ≤ x % des Gesamtgewinns; nur Warnung vor einem großen Tag, kein Grund für mehr Risiko | Topstep (Drittquellen): bester Tag < 50 % des Gewinns, sonst steigt das Ziel; FTMO 1-Step ähnlich (siehe [[Prop-Firms und Bot-Architektur]]) |
| News-Sperre | kein Einstieg in einem Fenster um Termine aus [[Makro-Termine]], wenn die Firma das verlangt | je Firma; Topstep verlangt laut Hilfe-Center **kein** Glattstellen zu Wirtschaftsdaten, andere Firmen schon |
| Tagesgrenze/Reset | Handelstag der Firma statt New Yorker Kalendertag | FTMO 0:00 CE(S)T; Topstep-Tag laut Drittquellen 17:00 bis 15:10 CT (nicht bestätigt) |
| Erlaubte Instrumente und Größe | Instrument auf der Liste der Firma, Kontrakte ≤ Höchstzahl | je Firma |
| Abstand halten | eigenes Tageslimit deutlich **unter** dem der Firma | z. B. halbe Firmengrenze; [[Tageslimits und Regelwerk]] |

Skizze:

```
konto = adapter.account()            # Kontostand, Equity, offene P&L, Untergrenzen der Firma
offen = summe(verlust_bis_stop(p) for p in adapter.positions())
schlimmstfall = konto.equity - offen - order.verlust_am_stop - puffer
wenn schlimmstfall <= konto.tagesgrenze: BLOCK "Tageslimit der Firma"
wenn schlimmstfall <= konto.max_verlust_grenze: BLOCK "Maximalverlust der Firma"
wenn news_fenster(jetzt): BLOCK "News-Sperre"
```

Wichtig: Diese Rechnung geht davon aus, dass jede Position einen Stop beim Broker hat. Ohne serverseitigen Stop ist der offene Verlust unbegrenzt und die Prüfung wertlos. Schlupf bei schnellen Märkten bleibt ein Restrisiko (Topstep: keine Ausnahmen für Slippage).

## Architektur

```
   Cloud-Sitzung (Zeitplan)                       Ausführer (wo die Firma es erlaubt)
 ┌────────────────────────────┐                 ┌──────────────────────────────────┐
 │ scanner → news → entry     │                 │ liest trader/orders.json + PASS  │
 │ → exit → timemachine       │  Vorschlag      │ fragt Yannick (Ja je Order)      │
 │ → budget → risk (PASS)     │ ──────────────▶ │ adapter.place_bracket()          │
 │ → journal, Discord         │                 │ adapter.fills() / positions()    │
 │                            │ ◀────────────── │ adapter.flatten() vor Schluss    │
 │                            │  Fills, Stand   │ prüft: Stop liegt beim Broker?   │
 └────────────────────────────┘                 └───────────────┬──────────────────┘
                                                                │ REST / WebSocket
                                                       ┌────────▼─────────┐
                                                       │ Plattform der    │
                                                       │ Firma: Stop und  │
                                                       │ Ziel liegen hier │
                                                       └──────────────────┘
```

Die Trennung passt zu Topsteps Regel „your server can watch and record, but it cannot trade“: Analyse, Simulation und Journal dürfen auf einem Server laufen, das Senden von Orders nicht.

### Adapter-Schnittstelle

Ein Adapter je Plattform, alle mit derselben Form; `paper_auto.py` wäre der Alpaca-Paper-Adapter.

| Methode | Eingabe | Ausgabe | Pflichten |
| --- | --- | --- | --- |
| `instrument(symbol)` | Signal-Symbol | Plattform-ID, Tick-Größe, Tick-Wert, Mindestgröße | aktiven Kontrakt wählen |
| `account()` | – | Kontostand, Equity, offene P&L, Grenzen der Firma soweit abfragbar | nie Schlüssel ausgeben |
| `place_bracket(order)` | Seite, Größe, Einstieg, Stop, Ziel | Order-ID, Status | Einstieg, Stop und Ziel **in einem Auftrag**; danach prüfen, ob Stop und Ziel wirklich liegen; sonst sofort glattstellen und melden |
| `positions()` | – | offene Positionen mit Einstieg, Größe, aktuellem Stop | |
| `fills(since)` | Zeitpunkt | Ausführungen (Einstieg, Stop, Ziel, Gebühren) | jede nur einmal liefern (wie `sync` heute) |
| `flatten(symbol=None)` | optional Symbol | Ergebnis | erst Stop/Ziel streichen, dann schließen; nie mehr verkaufen als gehalten |

Plattform-Eigenheiten, die der Adapter auffangen muss:

- **ProjectX:** Bracket in Ticks; Konto muss auf „Auto OCO Brackets“ stehen, sonst wird nur der Einstieg angelegt. Token 24 h. 200 Anfragen/Minute.
- **Tradovate:** `placeOSO` mit zwei Brackets; Token ~90 min erneuern; nur eine Client-Verbindung je Kunde; Strafzeiten bei zu vielen Anmeldungen.
- **cTrader:** bei Market-Orders nur relativer Stop/Ziel.
- **MT5:** `sl`/`tp` an der Order; Terminal muss laufen.
- **Alpaca (heute):** Bracket-Beine sind Tagesorders und enden mit dem Schluss.

## Betrieb: Cloud-Sitzung oder dauerhafter Prozess?

| Frage | Cloud-Sitzung (heute) | Eigener Rechner / VPS |
| --- | --- | --- |
| Dauer | Läufe nach Zeitplan, Hintergrundprozesse enden nach etwa 2 Stunden und werden neu gestartet (11:40, 13:40) | läuft durch |
| Stehende Verbindungen (Rithmic, SignalR, Tradovate-WebSocket, MT5-Terminal) | brechen mit jedem Neustart ab; Token-Erneuerung und Wiederaufbau nötig | möglich |
| Windows für MT5 | nein (Linux-Container) | Windows-PC oder Windows-VPS |
| Standort | fremder Server; eine Stichprobe in dieser Sitzung zeigte eine US-Adresse (Google Cloud, Ohio) | eigener Standort |
| Erlaubt? | Topstep: Orders von Remote-Servern verboten. FTMO: VPS erlaubt, aber keine US-Geolokation bei MetaTrader/cTrader. Andere Firmen: vorher schriftlich fragen | Topstep verlangt das eigene Gerät; VPS je Firma |

Folgerungen:

- **Ein REST-Adapter mit serverseitigen Brackets kommt ohne Dauerprozess aus.** Der Schutz liegt beim Broker, nicht im Bot. Die Cloud-Läufe würden wie heute Fills holen und vor Schluss glattstellen. Technisch reicht das, **wenn** die Firma Orders von dort erlaubt.
- **Ausfälle:** Fällt der Lauf aus (Nutzungslimit, Neustart, Netz), müssen Stop und Ziel trotzdem greifen; das geht nur, wenn sie beim Broker liegen. Zusätzlich: Die Firma stellt am Ende ihres Tages nicht unbedingt glatt; ein verpasster 15:47-Lauf darf keine Position über Nacht lassen. Absicherung: Ziel und Stop als Tages- bzw. GTC-Orders, ein zweiter, späterer Glattstell-Lauf, und wo möglich eine Glattstell-Einstellung in der Plattform selbst.
- **Nie ein „Stop im Bot“:** Ein Stop, den ein Python-Prozess überwacht und bei Erreichen eine Market-Order schickt, endet mit dem Prozess nach 2 Stunden.
- **Realistische Varianten:**
  1. *Halbautomatisch, Cloud schlägt vor:* Cloud-Lauf erzeugt das Ticket und schickt es per Discord; Yannick bestätigt und platziert selbst oder lässt einen Ausführer auf **seinem** Rechner senden. Passt zur Repo-Regel und zu Firmen, die ein eigenes Gerät verlangen.
  2. *Ausführer auf eigenem Rechner/VPS:* ein kleiner Dauerprozess mit Adapter, der nur Orders sendet, die `trader-risk` geprüft hat und die Yannick bestätigt hat. Nötig für MT5 (Windows), Rithmic und NinjaTrader.
  3. *Alles in der Cloud:* nur bei einer Firma, die das schriftlich erlaubt, und nur nach einer neuen Entscheidung Yannicks zur Autonomie.

## Testphase

1. **Paper-Konto mit den Prop-Limits:** Die Regeln der Wunschfirma zuerst als zusätzliche Prüfungen gegen das Alpaca-Paper-Konto laufen lassen (gleiche Grenzen in Dollar, gleiche Tagesgrenze). Zeigt, wie oft der Bot an die Grenzen stößt, ohne neue Plattform.
2. **Demo-/Sim-Konto der Plattform:** kostenloses Demo- oder Practice-Konto (cTrader- und TradeLocker-Demo-Server, Bybit-Demo, Topstep-Practice-Konto; Topstep hat keine Sandbox). Dort Adapter testen: Bracket wirklich angelegt? Was passiert bei Ablehnung, Teilausführung, Token-Ablauf, Verbindungsabbruch, Rollover?
3. **Störfälle üben:** Lauf mitten im Trade abbrechen und prüfen, dass Stop und Ziel weiter beim Broker liegen; Glattstellen bei vollem Tageslimit; doppelte Order nach Neustart ausgeschlossen.
4. **Nachweis vor dem Kauf:** genug Trades im Journal mit gleichbleibenden Regeln und positivem Erwartungswert nach Kosten (Gebühren, Abo, Challenge-Preis). Fünf Trades reichen nicht; siehe [[Wie viele Day Trader gewinnen]] und [[Backtesting und Overfitting]].
5. **Regeln schriftlich bestätigen lassen:** Bot erlaubt? API für diesen Kontotyp? Ausführung von wo (Cloud, VPS, Land)? Siehe [[Kauf und Ablauf einer Challenge]].

## Für diesen Bot

- **Kleinster sinnvoller Schritt ohne Geld:** Prop-Prüfungen (Equity-Tageslimit inkl. offener Verluste, nachziehender Maximalverlust, Konsistenz, News-Sperre) in `trader-risk` als abschaltbarer Abschnitt der Config planen und gegen das Paper-Konto laufen lassen. Die Skills unter `.claude/skills/trader-*` sind eine Kopie fremden Codes und werden nur nach Rückfrage geändert; besser als eigene Zusatzprüfung daneben.
- **Größter Umbau:** Markt und Größe. Von US-Aktien zu Futures oder CFDs heißt neue Daten, neue Einheiten, neue Quoten in der Time Machine. Die bisherigen Ergebnisse lassen sich nicht übertragen.
- **Cloud ist für das Senden von Orders fraglich:** Topstep verbietet es ausdrücklich, FTMO will keine US-Geolokation, und die Cloud-Sitzung lief in der Stichprobe über eine US-Adresse. Analyse und Journal können in der Cloud bleiben.
- **Autonomie:** Die heutige Freigabe gilt nur für das Alpaca-Paper-Konto. Für eine Challenge gilt das Ja je Order, bis Yannick ausdrücklich anders entscheidet; dann als eigene Notiz unter `Gedächtnis/Entscheidungen/`. Manche Firmen (laut Drittquellen Apex) verbieten vollautomatisches Handeln auf Funded-Konten ohnehin.
- Keine Anlage-, Steuer- oder Rechtsberatung; siehe [[Recht Steuern und Risiken]] und [[Steuern in Deutschland]].

## Quellen

Abgerufen 2026-10-23.

- Bot-Code im Repo: `.claude/scripts/paper_auto.py` und `Trading/Autopilot.md` (Branch `claude/confident-volta-acdyxn`), `.claude/skills/trader-broker/SKILL.md`, `.claude/skills/trader-budget/SKILL.md`, `.claude/skills/trader-risk/SKILL.md`
- [Topstep Help Center: TopstepX API Access](https://help.topstep.com/en/articles/11187768) (API-Abo, Live-Funded ausgeschlossen, VPS/Remote-Server verboten)
- [Topstep Help Center: What is the Maximum Loss Limit?](https://intercom.help/topstep-llc/en/articles/8284204)
- [Topstep Help Center: What are economic releases?](https://help.topstep.com/en/articles/8284211-what-are-economic-releases)
- [FTMO: Trading Objectives](https://ftmo.com/en/trading-objectives/) (Maximum Daily Loss, Equity, 0:00 CE(S)T)
- [FTMO FAQ: Can I travel or use VPN/VPS?](https://ftmo.com/en/faq/can-i-travel-or-use-vpn-vps/)
- [ProjectX Gateway: Place an Order](https://gateway.docs.projectx.com/docs/api-reference/order/order-place/)
- [ProjectX Gateway: Search Contracts](https://gateway.docs.projectx.com/docs/api-reference/market-data/search-contracts/)
- [ProjectX Gateway: Rate Limits](https://gateway.docs.projectx.com/docs/getting-started/rate-limits/)
- [NinjaTrader/Tradovate API: Authentication](https://docs.ninjatrader.com/api/authentication)
- [cTrader Open API: Messages](https://help.ctrader.com/open-api/messages/)
- [MetaTrader 4 Hilfe: Trailing Stop](https://www.metatrader4.com/en/trading-platform/help/positions/trailing) (Stop/Ziel auf dem Server, Trailing im Terminal)
- Ratgeber (Drittanbieter, teils Verkäufer von Automatisierung): [TradersPost: Topstep Rules](https://blog.traderspost.io/article/how-to-get-funded-with-topstep), [ProptradingVibes: Topstep Consistency Rule](https://proptradingvibes.com/blog/topstep-consistency-rule), [FuturesHive: Topstep Combine Rules](https://www.futureshive.com/blog/topstep-rules-explained)
- Standort der Cloud-Sitzung: eigene Abfrage der ausgehenden Adresse über ipinfo.io in dieser Sitzung (Stichprobe, kann je Sitzung wechseln)
