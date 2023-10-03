from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from api.database.database_handler import db


class Tournament(db.Model):
    __tablename__ = "tournament"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    date = Column(DateTime)
    players = relationship("Player", secondary="player_event", back_populates="tournament")
    matches = relationship("Match", back_populates="tournament")
