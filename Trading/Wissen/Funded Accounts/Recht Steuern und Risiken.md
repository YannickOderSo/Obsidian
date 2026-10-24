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

# Recht Steuern und Risiken

Was in Deutschland rechtlich und steuerlich für Auszahlungen von Prop-Firms gilt, welche Aufsicht zuständig ist (meist keine), woran Firmen gescheitert sind, mit welchen AGB-Klauseln Auszahlungen verweigert werden und ab wann ein Bot überhaupt „bereit“ für eine Challenge wäre.

Zurück zum Hub: [[Funded Accounts]] · Ablauf und Kosten: [[Kauf und Ablauf einer Challenge]] · Steuern auf eigene Trades: [[Steuern in Deutschland]]

> [!warning] Keine Rechts- oder Steuerberatung
> Diese Notiz fasst Gesetze, AGB, Behördenmitteilungen und Presse zusammen (Stand 23.10.2026). Die steuerliche Einordnung von Prop-Auszahlungen ist in Deutschland **ungeklärt**. Vor der ersten Auszahlung eine Steuerberaterin fragen, vor dem Kauf die aktuellen AGB lesen.

## Steuern in Deutschland

### Keine Kapitalerträge, keine Abgeltungsteuer

Bei einer Prop-Firm setzt man kein eigenes Kapital ein; gehandelt wird auf einem simulierten Konto. Die Auszahlung ist deshalb kein Gewinn aus einer Kapitalanlage (§ 20 EStG), sondern eine Vergütung, die die Firma vertraglich zusagt. Darin sind sich die gefundenen Ratgeber einig, und so lesen es auch die AGB: FTMO nennt die Konten „accounts for simulated trading“ und die Tätigkeit „not trading in real financial instruments“. Folge: **keine Abgeltungsteuer von 25 %, kein Sparerpauschbetrag**, sondern der persönliche Einkommensteuersatz.

### Gewerblich (§ 15) oder sonstige Einkünfte (§ 22 Nr. 3)?

| | Gewerbebetrieb, § 15 EStG | Sonstige Einkünfte, § 22 Nr. 3 EStG |
| --- | --- | --- |
| Wann | nachhaltig, mit Gewinnerzielungsabsicht, Teilnahme am allgemeinen wirtschaftlichen Verkehr (§ 15 Abs. 2) | „Einkünfte aus Leistungen“, die keiner anderen Einkunftsart zugehören |
| Steuersatz | persönlicher Tarif | persönlicher Tarif |
| Freigrenze | – | unter **256 €** im Jahr steuerfrei (Freigrenze: darüber voll steuerpflichtig) |
| Gebühren (Challenges, Daten, Software) | Betriebsausgaben | Werbungskosten |
| Verluste | mit anderen Einkünften verrechenbar (Liebhaberei-Prüfung bei Dauerverlust) | **nur** mit Einkünften nach § 22 Nr. 3 im Vorjahr oder in Folgejahren (§ 22 Nr. 3 Satz 3 und 4) |
| Gewerbeanmeldung | ja (§ 14 GewO) | nein |
| Gewerbesteuer | ja, Freibetrag **24.500 €** für Einzelunternehmer (§ 11 Abs. 1 GewStG), teils auf die Einkommensteuer anrechenbar (§ 35 EStG) | nein |

> [!caution] Stand der Unsicherheit
> - Ein Urteil des BFH oder ein BMF-Schreiben speziell zu Prop-Auszahlungen habe ich **nicht gefunden**; die Ratgeber schreiben übereinstimmend, dass es keins gibt.
> - Die Ratgeber widersprechen sich: der/proptrader (mit Verweis auf einen Steuerberater) hält § 15 für herrschende Meinung; Track360 schreibt, die „Mehrheit der Finanzämter“ nehme § 22 Nr. 3, ohne Beleg; andere sagen, Finanzämter entschieden unterschiedlich.
> - Einige Ratgeber enthalten veraltete Zahlen (z. B. Kleinunternehmergrenze 22.000 € statt seit 2025 25.000 €/100.000 €, oder die 2024 gestrichene 20.000-€-Grenze für Termingeschäfte). Solche Seiten sind ein Hinweis, wie unzuverlässig der Stand ist.
> - Praktisch heißt das: vor der ersten Auszahlung klären lassen, notfalls eine **verbindliche Auskunft** beim Finanzamt beantragen (§ 89 Abs. 2 AO, gebührenpflichtig).

