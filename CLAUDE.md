# Obsidian-Vault: Gedächtnis und Trading-Journal

Dieses Repo ist ein Obsidian-Vault und zugleich das Gedächtnis von Claude. Antworten und Notizen auf Deutsch.

@Gedächtnis/Kern.md

## Gedächtnis

- Vor Antworten zu Personen, Projekten oder früheren Entscheidungen erst `Gedächtnis/Index.md` und die verlinkten Notizen lesen. Regeln zum Merken, Erinnern und Aufräumen: Skill `gedaechtnis`.
- Was über die Sitzung hinaus zählt, als verlinkte Notiz festhalten, nicht nur im Chat sagen. Keine Schlüssel, Passwörter oder Kontodaten in den Vault.
- `Gedächtnis/Kern.md` bleibt unter 40 Zeilen, es wird jede Sitzung geladen.
- In einer Cloud-Sitzung nach Änderungen am Gedächtnis committen und pushen, sonst sind sie weg.

## Trading

- Die Day-Trader-Skills (`/trader-scanner` bis `/trader-pelosi`, in `.claude/skills/trader-*`) schreiben nach `trader/`. Befehle immer in der Wurzel dieses Repos ausführen.
- Nach jedem Schritt der Kette (`trader-exit`, `-timemachine`, `-budget`, `-risk`, `-broker`) den Trade mit dem Skill `trading-journal` ins Journal schreiben. Nach dem Ausstieg schließen und die Reflexion mit dem Nutzer festhalten.
- Paper Trading ist Standard (`"paper": true` in `trader/config.json`). Nie `paper` oder Limits in `trader/config.json` ändern, ohne dass der Nutzer es verlangt.
- Autonomes Paper-Experiment (Freigabe 2026-10-22): Solange `"paper": true` gilt und der Endpunkt `paper-api.alpaca.markets` ist, darf Claude Orders selbst schicken, auch aus geplanten Läufen, aber nur über `.claude/scripts/paper_auto.py` und nur nach einem PASS von `trader-risk`. Mit echtem Geld nie eine Order ohne ein ausdrückliches Ja des Nutzers für genau diese Order.
- Blockiert die Cloud-Umgebung eine Datenquelle, auf die Liste der Adressen im README (Abschnitt „In einer Cloud-Sitzung“) verweisen und keine Ergebnisse nachbauen.
- Keine Anlageberatung geben. Quoten der Time Machine sind eine Simulation, keine Vorhersage.

## Aufbau

- `Gedächtnis/`: Kern, Index, Personen, Projekte, Entscheidungen, Erkenntnisse
- `Tagesnotizen/`, `00 Eingang/`, `Vorlagen/`
- `Trading/`: Regeln, Übersicht mit `Trades.base`, `Trades/` (eine Notiz je Trade), `Statistik.md` (erzeugt)
- `trader/`: Daten der Skills, in Obsidian ausgeblendet; nur Einstellungen, Konto und Protokoll sind in Git
- `.claude/skills/`: `gedaechtnis`, `trading-journal` und die Day-Trader-Skills `trader-*` (Kopie von Jakeschincariol/day-trader-skill, Stand `3d0f4ef`; nicht ohne Nachfrage ändern oder aktualisieren)
- Tests: `python3 -m unittest discover -s .claude/tests` (Journal) und `-s .claude/tests/day-trader` (Skills)
