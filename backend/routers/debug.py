from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db, get_db_path
from models import Team, Player, RegistryPlayer
import os

router = APIRouter(prefix="/debug", tags=["debug"])


@router.get("/db")
def check_database(db: Session = Depends(get_db)):
    db_path = get_db_path()

    try:
        db_size_kb = round(os.path.getsize(db_path) / 1024, 2)
    except:
        db_size_kb = 0

    teams_count    = db.query(Team).count()
    players_count  = db.query(Player).count()
    registry_count = db.query(RegistryPlayer).count()

    last_teams = db.query(Team).order_by(Team.updated_at.desc()).limit(5).all()
    last_teams_data = [
        {
            "id":         t.id,
            "name":       t.name,
            "formation":  t.formation,
            "updated_at": str(t.updated_at),
            "players":    db.query(Player).filter(Player.team_id == t.id).count(),
        }
        for t in last_teams
    ]

    result = db.execute(text("SELECT name FROM sqlite_master WHERE type='table'"))
    tables = [row[0] for row in result]

    return {
        "status":         "ok",
        "db_path":        db_path,
        "db_size_kb":     db_size_kb,
        "tables":         tables,
        "teams_count":    teams_count,
        "players_count":  players_count,
        "registry_count": registry_count,
        "last_teams":     last_teams_data,
    }


@router.delete("/db/reset")
def reset_database(db: Session = Depends(get_db)):
    db.query(Player).delete()
    db.query(Team).delete()
    db.commit()
    return {"status": "ok", "message": "Squadre e formazioni eliminate (anagrafica intatta)"}


@router.delete("/db/reset-all")
def reset_all(db: Session = Depends(get_db)):
    db.query(Player).delete()
    db.query(Team).delete()
    db.query(RegistryPlayer).delete()
    db.commit()
    return {"status": "ok", "message": "Database svuotato completamente"}


@router.post("/db/query")
def run_query(payload: dict, db: Session = Depends(get_db)):
    """Esegue una SELECT sul database e restituisce i risultati"""
    sql = payload.get("sql", "").strip()
    if not sql:
        raise HTTPException(status_code=400, detail="Query vuota")
    # Sicurezza: solo SELECT permesse
    if not sql.upper().startswith("SELECT"):
        raise HTTPException(status_code=400, detail="Solo query SELECT sono permesse")
    try:
        result = db.execute(text(sql))
        columns = list(result.keys())
        rows = [dict(zip(columns, row)) for row in result.fetchall()]
        return {"columns": columns, "rows": rows, "count": len(rows)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Errore SQL: {str(e)}")