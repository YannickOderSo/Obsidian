---
typ: wissen
erstellt: 2026-10-22
aktualisiert: 2026-10-22
quelle: Recherche
tags:
  - trading
  - wissen
  - markt
---

# Paper Trading bei Alpaca

Wie Alpaca im Paper-Konto Orders füllt, was dabei fehlt und was man aus Paper-Ergebnissen lernen kann und was nicht. Paper Trading ist im Vault der Standard (`"paper": true`).

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## So simuliert Alpaca die Fills

Laut Alpaca-Doku (Seite aktualisiert 07.07.2026) und Antworten von Alpaca-Mitarbeitern im Forum:

| Punkt | Verhalten im Paper-Konto |
| --- | --- |
| Preis | Gefüllt wird gegen das **NBBO**: Käufe am Ask, Verkäufe am Bid (laut Mitarbeiter auf Basis der vollständigen SIP-Quotes) |
| Marktfähigkeit | Eine Order füllt erst, wenn sie marktfähig ist: Kauf-Limit am oder über dem Ask, Verkaufs-Limit am oder unter dem Bid |
| Größe | Die Ordergröße wird **nicht** gegen die angebotene Menge am Quote geprüft. Auch 10.000 Aktien füllen zum Ask |
| Teilausführung | In etwa **10 %** der Fälle gibt es zufällig einen Teil-Fill; der Rest wird neu geprüft, solange die Order marktfähig ist |
| Kein Routing | Paper-Orders gehen an keinen Handelsplatz; es gibt keine Preisverbesserung |
| Auktionen | OPG- und CLS-Orders füllt Paper wie Market-Orders zum Quote, nicht in der Eröffnungs- oder Schlussauktion |
| API | Gleiche API wie live, eigene Schlüssel, Endpunkt `paper-api.alpaca.markets` |

### Was nicht simuliert wird

Alpaca nennt ausdrücklich:

- **Marktauswirkung** der eigenen Orders
- **Informationsabfluss**
- **Slippage durch Latenz**
- **Position in der Warteschlange** bei nicht marktfähigen Limit-Orders (eine Limit-Order füllt, sobald der Quote sie erreicht, als stünde man ganz vorne)
- **Preisverbesserung** (Price Improvement)
- **Regulatorische Gebühren** (SEC, FINRA TAF, CAT)
- **Dividenden**
- **Leihgebühren** für Leerverkäufe („Coming Soon“, live werden sie berechnet)

Außerdem: keine Bestätigungs-E-Mails für Fills.

## In welche Richtung täuscht Paper?

| Effekt | Paper wirkt … | Warum |
| --- | --- | --- |
| Kein Price Improvement | **schlechter** als live | Live-Orders füllen laut Alpaca-Mitarbeitern teils besser als der Quote; Paper-Fills seien „probably a worst case scenario“ |
| Keine Größenprüfung, keine Marktauswirkung | **besser** als live | Große Orders in dünnen Aktien füllen in Paper vollständig zum Quote |
| Keine Warteschlange | **besser** als live | Limit-Orders füllen in Paper, wo sie live noch hinter anderen warten würden |
| Keine Gebühren | etwas **besser** | Bei Vault-Größen nur Cent-Beträge |
| Gaps, Halts, schnelle Märkte | **ähnlich** | Stops füllen auch in Paper am nächsten Quote, der weit weg sein kann |
| Emotionen | viel **besser** | Kein echtes Geld, kein echter Verlustschmerz (siehe [[Psychologie und Disziplin]]) |

Für liquide Large Caps in kleinen Stückzahlen (wie im Vault) sind Paper-Fills also eher leicht pessimistisch. Für Small Caps, große Stückzahlen und Limit-Orders an umkämpften Preisen sind sie zu optimistisch.

## Marktdaten: IEX gegen SIP

- **Basic-Plan (kostenlos, Standard für Paper und Live):** Echtzeit-Daten nur von der Börse **IEX**, also von einem einzelnen Handelsplatz statt von allen US-Börsen. Einen Volumenanteil nennt Alpaca nicht. Historische Daten im Basic-Plan nicht für die jüngsten 15 Minuten; 200 API-Aufrufe je Minute; Websocket für 30 Symbole.
- **Algo Trader Plus (99 $ im Monat):** volle Abdeckung aller US-Börsen (CTA/UTP-SIP, „100 % of market volume“), 10.000 Aufrufe je Minute.
- Wichtig: Laut Alpaca-Mitarbeiter hat das Datenabo **keinen Einfluss** auf die Fills. Das Paper-Konto füllt gegen das volle NBBO, auch wenn man selbst nur IEX-Daten sieht. Die eigenen Charts und der Fill-Preis können daher voneinander abweichen.

