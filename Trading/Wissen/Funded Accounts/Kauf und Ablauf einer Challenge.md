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

# Kauf und Ablauf einer Challenge

Was man bei einer Prop-Firm eigentlich kauft, wie eine Challenge („Lizenz“) vom Konto bis zur Auszahlung abläuft und was sie wirtschaftlich bedeutet. Beispiele sind FTMO (CFD/Forex, 1-Step, 2-Step, Instant) und Topstep (Futures-Abo), weil beide ihre Abläufe und Zahlen offiziell veröffentlichen.

Zurück zum Hub: [[Funded Accounts]] · Grundlage: [[Prop-Firms und Bot-Architektur]] · Recht und Steuern: [[Recht Steuern und Risiken]]

> [!warning] Keine Kaufempfehlung, keine Anlageberatung
> Diese Notiz beschreibt Abläufe und rechnet Beispiele. Ob eine Challenge gekauft wird, entscheidet Yannick. Bis dahin gilt [[Trading/Regeln]] (Paper Trading). Preise und Regeln ändern sich laufend; Stand der Prüfung 23.10.2026, vor jedem Kauf die Seite des Anbieters lesen.

## Was man kauft

> [!important] Eine Dienstleistung, kein Kapital
> Man kauft den Zugang zu einer **Prüfung auf einem simulierten Konto**. Man bekommt kein Geld geliehen und investiert nichts. Wer besteht, bekommt in der Regel wieder ein **simuliertes** Konto und einen vertraglichen Anspruch auf eine „Reward“ (Gewinnbeteiligung), die die Firma aus ihren eigenen Einnahmen zahlt.

| Firma | Was sie selbst sagt |
| --- | --- |
| FTMO | „all accounts we provide to our clients are demo accounts with fictitious funds“; „all trading is processed on simulated accounts; our clients do not trade with real capital“ (FAQ) |
| Topstep | Statistiken umfassen „both a simulated trading environment and a live trading environment“; das Express Funded Account ist simuliert, nur **0,71 %** der Express-Händler wurden 2025 in ein Live Funded Account übernommen |

Das heißt: Auch das „Funded Account“ ist meist eine Simulation. Echte Orders an einer Börse gibt es nur bei wenigen Firmen und dort meist erst in einer späten Stufe (Topstep: Live Funded Account nach Auswahl durch das Risk Team). **Für Deutschland gibt es das bei Topstep nicht:** Das Help Center führt Deutschland unter „Countries Eligible for an XFA — Not LFA“; die Terms of Use sagen für solche Länder, das Funded Account bleibe „exclusively in a simulated trading environment“.

## Die Modelle

| Modell | Ablauf | Beispiel (Stand 10/2026) | Gebühr zurück? |
| --- | --- | --- | --- |
| **2-Step** | Phase 1 (Ziel 10 %), Phase 2 / Verification (Ziel 5 %), dann Funded | FTMO 2-Step: Tagesverlust 5 %, Maximalverlust 10 % statisch, mindestens 4 Handelstage je Phase; 100k-Konto **€540** | FTMO: ja, mit der ersten Reward-Auszahlung |
| **1-Step** | Eine Phase (Ziel 10 %), dann Funded | FTMO 1-Step: Tagesverlust 3 %, Maximalverlust 10 % nachziehend zum Tagesende, bester Tag ≤ 50 % des Gesamtgewinns (Bestellungen ab 12.10.2026); 100k **€499** | FTMO: nein |
| **Instant Funding** | Keine Prüfung, sofort „Funded“, strengere Regeln | FTMO Instant: Tagesverlust 3 %, Maximalverlust 10 % intraday nachziehend, bester Tag ≤ 30 %; Preis auf der Seite nicht gefunden | FTMO: nein |
| **Futures-Abo** | Monatsabo bis zum Bestehen, dann Aktivierungsgebühr | Topstep Trading Combine 50K: **$49/Monat** + **$149** Aktivierung, oder „No Activation Fee“ **$95/Monat** (100K $99/$149, 150K $199/$229) | Topstep: nein |

