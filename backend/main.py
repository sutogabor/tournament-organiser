from flask import Flask, jsonify, request
from database_config import db_name
from flask_sqlalchemy import SQLAlchemy
import model
app = Flask(__name__)


# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = db_name

db = SQLAlchemy()

db.init_app(app)


@app.route('/event', methods=['GET'])
def get_events():
    events = db.session.query(model.Event).all()
    event_list = []
    for event in events:
        event_data = {
            'id': event.id,
            'name': event.name,
            'date': event.date.strftime('%Y-%m-%d')
        }
        event_list.append(event_data)
    return jsonify(event_list)


@app.route('/event/add', methods=['POST'])
def add_event():
    added_event = request.get_json()
    event = model.Event(name=added_event['name'], date=added_event['date'])
    db.session.add(event)
    db.session.commit()
    return jsonify({'message': 'Event created successfully.'}), 201


if __name__ == "__main__":
    app.run(
        port=8080,
        debug=True,
        host='localhost'
    )

