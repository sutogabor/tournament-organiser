from flask import jsonify, request
import models
from main import bp, db


@bp.route("/event", methods=['GET'])
def get_events():
    events = db.session.query(models.Event).all()
    event_list = []
    for event in events:
        event_data = {
            'id': event.id,
            'name': event.name,
            'date': event.date.strftime()
        }
        event_list.append(event_data)
    return jsonify(event_list)


@bp.route("/event/add", methods=['POST'])
def add_event():
    added_event = request.get_json()
    event = models.Event(name=added_event["name"], date=added_event['date'])
    db.session.add(event)
    db.commit()
    return jsonify({"message": "Event successfully created."})


@bp.route("/event/delete/<int:event_id>", methods=['DELETE'])
def delete_event(event_id):
    event = db.session.query(models.Event).get(event_id)
    if not event:
        return jsonify({"message": "Event not found."}), 404
    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "Event deleted successfully."})


@bp.route("/event/<int:event_id>", methods=['GET'])
def get_event(event_id):
    event = db.session.query(models.Event).get(event_id)
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
    players = db.session.query(models.Player).all()
    player_list = []
    for player in players:
        player_data = {
            'id': player.id,
            'name': player.name
        }
        player_list.append(player_data)
    return jsonify(player_list)


@bp.route("/player/add", methods=['POST'])
def add_player():
    added_player = request.get_json()
    player = models.Player(name=added_player["name"])
    db.session.add(player)
    db.session.commit()
    return jsonify({"message": "Player successfully added."})


@bp.route("/player/delete/<id:player_id>", methods=['DELETE'])
def delete_player(player_id):
    player = db.session.query(models.Player).get(player_id)
    if not player:
        return jsonify({"message": "Player not found."}), 404
    db.session.delete(player)
    db.session.commit()
    return jsonify({"message": "Event deleted successfully."})


@bp.route("/player/<id:player_id>", methods=['GET'])
def get_player(player_id):
    player = db.session.query(models.Player).get(player_id)
    if not player:
        return jsonify({"message": "Player not found."}), 404
    player_data = {
        "id": player.id,
        "name": player.name
    }
    return jsonify(player_data)


@bp.route("/matches", methods=['GET'])
def get_matches():
    matches = db.session.query(models.Match).all()
    matches_list = []
    for match in matches:
        match_data = {
            "id": match.id,
            "player_1_id": match.player_1_id,
            "player_2_id": match.player_2_id,
            "event_id": match.event_id,
            "winner": match.winner
        }
        matches_list.append(match_data)
    return jsonify(matches_list)


@bp.route("/matches/add", methods=['POST'])
def add_match():
    added_match = request.get_json()
    match = models.Match(
        player_1_id=added_match["player_1_id"],
        player_2_id=added_match["player_1_id"],
        event_id=added_match["event_id"],
        winner=None)
    db.session.add(match)
    db.session.commit()
    return jsonify({"message": "Match successfully added."})


@bp.route("/matches/delete/<id:event_id>", methods=['DELETE'])
def delete_matches(event_id):
    matches = db.session.query(models.Match).get(event_id)
    if not matches:
        return jsonify({"message": "Matches not found."}), 404
    for match in matches:
        db.session.delete(match)
    db.session.commit()
    return jsonify({"message": "Matches deleted successfully."})

