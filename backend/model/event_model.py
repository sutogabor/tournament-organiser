from sqlalchemy import Column, Integer, String, Date
from backend.db import db


class Event(db.Model):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(Date)
    # players = relationship("Player", back_populates="events")