### Gewerbeanmeldung, Umsatzsteuer, Formalien

- **Gewerbeanmeldung:** Wird die Tätigkeit als gewerblich gesehen, ist sie vor Beginn anzumelden; dazu der steuerliche Erfassungsbogen über ELSTER. Einige Ratgeber empfehlen die Anmeldung vor der ersten Auszahlung.
- **Umsatzsteuer:** Ob der Händler überhaupt eine umsatzsteuerliche Leistung an die Firma erbringt, ist nicht geklärt. Wenn ja und wenn er Unternehmer ist, liegt der Leistungsort bei einem Unternehmer als Empfänger dort, wo dieser sitzt (§ 3a Abs. 2 UStG). Firma in der EU (z. B. FTMO in Prag): Reverse Charge im Sitzland der Firma, in Deutschland ggf. Zusammenfassende Meldung; Firma außerhalb der EU (z. B. Topstep, USA): in Deutschland nicht steuerbar. Kleinunternehmer nach § 19 UStG: Vorjahresumsatz höchstens **25.000 €**, laufendes Jahr höchstens **100.000 €**. Alles das ist eine Einordnung aus Ratgebern und dem Gesetzestext, keine bestätigte Verwaltungsauffassung.
- **Steuerformulare der Firma:** Topstep verlangt für Nicht-US-Personen das Formular **W-8BEN** mit dem Auszahlungsantrag; FTMO schreibt, der Kunde sei „solely responsible“ für alle Steuern.
- **Währung:** Auszahlungen in USD zum Kurs am Zuflusstag in Euro umrechnen; Gebühren in EUR oder USD je nach Firma. Belege (Rechnung über die Gebühr, Auszahlungsbestätigung) aufbewahren.
- **Verbraucherstatus:** Wer sich als Unternehmer registriert (bei FTMO „Entrepreneur“, bei Topstep mit Steuernummer im Konto), verliert nach den AGB die Verbraucherrechte (Widerruf, Gerichtsstand, siehe unten). Topstep: „if you provide an identification number, tax registration number … the provisions … that grant rights to consumers will not apply to you“.

## Verbraucherrecht

| | FTMO (Tschechien, EU) | Topstep (USA) |
| --- | --- | --- |
| Vertragspartner Challenge | FTMO Evaluation Global s.r.o., Prag | Topstep LLC, Chicago |
| Widerruf | 14 Tage, **erlischt mit dem ersten simulierten Trade** (Challenge-AGB Ziff. 12.1) | „all fees are final, non-cancelable, and non-refundable“ |
| Recht | tschechisches Recht (Ziff. 18.1) | Recht von Delaware |
| Streit | tschechische Gerichte (Ziff. 18.2); Verbraucher-Schlichtung über die tschechische Handelsinspektion (ČOI) | Schiedsverfahren (JAMS) in Wilmington, Delaware, Verzicht auf Sammelklagen |
| Rückbuchung (Chargeback) | FTMO darf dann Leistungen verweigern (Ziff. 14.3) | Terms: Verstöße führen zu Sperre ohne Erstattung |

Was das deutsche bzw. europäische Recht dazu sagt (Grundsätze, keine Beurteilung des Einzelfalls):

- **Widerruf bei Dienstleistungen:** Das Widerrufsrecht erlischt, wenn die Dienstleistung vollständig erbracht ist und der Verbraucher vorher ausdrücklich zugestimmt und bestätigt hat, dass er das Widerrufsrecht dadurch verliert (§ 356 Abs. 5 Nr. 2 BGB). FTMO baut genau darauf: Wer handelt, stimmt zu. Ob die Challenge damit „vollständig erbracht“ ist, ist eine Rechtsfrage, die ich nicht beantworten kann. Praktisch gilt: **Widerruf nur vor dem ersten Trade.**
- **Gerichtsstand bei EU-Verbrauchern:** Richtet eine Firma ihre Tätigkeit auf Deutschland aus, kann der Verbraucher an seinem Wohnsitz klagen, und Gerichtsstandsklauseln vor einem Streit gelten ihm gegenüber nur eingeschränkt (Brüssel-Ia-VO Art. 17–19). Die Rechtswahl darf ihm den Schutz zwingender Vorschriften seines Wohnsitzstaats nicht nehmen (Rom-I-VO Art. 6 Abs. 2).
- **Schiedsklauseln mit Verbrauchern** verlangen nach deutschem Recht eine eigenhändig unterschriebene Urkunde (§ 1031 Abs. 5 ZPO). Ein Haken im Online-Formular erfüllt das wohl nicht. Ein deutsches Urteil gegen eine US-Firma muss aber in den USA durchgesetzt werden; das ist teuer und unsicher.
- **EU-Schlichtungsplattform:** Die in den FTMO-AGB noch genannte EU-ODR-Plattform wurde am **20.07.2025 eingestellt** (VO (EU) 2024/3228). Die nationalen Schlichtungsstellen bestehen weiter.
- Fazit: Bei einer Firma in der EU hat ein deutscher Verbraucher realistische Rechtswege; bei Firmen in den USA, Dubai oder anderswo kaum. Die Gebühr sollte man als verloren betrachten können.

