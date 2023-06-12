from flask import Flask, jsonify, request
from database_config import db_name
from flask_sqlalchemy import SQLAlchemy
import model
from main import bp


db = SQLAlchemy()

db.init_app(bp)


@bp.route("/event", methods=['GET'])
def get_events():
    events = db.session.query(model.Event).all()
    event_list = []
    for event in events:
        event_data = {
            'id': event.id,
            'name': event.name,
            'date': event.date.strftime()
        }
        event_list.append(event_data)
    return jsonify(event_list)
