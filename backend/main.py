from flask import Flask, jsonify, request, Blueprint
from database_config import db_name
from flask_sqlalchemy import SQLAlchemy
import model
app = Flask(__name__)


# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = db_name

bp = Blueprint("app", __name__)
db = SQLAlchemy()

db.init_app(app)




@app.route('/event/delete/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    event = db.session.query(model.Event).get(event_id)
    if not event:
        return jsonify({'message': 'Event not found.'}), 404
    db.session.delete(event)
    db.session.commit()
    return jsonify({'message': 'Event deleted successfully.'})


@app.route('/event/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = model.Event.query.get(event_id)
    if not event:
        return jsonify({'message': 'Event not found.'}), 404
    event_data = {
        'id': event.id,
        'name': event.name,
        'date': event.date.strftime('%Y-%m-%d')
    }
    return jsonify(event_data)


if __name__ == "__main__":
    app.run(
        port=8080,
        debug=True,
        host='localhost'
    )