## Aufsicht: BaFin, ESMA und andere

> [!info] Kurz
> Prop-Firms, die nur simulierte Konten anbieten, sind in der EU **nicht als Finanzdienstleister zugelassen** und werden in der Regel von niemandem beaufsichtigt. Es gibt keinen Einlagen- oder Anlegerschutz.

| Stelle | Was sie gesagt oder getan hat |
| --- | --- |
| **BaFin** | Eine Warnung speziell zu Prop-Firms oder Challenges habe ich **nicht gefunden**. Die BaFin warnt laufend vor Plattformen, die „Bankgeschäfte und/oder Finanzdienstleistungen ohne Erlaubnis“ anbieten (§ 37 Abs. 4 KWG), z. B. am 21.07.2025 vor „Trading Kapital“ (trading-kapital.com) – das betraf keine Prop-Firm im engeren Sinn. Vor einem Kauf den Namen in der BaFin-Unternehmensdatenbank und in den Verbraucherwarnungen suchen. |
| **ESMA** | Keine eigene Stellungnahme gefunden. Laut dem Vorsitzenden des ESMA-Risikoausschusses (zugleich CySEC-Chef) ist die ESMA „not currently engaged in any substantive discussions regarding retail prop trading“ (Finance Magnates, 2026). |
| **FSMA (Belgien)**, 07.03.2024 | Warnt vor dem „shadow investment game“: Prop-Firms hätten „no authorization“, die Challenges seien teuer, schwer und würden oft mehrfach bezahlt; die Firma allein entscheide, ob und was ausgezahlt wird; das Spiel-Element fördere Selbstüberschätzung. |
| **Consob (Italien)**, 08.07.2024 | Warnt vor „videogiochi“ des Online-Tradings: Prüfungen mit Gebühr, Aussicht auf Gewinnbeteiligung mit angeblich echtem Kapital. |
| **CFTC (USA)** | Klage gegen My Forex Funds 2023 (unten). Größere US-Firmen lassen sich laut Finance Magnates inzwischen als Introducing Broker registrieren; Topstep wird dort als registrierter IB genannt (nicht selbst geprüft). |

## Wenn die Firma scheitert: Fälle

