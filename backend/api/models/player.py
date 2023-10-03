from sqlalchemy import Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from api.database.database_handler import db


class Player(db.Model):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    tournaments = relationship("Tournament", secondary="player_event", back_populates="player")


class PlayerTournament(db.Model):
    __tablename__ = "player_tournament"
    id = Column(Integer, Sequence("player_tournament_id_seq", start=1, increment=1), primary_key=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey("player.id"), primary_key=True)
    tournament_id = Column(Integer, ForeignKey("tournament.id"), primary_key=True)
