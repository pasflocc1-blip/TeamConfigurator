from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import RegistryPlayer
from schemas import RegistryPlayerCreate, RegistryPlayerResponse
from typing import List, Optional

router = APIRouter(prefix="/registry", tags=["registry"])


@router.get("/", response_model=List[RegistryPlayerResponse])
def get_players(
    role:   Optional[str] = None,
    search: Optional[str] = None,
    team:   Optional[str] = None,
    db: Session = Depends(get_db)
):
    q = db.query(RegistryPlayer)
    if role:
        q = q.filter(RegistryPlayer.role == role)
    if team:
        q = q.filter(RegistryPlayer.team_name == team)
    if search:
        q = q.filter(RegistryPlayer.name.ilike(f"%{search}%"))
    return q.order_by(RegistryPlayer.name).all()


@router.post("/", response_model=RegistryPlayerResponse)
def create_player(data: RegistryPlayerCreate, db: Session = Depends(get_db)):
    player = RegistryPlayer(**data.dict())
    db.add(player)
    db.commit()
    db.refresh(player)
    return player


@router.put("/{player_id}", response_model=RegistryPlayerResponse)
def update_player(player_id: int, data: RegistryPlayerCreate, db: Session = Depends(get_db)):
    player = db.query(RegistryPlayer).filter(RegistryPlayer.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Giocatore non trovato")
    for k, v in data.dict().items():
        setattr(player, k, v)
    db.commit()
    db.refresh(player)
    return player


@router.delete("/{player_id}")
def delete_player(player_id: int, db: Session = Depends(get_db)):
    player = db.query(RegistryPlayer).filter(RegistryPlayer.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Giocatore non trovato")
    db.delete(player)
    db.commit()
    return {"ok": True}