| Firma | Was geschah | Ausgang für Händler |
| --- | --- | --- |
| **My Forex Funds** (Traders Global Group, Kanada) | 29.08.2023: CFTC-Klage in New Jersey, Vermögen eingefroren; Vorwurf: Die Firma sei „counterparty to substantially all customer trades“, Auszahlungen kämen aus Gebühren anderer Kunden „in a manner similar to a Ponzi scheme“; Slippage und Verzögerung seien per Software gegen erfolgreiche Kunden eingestellt worden; > 135.000 Kunden, ≥ $310 Mio. Gebühren. Parallel Verfahren der Ontario Securities Commission. | **Mai 2025:** Klage *with prejudice* abgewiesen und die CFTC sanktioniert, weil sie das Gericht getäuscht hatte (u. a. eine als Vermögensverschiebung dargestellte Steuerzahlung von CAD 31,5 Mio.); die CFTC-Chefin nannte das Verhalten „inexcusable“. Über die Betrugsvorwürfe wurde **in der Sache nicht entschieden**. Kanada: Kostenentscheidung gegen die OSC (Feb. 2026). Laut Drittquellen ab April 2026 erste Nachzahlungen offener Auszahlungen und Pläne für einen Neustart, **nicht offiziell bestätigt**. |
| **True Forex Funds** (Ungarn) | Feb. 2024: MetaQuotes beendet die MT4/MT5-Lizenz; Betrieb ruht. | Mai 2024 laut Drittquelle Insolvenz; rund 300 Händler mit geschätzt $1,2 Mio. offenen Auszahlungen (Zahl nicht bestätigt). |
| **The Funded Trader** (USA) | März 2024: Auszahlungen gestoppt wegen „self imposed internal audit“, dann Betrieb pausiert. Der CEO zeigte $17 Mio. ausgezahlt gegen gut $2 Mio. verweigert, wegen „KYC, … fraud, credit card fraud and any prohibited trading strategies“. | Neustart angekündigt; Dez. 2024 wurden laut Bericht Händlern mit offenen Ansprüchen Sperren mitgeteilt. Ausgang 2025 nicht verlässlich belegt. |
| **SurgeTrader** | Mai 2024 geschlossen. | laut Drittquelle nur ein Teil der offenen Auszahlungen geleistet (nicht bestätigt). |
| **FundingTicks** | Dez. 2025 rückwirkende Regeländerungen (Mindesthaltedauer, geringere Anteile), 19.01.2026 Abwicklung angekündigt. | Gebühren aktiver Konten laut Firma voll erstattet, abgestufte Abfindungen für Funded-Konten. |
| **MyFundedFX / SeacrestFunded** | Prop-Handel (CFD) zum 06.02.2026 eingestellt, Fokus auf CFD-Broker. | Erstattung nur für aktive, ungebrochene Challenges auf Antrag bis 28.02.2026; Funded-Salden auf Antrag. |
| **ATFunded** (ATFX) | 06.06.2026 Betrieb pausiert für „full review of the business“. | Erstattung aktiver Käufe und offene Auszahlungen angekündigt; Erfüllung nicht geprüft. |

Laut Finance Magnates haben zwischen Januar 2024 und Anfang 2026 rund 80–100 Prop-Firms aufgegeben. Einen Fall „Funding Traders“ habe ich nicht gefunden; vermutlich ist The Funded Trader gemeint.

> [!warning] Muster
> Pleiten und Auszahlungsstopps kamen oft nach (1) Verlust der Plattform-Lizenz (MetaQuotes 2024), (2) rückwirkenden Regeländerungen, (3) auffällig vielen verweigerten Auszahlungen, (4) Behördenmaßnahmen. Wer ausgezahlt bekommen will, sollte Guthaben nicht auflaufen lassen.

## AGB-Klauseln, mit denen Auszahlungen verweigert werden

Die Klauseln stehen fast gleichlautend bei vielen Firmen. Wörtlich geprüft habe ich FTMO (Challenge-AGB vom 12.10.2026, Seite „Forbidden Trading Practices“) und Topstep (Terms of Use vom 21.09.2026, Help Center).

| Klausel | FTMO | Topstep | Folge |
| --- | --- | --- | --- |
| **KI / Software** | verboten: „use any software, artificial intelligence, ultra-high-speed tools, or mass data entry that might manipulate, abuse, or give you an unfair advantage“ | wortgleich: „Using any software, artificial intelligence, ultra-high speed, or mass Data entry which might manipulate, abuse, or give User an unfair advantage“ | Ermessen der Firma, was „unfair“ ist |
| **Bots / EAs** | erlaubt, aber nicht „hyperactive“: mehr als **2.000 Server-Anfragen am Tag**; fremde EAs können an der Kapitalgrenze scheitern | Bots über die TopstepX-API erlaubt, kein HFT; Orders nur vom **eigenen Gerät**, **„Using any VPN or VPS on Accounts is strictly prohibited“** | Kontoschließung, Verfall der Gewinne |
| **Glücksspiel / Risiko** | Firma darf Maßnahmen gegen Aktivitäten treffen, „we deem analogous to gambling“; verboten sind deutlich größere Positionen oder Positionszahlen als sonst, Überhebelung, „one-sided bets“ | „not responsible trading“, „not a viable trading strategy“ nach alleinigem Ermessen | Trades gestrichen, Ziel nicht erreicht |
| **Simulation ausnutzen** | Fehler in Kursen, Verzögerungen, langsame Datenfeeds | Slippage, Queue-Position, Gaps, viele Trades in kurzer Zeit ausnutzen; Gewinne, die live nicht möglich wären | Bestehen wird nicht anerkannt, **alle** Auszahlungen verfallen |
| **News / Gaps** | „gap trading“: Trades eröffnen, wenn Makrodaten oder **Unternehmenszahlen** anstehen, oder **„two hours or less before a relevant financial market is closed for at least two hours“** | Positionen bis 15:10 CT schließen, automatische Glattstellung | Regelbruch |
| **Copy Trading / Dritte** | niemand anderes darf handeln oder „in coordination“; kein Handel für andere | gleiche Strategie „in concert with others“, auch zwischen fremden Konten, verboten; kein Handel für andere | Schließung aller Konten |
| **Mehrere Konten** | erlaubt, aber höchstens **$400.000** Startkapital „per client, per strategy and per ultimate beneficial owner“; Gegenpositionen über Konten verboten | **nur ein Account** je Person; Gegenpositionen über Konten, „account stacking“ verboten | Sperre aller Konten |
| **IP / Standort** | Länderbeschränkungen; KYC-Daten müssen stimmen | VPN, Proxy, TOR verboten; geografische Beschränkungen umgehen verboten | Auszahlung verweigert |
| **Konsistenz** | 1-Step: bester Tag ≤ 50 % des Gewinns; Gewinne künstlich über Tage verteilen ist verboten | Combine: bester Tag < 55 %; Consistency-Auszahlung: ≤ 40 % | Auszahlung erst später |
| **Ermessen und Änderungen** | Firma entscheidet „at our own discretion“, ob eine verbotene Praxis vorliegt; keine Entschädigung, keine Erstattung (Ziff. 7.9) | Regeln „subject to change … with or without notice“ | – |

