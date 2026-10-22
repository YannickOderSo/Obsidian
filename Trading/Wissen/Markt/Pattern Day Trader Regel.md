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

# Pattern Day Trader Regel

Die frühere US-Regel, nach der man mit weniger als 25.000 $ im Margin-Konto höchstens drei Day Trades in fünf Tagen machen durfte, und was seit ihrer Abschaffung 2026 gilt. Stand der Recherche: 22. Oktober 2026.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

> [!success] Kurzfassung (Stand Oktober 2026)
> - Die **PDT-Regel ist abgeschafft.** Die SEC hat die Änderung von FINRA Rule 4210 am 14. April 2026 genehmigt, FINRA hat sie mit Regulatory Notice 26-10 (20. April 2026) zum **4. Juni 2026** in Kraft gesetzt.
> - Kein PDT-Status mehr, keine Zählung von Day Trades, keine 25.000-$-Mindestgrenze.
> - Ersetzt durch eine **Intraday-Margin-Regel**: Es zählt, ob das Konto im Tagesverlauf genug Sicherheiten hat, nicht wie oft gehandelt wird.
> - Broker dürfen die Umsetzung bis **20. Oktober 2027** strecken und eigene, strengere „House Rules“ haben.
> - **Alpaca** hat die PDT-Regel am 4. Juni 2026 entfernt.

## Die alte Regel (bis 3. Juni 2026)

FINRA Rule 4210 definierte einen **Pattern Day Trader** als Kunden, der in einem **Margin-Konto** innerhalb von fünf Geschäftstagen vier oder mehr Day Trades machte (sofern diese mehr als 6 % seiner Trades waren). Ein Day Trade war Kauf und Verkauf desselben Wertpapiers am selben Tag.

- Wer als PDT galt, musste mindestens **25.000 $ Eigenkapital** im Konto halten.
- Darunter wurde das Konto für Day Trades gesperrt (90 Tage oder bis zur Einzahlung).
- PDT-Konten bekamen eine „Day-Trading Buying Power“ von bis zu 4× des überschüssigen Kapitals.
- **Cash-Konten** waren nie betroffen, unterlagen aber den Settlement-Regeln (siehe unten).

Praktisch hieß das für kleine Konten wie das im Vault (5.000 $): höchstens drei Day Trades in fünf Tagen.

## Was seit 4. Juni 2026 gilt

FINRA hat die Day-Trading-Margin-Vorschriften „in ihrer Gesamtheit“ ersetzt, einschließlich des Zähltests und der 25.000-$-Grenze. Neu ist Rule 4210(d)(2), die **Intraday-Margin-Regel**:

| Element | Inhalt |
| --- | --- |
| Gilt für | Margin-Konten (nicht Good-Faith- und Portfolio-Margin-Konten) |
| Prüfung | An jedem Tag mit einer Transaktion, die die Intraday-Margin senkt (Kauf, Leerverkauf), ermittelt der Broker ein mögliches **Intraday Margin Deficit**. Echtzeitüberwachung ist nicht vorgeschrieben, eine Berechnung reicht |
| Ausgleich | „So schnell wie möglich“, durch Einzahlung oder Margin-Erhöhung; offen höchstens bis zum 15. Geschäftstag |
| Sanktion | Wer Defizite wiederholt nicht ausgleicht und eines bis zum 5. Geschäftstag offen lässt: **90 Tage** keine neuen Kredite oder Leerverkäufe |
| Bagatellgrenze | Defizite bis zum kleineren Betrag von 5 % des Eigenkapitals oder 1.000 $ zählen dafür nicht |
| Unverändert | Die normalen Maintenance-Margin-Vorschriften und Regulation T (2.000 $ Mindestkapital für Margin) |

**Übergang:** Inkraft am 4. Juni 2026; Mitglieder, die mehr Zeit brauchen, dürfen bis 20. Oktober 2027 schrittweise umsetzen. Die Notice sagt nicht ausdrücklich, ob ein Broker in dieser Zeit die alte PDT-Logik weiter anwenden darf; in der Praxis können Broker ohnehin strengere eigene Regeln haben.

## Alpaca

- Alpaca hat die PDT-Regel laut Blog (27. April 2026, aktualisiert 4. Juni 2026) **zum 4. Juni 2026** in Produktion entfernt, für Trading API und Broker API. Konten mit PDT-Sperre wurden freigegeben.
- Die API-Felder `pattern_day_trader`, `daytrade_count`, `daytrading_buying_power` u. a. sind veraltet und sollten bis 6. Juli 2026 entfernt werden; Ersatz ist `buying_power`.
- Statt Day-Trade-Buying-Power gibt es eine laufend berechnete **Intraday Buying Power**. Konten mit Hebel brauchen jetzt 2.000 $ statt 25.000 $ für 4× Intraday-Kaufkraft.
- Vorab-Prüfungen lehnen Orders ab, die das Konto in ein Margin-Defizit bringen würden.
- Alpaca behält sich eigene, auch kurzfristig geänderte House Requirements vor.

### Gilt das für Paper-Konten?

**Wahrscheinlich nein, aber nicht ausdrücklich bestätigt.**

- Früher galt die PDT-Sperre bei Alpaca ausdrücklich auch im Paper-Konto (ältere Fassung der Seite „User Protection“: dieselbe Schutzfunktion „triggers in your paper trading account“; im Alpaca-Forum wurde geraten, das Paper-Konto mit mehr als 25.000 $ neu anzulegen).
- Die aktuelle Seite „User Protection“ (aktualisiert 16.09.2026) führt keinen PDT-Schutz mehr, sondern verweist auf die Intraday-Margin-Regel. Die Paper-Trading-Seite (07.07.2026) erwähnt PDT gar nicht.
- Da Regel und API-Felder entfernt sind, spricht alles dafür, dass auch Paper-Konten nicht mehr zählen. Prüfen lässt sich das im eigenen Paper-Konto mit `get_account_info` (read only): Fehlen `pattern_day_trader` und `daytrade_count` (oder stehen sie auf false/0), ist die alte Logik weg.
- Rechtlich gilt FINRA 4210 ohnehin nur für echte Kundenkonten bei Broker-Dealern; ein Paper-Konto bewegt kein Geld.

