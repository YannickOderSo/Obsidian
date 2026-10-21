---
typ: entscheidung
erstellt: 2026-10-21
aktualisiert: 2026-10-21
quelle: Gespräch
tags:
  - entscheidung
---

# Obsidian als Gedächtnis

## Entscheidung

Dieses Repo ist zugleich Obsidian-Vault und Claude-Code-Projekt. Claude liest zu Beginn jeder Sitzung [[Kern]] und hält Neues nach den Regeln des Skills `gedaechtnis` fest. Day Trading läuft über die Day-Trader-Skills (Jake Schincariol, MIT), jeder Trade landet als Notiz in `Trading/Trades/`.

Die Skills liegen als feste Kopie (Stand `3d0f4ef`) in `.claude/skills/`, nicht als Plugin.

## Warum

- Markdown im Git-Repo: lesbar in Obsidian, durchsuchbar für Claude, versioniert, überlebt vergängliche Cloud-Sitzungen.
- Ein Journal macht sichtbar, ob ein Setup über viele Trades trägt, statt aus dem Bauch zu urteilen.

## Verworfen

- Installation als Plugin: in der Team-Umgebung sind Plugins nicht erlaubt. Die feste Kopie hat zudem den Vorteil, dass sich der Code nicht unbemerkt ändert.

## Leitplanken

- Paper Trading ist Standard. Keine Order ohne ausdrückliches Ja für genau diese Order.
- Keine Schlüssel, Passwörter oder Kontodaten im Vault.
