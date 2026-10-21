# Obsidian-Gedächtnis mit Trading-Journal

Ein Obsidian-Vault, der zugleich das Langzeitgedächtnis von Claude ist, plus ein Journal für die [Day-Trader-Skills](https://github.com/Jakeschincariol/day-trader-skill) von Jake Schincariol (11 Claude-Skills fürs Day Trading, MIT, Paper Trading als Standard).

Claude liest zu Beginn jeder Sitzung `Gedächtnis/Kern.md` (über `CLAUDE.md`), sucht bei Bedarf im Rest des Vaults und hält Neues als verlinkte Notiz fest. Jeder Trade wird eine Notiz in `Trading/Trades/` mit Plan, Quoten der Time Machine, Risiko-Check, Broker-Log und Ergebnis. So lässt sich nach Wochen nachrechnen, ob ein Setup trägt.

**Keine Anlageberatung.** Die meisten Day Trader verlieren Geld. Erst mit Spielgeld üben.

## Einrichten

1. **Vault öffnen:** Repo klonen und in Obsidian „Ordner als Vault öffnen“ wählen. Tagesnotizen, Vorlagen und Bases sind schon eingestellt.
2. **Synchronisieren:** In Obsidian das Community-Plugin *Obsidian Git* installieren (automatisch committen, pushen und pullen), damit Claude und Obsidian denselben Stand sehen.
3. **Claude Code im Vault starten:** `claude` in diesem Ordner. `CLAUDE.md` und die Skills `gedaechtnis` und `trading-journal` laden von selbst.
4. **Day-Trader-Skills:** liegen schon in `.claude/skills/trader-*`, kein Plugin nötig (in Team-Umgebungen sind Plugins oft gesperrt). Die Befehle heißen `/trader-scanner`, `/trader-news` usw. Sie brauchen Python 3.8 oder neuer und nichts zum Installieren.
5. **SEC-Kennung:** In `trader/config.json` `sec_user_agent` auf Name und E-Mail setzen (verlangt die SEC für News und Earnings), oder die Umgebungsvariable `SEC_USER_AGENT`.
6. **Broker, erst wenn gewünscht:** Alpaca-Paper-Konto anlegen und den Alpaca-MCP-Server in Claude verbinden. Schlüssel nur in Umgebungsvariablen, nie im Chat oder im Vault. In Claude für das Order-Werkzeug „Needs approval“ einstellen, nie „Always allow“.

### In einer Cloud-Sitzung

Die Skills holen ihre Daten aus dem Netz. In der Cloud-Umgebung von Claude Code müssen diese Adressen freigegeben sein (Menü der Umgebung in der Titelleiste, **Edit**, **Network access**, **Allowed domains**, „Allow package managers“ angehakt lassen; Anleitung: https://code.claude.com/docs/en/cloud-environments#network-access). Die Freigabe gilt ab einer neuen Sitzung.

| Adresse | gebraucht von |
| --- | --- |
| `www.nasdaqtrader.com` | Scanner (Liste der US-Aktien) |
| `query1.finance.yahoo.com`, `query2.finance.yahoo.com` | Scanner, Entry, Time Machine, Alerts (Kurse) |
| `feeds.finance.yahoo.com` | News (Schlagzeilen) |
| `stooq.com` | Alerts (Ersatzquelle für Kurse) |
| `www.sec.gov`, `data.sec.gov` | News (8-Ks), Analyst (Quartalszahlen) |
| `disclosures-clerk.house.gov` | Pelosi-Tracker |

## Benutzen

| Sag zu Claude | passiert |
| --- | --- |
| „Merk dir, dass …“ | Notiz in `Gedächtnis/`, Eintrag im Index |
| „Was weißt du über Neuzeit?“ | Antwort aus dem Vault, mit Quelle |
| „Scan den Markt“, „Plan für TSLA“ | Day-Trader-Skills, danach Eintrag im Journal |
| „Ich bin bei 370 raus“ | Trade schließen, R und Gewinn, Reflexion |
| „Wie laufen meine Trades?“ | `Trading/Statistik.md`, auch gegen die Quoten der Time Machine |
| „Räum das Gedächtnis auf“ | Eingang einsortieren, Index abgleichen |

Das Journal direkt:

```bash
python3 .claude/skills/trading-journal/journal.py write
python3 .claude/skills/trading-journal/journal.py close --exit 370.04
python3 .claude/skills/trading-journal/journal.py stats --write
```

## Aufbau

```
CLAUDE.md                 Regeln für Claude, lädt Gedächtnis/Kern.md
Gedächtnis/               Kern, Index, Personen, Projekte, Entscheidungen, Erkenntnisse
Tagesnotizen/             eine Notiz je Tag
00 Eingang/               Unsortiertes
Vorlagen/                 Tagesnotiz, Notiz, Person, Projekt, Entscheidung
Trading/                  Regeln, Übersicht, Trades.base, Trades/, Statistik.md
trader/                   Daten der Day-Trader-Skills (in Obsidian ausgeblendet)
.claude/skills/           gedaechtnis, trading-journal, trader-* (Day-Trader-Skills)
.claude/tests/            Tests fürs Journal, day-trader/ für die Skills
```

Von `trader/` sind nur `config.json`, `portfolio.json`, `alerts.json` und die Protokolle in `state/` in Git, damit Tageslimits auch über Sitzungen hinweg gelten. Der Rest sind Zwischenstände.

## Tests

```bash
python3 -m unittest discover -s .claude/tests -v               # Journal
python3 -m unittest discover -s .claude/tests/day-trader       # Day-Trader-Skills, offline
```

## Herkunft der Day-Trader-Skills

`.claude/skills/trader-*` und `.claude/tests/day-trader/` sind eine unveränderte Kopie von [Jakeschincariol/day-trader-skill](https://github.com/Jakeschincariol/day-trader-skill), Stand `3d0f4ef` (Version 2.0.0), MIT-Lizenz in `.claude/skills/LICENSE-day-trader-skill`. Geändert ist nur `.claude/tests/day-trader/_load.py` (Pfade) und weggelassen `tests/test_repo.py` (prüft den Aufbau des Original-Repos). Der Code liest nur öffentliche Daten (Yahoo Finance, Nasdaq Trader, SEC EDGAR, House Clerk) und platziert selbst keine Orders.

Aktualisieren nur bewusst: neue Version des Originals lesen, dann die Ordner ersetzen und beide Testläufe grün sehen.
