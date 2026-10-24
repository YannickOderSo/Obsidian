---
typ: wissen
erstellt: 2026-10-24
aktualisiert: 2026-10-24
quelle: Recherche
tags:
  - trading
  - wissen
  - funded
---

# Funded Accounts

Antwort auf [[Yannick]]s Frage vom 2026-10-23: Wie kaufe ich eine Challenge („Lizenz“), wo geht das, und wie verbinde ich den Bot aus diesem Repo damit? Recherchiert am 23./24.10.2026 auf Basis des echten Bots (Autopilot mit `paper_auto.py`, US-Aktien, nur long, ORB über Alpaca Paper). Ergänzt die geprüfte Gemini-Recherche [[Prop-Firms und Bot-Architektur]]. Zurück: [[Trading/Wissen/Übersicht]].

> [!warning] Keine Anlage-, Steuer- oder Rechtsberatung
> Regeln und Preise der Firmen ändern sich laufend. Vor jedem Kauf die Seite der Firma lesen und die Bot-Frage schriftlich klären. Bis Yannick anders entscheidet, gilt [[Trading/Regeln]]: autonom nur Paper, mit Geld ein Ja je Order.

## Kurz gesagt

1. **Wie:** Man kauft online eine Prüfung auf einem simulierten Konto (2-Step, 1-Step oder bei Futures ein Monatsabo), erreicht das Gewinnziel ohne die Verlustgrenzen zu reißen, macht dann Identitätsprüfung und Vertrag und bekommt Auszahlungen aus einem meist ebenfalls simulierten Funded Account. Ablauf und Kosten: [[Kauf und Ablauf einer Challenge]].
2. **Wo:** Keine Firma arbeitet mit Alpaca, und echte US-Aktien gibt es fast nur bei Trade The Pool (Automatisierung dort nur als genehmigungspflichtige Beta). Realistisch sind **Futures** (MES/MNQ statt Aktien) oder **CFDs** (MT5/cTrader). Übersicht unten, Details: [[Prop-Firms für US-Aktien]], [[Prop-Firms für Futures]], [[Prop-Firms für CFD und Forex]], [[Prop-Firms für Krypto]].
3. **Wie verbinden:** Scanner, Entry, Exit, Time Machine, Risk und Journal bleiben. `paper_auto.py` wird durch einen Adapter für die Plattform der Firma ersetzt, `trader-risk` bekommt die Prop-Regeln als harte Prüfungen. Der Haken: **Orders aus der Claude-Cloud sind oft nicht erlaubt** (Topstep verbietet Server und VPS, FTMO will keine US-Geolokation, die Cloud-Sitzung lief über eine US-Adresse). Details: [[Bot an Prop-Firm anbinden]], [[Schnittstellen für Bots]].
4. **Wann:** Noch nicht. Mit 5 Paper-Trades ist kein Vorteil belegt, und der Durchschnitt verliert: Bei Topstep bestanden 2025 16,8 % der Combines, und nur ein Drittel der Funded-Händler wurde je ausgezahlt. Kriterien für „bereit“: [[Recht Steuern und Risiken]].

## Wo: Firmen nach Markt

| Markt | Firmen mit Bot-Erlaubnis (laut Recherche) | Anbindung | Passt zum Bot? |
| --- | --- | --- | --- |
| US-Aktien echt | Trade The Pool (AGB verbieten eigene Algo-Software, Programmbedingungen: SignalStack-Beta nach Genehmigung, max. 2 Anfragen/Min.) | Webhook (SignalStack) | am nächsten am heutigen Setup, aber Automatisierung kaum erlaubt |
| US-Aktien als CFD | FTMO (EAs erlaubt), FundedNext (14 US-Aktien, Bots nur MT4/MT5 unter $50k mit Add-on) | MT5 (Windows-Terminal) | Setup übertragbar, Windows-Rechner nötig; FTMO-Klausel zu Trades kurz vor Schluss prüfen |
| Futures (MES, MNQ) | Topstep (offizielle API, $29/Monat, nur vom eigenen Gerät, nicht auf Live-Konten), Lucid, My Funded Futures, Tradeify (eigene Bots, ggf. Nachweisvideo) | ProjectX-API (REST), Tradovate, Rithmic | ORB auf Index-Futures gut übertragbar, Daten und Time Machine neu |
| Forex/CFD | FTMO, The5ers (eigener Code), Blueberry (schriftliche Zustimmung) | MT5, cTrader | anderer Markt, Scanner/News nutzlos |
| Krypto | HyroTrader (Bots und KI-Agenten offiziell erlaubt, Börsen-API über Bybit/BloFin) | REST-API | technisch am einfachsten, aber ein anderes Projekt (rund um die Uhr, keine Opening Range) |

