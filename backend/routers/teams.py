from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Team, Player
from schemas import TeamCreate, TeamUpdate, TeamResponse, TeamSummary
from typing import List

router = APIRouter(prefix="/teams", tags=["teams"])


@router.get("/", response_model=List[TeamSummary])
def get_teams(db: Session = Depends(get_db)):
    return db.query(Team).order_by(Team.updated_at.desc()).all()


@router.get("/{team_id}", response_model=TeamResponse)
def get_team(team_id: int, db: Session = Depends(get_db)):
    team = db.query(Team).filter(Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Squadra non trovata")
    return team


@router.post("/", response_model=TeamResponse)
def create_team(data: TeamCreate, db: Session = Depends(get_db)):
    existing = db.query(Team).filter(Team.name == data.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Esiste già una squadra con questo nome")

    team = Team(name=data.name, formation=data.formation)
    db.add(team)
    db.flush()

    for p in data.players:
        db.add(Player(
            team_id        = team.id,
            position_id    = p.position_id,
            position_label = p.position_label,
            name           = p.name,
            slot           = p.slot,
        ))

    db.commit()
    db.refresh(team)
    return team


@router.put("/{team_id}", response_model=TeamResponse)
def update_team(team_id: int, data: TeamUpdate, db: Session = Depends(get_db)):
    team = db.query(Team).filter(Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Squadra non trovata")

    if data.name is not None:
        dup = db.query(Team).filter(Team.name == data.name, Team.id != team_id).first()
        if dup:
            raise HTTPException(status_code=400, detail="Nome già in uso da un'altra squadra")
        team.name = data.name

    if data.formation is not None:
        team.formation = data.formation

    if data.players is not None:
        db.query(Player).filter(Player.team_id == team_id).delete()
        for p in data.players:
            db.add(Player(
                team_id        = team.id,
                position_id    = p.position_id,
                position_label = p.position_label,
                name           = p.name,
                slot           = p.slot,
            ))

    db.commit()
    db.refresh(team)
    return team


@router.delete("/{team_id}")
def delete_team(team_id: int, db: Session = Depends(get_db)):
    team = db.query(Team).filter(Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Squadra non trovata")
    db.delete(team)
    db.commit()
    return {"ok": True, "deleted": team_id}