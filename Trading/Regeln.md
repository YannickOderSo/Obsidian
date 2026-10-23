---
typ: regeln
aktualisiert: 2026-10-22
tags:
  - trading
---

# Trading-Regeln

> [!warning] Keine Anlageberatung
> Die Skills lesen öffentliche Daten und rechnen. Die meisten Day Trader verlieren Geld. Erst mit Spielgeld üben.

## Limits

Startwerte aus `trader/config.json`. Ändern nur dort, dann diese Tabelle nachziehen.

| Regel | Wert |
| --- | --- |
| Konto | Paper Trading (`"paper": true`) |
| Budget | $100,000 (Paper-Konto) |
| Max. Verlust je Trade | $1,000 (1 %) |
| Max. Verlust je Tag | $2,500 |
| Max. Trades je Tag | 8 (seit 2026-10-22; Orders je Tag 20) |
| Mindest-CRV | 1,5 |
| Max. Position | 50 % des Budgets, höchstens $50,000 je Order (seit 2026-10-22, ohne Margin) |
| Stop Pflicht | ja |
| Einstiege | 9:45 bis 15:30 New York |
| Flat bis | 15:55 New York |
| Optionen, Margin, Leerverkauf | aus |

## Ablauf eines Trades

1. `/trader-scanner` findet Setups, `/trader-news` prüft die Nachrichten
2. `/trader-entry` meldet den Einstieg, `/trader-exit` setzt Stop und Ziel **vor** dem Einstieg
3. `/trader-timemachine` zeigt die ehrlichen Quoten
4. `/trader-budget` rechnet die Größe, `/trader-risk` prüft gegen die Limits
5. `/trader-broker` zeigt das Ticket, Order nur nach einem Ja für genau diese Order
6. `/trader-alerts` meldet Stop, Ziel und 15:55
7. Nach jedem Schritt `/trading-journal write`, am Ende `close`

## Eigene Regeln

Hier ergänzen, was sich aus [[Gedächtnis/Erkenntnisse/Trading]] ergibt.

- **Mindestschwelle** (2026-10-23): Kein Trade, wenn die Time Machine im Schnitt unter +0,05 R liegt oder dieselbe Regel in der Historie negativ war. Grenzfälle um null sind Münzwürfe mit Kosten.
- **Risiko abwägen statt ausreizen** (2026-10-22): $1,000 je Trade ist die Obergrenze, kein Ziel. Die Größe richtet sich nach der Qualität des Setups: volles Risiko nur, wenn die Time Machine einen positiven Durchschnitts-R zeigt und die News nicht dagegen sprechen, sonst die Hälfte oder gar nicht.
