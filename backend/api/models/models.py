from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Sequence
from sqlalchemy.orm import declarative_base, relationship
from flask_sqlalchemy import SQLAlchemy


Base = declarative_base()
db = SQLAlchemy()


class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    tournaments = relationship("Event", secondary="player_event", back_populates="players")


class PlayerTournament(Base):
    __tablename__ = 'player_tournament'
    id = Column(Integer, Sequence('player_event_id_seq', start=1, increment=1), primary_key=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey('players.id'), primary_key=True)
    tournament_id = Column(Integer, ForeignKey('events.id'), primary_key=True)


class Tournament(Base):
    __tablename__ = "tournaments"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    date = Column(DateTime)
    players = relationship("Player", secondary="player_event", back_populates="events")
    matches = relationship("Match", back_populates="event")


class Match(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True)
    tournament_id = Column(Integer, ForeignKey("events.id"))
    player_1_id = Column(Integer, ForeignKey("players.id"))
    player_2_id = Column(Integer, ForeignKey("players.id"))
    winner_id = Column(Integer, ForeignKey("players.id"), nullable=True)
    state = Column(String(20))
    start_time = Column(DateTime)
    tournament_round_text = Column(String(10))
    next_match_id = Column(Integer, ForeignKey("matches.id"), nullable=True)

    tournament = relationship("Event", back_populates="matches")
    player_1 = relationship("Player", foreign_keys=[player_1_id])
    player_2 = relationship("Player", foreign_keys=[player_2_id])
    winner = relationship("Player", foreign_keys=[winner_id])
    next_match = relationship("Match", foreign_keys=[next_match_id], remote_side=[id])

