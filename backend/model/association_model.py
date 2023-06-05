from sqlalchemy import ForeignKey, Column, Integer, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Player_events(Base):
    __tablename__ = "player_events"
    id = Column(Integer, primary_key=True)
    #event_id = Column(Integer, ForeignKey("events.id"), primary_key=True)
    #player_id = Column(Integer, ForeignKey("players.id"), primary_key=True)
    date = Column(Date)
