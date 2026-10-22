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

# Steuern in Deutschland

Wie Gewinne und Verluste aus dem Handel mit US-Aktien bei einem in Deutschland steuerpflichtigen Privatanleger besteuert werden, besonders bei einem ausländischen Broker wie Alpaca. Stand der Recherche: 22. Oktober 2026.

Zurück zum Hub: [[Trading/Wissen/Übersicht]] · Limits: [[Trading/Regeln]]

> [!warning] Keine Steuerberatung
> Diese Notiz fasst Gesetze und Veröffentlichungen zusammen, sie ersetzt keine Steuerberatung. Steuerrecht ändert sich, mehrere Punkte unten sind strittig oder vor Gericht anhängig. Vor dem ersten echten Trade und vor jeder Steuererklärung mit Auslandsbroker eine Steuerberaterin oder einen Lohnsteuerhilfeverein fragen.

> [!success] Paper Trading ist steuerlich irrelevant
> Im Paper-Konto fließt kein Geld. Es gibt nichts zu versteuern und nichts zu erklären. Alles Folgende wird erst wichtig, wenn mit echtem Geld gehandelt wird.

## Abgeltungsteuer

Gewinne aus dem Verkauf von Aktien sind Einkünfte aus Kapitalvermögen (§ 20 Abs. 2 EStG) und werden mit dem gesonderten Steuersatz von **25 %** besteuert (§ 32d Abs. 1 EStG), unabhängig von der Haltedauer. Dazu kommen 5,5 % Solidaritätszuschlag auf die Steuer und ggf. Kirchensteuer. Die Kirchensteuer senkt die Abgeltungsteuer etwas (Formel in § 32d Abs. 1: (e − 4q) / (4 + k)).

| Fall | Abgeltungsteuer | Soli | Kirchensteuer | gesamt |
| --- | --- | --- | --- | --- |
| ohne Kirchensteuer | 25,00 % | 1,375 % | – | **26,375 %** |
| Kirchensteuer 8 % (Bayern, Baden-Württemberg) | 24,51 % | 1,35 % | 1,96 % | **27,82 %** |
| Kirchensteuer 9 % (übrige Länder) | 24,45 % | 1,34 % | 2,20 % | **27,99 %** |

Liegt der persönliche Steuersatz unter 25 %, kann man die Günstigerprüfung beantragen (§ 32d Abs. 6 EStG).

## Sparerpauschbetrag

**1.000 €** je Person, **2.000 €** bei Zusammenveranlagung (§ 20 Abs. 9 EStG), seit 2023 unverändert und auch 2026 so. Tatsächliche Kosten (Datenabo, Software) dürfen **nicht** abgezogen werden. Bei einer deutschen Bank wird er über den Freistellungsauftrag berücksichtigt; bei einem ausländischen Broker erst in der Steuererklärung.

## Verlustverrechnung

- Verluste aus Kapitalvermögen dürfen nicht mit Lohn oder anderen Einkunftsarten verrechnet werden; sie werden in Folgejahre vorgetragen (§ 20 Abs. 6 Satz 1–3 EStG).
- **Aktienverluste** dürfen nur mit **Aktiengewinnen** verrechnet werden (§ 20 Abs. 6 Satz 4 EStG). Ein Aktienverlust mindert also nicht die Steuer auf Zinsen, Dividenden oder ETF-Gewinne. Banken führen dafür einen eigenen Aktien-Verlustverrechnungstopf.
- **Anhängig:** Der BFH hält diese Beschränkung für verfassungswidrig und hat sie 2020 dem Bundesverfassungsgericht vorgelegt (VIII R 11/18, beim BVerfG 2 BvL 3/21). Das BVerfG hatte eine Entscheidung für 2026 angekündigt; eine veröffentlichte Entscheidung habe ich bis zum 22.10.2026 nicht gefunden. Steuerbescheide ergehen in diesem Punkt vorläufig.
- Die frühere Grenze von 20.000 € für Verluste aus Termingeschäften (Optionen) wurde mit dem Jahressteuergesetz 2024 gestrichen. Für den Vault ohne Bedeutung, Optionen sind aus.