- Die Euro-Preise von FTMO stehen auf der Bestellseite, nicht auf der Regelseite; sie stammen hier aus Drittquellen (PropFirmMap, ProptradingVibes), die die FTMO-Bestellseite wiedergeben. Der Preis kann je Land, Steuer und Währung abweichen, FTMO zeigt manchen Besuchern Rabatte.
- Topstep nennt auf verschiedenen eigenen Seiten unterschiedliche Abo-Preise (z. B. „No Activation Fee“ 50K $85 oder $95). Die Tabelle folgt dem Help Center; vor dem Kauf auf der Bestellseite prüfen.
- FTMO bietet zusätzlich einen kostenlosen **Free Trial** (Demo mit den Challenge-Regeln, ohne Zeitlimit). Für einen Bot ist das der naheliegende erste Test, bevor Geld fließt.

## Schritt für Schritt

### 1. Konto anlegen

Registrierung auf der Seite der Firma mit E-Mail, Name, Land. Noch keine Identitätsprüfung. Viele Firmen schließen Länder aus (Topstep führt eine Liste, wohin nicht ausgezahlt wird). Ob Deutschland zugelassen ist, habe ich nicht einzeln geprüft: vor dem Kauf die aktuelle Länderliste lesen.

### 2. Modell, Größe, Plattform wählen

Kontogröße (z. B. 10k bis 200k), Modell (oben) und Plattform. FTMO laut FAQ: MT4, MT5, cTrader oder TradingView; Topstep: TopstepX (mit API für Bots, $29/Monat) und weitere Plattformen laut Help Center Die Plattform entscheidet, wie ein Bot angebunden wird, siehe [[Schnittstellen für Bots]] und [[Bot an Prop-Firm anbinden]].

### 3. Zahlung

FTMO nimmt Karte, Apple Pay, Google Pay, Revolut Pay (ohne Gebühr), PayPal, Skrill und Krypto (je 3 % Gebühr) sowie Banküberweisung in EUR/CZK (2–5 Werktage). Topstep bucht das Abo monatlich ab, bis man besteht oder kündigt.

### 4. Zugangsdaten

FTMO legt das Konto nach Zahlungseingang an, meist in wenigen Stunden, selten bis 24 Stunden; die Zugangsdaten zur Plattform stehen dann im Client Area. Ab hier läuft die Prüfung.

### 5. Regeln akzeptieren

Mit dem Kauf akzeptiert man die AGB der Challenge (bei FTMO „Challenge Terms“). Darin stehen die Handelsregeln, verbotene Praktiken und die Gründe, aus denen Konten beendet oder Auszahlungen verweigert werden. Diese Klauseln lesen, bevor ein Bot läuft, siehe [[Recht Steuern und Risiken]] und [[Tageslimits und Regelwerk]].

### 6. Prüfung

Gewinnziel erreichen, ohne Tages- oder Maximalverlust zu reißen, Mindesttage und Konsistenzregeln einhalten. Wird eine Grenze gerissen, ist das Konto sofort beendet; die Gebühr ist weg. Offene Verluste (Equity) zählen bei FTMO für die Grenzen mit.

### 7. Identitätsprüfung (KYC) und Vertrag

- **FTMO:** Nach Erreichen der Ziele schaltet sich „FTMO Identity“ frei: Natürliche Person (KYC) oder Unternehmer/Firma (KYB). Adressnachweis höchstens 6 Monate alt. Prüfung meist unter 1 Werktag (Firmen bis 3). Danach unterschreibt man im Client Area die **FTMO Account Terms & Conditions**, einen eigenen Vertrag für die Funded-Phase. Beim Instant Account geschieht die Identitätsprüfung erst mit der ersten Auszahlung.
- **Topstep:** Mit dem Auszahlungsantrag gibt man das Steuerformular ab, für Nicht-US-Personen **W-8BEN**. Auszahlung nur auf ein Konto im eigenen Namen. Grundlage ist das „Express Funded Account Agreement“.

### 8. Funded-Phase und Auszahlung

