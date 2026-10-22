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

# Handelsstopps und LULD

Wann der Handel in einer einzelnen Aktie oder im ganzen Markt angehalten wird: Limit Up/Limit Down (LULD), die marktweiten Circuit Breaker, News-Halts und kurz die Short-Sale-Regel 201. Für einen Day Trader wichtig, weil ein Halt den Stop wirkungslos macht, bis wieder gehandelt wird.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

## Limit Up/Limit Down (LULD)

Der LULD-Plan verhindert Trades außerhalb eines Preisbands um einen gleitenden Referenzpreis. Er gilt für alle NMS-Aktien und ETPs (außer Rechten und Optionsscheinen) von 9:30 bis 16:00 ET.

**Referenzpreis:** Mittelwert der Trades der letzten 5 Minuten. Er wird nur aktualisiert, wenn er sich um mindestens 1 % bewegt.

**Tiers:**
- **Tier 1:** Aktien im S&P 500 und Russell 1000 sowie ausgewählte ETPs
- **Tier 2:** alle übrigen NMS-Aktien

### Bandbreiten

Maßgeblich ist der Schlusskurs des Vortags; die Prozentzahl ändert sich im Tagesverlauf nicht, wenn der Kurs eine Preisgrenze kreuzt.

| Schlusskurs Vortag | Tier 1 | Tier 2 |
| --- | --- | --- |
| über 3,00 $ | 5 % | 10 % |
| 0,75 $ bis 3,00 $ | 20 % | 20 % |
| unter 0,75 $ | kleiner von 0,15 $ oder 75 % | kleiner von 0,15 $ oder 75 % |

**Verdopplung:** In den letzten 25 Minuten (15:35–16:00 ET) werden die Bänder für Tier 1 und für Tier-2-Aktien bis 3,00 $ verdoppelt (also 10 %, 40 % usw.). Tier-2-Aktien über 3 $ bleiben bei 10 %.

> [!info] Alte Angaben im Netz
> Viele Seiten nennen noch eine Verdopplung auch in den ersten 15 Minuten (9:30–9:45). Der aktuelle Plan (luldplan.com) und die Nasdaq-FAQ (Stand Februar 2026) nennen nur die letzten 25 Minuten.

### Ablauf

1. Der Kurs erreicht das Band: Es wird nicht außerhalb gehandelt, aber am Band.
2. Steht der beste Quote 15 Sekunden am Band, ohne dass der Kurs zurückkommt (**Limit State**), folgt eine **Trading Pause von 5 Minuten**, die um weitere 5 Minuten verlängert werden kann.
3. Wiedereröffnung über eine Auktion der Heimatbörse. Der Eröffnungskurs kann weit vom letzten Kurs entfernt sein.

### Beispiel

Aktie mit Vortagesschluss 20 $ (Tier 2), Referenzpreis um 10:30 bei 22,00 $. Band: 19,80 $ bis 24,20 $ (±10 %). Bei derselben Aktie in Tier 1 wären es 20,90 $ bis 23,10 $ (±5 %). Ein Long mit Stop bei 21,50 $ ist bei einem Absturz innerhalb weniger Sekunden nicht vor 20,90 $ (Tier 1) bzw. 19,80 $ (Tier 2) „geschützt“: Erreicht der Kurs das Band und bleibt dort, wird pausiert, und der Stop füllt erst nach der Wiedereröffnung.

## Marktweite Circuit Breaker (MWCB)

Gemessen am **S&P 500** gegen den Schluss des Vortags:

| Stufe | Rückgang | Folge vor 15:25 ET | ab 15:25 ET |
| --- | --- | --- | --- |
| Level 1 | 7 % | 15 Minuten Pause, ganzer Markt | kein Halt |
| Level 2 | 13 % | 15 Minuten Pause | kein Halt |
| Level 3 | 20 % | Handel für den Rest des Tages beendet | Handel beendet |

Bekanntestes Beispiel nach dem heutigen System (seit 2013): Level 1 wurde im März 2020 an vier Tagen ausgelöst (9., 12., 16. und 18. März), dreimal davon in der ersten Handelsstunde. Für einen Trader, der bis 15:55 flat sein will, heißt das: An einem solchen Tag kann ein Ausstieg 15 Minuten unmöglich sein.

## News-Halts und andere Stopps

Die Heimatbörse kann den Handel in einer Aktie anhalten, etwa wenn wesentliche Nachrichten bevorstehen. Die Gründe stehen als Codes in den Halt-Listen der Börsen (Nasdaq Trader „Trading Halts“):

