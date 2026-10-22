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

# Ordertypen

Welche Ordertypen es gibt, was „Time in Force“ bedeutet und welche Regeln Alpaca dafür hat. Mit dem wichtigsten Punkt für jeden Day Trader: Ein Stop ist ein Auslöser, kein garantierter Preis.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Die Grundtypen

| Typ | Was er tut | Garantiert | Risiko |
| --- | --- | --- | --- |
| **Market** | Kauft/verkauft sofort zum besten verfügbaren Preis | Ausführung (bei liquiden Aktien) | Preis: Kauf am Ask, Verkauf am Bid, in schnellen Märkten schlechter |
| **Limit** | Nur zum Limit oder besser | Preis | Ausführung: kann ganz ausbleiben oder nur teilweise kommen |
| **Stop** (Stop-Market) | Wird beim Erreichen des Stop-Preises zur Market-Order | Auslösung, sobald gehandelt wird | Fill kann weit unter dem Stop liegen (Gap, schneller Markt) |
| **Stop-Limit** | Wird beim Stop-Preis zur Limit-Order | Kein Fill unter dem Limit | Bei einem Gap durch das Limit bleibt die Position **offen** |
| **Trailing Stop** | Stop, der dem Hoch (High Water Mark) im Abstand $ oder % folgt | Stop zieht automatisch nach | Wie Stop-Market; Abstand zu eng = Ausstieg im Rauschen |

### Ordergruppen (Order Classes)

| Klasse | Aufbau | Wofür |
| --- | --- | --- |
| **Bracket** | Einstieg + Take-Profit (Limit) + Stop-Loss (Stop oder Stop-Limit) | Der Standard der Skills: Stop und Ziel liegen ab dem Fill beim Broker |
| **OCO** (One-Cancels-Other) | Take-Profit + Stop-Loss für eine **bestehende** Position; einer füllt, der andere wird storniert | Ausstieg nachträglich absichern |
| **OTO** (One-Triggers-Other) | Einstieg + nur ein Ausstieg (Ziel **oder** Stop) | Selten sinnvoll, wenn ein Stop Pflicht ist |

### Time in Force

| TIF | Bedeutung bei Alpaca |
| --- | --- |
| **day** | Gilt nur am Tag der Eingabe, standardmäßig nur 9:30–16:00 ET. Nicht ausgeführte Teile werden nach der Schlussauktion storniert. Nach 16:00 eingegebene Orders gelten für den nächsten Tag |
| **gtc** | Bis auf Widerruf, bei Alpaca aber höchstens **90 Tage** (dann automatische Stornierung, `expires_at`) |
| **opg** | Market-on-Open / Limit-on-Open für die Eröffnungsauktion. Eingabe zwischen 9:28 und 19:00 ET wird abgelehnt; nach 19:00 gilt sie für den nächsten Morgen |
| **cls** | Market-on-Close / Limit-on-Close für die Schlussauktion. Eingabe zwischen 15:50 und 19:00 ET wird abgelehnt |
| **ioc** | Sofort ausführen, was geht, Rest stornieren |
| **fok** | Ganz oder gar nicht, sofort |

## Besonderheiten bei Alpaca

Aus der Alpaca-Doku „Orders at Alpaca“ (Stand der Seite August 2026):

- **Bracket:** Take-Profit und Stop-Loss werden erst aktiv, wenn der Einstieg **vollständig** gefüllt ist. Wird ein Teil storniert, fallen die anderen mit. Nur `day` oder `gtc`, **keine Extended Hours**. Beim Kauf-Bracket muss das Take-Profit-Limit über dem Stop liegen. Wird das Take-Profit nur teilweise gefüllt, passt Alpaca die Stückzahl des Stop-Loss an.
- **Basispreis-Regel:** Der Stop muss mindestens 0,01 $ unter dem Basispreis liegen (Limitpreis des Einstiegs, sonst aktueller Marktpreis), sonst kann Alpaca die Order ablehnen. Ein Plan, dessen Stop schon unter dem aktuellen Kurs liegt, fällt hier durch.
- **OCO** geht nur als Ausstieg auf eine bestehende Position, `type` ist `limit`, der Stop-Teil braucht `stop_price`.
- **Trailing Stop** nur als einfache Order mit `day`/`gtc`, (noch) nicht als Stop-Teil eines Brackets oder OCO, und er löst außerhalb der regulären Sitzung nicht aus.
- **Extended Hours** nur mit Limit-Orders, `day` oder `gtc` und `extended_hours: true`. Alles andere wird abgelehnt.
- **Preisschritte:** ab 1,00 $ höchstens zwei Nachkommastellen, darunter vier. Sonst Ablehnung.
- **Fractional/Notional:** Bruchstücke nur mit `day`, kein Bracket laut Skill-Doku (`trader-broker`: „A bracket is whole shares only“). Die Alpaca-Seite nennt Bruchstücke ausdrücklich nur für einfache Market-, Limit-, Stop- und Stop-Limit-Orders.
- **Auslösung von Stops:** Ein Verkaufs-Stop löst aus, wenn ein Trade auf dem konsolidierten Tape zum oder unter dem Stop stattfindet, der nicht außerhalb des NBBO liegt.
- **Paper:** OPG- und CLS-Orders füllt das Paper-Konto laut Alpaca-Mitarbeiter wie Market-Orders zum Quote, nicht in der Auktion (siehe [[Paper Trading bei Alpaca]]).

