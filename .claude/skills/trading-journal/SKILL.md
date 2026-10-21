---
name: trading-journal
description: >-
  Trading-Journal im Obsidian-Vault. Überträgt einen Day Trade aus trader/
  (plan.json, entry.json, timemachine.json, orders.json, state/risk.json,
  state/broker.json der Day-Trader-Skills) als Notiz nach
  Trading/Trades/<Datum> <SYMBOL> <setup>.md, schließt ihn mit Ausstieg,
  R und Gewinn, und rechnet die Statistik nach Trading/Statistik.md, auch
  gegen die Quoten der Time Machine. Verwenden, wenn der Nutzer sagt
  "ins Journal", "Trade festhalten", "Trade notieren", "Trade schließen",
  "ich bin bei X raus", "wie laufen meine Trades", "Trefferquote",
  "Statistik", "Journal", "was habe ich gelernt", oder nach jedem Schritt
  der Kette trader-exit, trader-timemachine, trader-risk, trader-broker.
argument-hint: "[write | close --exit PREIS | stats | list]"
---

# trading-journal

Das Gedächtnis für Trades. Die trader-Skills rechnen, dieses Skill erinnert:
jeder Trade wird eine Notiz im Vault, mit Plan, Quoten der Time Machine,
Risiko-Check, Broker-Log und am Ende dem Ergebnis. So lässt sich nach Wochen
prüfen, ob ein Setup wirklich trägt oder nur gut aussah.

Keine Anlageberatung. Das Skript liest nur Dateien und schreibt Markdown. Es
platziert nichts, ruft kein Netz auf und ändert nichts in `trader/`.

`${CLAUDE_SKILL_DIR}` ist der Ordner dieses Skills. Alle Befehle laufen in der
Wurzel des Vaults, dort liegt auch `trader/`.

```bash
python3 "${CLAUDE_SKILL_DIR}/journal.py" write                       # Trade anlegen oder auffrischen
python3 "${CLAUDE_SKILL_DIR}/journal.py" close --exit 370.04          # schließen, Grund wird erkannt
python3 "${CLAUDE_SKILL_DIR}/journal.py" close --exit 361 --reason flat --symbol TSLA
python3 "${CLAUDE_SKILL_DIR}/journal.py" stats --write                # -> Trading/Statistik.md
python3 "${CLAUDE_SKILL_DIR}/journal.py" list
```

Exit-Code 0 bei Erfolg, 2 mit einer Zeile Begründung, wenn etwas fehlt.

## Wann was

| Moment | Befehl |
| --- | --- |
| nach `/trader-exit` (Plan steht) | `write` legt die Notiz an, Status `geplant` |
| nach `/trader-timemachine`, `/trader-budget`, `/trader-risk` | `write` ergänzt Quoten, Größe, PASS oder BLOCK |
| nach jedem Schritt von `/trader-broker` | `write`: `freigegeben`, `abgelehnt`, `platziert`, `offen` |
| Stop, Ziel oder Flat bis zum Schluss erreicht | `close --exit PREIS`, oder `write`, wenn beide Fills mit `ticket.py fill` erfasst sind |
| Ende der Woche, oder auf Nachfrage | `stats --write`, dann mit dem Nutzer auf die Zahlen schauen |

`write` ist beliebig oft sicher. Es erneuert nur den Block zwischen
`<!-- journal:auto:start -->` und `<!-- journal:auto:end -->` und die
automatischen Eigenschaften. Die Reflexion, eigene Eigenschaften und Links des
Nutzers bleiben. Ein geschlossener Trade bleibt geschlossen.

## Eigenschaften der Notiz

`datum`, `symbol`, `setup`, `richtung`, `status`, `paper`, `einstieg`, `stop`,
`ziel`, `risiko_je_aktie`, `crv`, `flat_bis`, `stueck`, `max_verlust`,
`tm_ziel`, `tm_stop`, `tm_offen` (Prozent), `tm_urteil`, `hist_ausgeloest`,
`hist_ziel`, `hist_stop`, `risiko_check`, `einstieg_ist`, `ausstieg`,
`ausstieg_grund` (ziel, stop, flat, manuell), `ergebnis_r`, `gewinn_usd`,
`tags`. `Trading/Trades.base` zeigt sie als Tabelle.

R ist der Gewinn in Vielfachen des geplanten Risikos je Aktie: am Ziel eines
1R-Plans +1, am Stop −1. Gerechnet wird vom tatsächlichen Einstieg, wenn ein
Fill erfasst ist, sonst vom geplanten.

## Nach dem Schließen

1. Den Nutzer kurz fragen: Plan eingehalten? Was war anders als erwartet? Die
   Antwort unter `## Reflexion` in der Notiz festhalten, in seinen Worten.
2. Wiederkehrende Muster (ein Setup, das ständig am Stop endet, Einstiege nach
   15 Uhr, Regeln, die gebrochen wurden) als Erkenntnis nach
   `Gedächtnis/Erkenntnisse/Trading.md` übertragen, mit Link auf die Trades.
   Siehe Skill `gedaechtnis`.
3. Ändert der Nutzer daraufhin eine Regel, auch `Trading/Regeln.md` und
   `trader/config.json` anpassen, nur mit seinem Ja.

## Statistik lesen

`stats` vergleicht, was die Time Machine im Schnitt für "Ziel zuerst" gesagt
hat, mit dem Anteil der Trades, die wirklich am Ziel endeten. Bei wenigen
Trades ist das Rauschen. Unter etwa 30 geschlossenen Trades je Setup keine
Schlüsse ziehen und das dem Nutzer auch so sagen.
