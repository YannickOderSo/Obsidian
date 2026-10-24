---
typ: erkenntnis
erstellt: 2026-10-22
aktualisiert: 2026-10-22
quelle: Gespräch
tags:
  - erkenntnis
  - trading
---

# Alpaca unter Windows

Wie [[Yannick]] den Alpaca-MCP-Server für [[Trading/Regeln|Paper Trading]] in Claude Desktop auf seinem PC (`yannick-pc`) eingerichtet hat, am 2026-10-22. Die Schlüssel stehen nur in `claude_desktop_config.json` auf dem PC, nie hier.

- Paper-Konto bei Alpaca, Startguthaben 100.000 $ Spielgeld. Die Skills rechnen trotzdem mit dem Budget aus `trader/config.json`.
- `uv` braucht in PowerShell `-ExecutionPolicy ByPass` beim Installieren und liegt unter `C:\Users\Feuer\.local\bin\uvx.exe`. In der Konfiguration den vollen Pfad eintragen, Claude Desktop findet `uvx` sonst nicht.
- Claude Desktop ist als App-Paket installiert und sieht ein eigenes AppData. Was `uv` von dort nach `AppData\Roaming\uv` schreibt, ist in PowerShell unsichtbar. Darum im `env`-Block `UV_PYTHON_INSTALL_DIR` und `UV_CACHE_DIR` auf `C:\Users\Feuer\uv-data\…` setzen und Python vorher in PowerShell mit denselben Variablen installieren.
- `--python 3.12` in `args`: Zwei gleichzeitige Starts hatten Python 3.15 beim Herunterladen zerstört.
- `claude_desktop_config.json` enthält auch die App-Einstellungen. `mcpServers` gehört auf die oberste Ebene, nach `preferences` mit Komma. Fehler „Expected ',' or '}'“ heißt fast immer: Komma oder Klammer fehlt.
- Rechte in Claude Desktop: Order-Werkzeuge „Needs approval“, Optionen, Krypto und Sammelaktionen „Blocked“, Lese-Werkzeuge „Always allow“.
- Eine Cloud-Sitzung von Claude Code erreicht diesen Server nicht. Das Konto nur in Claude Desktop prüfen.
