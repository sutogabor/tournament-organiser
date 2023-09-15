from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Sequence
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Player(db.Model):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    result_text = Column(String(20), nullable=True)
    is_winner = Column(Boolean, default=False)
    status = Column(String(20), nullable=True)
    name = Column(String(255))

    tournaments = relationship("Tournament", secondary="player_tournament", back_populates="players")
    matches = relationship("Match", secondary="match_participants", back_populates="participants")


class Tournament(db.Model):
    __tablename__ = "tournaments"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    date = Column(DateTime)
    players = relationship("Player", secondary="player_tournament", back_populates="tournaments")
    matches = relationship("Match")


class PlayerTournament(db.Model):
    __tablename__ = 'player_tournament'
    id = Column(Integer, Sequence('player_tournament_id_seq', start=1, increment=1), primary_key=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey('players.id'), primary_key=True)
    tournament_id = Column(Integer, ForeignKey('tournaments.id'), primary_key=True)


class Match(db.Model):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True)
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    player_1_id = Column(Integer, ForeignKey("players.id"))
    player_2_id = Column(Integer, ForeignKey("players.id"))
    winner_id = Column(Integer, ForeignKey("players.id"), nullable=True)
    state = Column(String(20))
    start_time = Column(DateTime)
    tournament_round_text = Column(String(10))
    next_match_id = Column(Integer, ForeignKey("matches.id"), nullable=True)

    participants = relationship("Player", secondary="match_participants", back_populates="matches")
    tournament = relationship("Tournament", back_populates="matches")
    player_1 = relationship("Player", foreign_keys=[player_1_id])
    player_2 = relationship("Player", foreign_keys=[player_2_id])
    winner = relationship("Player", foreign_keys=[winner_id])
    next_match = relationship("Match", foreign_keys=[next_match_id], remote_side=[id])

    def __str__(self):
        return f"Match ID: {self.id}, Event ID: {self.tournament_id}, Player 1 ID: {self.player_1_id}, Player 2 ID: {self.player_2_id}, Next Match ID: {self.next_match_id}"

