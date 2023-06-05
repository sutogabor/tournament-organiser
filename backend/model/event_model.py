from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    date = Column(Date)
    #players = relationship("Player", secondary="player_events", back_populates="events")



