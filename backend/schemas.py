from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# ── Formazione ───────────────────────────────────────────

class PlayerBase(BaseModel):
    position_id:    str
    position_label: str
    name:           str
    slot:           int = 0


class PlayerResponse(PlayerBase):
    id: int
    class Config:
        from_attributes = True


class TeamCreate(BaseModel):
    name:      str
    formation: str
    players:   List[PlayerBase]


class TeamUpdate(BaseModel):
    name:      Optional[str]         = None
    formation: Optional[str]         = None
    players:   Optional[List[PlayerBase]] = None


class TeamResponse(BaseModel):
    id:         int
    name:       str
    formation:  str
    created_at: datetime
    updated_at: datetime
    players:    List[PlayerResponse]
    class Config:
        from_attributes = True


class TeamSummary(BaseModel):
    id:         int
    name:       str
    formation:  str
    updated_at: datetime
    class Config:
        from_attributes = True


# ── Anagrafica ───────────────────────────────────────────

class RegistryPlayerCreate(BaseModel):
    name:        str
    role:        str
    number:      Optional[int]  = None
    birth_year:  Optional[int]  = None
    nationality: Optional[str]  = None
    team_name:   Optional[str]  = None


class RegistryPlayerResponse(RegistryPlayerCreate):
    id:         int
    created_at: datetime
    class Config:
        from_attributes = True