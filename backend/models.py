from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Team(Base):
    __tablename__ = "teams"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String, nullable=False, unique=True)
    formation   = Column(String, nullable=False)
    created_at  = Column(DateTime, server_default=func.now())
    updated_at  = Column(DateTime, server_default=func.now(), onupdate=func.now())

    players = relationship("Player", back_populates="team",
                           cascade="all, delete-orphan")


class Player(Base):
    __tablename__ = "players"

    id             = Column(Integer, primary_key=True, index=True)
    team_id        = Column(Integer, ForeignKey("teams.id"), nullable=False)
    position_id    = Column(String, nullable=False)
    position_label = Column(String, nullable=False)
    name           = Column(String, nullable=False)
    slot           = Column(Integer, nullable=False, default=0)  # 0=titolare 1=riserva1 2=riserva2

    team = relationship("Team", back_populates="players")