## Cash-Konto: Was weiterhin gilt

Wer live ohne Margin handelt, war von PDT nie betroffen, ist aber an die Abwicklung gebunden. Seit 28. Mai 2024 werden US-Aktien in **T+1** abgewickelt, also am nächsten Geschäftstag.

- **Free Riding:** Kaufen und verkaufen, bevor der Kauf mit Geld bezahlt ist, verstößt gegen Regulation T. Folge: 90 Tage nur noch Käufe mit vorher eingezahltem Geld.
- **Good Faith Violation:** Mit noch nicht abgewickeltem Verkaufserlös kaufen und diese Position wieder verkaufen, bevor der Erlös abgewickelt ist.

Beispiel mit 5.000 $ im Cash-Konto: Trade 1 kauft für 2.913 $ und verkauft am selben Tag. Der Erlös ist erst am nächsten Geschäftstag abgewickelt. Für Trade 2 am selben Tag stehen nur die restlichen 2.087 $ abgewickeltes Geld zur Verfügung. Mit den Vault-Limits (max. 4.000 $ je Order, 10 % Cash-Puffer) reicht das oft für einen, selten für drei volle Trades am Tag.

> [!warning] Weniger Regel heißt nicht weniger Risiko
> Die PDT-Grenze hat kleine Konten vor allem vor zu vielen Trades geschützt. Die Vault-Regeln (max. 3 Trades und 150 $ Verlust je Tag) übernehmen diese Bremse jetzt allein. Siehe [[Tageslimits und Regelwerk]] und [[Wie viele Day Trader gewinnen]].

## Im Vault

- `trader/config.json` hat `"pdt_guard": false`. Das ist nach heutigem Stand passend: Alpaca wendet die Regel nicht mehr an.
- `trader-risk` beschreibt den Schalter: Mit `pdt_guard: true` blockiert es neue Einstiege, wenn in den letzten fünf Geschäftstagen schon drei Day Trades geloggt sind. Die Skill-Doku nennt dieselben Daten (Notice 26-10, 4. Juni 2026, Übergang bis 20. Oktober 2027). Einschalten nur, falls ein anderer Broker die alte Regel noch anwendet; ändern nur auf Wunsch des Nutzers.
- `max_trades_per_day: 3` begrenzt die Zahl der Trades unabhängig von PDT.
- Margin, Leerverkauf und Optionen sind aus (`allow_margin`, `allow_short`, `allow_options` false); die Intraday-Margin-Regel betrifft den Vault daher praktisch nicht.

## Quellen

- FINRA Regulatory Notice 26-10 (20.04.2026) – https://www.finra.org/rules-guidance/notices/26-10
- FINRA Regulatory Notice 26-10 (PDF) – https://www.finra.org/sites/default/files/2026-04/Regulatory-Notice-26-10.pdf
- FINRA Rule 4210 (Margin Requirements) – https://www.finra.org/rules-guidance/rulebooks/finra-rules/4210
- FINRA: Interpretations of Rule 4210 (gültig ab 4. Juni 2026) – https://www.finra.org/rules-guidance/guidance/interps-4210-202606
- FINRA: Frequent Intraday Trading – Understanding the Basics (04.06.2026) – https://www.finra.org/investors/investing/investment-products/stocks/day-trading
- WilmerHale (23.04.2026): SEC Approves Amendments to FINRA Rule 4210 – https://www.wilmerhale.com/en/insights/client-alerts/20260423-sec-approves-amendments-to-finra-rule-4210-replacing-day-trading-margin-requirements-with-a-modernized-intraday-margin-standard
- Alpaca Blog (27.04.2026, akt. 04.06.2026): FINRA Retires the PDT Rule – https://alpaca.markets/blog/finra-retires-the-pdt-rule-introducing-alpacas-new-intraday-margin-framework/
- Alpaca Docs: The Intraday Margin Rule – https://docs.alpaca.markets/us/docs/the-intraday-margin-rule
- Alpaca Docs: Intraday Margin Rule for Non-Leverage Margin Accounts – https://docs.alpaca.markets/us/docs/intraday-margin-rule-for-non-leverage-margin-accounts
- Alpaca Docs: Paper Trading – https://docs.alpaca.markets/docs/paper-trading
- FINRA: Understanding Settlement Cycles (T+1) – https://www.finra.org/investors/insights/understanding-settlement-cycles
- Investor.gov: Freeriding – https://www.investor.gov/introduction-investing/investing-basics/glossary/freeriding
- Investor.gov: Pattern Day Trader (Glossar, alte Definition mit 6-%-Test) – https://www.investor.gov/introduction-investing/investing-basics/glossary/pattern-day-trader
- SEC: New T+1 Settlement Cycle – What Investors Need to Know – https://www.sec.gov/oiea/investor-alerts-and-bulletins/new-t1-settlement-cycle-what-investors-need-know-investor
- Alpaca Docs: User Protection (aktuell, ohne PDT) – https://docs.alpaca.markets/docs/user-protection
- Alpaca Docs v1.1: User Protection (alte Fassung, PDT auch im Paper-Konto) – https://docs.alpaca.markets/us/v1.1/docs/user-protection
- Alpaca Forum: Paper trading pattern day trading restriction – https://forum.alpaca.markets/t/paper-trading-pattern-day-trading-restriction/13795