### Beispiele

| Jahr | Aktiengewinne | Aktienverluste | steuerpflichtig | Steuer (26,375 %) |
| --- | --- | --- | --- | --- |
| A | 1.800 € | 1.500 € | 300 € − 1.000 € Pauschbetrag = 0 € | 0 € |
| B | 4.000 € | 1.200 € | 2.800 € − 1.000 € = 1.800 € | 474,75 € |
| C | 600 € | 1.500 € | 0 €, Verlustvortrag 900 € nur für künftige Aktiengewinne | 0 € |

Im Fall C bleibt der Verlust „gefangen“, auch wenn im selben Jahr Zinsen anfallen.

## Ausländischer Broker: selbst erklären

Ein US-Broker wie Alpaca behält **keine** deutsche Kapitalertragsteuer ein und stellt keine deutsche Steuerbescheinigung aus. Kapitalerträge ohne Steuerabzug **müssen** in der Steuererklärung angegeben werden (§ 32d Abs. 3 EStG), mit der **Anlage KAP**.

- Im Formular 2025 stehen ausländische Erträge ohne Steuerabzug in Zeile 19, darin enthaltene Aktiengewinne zusätzlich in Zeile 20, Verluste in eigenen Zeilen. Die Zeilennummern ändern sich fast jedes Jahr, daher das aktuelle Formular und die Anleitung prüfen.
- Unterlagen: vollständige Trade-Historie mit Datum, Stückzahl, Kurs in USD und Gebühren. Ausländische Jahresberichte folgen nicht der deutschen Logik (kein Aktientopf, keine Euro-Umrechnung), man muss selbst rechnen.
- Das kann eine Steuererklärung nötig machen, auch wenn man bisher keine abgeben musste.

## Währungsumrechnung

Bei Geschäften in Fremdwährung werden die **Anschaffungskosten zum Kurs am Kauftag** und die **Einnahmen zum Kurs am Verkaufstag** in Euro umgerechnet (§ 20 Abs. 4 Satz 1 EStG). Der Wechselkursgewinn oder -verlust steckt damit im Aktiengewinn.

Beispiel mit dem TSLA-Plan der Skills (Wechselkurse angenommen):

| | USD | Kurs EUR/USD | EUR |
| --- | --- | --- | --- |
| Kauf 8 × 364,18 | 2.913,44 $ | 1,1600 | 2.511,59 € |
| Verkauf 8 × 370,04 | 2.960,32 $ | 1,1590 | 2.554,20 € |
| Gewinn | 46,88 $ | | **42,62 €** |

Bei Day Trades ist der Kurseffekt klein, weil Kauf und Verkauf am selben Tag liegen; über ein Jahr mit vielen Trades muss aber jeder einzeln umgerechnet werden. Welcher Kurs genau zu nehmen ist (Devisenkurs der Bank oder Referenzkurs), habe ich nicht verbindlich geklärt: mit der Steuerberatung abstimmen.

> [!warning] Fallstrick USD-Guthaben
> Wer Euro in Dollar tauscht und Dollar auf dem Konto hält, hat steuerlich ein **Fremdwährungsguthaben**. Laut BMF-Schreiben vom 19.05.2022 (Rz. 131, bestätigt am 14.05.2025) gilt: Bei **verzinsten** Fremdwährungskonten sind Währungsgewinne Kapitaleinkünfte (§ 20 EStG); bei **unverzinsten** Guthaben gilt § 23 EStG (privates Veräußerungsgeschäft, steuerpflichtig innerhalb eines Jahres, Freigrenze 1.000 € im Jahr seit 2024). Ob das Kauf von Aktien mit Dollar schon eine „Veräußerung“ der Dollar ist und wie ein Broker-Verrechnungskonto einzuordnen ist, ist strittig; das FG Rheinland-Pfalz hat im Oktober 2025 ernstliche Zweifel an der Verwaltungsauffassung geäußert. Bei vielen Trades in USD unbedingt fachlich klären.