| | FTMO | Topstep |
| --- | --- | --- |
| Erste Auszahlung | ab dem 14. Tag nach dem ersten Trade auf dem Funded Account; alle Positionen geschlossen | Standard: 5 Gewinntage mit je ≥ $150 netto (nicht am Stück); oder Consistency: 3 Handelstage, größter Tag ≤ 40 % des Gewinns |
| Anteil | 1-Step und Instant 90 %; 2-Step 80 %, mit Scaling oder Premium 90 % | 90 % (Bestandskunden vor 12.01.2026: erste $10.000 zu 100 %) |
| Mindestbetrag | $20 (Überweisung, Visa Direct, Mastercard Send), $50 Krypto | $125 |
| Höchstbetrag je Antrag | Visa/Mastercard bis $20.000, Skrill bis $3.000 | bis 50 % des Saldos; 50K $2.000/$3.000, 100K $3.000/$4.000, 150K $5.000/$6.000 (Standard/Consistency) |
| Methoden | Überweisung, Visa Direct, Mastercard Send, Skrill, Krypto (oder FTMO Points, nicht in Geld tauschbar) | International: Wire/SWIFT 5–10 Werktage, $30 Gebühr; Wise (nur China, Kanada, UK); weitere nur USA |
| Bearbeitung | Prüfung 1–2 Werktage, Zahlung meist 1–2 Werktage nach Freigabe der Rechnung | Freigabe 1–3 Werktage |
| Prüfung vor Zahlung | Einhaltung der Ziele und Account Terms | Payout Policy, Prohibited Conduct, Terms of Use, verbotene Strategien |

Bei Topstep wird die Maximalverlust-Grenze nach jeder Auszahlung laut Help Center dauerhaft auf $0 gesetzt und die Zählung der Gewinntage beginnt neu: Wer auszahlt, hat danach weniger Spielraum. Bei FTMO Instant wird die Maximalverlust-Grenze nach einer Auszahlung **nicht** zurückgesetzt.

> [!example] Topstep-Rechenbeispiel aus dem Help Center
> $500 Auszahlung per ACH: 10 % Anteil der Firma und $30 Gebühr, ausgezahlt werden **$420**. Bei Wire/SWIFT nach Deutschland gilt dieselbe Gebühr von $30.

### 9. Rückerstattung der Gebühr

- FTMO 2-Step: Gebühr kommt mit der **ersten Reward-Auszahlung** zurück, auf dem ursprünglichen Zahlungsweg. 1-Step und Instant: keine Rückerstattung.
- Topstep: Abo und Aktivierung werden nicht erstattet.
- Viele andere Firmen werben mit Rückerstattung „mit der ersten“ oder „vierten Auszahlung“: Wer nie auszahlt, bekommt nichts zurück.

### 10. Reset, Retry, Reaktivierung

- **FTMO:** Ein Zurücksetzen nach einem Regelbruch habe ich auf den aktuellen Seiten nicht gefunden; man kauft eine neue Challenge. Ein früher übliches „Free Retry“ ist auf den aktuellen Seiten nicht bestätigt.
- **Topstep:** Das Abo läuft monatlich weiter; wie ein gescheiterter Combine neu startet und was das kostet, steht im Help Center (nicht einzeln geprüft). Ein verlorenes Express Funded Account kann laut Help Center für **$599 / $699 / $829** (50K/100K/150K) reaktiviert werden („Back2Funded“, Bedingungen im Help Center).
- Reset-Gebühren sind ein großer Teil des Umsatzes der Branche: Jeder Neuversuch ist eine neue Gebühr.

### 11. Skalierung

- **FTMO Scaling Plan:** alle 4 Monate +25 % Kontogröße, wenn in diesen 4 Monaten mindestens 10 % Nettogewinn erzielt und mindestens 2 Rewards ausgezahlt wurden und der Saldo positiv ist; höchstens $2.000.000 über alle FTMO-Konten. Nicht für Instant Accounts.
- **Topstep:** Im Express Funded Account bestimmt ein „Scaling Plan“, wie viele Kontrakte man je nach Gewinnpuffer halten darf; das Live Funded Account vergibt das Risk Team.

## Geschäftsmodell der Firmen

Die Firmen verdienen an **Gebühren**, nicht am Handel. Weil die Konten simuliert sind, kostet ein verlierender Kunde die Firma nichts, ein gewinnender Kunde wird aus den Gebühren der anderen bezahlt. Das funktioniert, solange genug Kunden scheitern.

