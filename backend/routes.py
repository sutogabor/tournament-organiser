from flask import jsonify, request, Blueprint
import models
from datetime import datetime


routes_bp = Blueprint("routes", __name__)


@routes_bp.route("/event", methods=['GET'])
def get_events():
    events = models.db.session.query(models.Event).all()
    event_list = []
    for event in events:
        event_data = {
            'id': event.id,
            'name': event.name,
            'date': event.date.strftime("%Y-%m-%dT%H:%M")
        }
        event_list.append(event_data)
    return jsonify(event_list)


@routes_bp.route("/event/add", methods=['POST'])
def add_event():
    added_event = request.get_json()
    event = models.Event(name=added_event["name"], date=added_event['date'])
    models.db.session.add(event)
    models.db.session.commit()
    return jsonify({"message": "Event successfully created."})


@routes_bp.route("/event/delete/<int:event_id>", methods=['DELETE'])
def delete_event(event_id):
    event = models.db.session.query(models.Event).get(event_id)
    if not event:
        return jsonify({"message": "Event not found."}), 404
    models.db.session.delete(event)
    models.db.session.commit()
    return jsonify({"message": "Event deleted successfully."})


@routes_bp.route("/event/<int:event_id>", methods=['GET'])
def get_event(event_id):
    event = models.db.session.query(models.Event).get(event_id)
    if not event:
        return jsonify({"message": "Event not found."}), 404
    event_data = {
        'id': event.id,
        'name': event.name,
        'date': event.date.strftime("%Y-%m-%dT%H:%M")
    }
    return jsonify(event_data)


@routes_bp.route("/player", methods=['GET'])
def get_players():
    players = models.db.session.query(models.Player).all()
    player_list = []
    for player in players:
        player_data = {
            'id': player.id,
            'name': player.name
        }
        player_list.append(player_data)
    return jsonify(player_list)


@routes_bp.route("/player/add", methods=['POST'])
def add_player():
    added_player = request.get_json()
    player = models.Player(name=added_player["name"])
    models.db.session.add(player)
    models.db.session.commit()
    return jsonify({"message": "Player successfully added."})


@routes_bp.route("/player/delete/<int:player_id>", methods=['DELETE'])
def delete_player(player_id):
    player = models.db.session.query(models.Player).get(player_id)
    if not player:
        return jsonify({"message": "Player not found."}), 404
    models.db.session.delete(player)
    models.db.session.commit()
    return jsonify({"message": "Event deleted successfully."})


@routes_bp.route("/player/<int:player_id>", methods=['GET'])
def get_player(player_id):
    player = models.db.session.query(models.Player).get(player_id)
    if not player:
        return jsonify({"message": "Player not found."}), 404
    player_data = {
        "id": player.id,
        "name": player.name
    }
    return jsonify(player_data)


@routes_bp.route("/matches", methods=['GET'])
def get_matches():
    matches = models.db.session.query(models.Match).all()
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


@routes_bp.route("/matches/<int:match_id>")
def get_match(match_id):
    match = models.db.session.query(models.Match).get(match_id)
    if not match:
        return jsonify({"message": "Match not found."}), 404
    match_data = {
        "id": match.id,
        "player_1_id": match.player_1_id,
        "player_2_id": match.player_2_id,
        "event_id": match.event_id,
        "winner": match.winner
    }
    return jsonify(match_data)


@routes_bp.route("/matches/add", methods=['POST'])
def add_match():
    added_match = request.get_json()
    match = models.Match(
        player_1_id=added_match["player_1_id"],
        player_2_id=added_match["player_1_id"],
        event_id=added_match["event_id"],
        winner=None)
    models.db.session.add(match)
    models.db.session.commit()
    return jsonify({"message": "Match successfully added."})


@routes_bp.route("/matches/delete/<int:event_id>", methods=['DELETE'])
def delete_matches(event_id):
    matches = models.db.session.query(models.Match).get(event_id)
    if not matches:
        return jsonify({"message": "Matches not found."}), 404
    for match in matches:
        models.db.session.delete(match)
    models.db.session.commit()
    return jsonify({"message": "Matches deleted successfully."})


@routes_bp.route("/event/<int:event_id>/players", methods=['GET'])
def get_players_by_event(event_id):
    participants = models.db.session.query(models.PlayerEvent).get(event_id)
    players = []
    if not participants:
        return jsonify({"message": "Players not found."}), 404
    for player in participants:
        player_data = {
            "id": player.id,
            "name": player.name
        }
        players.append(player_data)
    return jsonify(players)
