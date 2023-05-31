from sqlalchemy import column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database_handler import base


class Player(base):
    __tablename__ = "players"
    id = mapped_column(Integer, primary_key=True)
    name = column(String)
    event_id = column(Integer, ForeignKey("event.id"))
    event = relationship("Event", back_populates="players")
