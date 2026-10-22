---
typ: wissen
erstellt: 2026-10-22
aktualisiert: 2026-10-22
quelle: Recherche
tags:
  - trading
  - wissen
  - risiko
---

# Positionsgröße

Die Positionsgröße entscheidet, wie viel ein Trade kostet, wenn er schiefgeht. Diese Notiz erklärt, wie man die Stückzahl aus dem Stop rechnet statt aus dem Bauchgefühl, und wie `/trader-budget` das mit unseren Limits ($5.000 Budget, $50 Max-Verlust je Trade) macht.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Grundidee: der Stop bestimmt die Größe

Die zentrale Gleichung des Risikomanagements:

> **Risiko je Trade = Stückzahl × (Einstieg − Stop)**

Umgestellt nach der Stückzahl:

> **Stückzahl = Max-Verlust ÷ (Einstieg − Stop)**, abgerundet auf ganze Aktien

Daraus folgt das Wichtigste der ganzen Notiz: **Erst der Stop, dann die Größe.** Wer zuerst „100 Aktien“ festlegt und dann einen Stop sucht, der zu den 100 Aktien passt, setzt den Stop nach dem Geldbeutel statt nach dem Chart. `/trader-exit` setzt den Stop deshalb vor allem anderen, `/trader-budget` rechnet erst danach (siehe [[Stop-Platzierung]]).

Je weiter der Stop weg ist, desto weniger Aktien. Das Risiko in Dollar bleibt gleich, egal ob die Aktie $8 oder $400 kostet.

## Verfahren im Überblick

| Verfahren | Regel | Vorteil | Nachteil |
| --- | --- | --- | --- |
| Feste Stückzahl | immer 100 Aktien | einfach | Risiko schwankt mit Preis und Stop-Abstand völlig unkontrolliert |
| Fester Dollarbetrag | immer $2.000 Positionswert | einfach | ein enger und ein weiter Stop riskieren ganz verschieden viel |
| **Fester Dollar-Verlust** (unser System) | immer höchstens $50 bis zum Stop | jeder Verlust ist gleich groß, R wird vergleichbar | wächst nicht mit dem Konto |
| **Fixed Fractional** | immer x % des aktuellen Kontos bis zum Stop, z. B. 1 % | passt sich an Gewinne und Verluste an | nach Verlusten kleinere Positionen, Erholung dauert länger |
| Volatilitätsbasiert | Stop = k × ATR, Größe daraus | berücksichtigt, wie stark die Aktie schwankt | ATR ist eine Schätzung aus der Vergangenheit |
| Kelly | Anteil aus Trefferquote und CRV | maximiert langfristiges Wachstum, wenn die Zahlen stimmen | die Zahlen stimmen fast nie, siehe [[Kelly-Kriterium]] |

**Fixed Fractional** heißt: Man riskiert je Trade einen festen Bruchteil des aktuellen Kontos. Bei 1 % und $5.000 sind das $50, nach einem Rückgang auf $4.500 nur noch $45. Unser System nutzt einen **festen Dollar-Betrag** (`max_loss_per_trade_usd: 50`), der bei Start genau 1 % des Budgets ist. Er bleibt bei $50, bis der Nutzer ihn in `trader/config.json` ändert. Der Unterschied ist bei kleinen Verlusten gering, bei einem großen Drawdown aber spürbar: Fixed Fractional bremst automatisch, ein fester Betrag nicht (Simulation in [[Drawdown und Risk of Ruin]]).