> [!quote] Primärquelle: CFTC-Klage gegen My Forex Funds (2023)
> Laut der Klage der US-Aufsicht CFTC zahlten über 135.000 Kunden mindestens **$310 Mio.** Gebühren; ausgezahlt wurden etwa $137 Mio., Nettogewinn rund $172 Mio. Die CFTC nannte die Auszahlungen „in a manner similar to a Ponzi scheme“ aus den Gebühren anderer Kunden finanziert. Die Klage wurde 2025 wegen Fehlverhaltens der CFTC abgewiesen, über die Vorwürfe selbst wurde nicht entschieden. Details: [[Recht Steuern und Risiken]].

Die Zahlen zeigen das Muster der Branche: Mehrheit zahlt Gebühren, Minderheit wird ausgezahlt. Das ist nicht per se Betrug, aber es heißt, dass die Firma von Kunden lebt, die scheitern.

## Was die Firmen über Erfolgsquoten veröffentlichen

| Quelle | Zahl | Einordnung |
| --- | --- | --- |
| **Topstep, offiziell, Jan–Dez 2025** | 16,8 % aller begonnenen Trading Combines bestanden | je Combine, nicht je Person |
| | 51,8 % der Teilnehmer erreichten in mindestens einem Combine das Funded Level | je Person, über beliebig viele Versuche |
| | **33,3 %** der Personen im Funded Level erhielten eine Auszahlung | 2 von 3 Funded-Händlern bekamen **nichts** |
| | 0,71 % der Express-Händler wurden in ein Live Funded Account übernommen | echte Börse nur für sehr wenige |
| Topstep, Werbung | 99,26 % der Auszahlungsanträge genehmigt; über $1,4 Mrd. ausgezahlt | Firmenangabe, nicht geprüft; misst nur die, die einen Antrag stellen |
| **FTMO, offiziell** | über 4,5 Mio. Kunden, über $650 Mio. Rewards ausgezahlt | keine Bestehens- oder Auszahlungsquote veröffentlicht |
| FTMO (Finance Magnates, Okt. 2026) | über $200 Mio. in 12 Monaten, rund $16 Mio. im Monat | Firmenangabe |
| Branchen-Tracker Prop Firm Match | rund $325 Mio. Auszahlungen 2025 bei den erfassten Firmen | ohne FTMO und The5ers; nicht vollständig |
| Ratgeber/Anbieter von Technik | „etwa 7 % der Käufer erhalten eine Auszahlung“ | Branchenschätzung, **nicht bestätigt** |

> [!info] FTMO-Zahlen richtig lesen
> $650 Mio. bei 4,5 Mio. Kunden sind im Mittel rund $144 je registriertem Kunden, ohne zu wissen, wie viele davon gezahlt haben und wie viele Gebühren sie zahlten. Eine Quote „wie viele Käufer werden ausgezahlt“ veröffentlicht FTMO nicht.

## Kosten-Nutzen-Rechnung

### Topstep 50K, Standard-Weg

Annahmen: ein Combine dauert einen Monat; die Quote von 16,8 % gilt für jeden Versuch gleich (für einen einzelnen Händler stimmt das nicht, siehe unten).

| Posten | Rechnung | Betrag |
| --- | --- | --- |
| Erwartete Zahl Versuche bis zum Bestehen | 1 / 0,168 | ≈ 6 Monate |
| Abo | 6 × $49 | ≈ $292 |
| Aktivierung | einmal | $149 |
| **Erwartete Kosten bis Funded** | | **≈ $440** |
| Chance, danach überhaupt ausgezahlt zu werden | 33,3 % | |
| Erste Auszahlung bei 5 Gewinntagen à $150 | $750 brutto × 90 % − $30 Wire | **$645** |

Erwartungswert der ersten Auszahlung: 0,333 × $645 ≈ **$215** gegen ≈ $440 Kosten. Für den Durchschnitt ist das ein Verlust. Es lohnt sich nur, wenn die eigene Chance klar über dem Durchschnitt liegt oder mehrere Auszahlungen folgen.

### FTMO 2-Step 100k

Annahme: Nach dem Bestehen wird einmal ausgezahlt, bei 3 % Gewinn ($3.000 × 80 % = $2.400) plus Rückerstattung der Gebühr (€540, hier ≈ $630 gerechnet). p = Chance, beide Phasen zu bestehen; q = Chance, danach auszuzahlen. FTMO veröffentlicht weder p noch q.

