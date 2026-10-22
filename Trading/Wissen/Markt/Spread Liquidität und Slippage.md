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

# Spread Liquidität und Slippage

Was ein Trade wirklich kostet, auch ohne Kommission: der Abstand zwischen Bid und Ask, die Abweichung des Fills vom Plan und die Gebühren. Umgerechnet in R, weil das die Einheit ist, in der die Skills planen.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Begriffe

| Begriff | Bedeutung |
| --- | --- |
| **Bid** | Höchster Preis, zu dem gerade jemand kaufen will. Dort verkauft eine Market-Order |
| **Ask** | Niedrigster Preis, zu dem gerade jemand verkaufen will. Dort kauft eine Market-Order |
| **NBBO** | National Best Bid and Offer: bester Bid und bester Ask über alle US-Börsen |
| **Spread** | Ask minus Bid. Quoted Spread = was man sieht; Effective Spread = was man tatsächlich zahlt (Fill gegen Mittelkurs) |
| **Mittelkurs** | (Bid + Ask) / 2, der „faire“ Preis im Moment |
| **Slippage** | Fill minus geplanter Preis (beim Kauf), geplanter Preis minus Fill (beim Verkauf) |
| **Liquidität** | Wie viel man handeln kann, ohne den Preis zu bewegen: Tiefe des Orderbuchs, Volumen |
| **Tick** | Kleinster Preisschritt: 0,01 $ ab 1 $, darunter 0,0001 $ |

Der Mindest-Spread ist ein Tick, also 1 Cent. Die SEC hat 2024 einen Halb-Cent-Tick für sehr enge Aktien beschlossen; die Umsetzung wurde im Juni 2026 erneut verschoben, auf November 2027. Bis dahin bleibt es bei 1 Cent.

## Was ein Round Trip kostet

Kauf mit Market-Order am Ask, Verkauf mit Market-Order am Bid: Man verliert **einen ganzen Spread**, bevor sich der Kurs überhaupt bewegt hat. Dazu kommt Slippage, vor allem beim Stop (siehe [[Ordertypen]]).

**Kosten in R** = (Spread + erwartete Slippage) / Risiko je Aktie

Das Risiko je Aktie ist der Abstand Einstieg–Stop. Je enger der Stop, desto teurer wird derselbe Spread in R.

### Beispiel 1: Large Cap, weiter Stop

TSLA-Plan der Skills: Risiko 5,86 $ je Aktie, 8 Aktien.

| Annahme | Kosten je Aktie | Kosten gesamt | in R |
| --- | --- | --- | --- |
| Spread 0,05 $ | 0,05 $ | 0,40 $ | 0,009 R |
| + 0,10 $ Slippage am Stop | 0,15 $ | 1,20 $ | 0,026 R |

Kaum spürbar. Die Spread-Annahme ist ein Rechenbeispiel, keine gemessene Zahl: Den echten Spread vor dem Trade aus dem Quote ablesen.

### Beispiel 2: Billige Aktie, enger Stop

Aktie zu 3,00 $, Opening Range 2,96–3,02, Stop 0,06 $ unter dem Einstieg. Max. Verlust 50 $ → 50 / 0,06 = **833 Aktien** = 2.499 $.

| Annahme | Kosten je Aktie | Kosten gesamt | in R |
| --- | --- | --- | --- |
| Spread 0,02 $ | 0,02 $ | 16,66 $ | **0,33 R** |
| + 0,02 $ Slippage am Stop | 0,04 $ | 33,32 $ | **0,67 R** |

Hier frisst der Spread ein Drittel des Risikos, bevor etwas passiert ist. Bei einem Stop-Fill kostet der Trade dann fast 1,7 R statt 1 R.

### Was das für die Trefferquote heißt

Bei einem 1R-Ziel und Kosten c (in R) gewinnt ein Treffer 1 − c und ein Verlust kostet 1 + c. Break-even liegt dann bei:

**Trefferquote = (1 + c) / 2**

| Kosten c | nötige Trefferquote bei 1R-Ziel |
| --- | --- |
| 0 R | 50,0 % |
| 0,03 R | 51,5 % |
| 0,10 R | 55,0 % |
| 0,33 R | 66,5 % |

Mehr dazu in [[R-Multiple und Erwartungswert]].

## Gebühren

Laut Alpaca-Gebührenverzeichnis (Stand 17.09.2026):

- **Kommission:** keine für selbst gesteuerte Konten, die US-Aktien über die API handeln (Ausnahmen: Index-Optionen, Elite Smart Router, nicht-retail Orderflow).
- **SEC-Gebühr (Section 31):** nur auf Verkäufe, 0,0000206 × Verkaufswert, also **20,60 $ je 1 Mio. $** (gilt seit 4. April 2026, davor 0 $).
- **FINRA TAF:** nur auf Verkäufe, **0,000195 $ je Aktie**, höchstens 9,79 $ je Trade.
- **CAT-Gebühr:** 0,000003 $ je Aktie, auf Käufe und Verkäufe.
- Alpaca bucht die Gebühren am Tagesende und rundet auf den Cent **auf**.