> [!tip] Faustregel aus der Praxis
> Die „1-%-Regel“ (höchstens 1 %, selten bis 2 % des Kontos je Trade riskieren) ist in Trading-Ratgebern verbreitet ([Pepperstone](https://pepperstone.com/en-gb/analysis/trading-guides/one-percent-rule-in-day-trading/), [Trade That Swing](https://tradethatswing.com/the-1-risk-rule-for-day-trading-and-swing-trading/)); 1 % entspricht unseren $50. Das ist Praktiker-Konvention, keine bewiesene Optimalzahl. Was zu viel ist, zeigt die Mathematik in [[Kelly-Kriterium]] und [[Drawdown und Risk of Ruin]]: Bei 5 bis 10 % je Trade führen schon normale Verlustserien zu Drawdowns von 50 % und mehr.

## Wie /trader-budget rechnet

`/trader-budget` liest `trader/plan.json` (Einstieg, Stop, Ziel) und `trader/config.json` und nimmt das **Minimum aus vier Grenzen**, immer ganze Aktien:

| Grenze | Formel | Config-Wert |
| --- | --- | --- |
| Max-Verlust | `max_loss_per_trade_usd` ÷ (Einstieg − Stop) | $50 |
| Positionsdeckel | Budget × `max_position_pct` ÷ Einstieg | 75 % von $5.000 = $3.750 |
| Max-Order | `max_order_usd` ÷ Einstieg | $4.000 |
| Cash | (Budget − Cash-Puffer) ÷ Einstieg | $5.000 − 10 % = $4.500 |

Das Skill sagt, welche Grenze entschieden hat. Es rechnet mit dem höheren Wert aus geplantem Einstieg und frischem Kurs aus `trader/prices.json` (jünger als 15 Minuten): Ist der Kurs seit dem Plan gestiegen, wird das Risiko je Aktie größer und die Stückzahl kleiner. Es verweigert die Order, wenn null Aktien herauskommen, das CRV unter `min_reward_risk` fällt oder der Stop zu weit weg ist. Es verkleinert nie den Stop, um mehr Aktien unterzubringen.

## Beispielrechnungen mit unseren Limits

**A) TSLA, das Beispiel aus dem Skill.** Einstieg 364,18, Stop 358,32 (Mitte der Opening Range), Risiko 5,86 je Aktie.

| Grenze | Rechnung | Aktien |
| --- | --- | --- |
| Max-Verlust | 50 ÷ 5,86 = 8,5 | **8 (entscheidet)** |
| Positionsdeckel | 3.750 ÷ 364,18 | 10 |
| Max-Order | 4.000 ÷ 364,18 | 10 |
| Cash | 4.500 ÷ 364,18 | 12 |

8 Aktien = $2.913,44 Positionswert, Verlust am Stop 8 × 5,86 = **$46,88**. Kostet der Kurs beim Absenden schon 366,48, wird mit 8,16 je Aktie gerechnet: nur noch 6 Aktien, und das CRV fällt auf 0,44, also Ablehnung.

**B) $20-Aktie, Stop 2 % unter dem Einstieg.** Einstieg 20,00, Stop 19,60, Risiko 0,40.
Max-Verlust: 50 ÷ 0,40 = 125 Aktien. Deckel: 3.750 ÷ 20 = 187. Max-Order: 200. Cash: 225.
→ **125 Aktien**, $2.500 Positionswert, Verlust am Stop $50,00.

**C) Enger Stop: der Deckel entscheidet.** Einstieg 50,00, Stop 49,90, Risiko 0,10.
Max-Verlust: 500 Aktien. Deckel: 3.750 ÷ 50 = **75 Aktien** (entscheidet). Verlust am Stop nur $7,50.
Ein sehr enger Stop „erlaubt“ rechnerisch riesige Positionen. Der Positionsdeckel verhindert, dass ein Gap oder Halt, der weit über den Stop springt, das Konto trifft (siehe [[Handelsstopps und LULD]]).

**D) Zu weiter Stop: keine Order.** Einstieg 400,00, Stop 340,00, Risiko 60,00 je Aktie. Schon eine Aktie riskiert mehr als $50 → `/trader-budget` lehnt ab. Die Lösung ist ein näherer, sinnvoller Stop aus `/trader-exit` oder eine andere Aktie, nie ein Stop, der nur wegen der Größe enger gesetzt wird.

**E) Billige Aktie.** Einstieg 8,00, Stop 7,80, Risiko 0,20 → 250 Aktien, $2.000. Bei billigen Aktien ist der Spread im Verhältnis zum Risiko oft groß; das frisst R, siehe [[R-Multiple und Erwartungswert]] und [[Spread Liquidität und Slippage]].

## Was die Rechnung nicht abdeckt