> [!info] Im Vault kommen die Kurse von Yahoo
> Die Skills lesen freie, verzögerte und inoffizielle Yahoo-Daten. Für Alarme und Größenprüfungen reicht das, für das Timing einer Order nicht. Der Preis, der füllt, ist der des Brokers.

## Konto anlegen und zurücksetzen

- Ein neues Paper-Konto startet standardmäßig mit **100.000 $**.
- Das alte „Reset“ wurde ersetzt: Im Dashboard kann man über die Kontonummer oben links **ein neues Paper-Konto anlegen** und dabei den Betrag wählen, alte Konten löschen. Neue Konten brauchen neue API-Schlüssel.
- Der Betrag lässt sich nach dem Anlegen nicht ändern.

> [!tip] Paper-Konto mit 5.000 $ anlegen
> Mit 100.000 $ greifen die Vault-Limits zwar trotzdem (die Skills rechnen mit `budget: 5000`), aber Buying Power, Kontoanzeige und Gefühl stimmen nicht. Ein Paper-Konto mit **5.000 $** passt zu `trader/config.json` und zeigt z. B., wie wenig Cash nach einem Trade frei ist. Die Schlüssel gehören nur in die Claude-Desktop-Konfiguration, nie in den Chat.

## Was man aus Paper lernen kann und was nicht

**Lernen kann man:**
- den Ablauf der Kette (Scanner bis Journal) und die eigenen Regeln einhalten
- wie Bracket-Orders, Stops, Ziele und das Glattstellen bis 15:55 technisch funktionieren
- ob Plan und Fill zusammenpassen (bei liquiden Aktien)
- eine erste, grobe Trefferquote und R-Verteilung über viele Trades, mit dem Vorbehalt kleiner Stichproben (siehe [[Backtesting und Overfitting]])

**Nicht lernen kann man:**
- wie man unter echtem Verlust entscheidet: Ob man die Regeln auch hält, wenn echtes Geld weg ist, zeigt Paper nicht
- realistische Fills bei Small Caps, großen Stückzahlen oder Limit-Orders in der Warteschlange
- ob eine Strategie live profitabel ist: Ein positives Paper-Ergebnis über 20 Trades ist statistisch fast nichts wert

> [!warning] Paper-Gewinne sind kein Beleg
> Alpaca selbst schreibt, dass Paper Trading nur eine Simulation ist und die Ergebnisse von echtem Handel abweichen können. Wer wechseln will, sollte vorher Slippage und Kosten aus dem eigenen Journal in R einrechnen ([[Spread Liquidität und Slippage]]) und die Zahlen gegen [[Wie viele Day Trader gewinnen]] halten. Steuerlich spielt Paper keine Rolle ([[Steuern in Deutschland]]).

## Im Vault

- `trader/config.json`: `"paper": true`, `"broker": "alpaca"`. Nur der Nutzer selbst stellt auf live um.
- `trader-broker` zeigt jedes Ticket als „PAPER account, Alpaca“ und arbeitet mit Alpacas MCP-Server, `ALPACA_PAPER_TRADE: "true"` ist Standard.
- `trader-risk` warnt bei einem LIVE-Konto.
- Das Journal rechnet R vom echten Fill. So sieht man die Paper-Slippage Trade für Trade und kann sie später mit Live-Fills vergleichen.
- PDT spielt im Paper-Konto nach heutigem Stand keine Rolle mehr, siehe [[Pattern Day Trader Regel]].

## Quellen

- Alpaca Docs: Paper Trading (aktualisiert 07.07.2026) – https://docs.alpaca.markets/docs/paper-trading
- Alpaca Docs: About Market Data API (IEX, SIP, Pläne) – https://docs.alpaca.markets/docs/about-market-data-api
- Alpaca Forum (Staff, 29.05.2024): Does a paid account give more accurate paper market fills? – https://forum.alpaca.markets/t/does-a-paid-account-give-more-accurate-paper-market-fills/14303
- Alpaca Forum (Staff, 17.12.2020): Order filled above the market price? – https://forum.alpaca.markets/t/order-filled-above-the-market-price/3643
- Alpaca Docs: Orders at Alpaca – https://docs.alpaca.markets/docs/orders-at-alpaca
- Alpaca Securities: Brokerage Fee Schedule (17.09.2026) – https://files.alpaca.markets/disclosures/BrokFeeSched.pdf
- Skill-Doku `trader-broker`, `trader-risk`, `trader-alerts` in `.claude/skills/`