## US-Steuern

- **Kursgewinne:** Für Personen ohne US-Steuerpflicht (Nonresident Aliens) sind Gewinne aus dem Verkauf von US-Aktien in der Regel in den USA steuerfrei, solange man sich weniger als 183 Tage im Jahr in den USA aufhält und kein US-Geschäftsbetrieb vorliegt (IRS Publication 519). Versteuert wird in Deutschland.
- **Dividenden:** Ohne Formular **W-8BEN** behält der Broker 30 % US-Quellensteuer ein, mit W-8BEN nach dem Doppelbesteuerungsabkommen **15 %**. Diese 15 % werden auf die deutsche Abgeltungsteuer angerechnet (§ 32d Abs. 5 EStG). Wer flat bis 15:55 ist, hält über Nacht nichts und bekommt in der Regel keine Dividenden.
- **Publicly Traded Partnerships (PTP):** Beim Verkauf von Anteilen an US-Partnerships (z. B. manche Energie-MLPs) müssen Broker seit 2023 bei Nicht-US-Personen 10 % des **Bruttoerlöses** einbehalten (Section 1446(f)), sofern die PTP keine Ausnahme meldet. Bei einer Position von rund 2.900 $ wären das etwa 290 $ Einbehalt, fast das Sechsfache des geplanten Risikos von 50 $: solche Titel meiden.

## Gewerblicher Handel als Risiko

Nach der Rechtsprechung des BFH ist der An- und Verkauf von Wertpapieren für eigene Rechnung auch in großem Umfang in der Regel **private Vermögensverwaltung**. Gewerblich wird es nur ausnahmsweise, wenn das Gesamtbild einem Händler oder einer Bank gleicht (z. B. Handel für andere, eigene Büroorganisation, Anbieten gegenüber der Öffentlichkeit). Dann gälten der normale Einkommensteuertarif und ggf. Gewerbesteuer, Verluste wären dafür voll verrechenbar. Für einen Privatanleger mit eigenem Geld ist das Risiko gering, aber nicht null; viele Trades allein machen es nicht gewerblich.

## Sonstiges

- **AWV-Meldung:** Reine Überweisungen auf ein eigenes Konto im Ausland sind laut Bundesbank-FAQ nicht meldepflichtig. Zahlungen an Ausländer über 12.500 € können nach § 67 AWV meldepflichtig sein. Bei 5.000 $ Budget kaum relevant, beim Wechsel zu größeren Beträgen prüfen.

## Im Vault

- Solange `"paper": true` gilt, entsteht kein steuerlicher Vorgang.
- Das Journal (`Trading/Trades/`, `Trading/Statistik.md`) rechnet in Dollar und R. Für die Steuer bräuchte man je Trade Datum, Stückzahl, Kurse in USD und die Wechselkurse beider Tage. Wer live geht, sollte das von Anfang an mitschreiben.
- Keine Kontodaten, Steuer-IDs oder Schlüssel in den Vault (siehe `CLAUDE.md`).
- Siehe auch [[Paper Trading bei Alpaca]] und [[Wie viele Day Trader gewinnen]].

## Quellen

