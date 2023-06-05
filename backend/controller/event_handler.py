from flask_sqlalchemy import SQLAlchemy
from ..model import model

from sqlalchemy.orm import Session


db = SQLAlchemy()


def add_event(name, date):
    event = model.Event(name=name, date=date)
    db.session.add(event)
    db.session.commit()

