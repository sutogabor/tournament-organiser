from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.database.database_handler import db


class Match(db.Model):
    __tablename__ = "match"
    id = Column(Integer, primary_key=True)
    tournament_id = Column(Integer, ForeignKey("tournament.id"))
    player_1_id = Column(Integer, ForeignKey("player.id"))
    player_2_id = Column(Integer, ForeignKey("player.id"))
    winner_id = Column(Integer, ForeignKey("player.id"), nullable=True)
    state = Column(String(20))
    start_time = Column(DateTime)
    tournament_round_text = Column(String(20))
    next_match_id = Column(Integer, ForeignKey("match.id"), nullable=True)

    tournament = relationship("Tournament", back_populates="match")
    player_1 = relationship("Player", foreign_keys=[player_1_id])
    player_2 = relationship("Player", foreign_keys=[player_2_id])
    winner = relationship("Player", foreign_keys=[winner_id])
    next_match = relationship("Match", foreign_keys=[next_match_id], remote_side=[id])