- § 20 EStG (Fassung JStG 2024) – https://dejure.org/gesetze/EStG/20.html
- § 32d EStG – https://dejure.org/gesetze/EStG/32d.html
- § 23 EStG – https://www.buzer.de/23_EStG.htm
- Lohnsteuer kompakt: Private Veräußerungsgeschäfte – Erhöhung der Freigrenze auf 1.000 Euro – https://www.lohnsteuer-kompakt.de/steuerwissen/private-veraeusserungsgeschaefte-erhoehung-der-freigrenze-auf-1-000-euro/
- capitalo.de: Abgeltungssteuer (Sätze mit Kirchensteuer) – https://www.capitalo.de/lexikon/abgeltungssteuer
- Finanztip: Freistellungsauftrag / Sparerpauschbetrag – https://www.finanztip.de/freistellungsauftrag/
- steuertipps.de: Aktienverluste nur mit Aktiengewinnen verrechenbar? Urteil für 2026 erwartet – https://www.steuertipps.de/altersvorsorge-rente-finanzen/aktienverluste-nur-mit-aktiengewinnen-verrechenbar-verfassungswidrig
- taxgate: BVerfG – Entscheidung zur Verlustverrechnungsbeschränkung für Aktienverluste kommt – https://taxgate.com/bverfg-entscheidung-zur-verlustverrechnungsbeschraenkung-fuer-aktienverluste-kommt/
- DSW (27.03.2026): Stellungnahme für das Bundesverfassungsgericht – https://www.dsw-info.de/presse/pressemitteilungen-2026/dsw-stellungnahme-fuer-das-bundesverfassungsgericht-verlustverrechnungsbeschraenkung-fuer-aktien-verstoesst-gegen-gleichheitsgrundsatz/
- CMS: Verlustverrechnungsbeschränkung bei Termingeschäften – Gesetzgeber schafft Vorschrift ab – https://cms.law/de/deu/legal-updates/verlustverrechnungsbeschraenkung-bei-termingeschaeften-gesetzgeber-schafft-vorschrift-ab
- Haufe: Anlage KAP 2025 – Kapitalerträge ohne Steuerabzug (Zeilen 18–26) – https://www.haufe.de/id/beitrag/anlage-kap-einkuenfte-aus-kapitalvermoegen-2025-3-kapitalertraege-ohne-steuerabzug-anlagekap-zeilen1826-HI16887024.html
- Haufe (03.02.2026): Private Fremdwährungskonten – „Neue“ steuerliche Regeln seit 2025? – https://www.haufe.de/steuern/steuerwissen-tipps/private-fremdwaehrungskonten-neue-steuerliche-regeln-seit-2025_170_671044.html
- Kleeberg (13.07.2026): Fremdwährungskonten im Privatvermögen – Zweifel an Besteuerung fiktiver Kursgewinne – https://www.kleeberg.de/en/2026/07/13/fremdwaehrungskonten-im-privatvermoegen-zweifel-an-besteuerung-fiktiver-kursgewinne/
- IRS Publication 519 (2025): U.S. Tax Guide for Aliens – https://www.irs.gov/publications/p519
- IRS: Instructions for Form W-8BEN – https://www.irs.gov/pub/irs-pdf/iw8ben.pdf
- IRS: Tax treaty Germany (Dokumente) – https://www.irs.gov/pub/irs-trty/germany.pdf
- juhn.com: Doppelbesteuerung USA (DBA, Dividenden 15 %) – https://www.juhn.com/fachwissen/internationales-steuerrecht/dba-usa/
- IRS: Instructions for Form 8288 (01/2026), Section 1446(f) – https://www.irs.gov/instructions/i8288
- EY Tax News (04.01.2023): IRS guidance for brokers on transfers of interests in PTPs – https://taxnews.ey.com/news/2023-0026
- BFH, Urteil X R 14/07 (Abgrenzung gewerblicher Wertpapierhandel), NWB – https://datenbank.nwb.de/Dokument/310602/
- IWW: BFH – Abgrenzung zwischen gewerblichem Wertpapierhandel und privater Vermögensverwaltung (X R 7/99) – https://www.iww.de/gstb/archiv/bundesfinanzhof-abgrenzung-zwischen-gewerblichem-wertpapierhandel-und-privater-vermoegensverwaltung-f45259
- Deutsche Bundesbank: FAQs zu AWV-Zahlungsmeldungen – https://bundesbank.de/resource/blob/611818/91551718a7066e282189b917027a4b8b/472B63F073F071307366337C94F8C870/faqs-zur-awv-zahlungsmeldungen-data.pdf