Andere Firmen sind strenger. Laut deren eigenen Seiten (über Suchergebnisse, nicht vollständig gelesen): **Apex Trader Funding** verbietet seit 2026 „any form of AI, Autobots, algorithms, fully automated trading systems“ auf allen Kontoarten; die User Agreement verbietet jedes Werkzeug, das Orders automatisch eingibt. Alpha Futures, E8 Futures und Elite Trader Funding verbieten KI und Bots laut Ratgebern ebenfalls.

> [!important] Was das für einen LLM-Bot heißt
> Kein gefundenes Regelwerk erlaubt **ausdrücklich** einen von einem Sprachmodell gesteuerten Bot. Die KI-Klauseln verbieten KI nicht pauschal, aber sie geben der Firma das Ermessen, sie als „unfair advantage“ zu werten. Vor dem Kauf schriftlich (E-Mail, Ticket) bestätigen lassen: vollautomatisch, LLM entscheidet über Einstiege, läuft in der Cloud, Orders per API. Keine Tricks, um Erkennung zu umgehen: Das ist selbst ein Kündigungsgrund.

## Checkliste zur Prüfung einer Firma

- [ ] **Wer ist der Vertragspartner?** Firmenname, Sitz, Registernummer in den AGB; Handelsregister des Landes prüfen. EU-Sitz ist für Verbraucher besser.
- [ ] **Wie lange am Markt, wie groß?** Jahre, veröffentlichte Auszahlungssummen, offizielle Statistiken wie bei Topstep.
- [ ] **Aufsicht und Warnungen:** BaFin-Unternehmensdatenbank und Verbraucherwarnungen, FSMA- und Consob-Listen, CFTC (bei US-Firmen); Nachrichten (Finance Magnates, FX News Group) nach Namen + „payout“ durchsuchen.
- [ ] **AGB-Stand und Änderungsklausel:** Datum der Fassung; dürfen Regeln rückwirkend für laufende Konten geändert werden?
- [ ] **Automatisierung:** KI-, Bot-, VPS-, Copy-Trading- und HFT-Klauseln; schriftliche Bestätigung für genau diesen Bot.
- [ ] **Auszahlung:** Rhythmus, Mindestbetrag, Höchstbetrag, Methoden nach Deutschland, Gebühren, Konsistenzregeln, Identitätsprüfung.
- [ ] **Erstattung:** Gibt es eine Rückerstattung der Gebühr, wann, wie?
- [ ] **Plattform:** Welche Software, wessen Lizenz (MetaQuotes hat 2024 Lizenzen entzogen)?
- [ ] **Recht und Gerichtsstand:** EU-Recht, Schiedsklausel, Verzicht auf Sammelklagen?
- [ ] **Zahlung:** Kreditkarte statt Krypto (Krypto-Zahlungen lassen sich nicht zurückholen).
- [ ] **Beschwerdemuster:** viele verweigerte Auszahlungen in kurzer Zeit (Trustpilot, Foren) als Warnsignal, nicht als Beweis.
- [ ] **Für Deutschland:** Ist Deutschland zugelassen, gibt es ein Live-Konto (Topstep: nein, nur simuliert)?