## Was mit einem Stop im Gap passiert

Ein Stop-Market wird bei einem Gap zur Market-Order und füllt zum nächsten verfügbaren Preis, der weit unter dem Stop liegen kann. Ein Stop-Limit wird ausgelöst, aber nicht gefüllt, wenn der Kurs unter das Limit springt; er bleibt dann als Limit-Order liegen und die Position bleibt offen. FINRA warnt ausdrücklich, dass kurze Kursspitzen in volatilen Phasen Stops auslösen können und die Aktie sich am selben Tag wieder erholt.

Intraday entstehen Gaps vor allem nach **Handelsstopps** (News-Halt, LULD-Pause, siehe [[Handelsstopps und LULD]]): Die Aktie öffnet nach der Pause in einer Auktion, oft deutlich entfernt vom letzten Kurs.

### Beispielrechnung mit den Vault-Limits

TSLA-Plan aus den Skills: Einstieg 364,18 $, Stop 358,32 $, Risiko 5,86 $ je Aktie, 8 Aktien.

| Szenario | Fill | Verlust | in R |
| --- | --- | --- | --- |
| Stop füllt am Stop | 358,32 $ | 8 × 5,86 = **46,88 $** | −1,0 R |
| Schneller Markt, 0,10 $ Slippage | 358,22 $ | 8 × 5,96 = 47,68 $ | −1,02 R |
| Halt, Wiederöffnung bei 352,00 $ | 352,00 $ | 8 × 12,18 = **97,44 $** | −2,1 R |
| Stop-Limit 358,32/358,00, Wiederöffnung 352 $ | kein Fill | offen, Verlust wächst weiter | unbegrenzt |

Der dritte Fall sprengt das Limit von 50 $ je Trade und zwei davon fast das Tageslimit von 150 $. Darum ist das Max-Loss-Limit ein **Planwert**, kein Deckel.

> [!warning] Stop ist ein Plan, keine Garantie
> Für Long-Day-Trades ist ein **Stop-Market** meist das kleinere Übel: Er bringt einen raus, wenn auch schlechter. Ein Stop-Limit schützt den Preis, kann aber die Position im Fall stehen lassen, gegen den er schützen soll. Wer flat bis 15:55 ist, vermeidet das Übernacht-Gap, nicht aber Gaps nach einem Halt am Tag.

> [!tip] Market oder Limit zum Einstieg?
> Ein Market-Einstieg nach einem Breakout füllt am Ask, in schnellen Momenten darüber. Ein Limit leicht über dem Breakout-Level begrenzt den Preis, kann aber den Trade verpassen. Beides ist legitim; entscheidend ist, dass `trader-risk` vom **höheren** Preis aus rechnet (Plan oder frischer Kurs). Belastbare Studien, welche Variante für Privatanleger besser abschneidet, habe ich nicht gefunden.

## Im Vault

- `trader-budget` schreibt **eine** Bracket-Order: Market, `day`, `order_class: bracket`, `take_profit_limit_price`, `stop_loss_stop_price`, ganze Aktien. Mit `--limit` wird der Einstieg eine Limit-Order.
- `trader-risk` prüft das Format: Bracket nur mit ganzen Aktien, `day` oder `gtc`, beide Beine vorhanden; Stop auf der richtigen Seite; Limit-Order mit Limitpreis.
- Die Bracket-Beine sind `day`-Orders und verfallen zum Schluss: ein Grund mehr, bis 15:55 flat zu sein.
- `trader-broker flatten`: Solange Stop und Ziel des Brackets die Aktien „halten“, lehnt Alpaca einen neuen Verkauf ab. Erst die Beine mit `cancel_order_by_id` stornieren (Needs approval), dann verkaufen.
- Ein MOC-Ausstieg (`cls`) ist für Flat by 15:55 keine Option: Alpaca nimmt CLS-Orders nur bis 15:50 ET an. Der Ausstieg um 15:55 ist eine Market-Order im laufenden Handel.
- Die Time Machine zählt einen Gap durch den Stop als −1 R. In der Realität kann es mehr sein, siehe [[R-Multiple und Erwartungswert]] und [[Stop-Platzierung]].

## Quellen

- Alpaca Docs: Orders at Alpaca – https://docs.alpaca.markets/docs/orders-at-alpaca
- Alpaca Forum (Staff, 29.05.2024): Does a paid account give more accurate paper market fills? – https://forum.alpaca.markets/t/does-a-paid-account-give-more-accurate-paper-market-fills/14303
- FINRA: Stop Orders – Factors to Consider During Volatile Markets – https://www.finra.org/investors/insights/stop-orders-factors-consider-during-volatile-markets
- FINRA: Order Types – https://www.finra.org/investors/investing/investment-products/stocks/order-types
- FINRA Rule 5350: Stop Orders – https://www.finra.org/rules-guidance/rulebooks/finra-rules/5350
- FINRA Regulatory Notice 16-19 (Stop-Orders um Eröffnung und Schluss) – https://www.finra.org/rules-guidance/notices/16-19
- SEC/Investor.gov: Stop, Stop-Limit, and Trailing Stop Orders – https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15
- Skill-Doku `trader-broker`, `trader-budget`, `trader-risk`, `trader-timemachine` in `.claude/skills/`