| Code | Bedeutung |
| --- | --- |
| **T1** | News pending: wesentliche Nachricht steht aus |
| **T2** | News released: Nachricht wird verbreitet |
| **T12** | Börse verlangt weitere Informationen vom Unternehmen |
| **H10** | SEC hat den Handel ausgesetzt |
| **LUDP** | LULD-Volatilitätspause |
| **MWC1–3** | Marktweiter Circuit Breaker |
| **T3** | Wiederaufnahme: zuerst Zeitpunkt für Quotes, dann für Trades |

News-Halts dauern unterschiedlich lange, von Minuten bis zu Tagen (eine SEC-Aussetzung nach H10 dauert bis zu 10 Handelstage, und danach läuft der Handel nicht automatisch wieder an). Der Auslöser ist meist eine wesentliche Unternehmensnachricht; was danach passiert, ist nicht vorhersehbar. Siehe [[Katalysatoren]] und [[News richtig lesen]].

> [!warning] Was ein Halt mit dem Stop macht
> Während eines Halts füllt keine Order. Der Bracket-Stop bleibt liegen und füllt nach der Wiedereröffnung zum ersten handelbaren Preis, der weit unter dem Stop liegen kann. Alpaca nennt Trading Halts ausdrücklich als Grund für Fills schlechter als der Stop-Preis. Beispielrechnung in [[Ordertypen]]: Aus geplanten 46,88 $ können so 97,44 $ werden.

## Short-Sale-Regel 201 (SSR)

Fällt eine Aktie um **10 % oder mehr** gegen den Vortagesschluss, dürfen Leerverkäufe für den Rest des Tages und den **ganzen nächsten Handelstag** nur noch über dem aktuellen besten Bid ausgeführt werden (Alternative Uptick Rule, SEC 2010). Für den Vault nur als Information wichtig: Leerverkauf ist aus (`allow_short: false`). Eine SSR-Markierung zeigt aber, dass die Aktie stark gefallen ist, was im Scanner bei Oversold-Setups auftauchen kann (siehe [[Mean Reversion und Oversold Bounce]]).

## Im Vault

- Kein Skill erkennt einen laufenden Halt. `trader-alerts` sieht nur, dass der Kurs sich nicht bewegt; `trader-news` kann Halt-Meldungen als „halt“ taggen, wenn sie in den Schlagzeilen stehen.
- Bei Tier-2-Aktien und billigen Aktien sind die Bänder weiter, Pausen kommen häufiger vor. Der Scanner filtert standardmäßig Aktien unter 5 $ heraus (`--min-price 5`), was die 20-%-Klasse vermeidet.
- Die Verdopplung der Bänder ab 15:35 fällt in die letzte halbe Stunde, in der der Vault nur noch Ausstiege erlaubt (Einstiege bis 15:30, Flat by 15:55).
- Ein Halt ist der Hauptgrund, warum der maximale Verlust je Trade (50 $) überschritten werden kann. Das Tageslimit von 150 $ in `trader-risk` rechnet mit den geplanten Verlusten am Stop, nicht mit den tatsächlichen.
- Die Time Machine kennt keine Halts. Siehe [[Stop-Platzierung]] und [[Drawdown und Risk of Ruin]].

## Quellen

- LULD Plan: Overview (Tiers, Bänder, Verdopplung, Limit State) – https://www.luldplan.com/
- Nasdaq: Limit Up-Limit Down – Frequently Asked Questions (PDF, Stand Feb. 2026) – https://m.nasdaqtrader.com/content/MarketRegulation/LULD_FAQ.pdf
- SEC: Investor Bulletin – New Measures to Address Market Volatility – https://www.sec.gov/investor/alerts/circuitbreakersbulletin.htm
- FINRA: Guardrails for Market Volatility – https://www.finra.org/investors/insights/guardrails-market-volatility
- Nasdaq Trader: Trading Halt Codes – https://www.nasdaqtrader.com/Trader.aspx?id=TradeHaltCodes
- SEC: Trading Suspensions – https://www.sec.gov/enforcement-litigation/trading-suspensions
- World Economic Forum (03/2020): Mad March – how the stock market is being hit by COVID-19 – https://weforum.org/stories/2020/03/stock-market-volatility-coronavirus
- moomoo Learn: What is Circuit Breakers? (Liste der MWCB-Auslösungen) – https://www.moomoo.com/us/learn/what-is-circuit-breakers
- SEC Pressemitteilung 2010-26: SEC Approves Short Selling Restrictions (Rule 201) – https://www.sec.gov/news/press/2010/2010-26.htm
- SEC: Final Rule Release 34-61595 (Regulation SHO, Rule 201) – https://www.sec.gov/rules/final/2010/34-61595-secg.htm
- Alpaca Docs: Orders at Alpaca (Stops bei Gaps und Halts) – https://docs.alpaca.markets/docs/orders-at-alpaca
