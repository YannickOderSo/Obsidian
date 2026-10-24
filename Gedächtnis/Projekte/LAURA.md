---
typ: projekt
erstellt: 2026-10-24
aktualisiert: 2026-10-24
quelle: Repo
tags:
  - projekt
  - trading
---

# LAURA

L.A.U.R.A („Logical Algorithmic Unified Risk Analytics“): Web-Oberfläche für das Trading dieses Vaults, die [[Yannick]] am 2026-10-23/24 mit Gemini in Google AI Studio gebaut hat. Repo `YannickOderSo/Overview-Obsidian` (öffentlich), Ordner `LAURA/` mit Spezifikationen.

## Ziel

Ein Cockpit für den [[Trading/Autopilot]]: Live-Positionen mit Abstand zu Stop und Ziel, R-Meter, die Kette Setup → Time Machine → Größe → Risikoprüfung → Order je Trade, Auswertung des Journals und ein Betrachter für die Vault-Notizen.

## Stand (geprüft 2026-10-24)

- React 19 + Vite + Tailwind, nur Frontend. Typprüfung und Build laufen fehlerfrei.
- **Alles ist Simulation:** Die Trades (TSLA, AAPL, NVDA, KO) sind Beispiele, der Live-Kurs ist ein Zufallsticker, die „Time Machine“ hat feste Quoten je Symbol statt der echten Simulation. Es gibt keine Verbindung zu Alpaca oder zum Repo; gespeichert wird nur im Browser (localStorage). Die Anzeige „Alpaca Paper Feed verbunden“ stimmt nicht.
- Der Vault steckt als Kopie in `src/data/bundledVault.json` (61 Dateien, Stand vor den echten Autopilot-Trades und vor [[Funded Accounts]]).
- Die Texte in `LAURA/` weichen von den echten Regeln ab: Budget $10.000, Glattstellen 15:30, PDT-Regel (abgeschafft), erfundene Schwellen (EV > 0,15 R, Trefferquote ≥ 40 %), andere Config-Schlüssel und ein anderes Dateiformat für Trades. Maßgeblich bleiben [[Trading/Regeln]], [[Trading/Autopilot]] und `trader/config.json` hier.

## Offen

- **Repo ist öffentlich** und enthält Gedächtnis-Notizen (Personen, [[Neuzeit]]) und eine E-Mail-Adresse in `trader/config.json`. Auf privat stellen oder diese Dateien entfernen (Entscheidung Yannick).
- Echte Daten anbinden: Trades aus `Trading/Trades/` und `trader/state/broker.json` lesen statt Beispieltrades, Kurse nur aus einer echten Quelle, sonst klar als Demo kennzeichnen.
- `LAURA/` an die echten Regeln angleichen, bevor Claude die Dateien als Anleitung nutzt.
