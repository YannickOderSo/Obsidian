---
typ: regeln
aktualisiert: 2026-10-21
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
| Budget | $5,000 |
| Max. Verlust je Trade | $50 |
| Max. Verlust je Tag | $150 |
| Max. Trades je Tag | 3 |
| Mindest-CRV | 1,0 |
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
