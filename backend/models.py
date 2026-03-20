from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Team(Base):
    __tablename__ = "teams"

    id         = Column(Integer, primary_key=True, index=True)
    name       = Column(String, nullable=False, unique=True)
    formation  = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    players = relationship("Player", back_populates="team",
                           cascade="all, delete-orphan")


class Player(Base):
    """Giocatori assegnati a una posizione nella formazione"""
    __tablename__ = "players"

    id             = Column(Integer, primary_key=True, index=True)
    team_id        = Column(Integer, ForeignKey("teams.id"), nullable=False)
    position_id    = Column(String, nullable=False)
    position_label = Column(String, nullable=False)
    name           = Column(String, nullable=False)
    slot           = Column(Integer, default=0)  # 0=titolare, 1=riserva1, 2=riserva2

    team = relationship("Team", back_populates="players")


class RegistryPlayer(Base):
    """Anagrafica calciatori — indipendente dalle formazioni"""
    __tablename__ = "registry_players"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String, nullable=False)
    role        = Column(String, nullable=False)
    number      = Column(Integer, nullable=True)
    birth_year  = Column(Integer, nullable=True)
    nationality = Column(String, nullable=True)
    team_name   = Column(String, nullable=True)   # squadra di appartenenza
    created_at  = Column(DateTime, server_default=func.now())