## Wann ist ein Bot bereit für eine Challenge

Vorschlag zum Festlegen, bevor Geld fließt. Keine allgemein anerkannte Regel; die Zahlen sind bewusst streng gewählt (siehe [[Wie viele Day Trader gewinnen]], [[Backtesting und Overfitting]]).

| Kriterium | Schwelle (Vorschlag) | Woher |
| --- | --- | --- |
| Geschlossene Trades mit unveränderten Regeln | **≥ 100**, über mindestens 3 Monate | Journal (`Trading/Trades/`, Feld `ergebnis_r`) |
| Erwartungswert nach Kosten | Mittel-R minus Kosten **≥ +0,15 R**, und die untere Grenze eines 95-%-Bootstrap-Intervalls **> 0** | `ergebnis_r` minus Kostenabschlag des Prop-Instruments (Spread, Kommission, Slippage; mindestens 0,05–0,10 R) |
| Maximaler Drawdown | 99-%-Wert der simulierten Drawdowns × Risiko je Trade **≤ 50 %** der Maximalverlust-Grenze der Firma | Monte-Carlo auf die R-Folge |
| Schlechtester Tag | schlimmster denkbarer Tag (Trades/Tag × Risiko je Trade + Slippage) **< Tagesgrenze** der Firma | Bot-Limits |
| Simulierte Bestehensquote | p × q (bestehen × auszahlen) **über der Gewinnschwelle** der Gebühr | siehe unten und [[Kauf und Ablauf einer Challenge#Kosten-Nutzen-Rechnung]] |
| Regeltreue | 0 Regelbrüche in den letzten 30 Trades (kein Trade ohne Stop, keine Trades in Sperrzeiten) | Journal, `/trader-risk` |
| Probelauf | ≥ 20 Handelstage auf dem kostenlosen Testkonto der Firma (FTMO Free Trial, Topstep Practice), mit Abweichung zum Paper-Journal im erwarteten Rahmen | Testkonto |
| Regelkonformität der Technik | Betrieb, Orderzahl, Sperrzeiten passen zu den AGB, schriftlich bestätigt | AGB, Support |

### Die Prop-Regeln auf die eigenen Trades legen

1. Aus dem Journal je Trade `datum` und `ergebnis_r` lesen, Kostenabschlag abziehen.
2. Risiko je Trade in Prozent des Prop-Kontos festlegen (z. B. 0,5 %).
3. Viele zufällige Reihenfolgen der **Handelstage** ziehen (Tage als Block, damit Tagesverluste realistisch bleiben), 10.000-mal.
4. Für jede Reihe Tag für Tag prüfen: Tagesverlust gerissen? Maximalverlust (statisch oder nachziehend) gerissen? Gewinnziel erreicht? Mindesttage, Konsistenzregel (bester Tag ≤ 50 %)?
5. Ergebnis: Anteil bestanden (p), Anteil gerissen, mittlere Dauer bis zum Ziel. Danach dieselbe Simulation für die Funded-Phase bis zur ersten Auszahlung (q).

> [!example] Größenordnung, FTMO 2-Step mit 0,5 % Risiko je Trade
> Ziel 10 % = **20 R**, Tagesgrenze 5 % = 10 R, Maximalverlust 10 % = 20 R. Mit 0,15 R Erwartungswert nach Kosten braucht der Bot im Mittel rund **130 Trades** für Phase 1. Der Weg dorthin schwankt stark; die Simulation zeigt, wie oft er vorher 20 R verliert. Mit dem aktuellen Tageslimit des Bots ($2.500 auf $100.000 = 2,5 %) bliebe man unter der 5-%-Grenze, bei FTMO 1-Step (3 %) wäre der Abstand knapp.

## Für diesen Bot

- **Noch nicht bereit:** 5 geschlossene Paper-Trades vom 22. und 23.10.2026, zusammen +3,35 R (−0,72, +1,59, +0,72, −0,26, +2,02). Das ist über zwei Tage kein Beleg für einen Vorteil; nach dem Vorschlag oben fehlen mindestens 95 Trades.
- **Cloud passt nicht überall:** Der Autopilot läuft in Claude-Code-Cloud-Sitzungen. Topstep verbietet VPS und verlangt Orders vom eigenen Gerät; FTMO erlaubt Bots, hat aber eine KI-Klausel nach Ermessen. Vor jedem Kauf genau das schriftlich klären.
- **Sperrzeiten nachbauen:** FTMOs Gap-Regel (Unternehmenszahlen, Makro-Termine, letzte zwei Stunden vor einem längeren Handelsschluss) würde das Einstiegsfenster bis 15:30 NY treffen, falls der Bot Aktien-CFDs handelt. Das gehört als harte Regel in `/trader-risk`, nicht in den Prompt. Termine: [[Makro-Termine]].
- **Deutschland bei Topstep nur simuliert:** Ein Live-Konto gibt es dort für Deutschland nicht; Auszahlungen bleiben vertragliche Rewards aus einem simulierten Konto.
- **Steuern ab der ersten Auszahlung:** Paper Trading und eine nicht bestandene Challenge erzeugen keine Einnahmen; die Gebühr wäre im besten Fall Werbungskosten oder Betriebsausgabe. Ab der ersten Auszahlung Belege sammeln und eine Steuerberaterin fragen (§ 15 oder § 22 Nr. 3, Gewerbe ja/nein).
- Mit echtem Geld gilt weiter [[Trading/Regeln]]: Kauf einer Challenge und jede echte Order nur mit ausdrücklichem Ja von Yannick. Keine Zugangsdaten, Ausweisdaten oder Steuernummern in den Vault.

## Quellen

Abgerufen am 23.10.2026.

Gesetze:
- § 15 EStG – https://www.gesetze-im-internet.de/estg/__15.html
- § 22 EStG (Nr. 3, Freigrenze 256 €, Verlustverrechnung) – https://www.gesetze-im-internet.de/estg/__22.html
- § 11 GewStG (Freibetrag 24.500 €) – https://www.gesetze-im-internet.de/gewstg/__11.html
- § 19 UStG (Kleinunternehmer 25.000 €/100.000 €) – https://www.gesetze-im-internet.de/ustg_1980/__19.html
- § 3a UStG (Ort der sonstigen Leistung) – https://www.gesetze-im-internet.de/ustg_1980/__3a.html
- § 89 AO (verbindliche Auskunft) – https://www.gesetze-im-internet.de/ao_1977/__89.html
- § 356 BGB (Erlöschen des Widerrufsrechts) – https://www.gesetze-im-internet.de/bgb/__356.html
- § 1031 ZPO (Schiedsvereinbarung mit Verbrauchern) – https://www.gesetze-im-internet.de/zpo/__1031.html
- Brüssel-Ia-VO (EU) Nr. 1215/2012 – https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32012R1215
- Rom-I-VO (EG) Nr. 593/2008 – https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32008R0593
- CMS: The ODR platform is closing (VO 2024/3228) – https://cms.law/en/deu/legal-updates/the-odr-platform-is-closing-what-businesses-need-to-know

Behörden:
- CFTC v. Traders Global Group, Complaint (29.08.2023) – https://www.cftc.gov/media/9196/enftradersglobalgroupcomplaint082923/download
- CFTC Press Release 8771-23 – https://www.cftc.gov/PressRoom/PressReleases/8771-23
- CFTC Press Release 9074-25: Acting Chairman Pham Statement on Court Sanctions Against CFTC (13.05.2025) – https://www.cftc.gov/PressRoom/PressReleases/9074-25
- Special Master Report and Recommendation (13.05.2025) – https://www.cftc.gov/media/12106/ogc_KazmiReportRecommendationSactions051325/download
- OSC: Temporary cease trade order against myforexfunds.com – https://osc.ca/en/news-events/news/osc-issues-temporary-cease-trade-order-against-myforexfundscom
- BaFin Verbraucherwarnung Trading Kapital (21.07.2025) – https://www.bafin.de/SharedDocs/Veroeffentlichungen/DE/Verbrauchermitteilung/unerlaubte/2025/meldung_2025_07_21_trading_kapital_com.html
- FSMA: The FSMA warns consumers against shadow investment game (07.03.2024) – https://www.fsma.be/en/warnings/fsma-warns-consumers-against-shadow-investment-game

Firmen:
- FTMO Challenge Terms and Conditions (Stand 12.10.2026) – https://ftmo.com/en/terms-and-conditions/
- FTMO: Forbidden Trading Practices – https://ftmo.com/en/forbidden-trading-practices/
- FTMO: Which instruments can I trade and what strategies am I allowed to use? – https://ftmo.com/en/faq/which-instruments-can-i-trade-and-what-strategies-am-i-allowed-to-use/
- Topstep Terms of Use (Stand 21.09.2026) – https://www.topstep.com/terms-of-use
- Topstep Help Center: Prohibited Conduct – https://help.topstep.com/en/articles/10296582-prohibited-conduct
- Topstep Help Center: TopstepX API Access – https://help.topstep.com/en/articles/11187768-topstepx-api-access
- Topstep Help Center: Payout Policy (W-8BEN) – https://help.topstep.com/en/articles/8284233-topstep-payout-policy
- Topstep Help Center: Am I Eligible to Trade with Topstep? – https://help.topstep.com/en/articles/8284116-am-i-eligible-to-trade-with-topstep
- Apex Trader Funding: Performance Account and Compliance – https://support.apextraderfunding.com/hc/en-us/articles/31519788944411-Performance-Account-PA-and-Compliance
- Apex Trader Funding: User Agreement – https://dashboard.apextraderfunding.com/agreement/user-agreement

Presse:
- Finance Magnates: In a Blow to the CFTC, US Court Throws Out My Forex Funds Lawsuit (14.05.2025) – https://www.financemagnates.com/forex/my-forex-funds-parent-defeats-cftc-in-court-as-judge-imposes-sanctions/
- Willkie Compliance Concourse: New Jersey Federal Judge Dismisses Forex Case With Prejudice – https://complianceconcourse.willkie.com/articles/new-jersey-federal-judge-dismisses-forex-case-with-prejudice-and-awards-attorney-fees/
- Bloomberg Government: Canada Court Rebukes Securities Watchdog Over Forex Trading Case – https://news.bgov.com/securities-law/canada-court-rebukes-securities-watchdog-over-forex-trading-case
- FX News Group: Prop trading firm True Forex Funds shut down by MetaQuotes move – https://fxnewsgroup.com/forex-news/retail-forex/exclusive-prop-trading-firm-true-forex-funds-shut-down-by-metaquotes-move/
- Finance Magnates: The Funded Trader pauses all operations – https://www.financemagnates.com/forex/breaking-prop-trading-firm-the-funded-trader-pauses-all-operations/
- FinanceFeeds: The Funded Trader is back? Traders report account closures – https://financefeeds.com/the-funded-trader-is-back-traders-report-account-closures/
- Finance Magnates: FundingTicks begins winding down (19.01.2026) – https://www.financemagnates.com/forex/following-profit-cuts-and-trading-limits-prop-firm-fundingticks-begins-winding-down/
- Finance Magnates: Seacrest ends prop trading (04.02.2026) – https://www.financemagnates.com/forex/seacrest-ends-prop-trading-after-integrating-myfundedfx-shifts-focus-to-cfds/
- Finance Magnates: ATFX suspends its prop trading operations (06.06.2026) – https://www.financemagnates.com/forex/atfx-suspends-its-prop-trading-operations/
- Finance Magnates: Prop Trading Slips Down Paris' Agenda as the US Steps Up – https://www.financemagnates.com/forex/prop-trading-slips-down-paris-agenda-as-the-us-steps-up/
- Finance Magnates: Another Regulator Warns against Prop Firms (Consob) – https://www.financemagnates.com/forex/another-regulator-warns-against-prop-firms-calls-them-trading-video-games
- LaPresse: Consob, attenzione ai „videogiochi“ di trading online (08.07.2024) – https://www.lapresse.it/economia/2024/07/08/finanza-la-consob-attenzione-ai-videogiochi-di-trading-online/

Ratgeber (teils mit Affiliate- oder Produktinteressen, als Meinung lesen):
- der/proptrader: Prop-Trading & Steuern in Deutschland (2026) – https://derproptrader.de/blog/prop-trading-steuern-in-deutschland
- Track360: Prop Trading Steuern 2026 (Anbieter von Affiliate-Software) – https://track360.io/de/blog/prop-trading-steuern-deutschland-2026
- Trader Notion: Prop Firms That Shut Down in 2023–2026 (mit Referral-Links) – https://www.tradernotion.com/blog/prop-firms-that-shut-down-in-2023-2026
- fundedtrading.com: What happened to True Forex Funds – https://fundedtrading.com/true-forex-funds-shutdown/
- fundedtrading.com: What happened to My Forex Funds – https://fundedtrading.com/what-happened-to-my-forex-funds/
- AI Journal: Prop Firms Say They Allow AI Trading. Their Rulebooks Say Something Else – https://aijourn.com/prop-firms-say-they-allow-ai-trading-their-rulebooks-say-something-else/
