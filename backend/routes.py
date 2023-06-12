from flask import jsonify, request
import model
from main import bp, db


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


@bp.route("/event/add", methods=[])
def add_event():
    added_event = request.get_json()
    event = model.Event(name=added_event["name"], date=added_event['date'])
    db.session.add(event)
    db.commit()
    return jsonify({"message": "Event successfully created."})


@bp.route("/event/delete/<int:event_id>", methods=['POST'])
def delete_event(event_id):
    event = db.session.query(model.Event).get(event_id)
    if not event:
        return jsonify({"message": "Event not found."}), 404
    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "Event deleted successfully."})


@bp.route("/event/<int:event_id>", methods=['GET'])
def get_event(event_id):
    event = db.session.query(model.Event).get(event_id)
    if not event:
        return jsonify({"message": "Event not found."}), 404
    event_data = {
        'id': event.id,
        'name': event.name,
        'date': event.date.strftime('%Y-%m-%d')
    }
    return jsonify(event_data)


@bp.route("/player", methods=['GET'])
def get_players():
    players = db.session.query(model.Player).all()
    player_list = []
    for player in players:
        player_data = {
            'id': player.id,
            'name': player.name
        }
    return jsonify(player_list)


@bp.route("/player/add", methods=['POST'])
def add_player():
    added_player = request.get_json()
    player = model.Player(name=added_player["name"])
    db.session.add(player)
    db.session.commit()
    return jsonify({"message": "Player successfully added."})


@bp.route("/player/delete/<id:player_id>")
def delete_player(player_id):
    player = db.session.query(model.Player).get(player_id)
    if not player:
        return jsonify({"message": "Player not found."}), 404
    db.session.delete(player)
    db.session.commit()
    return jsonify({"message": "Event deleted successfully."})