| p (bestehen) | q (auszahlen) | p × q | Erwartete Einnahme | minus Gebühr | Erwartungswert |
| --- | --- | --- | --- | --- | --- |
| 10 % | 33 % | 3,3 % | 0,033 × $3.030 = $100 | $630 | **−$530** |
| 20 % | 50 % | 10 % | $303 | $630 | **−$327** |
| 40 % | 60 % | 24 % | $727 | $630 | **+$97** |

Gewinnschwelle: p × q ≈ $630 / $3.030 ≈ **21 %**. Ein Bot müsste also etwa jede fünfte Challenge bis zur Auszahlung bringen, nur damit sich die erste Auszahlung trägt. Mit mehreren Auszahlungen sinkt die Schwelle, mit Spreads, Kommissionen und Währungsverlusten steigt sie.

> [!tip] Eigene Zahlen einsetzen
> Die Durchschnittsquoten mischen alle Käufer, auch die ohne Plan. Für einen Bot mit festen Regeln lässt sich p besser schätzen: die Prop-Regeln (Ziel, Tagesverlust, Maximalverlust, Konsistenz) auf die eigenen Journal-Trades anwenden und viele Zufallsreihenfolgen durchspielen. Wie das geht und wann ein Bot „bereit“ ist: [[Recht Steuern und Risiken#Wann ist ein Bot bereit für eine Challenge]]. Hintergrund: [[Wie viele Day Trader gewinnen]], [[Backtesting und Overfitting]].

## Für diesen Bot

- **Markt passt nicht direkt:** Der Bot handelt US-Aktien long über Alpaca. FTMO ist CFD/Forex auf MT4/MT5/cTrader, Topstep ist Futures. Ein ORB auf Aktien wird dort zu einem ORB auf CFDs oder Futures (z. B. Index-Futures) mit anderen Kosten und Zeiten. Welche Firmen Aktien anbieten: [[Prop-Firms für US-Aktien]], [[Prop-Firms für Futures]], [[Prop-Firms für CFD und Forex]].
- **Cloud-Betrieb kann verboten sein:** Topstep schreibt in der API-Beschreibung, dass alle Orders vom **eigenen Gerät** kommen müssen und VPS, VPN und Remote-Server verboten sind („your server can watch and record, but it cannot trade“); Live-Konten sind über die API gar nicht erreichbar. Die Terms of Use (Stand 21.09.2026) sagen: „Using any VPN or VPS on Accounts is strictly prohibited“. Der Autopilot in Claude-Code-Cloud-Sitzungen wäre dort ein Regelverstoß. Vor jedem Kauf genau diese Frage schriftlich klären.
- **FTMO-Klauseln mit Bezug zum ORB:** Die Liste der verbotenen Praktiken nennt „gap trading“, also Trades zu angesetzten Unternehmenszahlen oder Makro-Terminen und „two hours or less before a relevant financial market is closed for at least two hours“. Nach dem Wortlaut könnten Einstiege in Aktien-CFDs ab etwa 14:00 NY darunter fallen; das Einstiegsfenster des Bots reicht bis 15:30. Vor dem Kauf bei FTMO nachfragen. Details: [[Recht Steuern und Risiken]].
- **Limits übersetzen:** $100.000 Paper-Konto mit $1.000 Verlust je Trade und $2.500 je Tag sind 1 % und 2,5 %. Das liegt unter FTMOs 5 % (2-Step) bzw. 3 % (1-Step) Tagesgrenze, aber das Paper-Limit gilt am Stop, die Prop-Grenze auf die Equity inklusive Slippage. Bei 1-Step blieben bei zwei Verlusttrades und schlechter Ausführung wenig Reserve.
- **Kostenloser Test zuerst:** FTMO Free Trial (kostenlos, gleiche Regeln) und Topstep Practice Account erlauben, die Anbindung und die Regeln ohne Gebühr zu prüfen.
- **Mit 5 geschlossenen Trades** ist p nicht schätzbar; die Rechnung oben bleibt bis auf Weiteres eine Wette auf den Durchschnitt, und der ist negativ.
- Mit echtem Geld gilt weiter: keine Order ohne ausdrückliches Ja von Yannick, siehe [[Trading/Regeln]]. Eine bezahlte Challenge ist zwar simuliert, die Gebühr aber echtes Geld.

## Quellen

Abgerufen am 23.10.2026.

Offizielle Seiten der Firmen:
- FTMO FAQ (Übersicht, Demo-Hinweis) – https://ftmo.com/en/faq/
- FTMO: How do I withdraw my reward? – https://ftmo.com/en/faq/how-do-i-withdraw-my-profits/
- FTMO: Is the entry fee refunded? – https://ftmo.com/en/faq/is-the-entry-fee-refunded/
- FTMO: What is FTMO Identity, and when do I complete it? – https://ftmo.com/en/faq/what-is-ftmo-identity-and-when-do-i-complete-it/
- FTMO: Legal relationship after signing the FTMO Account Terms & Conditions – https://ftmo.com/en/faq/what-is-the-legal-relationship-between-an-ftmo-trader-and-ftmo-after-signing-the-ftmo-account-terms-conditions/
- FTMO: What payment methods are available? – https://ftmo.com/en/faq/what-payment-methods-are-available/
- FTMO: I paid for my order, when will I get the account? – https://ftmo.com/en/faq/i-paid-for-my-order-when-will-i-get-the-account/
- FTMO: How do the different accounts provided by FTMO differ? – https://ftmo.com/en/faq/how-do-the-different-accounts-provided-by-ftmo-differ/
- FTMO: Trading Objectives – https://ftmo.com/en/trading-objectives/
- FTMO: Reward Growth and Scaling Plan – https://ftmo.com/en/reward-growth-and-scaling-plan/
- FTMO: Which instruments can I trade and what strategies am I allowed to use? – https://ftmo.com/en/faq/which-instruments-can-i-trade-and-what-strategies-am-i-allowed-to-use/
- FTMO Startseite (Kennzahlen 4,5 Mio. Kunden, $650 Mio. Rewards) – https://ftmo.com/en/
- FTMO Free Trial – https://ftmo.com/en/ftmo-free-trial/
- Topstep: Statistiken 2025 – https://www.topstep.com/topstep-prop
- Topstep Help Center: Payout Policy – https://help.topstep.com/en/articles/8284233-topstep-payout-policy
- Topstep Help Center: Program Overview (Stand 10.09.2026) – https://help.topstep.com/en/articles/8284099-topstep-program-overview
- Topstep Help Center: Pricing and Payment Questions – https://help.topstep.com/en/articles/14289835-topstep-pricing-and-payment-questions
- Topstep Help Center: Back2Funded – https://help.topstep.com/en/articles/12060405-back2funded-rules-guidelines-and-how-it-works
- Topstep Help Center: TopstepX API Access – https://help.topstep.com/en/articles/11187768-topstepx-api-access
- Topstep Help Center: Am I Eligible to Trade with Topstep? – https://help.topstep.com/en/articles/8284116-am-i-eligible-to-trade-with-topstep
- Topstep Terms of Use (Stand 21.09.2026) – https://www.topstep.com/terms-of-use
- FTMO: Forbidden Trading Practices – https://ftmo.com/en/forbidden-trading-practices/
- Topstep: Instant Payouts (99,26 %, $1,4 Mrd.) – https://www.topstep.com/instant-payouts

Behörden:
- CFTC v. Traders Global Group, Complaint (D.N.J., 29.08.2023) – https://www.cftc.gov/media/9196/enftradersglobalgroupcomplaint082923/download
- CFTC Press Release 8771-23 – https://www.cftc.gov/PressRoom/PressReleases/8771-23

Presse und Ratgeber (Ratgeber teils mit Affiliate-Links, als solche lesen):
- Finance Magnates: FTMO Adds $200 Million to Lifetime Payouts in One Year – https://www.financemagnates.com/forex/ftmo-adds-200-million-to-lifetime-payouts-in-one-year-as-monthly-rewards-near-15-million/
- Finance Magnates: Prop Firm Match Tracked About $325 Million in Payouts in 2025 – https://financemagnates.com/forex/prop-firm-match-tracked-about-325-million-in-payouts-to-traders-in-2025
- PropFirmMap (Ratgeber, Preise FTMO) – https://propfirmmap.com/firms/ftmo
- ProptradingVibes (Ratgeber, Preise FTMO) – https://proptradingvibes.com/de/blog/ftmo-account-sizes-pricing