> [!warning] Der Stop ist ein Plan, kein Preis
> Ein Stop wird bei Alpaca zur Market-Order, sobald der Stop-Preis gehandelt wird. Der Fill kann darunter liegen, in schnellen Märkten oder bei Halts deutlich ([Alpaca: Orders](https://docs.alpaca.markets/docs/orders-at-alpaca), [SEC/Investor.gov: Stop-Orders](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14)). Bei 8 TSLA-Aktien macht ein Fill $0,50 unter dem Stop $4 mehr Verlust: $50,88 statt $46,88. Der Max-Verlust ist also ein **geplanter** Verlust.

- **Ganze Aktien und Abrunden**: Der tatsächliche Max-Verlust liegt meist etwas unter $50 (Beispiel A: $46,88).
- **Gebühren**: Bei Alpaca keine Kommission für US-Aktien, aber SEC-Gebühr und FINRA TAF auf Verkäufe. Seit 4. April 2026 beträgt die SEC-Gebühr $20,60 je Million Dollar Verkaufswert, die TAF $0,000195 je verkaufter Aktie ([SEC Fee Rate Advisory 2026-2](https://www.sec.gov/rules-regulations/fee-rate-advisories/2026-2), [Investrade zur TAF 2026](https://investrade.com/commissions-fees/)). Für 8 TSLA-Aktien sind das wenige Cent. Paper Trading rechnet diese Gebühren gar nicht ein ([Alpaca: Paper Trading](https://docs.alpaca.markets/docs/paper-trading)).
- **Korrelation**: Drei Trades am selben Tag in drei Tech-Aktien sind fast ein großer Trade. Die Limits zählen sie getrennt.
- **Tageslimit**: Drei volle Trades à $50 Risiko füllen das Tageslimit von $150 genau aus, siehe [[Tageslimits und Regelwerk]].

## Im Vault

- **`/trader-exit`** setzt Stop und Ziel und schreibt `trader/plan.json`. Ohne Plan keine Größe.
- **`/trader-budget`** rechnet die Größe nach den vier Grenzen oben und schreibt *eine* Bracket-Order nach `trader/orders.json`. Sie wird nie platziert, nur vorgeschlagen.
- **`/trader-risk`** prüft die Größe noch einmal unabhängig: `qty × (Einstieg − Stop)` gegen `max_loss_per_trade_usd`, gemessen vom höheren Wert aus Plan-Einstieg und frischem Kurs. Eine Aktie zu viel (9 statt 8 TSLA = $52,74) ist ein BLOCK.
- **`/trading-journal`** speichert `stueck`, `max_verlust` und `risiko_je_aktie` in der Trade-Notiz.
- Grenzen der Skills: Sie kennen keine Korrelation zwischen Positionen und kein Gap-Risiko über den Stop hinaus. Werte in `trader/config.json` ändert nur der Nutzer.

## Quellen

- Day-Trader-Skills im Vault: `.claude/skills/trader-budget/SKILL.md`, `trader-exit/SKILL.md`, `trader-risk/SKILL.md` (Formeln, Grenzen, TSLA-Beispiel)
- [Alpaca Docs: Orders at Alpaca](https://docs.alpaca.markets/docs/orders-at-alpaca) – Stop wird Market-Order, Fill kann schlechter sein; Bracket-Regeln
- [Alpaca Docs: Paper Trading](https://docs.alpaca.markets/docs/paper-trading) – keine Gebühren, kein Slippage-Modell
- [Investor.gov: Stop, Stop-Limit und Trailing-Stop-Orders](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14)
- [SEC Fee Rate Advisory 2026-2](https://www.sec.gov/rules-regulations/fee-rate-advisories/2026-2) – $20,60 je Million ab 4. April 2026
- [Investrade: Commissions & Fees](https://investrade.com/commissions-fees/) – FINRA TAF $0,000195 je Aktie ab 1. Januar 2026 (Sekundärquelle)
- [MacLean, Thorp, Ziemba (2010): Good and bad properties of the Kelly criterion](https://www.stat.berkeley.edu/~aldous/157/Papers/Good_Bad_Kelly.pdf) – zu großer Einsatz senkt Wachstum und erhöht Risiko
- [Pepperstone: The Significance of the 1% Rule in Day Trading](https://pepperstone.com/en-gb/analysis/trading-guides/one-percent-rule-in-day-trading/) und [Trade That Swing: The 1% Risk Rule](https://tradethatswing.com/the-1-risk-rule-for-day-trading-and-swing-trading/) – Praktiker-Konvention, keine Studie
- Beispielrechnungen B bis E: eigene Rechnung mit den Werten aus `trader/config.json`