Nicht erlaubt laut Drittquellen: Apex, Alpha Futures, Take Profit Trader (vollautomatisch). Unsicheres steht in den Einzelnotizen.

## Wie verbinden: drei Wege

| Weg | Was läuft wo | Für wen |
| --- | --- | --- |
| **1. Cloud schlägt vor, Yannick bestätigt** | Cloud-Läufe wie heute, Ticket per Discord; Order setzt Yannick selbst oder ein kleiner Ausführer auf seinem Rechner | passt zur Repo-Regel und zu Firmen, die das eigene Gerät verlangen; erster sinnvoller Schritt |
| **2. Ausführer auf eigenem Rechner/VPS** | Analyse in der Cloud, Orders von einem Dauerprozess mit Adapter (nur geprüfte, freigegebene Orders) | nötig für MT5 (Windows), Rithmic, NinjaTrader |
| **3. Alles in der Cloud** | wie der Paper-Autopilot | nur wenn die Firma das schriftlich erlaubt und Yannick neu über Autonomie entscheidet |

In jedem Fall: Stop und Ziel als Bracket **beim Broker**, nie als Überwachung im Bot, weil Cloud-Prozesse nach 2 Stunden enden.

## Fahrplan ohne Geld

1. **Prop-Regeln auf Paper simulieren:** Tagesverlust auf Equity inkl. offener Verluste, nachziehender Maximalverlust, Konsistenzregel, News-Sperre als eigene Zusatzprüfung neben `trader-risk` (die Skills selbst nur nach Rückfrage ändern). Limits der Wunschfirma auf das Paper-Konto umrechnen.
2. **Journal füllen:** gleiche Regeln, deutlich mehr als 30 Trades, Erwartungswert in R nach Kosten. Die Prop-Regeln auf die Journal-Trades anwenden und viele Reihenfolgen durchspielen: So wird die Chance zu bestehen schätzbar.
3. **Markt entscheiden:** Aktien-CFD (MT5) oder Futures (ProjectX). Dann Daten und Time Machine für diesen Markt.
4. **Kostenlos testen:** FTMO Free Trial, Topstep Practice, cTrader-/TradeLocker-Demo. Adapter, Brackets, Abbrüche, Glattstellen üben.
5. **Schriftlich fragen:** Ist dieser Bot erlaubt, von welchem Ort aus, auf welchem Kontotyp, auch beim Funded Account?
6. **Erst dann kaufen**, und vorher hier eine Entscheidung festhalten (`Gedächtnis/Entscheidungen/`).

## Notizen

- [[Kauf und Ablauf einer Challenge]]: Schritt für Schritt, Geschäftsmodell, Erfolgsquoten, Kosten-Nutzen-Rechnung
- [[Prop-Firms für US-Aktien]] · [[Prop-Firms für Futures]] · [[Prop-Firms für CFD und Forex]] · [[Prop-Firms für Krypto]]
- [[Schnittstellen für Bots]]: zehn Plattform-APIs im Vergleich
- [[Bot an Prop-Firm anbinden]]: Umbauplan für diesen Bot
- [[Recht Steuern und Risiken]]: Steuern in Deutschland, Pleiten und verweigerte Auszahlungen, Checkliste, wann ein Bot bereit ist
- Vorher: [[Prop-Firms und Bot-Architektur]] (Gemini-Recherche geprüft)
