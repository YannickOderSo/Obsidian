---
name: gedaechtnis
description: >-
  Langzeitgedächtnis im Obsidian-Vault. Sucht vor einer Antwort, was über
  den Nutzer, seine Projekte, Entscheidungen und Erkenntnisse schon
  bekannt ist, und hält Neues als verlinkte Notiz fest. Verwenden, wenn der
  Nutzer sagt "merk dir", "vergiss nicht", "notier dir", "erinnerst du
  dich", "was weißt du über", "was hatten wir zu X entschieden", "räum das
  Gedächtnis auf", oder wenn im Gespräch eine dauerhafte Vorliebe, eine
  Entscheidung, eine Person, ein Projekt oder eine Lehre auftaucht, die
  über diese Sitzung hinaus zählt.
argument-hint: "[merken | erinnern | aufräumen] [Thema]"
---

# gedaechtnis

Der Vault ist das Gedächtnis. Was hier steht, weiß die nächste Sitzung. Was
nicht hier steht, ist vergessen. `Gedächtnis/Kern.md` lädt jede Sitzung über
`CLAUDE.md` von selbst, der Rest wird bei Bedarf gelesen.

## Aufbau

| Ort | was hinein gehört |
| --- | --- |
| `Gedächtnis/Kern.md` | das Wichtigste über den Nutzer und wie er arbeiten will. Höchstens 40 Zeilen, wird immer geladen |
| `Gedächtnis/Index.md` | eine Zeile je Notiz mit Link, nach Bereichen. Erst hier suchen |
| `Gedächtnis/Personen/` | eine Notiz je Person: Rolle, Bezug, was wichtig ist |
| `Gedächtnis/Projekte/` | eine Notiz je Projekt: Ziel, Stand, Repos, offene Punkte |
| `Gedächtnis/Entscheidungen/` | `JJJJ-MM-TT Titel.md`: was entschieden wurde, warum, was verworfen wurde |
| `Gedächtnis/Erkenntnisse/` | eine Notiz je Thema (z. B. `Trading.md`): Lehren, die sich wiederholen |
| `Tagesnotizen/JJJJ-MM-TT.md` | was heute passiert ist, kurz, mit Links |
| `00 Eingang/` | Unsortiertes, das später einsortiert wird |
| `Trading/` | Journal und Regeln, siehe Skill `trading-journal` |

## Erinnern

1. `Gedächtnis/Index.md` lesen, dann gezielt die verlinkten Notizen.
2. Reicht das nicht, im Vault suchen (Grep über `*.md`, ohne `trader/` und
   `.claude/`), auch nach Synonymen und Links `[[...]]`.
3. In der Antwort sagen, woher etwas stammt ("laut [[Neuzeit]] ..."). Steht
   nichts da, das sagen und nicht raten.

## Merken

Nur festhalten, was über diese Sitzung hinaus zählt: Vorlieben, Fakten über
Personen und Projekte, Entscheidungen mit Begründung, wiederkehrende Lehren.
Keine Gesprächsprotokolle, keine Dinge, die im Code oder in Git schon stehen,
keine Passwörter, Schlüssel oder Kontodaten.

1. Erst suchen, ob es schon eine passende Notiz gibt, und die erweitern statt
   eine zweite anzulegen.
2. Neue Notiz mit der passenden Vorlage aus `Vorlagen/` und diesen Eigenschaften:

   ```yaml
   ---
   typ: person | projekt | entscheidung | erkenntnis | notiz
   erstellt: 2026-10-21
   aktualisiert: 2026-10-21
   quelle: Gespräch | Repo | Trade | Nutzer
   tags: []
   ---
   ```

3. Mit bestehenden Notizen verlinken (`[[Neuzeit]]`, `[[Yannick]]`), damit der
   Graph trägt. Dateinamen ohne Datum, außer bei Entscheidungen und
   Tagesnotizen.
4. Eine Zeile in `Gedächtnis/Index.md` ergänzen.
5. Nur wenn es wirklich jede Sitzung braucht: in `Kern.md`, knapp. Lieber dort
   auf die Notiz verlinken als den Inhalt kopieren.
6. Bei Widerspruch zu Altem: die alte Aussage nicht stumm überschreiben,
   sondern ändern und `aktualisiert` setzen. Bei Entscheidungen die neue als
   eigene Notiz anlegen und die alte darauf verlinken ("ersetzt durch").
7. Dem Nutzer in einem Satz sagen, was gemerkt wurde und wo.

Fragt der Nutzer "merk dir X" ausdrücklich, immer festhalten. Taucht etwas
nur nebenbei auf, kurz nachfragen, ob es gemerkt werden soll, außer es ist
eindeutig dauerhaft (ein neues Projekt, eine getroffene Entscheidung).

## Tagesnotiz

Am Ende einer Sitzung mit Ergebnissen eine Zeile oder drei in
`Tagesnotizen/<heute>.md` (Vorlage `Vorlagen/Tagesnotiz.md`): was erledigt
wurde, mit Links auf Notizen, Trades und Commits. Gibt es die Datei schon,
unten ergänzen.

## Aufräumen

Auf Nachfrage, oder wenn `00 Eingang/` mehr als zehn Notizen hat: einsortieren,
Doppeltes zusammenführen, tote Links reparieren, `Index.md` mit dem Inhalt
abgleichen, `Kern.md` unter 40 Zeilen halten. Vorher sagen, was sich ändert.

## Sichern

Der Vault ist ein Git-Repo. In einer Cloud-Sitzung ist der Container
vergänglich: nach Änderungen am Gedächtnis committen und pushen, sonst ist es
in der nächsten Sitzung weg. Commit-Nachricht auf Deutsch, z. B.
`Gedächtnis: Entscheidung zu Calendly`. Lokal synchronisiert der Nutzer mit
Obsidian (Plugin Obsidian Git) oder per Hand.