Beispiel: 8 TSLA zu 370 $ verkauft = 2.960 $ → SEC 0,06 $, TAF 0,0016 $. Gebühren sind bei diesen Größen Cent-Beträge; der Spread und die Slippage sind die echten Kosten.

## Liquidität und Mindestvolumen

- **Tageszeit:** Spreads sind direkt nach der Eröffnung am breitesten und fallen danach (McInish/Wood 1992). Die Vault-Regel „Einstiege erst ab 9:45“ meidet die teuerste Phase.
- **Ordergröße:** Bei 5.000 $ Budget sind die Positionen winzig gegenüber dem Volumen liquider Aktien. Marktauswirkung spielt dort praktisch keine Rolle, wohl aber bei sehr dünnen Titeln.
- **Faustregeln aus der Praxis** (nicht wissenschaftlich belegt): Tagesvolumen von mindestens 1 Mio. Aktien, Kurs über 5 $, Spread unter etwa 0,1 R. Die ersten beiden sind die Standardfilter des Scanners.

> [!warning] Small Caps und Penny Stocks
> Billige, wenig gehandelte Aktien haben breite Spreads, dünne Orderbücher, häufigere Handelsstopps und breitere LULD-Bänder (Tier 2: 10 % über 3 $, 20 % zwischen 0,75 $ und 3 $; siehe [[Handelsstopps und LULD]]). Genau dort sehen Gap-and-Go-Setups oft am spektakulärsten aus, siehe [[Momentum und Gap and Go]]. Im Paper-Konto wirken sie außerdem besser, als sie sind, weil Alpaca die Ordergröße nicht gegen das Angebot am Quote prüft.

> [!tip] Kosten realistisch einrechnen
> 1. Vor dem Trade Bid/Ask ansehen (Alpaca `get_stock_latest_quote`) und den Spread durch das Risiko je Aktie teilen.
> 2. Über 0,1 R: Trade überdenken oder einen weiteren Stop mit weniger Aktien wählen.
> 3. Nach dem Trade im Journal den geplanten Preis mit dem Fill vergleichen. Über 20–30 Trades ergibt das die eigene, echte Slippage.
> 4. Die Quoten der Time Machine um diese Kosten nach unten korrigieren.

## Im Vault

- `trader-scanner`: `--min-price 5` und `--min-volume 1000000` für den Tages-Scan; im ORB-Scan ist das Mindestvolumen 0, dort sortiert er nach Kurs × Volumen.
- `trader-exit` lehnt einen Stop ab, dessen Risiko unter 0,05 % des Kurses liegt, „too tight to survive the spread“. Das ist eine Untergrenze, keine Kostenprüfung: Bei 3 $ sind 0,05 % nur 0,0015 $.
- `trader-timemachine` rechnet ohne Spread und Slippage und zählt einen Gap durch den Stop als −1 R. Seine Quoten sind daher eher zu gut.
- `trader-risk` misst das Risiko vom höheren Wert aus Plan und frischem Kurs, berücksichtigt aber keinen Spread.
- Das Journal (`trading-journal`) rechnet R vom echten Fill, sobald er erfasst ist. So wird Slippage sichtbar. Siehe [[Positionsgröße]] und [[Volumen und relatives Volumen]].

## Quellen

- Alpaca Docs: Orders at Alpaca (Preisschritte, Market-Orders) – https://docs.alpaca.markets/docs/orders-at-alpaca
- Alpaca Docs: Regulatory Fees – https://docs.alpaca.markets/docs/regulatory-fees
- Alpaca Securities: Brokerage Fee Schedule (revidiert 17.09.2026) – https://files.alpaca.markets/disclosures/BrokFeeSched.pdf
- Alpaca Support: Will I incur commission or clearing fees with Alpaca? – https://alpaca.markets/support/commission-clearing-fees
- Alpaca Docs: Paper Trading – https://docs.alpaca.markets/docs/paper-trading
- SEC: Fee Rate Advisory 2026-2 (Section 31, 20,60 $ je Mio. ab 04.04.2026) – https://www.sec.gov/rules-regulations/fee-rate-advisories/2026-2
- FINRA Information Notice 17.03.2026 – https://www.finra.org/rules-guidance/notices/information-notice-20260317
- SEC (11.06.2026): Statement von Chairman Atkins zu Minimum Pricing Increments und Access Fee Caps – https://www.sec.gov/newsroom/speeches-statements/atkins-statement-minimum-pricing-increments-access-fee-caps-061126
- SEC Pressemitteilung 2024-137 (Tick-Größen, Access Fees) – https://www.sec.gov/newsroom/press-releases/2024-137
- McInish, Wood (1992): An Analysis of Intraday Patterns in Bid/Ask Spreads for NYSE Stocks, Journal of Finance 47(2) – https://doi.org/10.1111/j.1540-6261.1992.tb04408.x
- LULD Plan – https://www.luldplan.com/
- Skill-Doku `trader-scanner`, `trader-exit`, `trader-timemachine`, `trader-risk` in `.claude/skills/`
