#!/usr/bin/env python3
"""
Script di verifica e ispezione del database SQLite.
Uso:
  python verifica_db.py                     # cerca db nella cartella corrente
  python verifica_db.py /percorso/file.db   # percorso esplicito
"""
import sys, os, sqlite3

SEP  = "═" * 70
SEP2 = "─" * 70


def find_db():
    candidates = [
        "myapp.db", "backend/myapp.db",
        os.path.expanduser("~/.myapp/myapp.db"),
        os.path.expanduser("~/.teamconfigurator/data.db"),
    ]
    if len(sys.argv) > 1:
        return sys.argv[1]
    for p in candidates:
        if os.path.exists(p):
            return p
    return None


def verify(path):
    print(f"\n{SEP}")
    print(f"  📂  DATABASE : {os.path.abspath(path)}")
    print(f"  💾  Dimensione: {os.path.getsize(path)/1024:.1f} KB")
    print(SEP)

    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    # ── Tabelle ────────────────────────────────────────────────────────
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = [r[0] for r in cur.fetchall()]
    print(f"\n📋  Tabelle presenti: {', '.join(tables) if tables else '⚠️  NESSUNA'}")

    if not tables:
        print("\n  Il database è vuoto. Hai avviato il backend almeno una volta?")
        con.close(); return

    # ── Schema di ogni tabella ─────────────────────────────────────────
    print(f"\n{SEP2}")
    print("  SCHEMA TABELLE")
    print(SEP2)
    for table in tables:
        cur.execute(f"PRAGMA table_info({table})")
        cols = cur.fetchall()
        cur.execute(f"SELECT COUNT(*) FROM {table}")
        n = cur.fetchone()[0]
        print(f"\n  [{table}]  ({n} righe)")
        for col in cols:
            pk = " 🔑" if col["pk"] else ""
            nn = " NOT NULL" if col["notnull"] else ""
            df = f" DEFAULT={col['dflt_value']}" if col["dflt_value"] else ""
            print(f"    {col['name']:20s} {col['type']}{pk}{nn}{df}")

    # ── Verifica colonna slot ──────────────────────────────────────────
    if "players" in tables:
        cur.execute("PRAGMA table_info(players)")
        cols_names = [c["name"] for c in cur.fetchall()]
        if "slot" in cols_names:
            print(f"\n  ✅  Colonna 'slot' presente")
        else:
            print(f"\n  ❌  Colonna 'slot' MANCANTE — cancella myapp.db e riavvia il backend!")

    # ── Dati teams ─────────────────────────────────────────────────────
    if "teams" in tables:
        cur.execute("SELECT * FROM teams ORDER BY id")
        teams = cur.fetchall()
        print(f"\n{SEP}")
        print(f"  SQUADRE SALVATE  ({len(teams)})")
        print(SEP)

        if not teams:
            print("  Nessuna squadra nel database.")
        else:
            for team in teams:
                print(f"\n  🏟️  ID={team['id']}  Nome='{team['name']}'  Modulo={team['formation']}")
                print(f"       Creata: {team['created_at']}   Aggiornata: {team['updated_at']}")

                # Giocatori raggruppati per posizione
                cur.execute("""
                    SELECT position_id, position_label, slot, name
                    FROM players WHERE team_id=?
                    ORDER BY position_id, slot
                """, (team["id"],))
                rows = cur.fetchall()

                if not rows:
                    print("       ⚠️  Nessun giocatore!")
                    continue

                # Raggruppa per position_id
                pos_map = {}
                for r in rows:
                    pid = r["position_id"]
                    if pid not in pos_map:
                        pos_map[pid] = {"label": r["position_label"], "slots": {}}
                    pos_map[pid]["slots"][r["slot"]] = r["name"]

                print(f"       Giocatori ({len(rows)} record, {len(pos_map)} posizioni):")
                slot_labels = {0: "Titolare ", 1: "Riserva1 ", 2: "Riserva2 "}
                for pid, data in sorted(pos_map.items()):
                    parts = []
                    for s in [0, 1, 2]:
                        name = data["slots"].get(s)
                        if name:
                            parts.append(f"{slot_labels[s]}: {name}")
                    print(f"         [{data['label']:4s} / {pid:6s}]  " + "  |  ".join(parts))

    # ── Statistiche generali ───────────────────────────────────────────
    if "players" in tables and "slot" in cols_names if "players" in tables else []:
        print(f"\n{SEP2}")
        print("  STATISTICHE GIOCATORI")
        print(SEP2)
        cur.execute("SELECT COUNT(*) FROM players")
        tot = cur.fetchone()[0]
        print(f"  Totale record giocatori: {tot}")
        cur.execute("SELECT slot, COUNT(*) n FROM players GROUP BY slot ORDER BY slot")
        for r in cur.fetchall():
            lbl = {0:"Titolari ", 1:"Riserve 1", 2:"Riserve 2"}.get(r["slot"], f"Slot {r['slot']}")
            print(f"  {lbl}: {r['n']}")

    # ── Integrità ──────────────────────────────────────────────────────
    print(f"\n{SEP2}")
    cur.execute("PRAGMA integrity_check")
    res = cur.fetchone()[0]
    icon = "✅" if res == "ok" else "❌"
    print(f"  {icon}  Integrity check: {res}")
    print(f"{SEP2}\n")

    con.close()


if __name__ == "__main__":
    path = find_db()
    if not path:
        print("\n❌  Database non trovato nei percorsi di default.")
        print("    Usa: python verifica_db.py C:\\percorso\\myapp.db\n")
        sys.exit(1)
    verify(path)