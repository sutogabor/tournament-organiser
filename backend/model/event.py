from sqlalchemy import column, Integer, String, Date
from sqlalchemy.orm import relationship
from ..database_handler import base


class Event(base):
    __tablename__ = "events"
    id = column(Integer, primary_key=True)
    name = column(String)
    date = column(Date)
    players = relationship("Player", back_populates="events")
