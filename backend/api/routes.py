from flask import jsonify, request, Blueprint
from api.models.match import Match
from api.models.player import Player
from api.models.tournament import Tournament
from api.database.database_handler import db


routes_bp = Blueprint("routes", __name__)

@routes_bp.route("/tournaments", methods=['GET'])
def get_tournaments():
    tournaments = Tournament.query.all()
    tournament_list = []
    for tournament in tournaments:
        tournament_data = {
            'id': tournament.id,
            'name': tournament.name,
            'date': tournament.date.strftime("%Y-%m-%dT%H:%M"),
            'players': [player.name for player in tournament.players],
            'matches': [
                {
                    'match_id': match.id,
                    'player_1': match.participants[0].name if match.participants and len(match.participants) >= 1 else None,
                    'player_2': match.participants[1].name if match.participants and len(match.participants) >= 2 else None,
                    'winner': match.winner.name if match.winner else None
                }
                for match in tournament.matches
            ]
        }
        tournament_list.append(tournament_data)
    return jsonify(tournament_list)


@routes_bp.route("/tournaments-with-players", methods=['GET'])
def get_tournaments_with_players():
    tournaments = Tournament.query.options(db.joinedload(Tournament.players)).all()
    tournament_list = []
    for tournament in tournaments:
        tournament_data = {
            'id': tournament.id,
            'name': tournament.name,
            'date': tournament.date.strftime("%Y-%m-%dT%H:%M"),
            'players': [{'id': player.id, 'name': player.name} for player in tournament.players]
        }
        tournament_list.append(tournament_data)
    return jsonify(tournament_list)


@routes_bp.route("/tournament", methods=['POST'])
def add_tournament():
    added_tournament = request.get_json()
    tournament = Tournament(name=added_tournament["name"], date=added_tournament['date'])
    db.session.add(tournament)
    db.session.commit()
    return jsonify({"message": "Tournament successfully created."})


@routes_bp.route("/tournament/<int:tournament_id>", methods=['DELETE'])
def delete_tournament_by_id(tournament_id):
    tournament = db.session.query(Tournament).get(tournament_id)
    if not tournament:
        return jsonify({"message": "Event not found."}), 404
    db.session.delete(tournament)
    db.session.commit()
    return jsonify({"message": "Tournament deleted successfully."})


@routes_bp.route("/tournament/<int:tournament_id>", methods=['GET'])
def get_tournament_by_id(tournament_id):
    tournament = db.session.query(Tournament).get(tournament_id)
    if not tournament:
        return jsonify({"message": "Tournament not found."}), 404
    tournament_data = {
        'id': tournament.id,
        'name': tournament.name,
        'date': tournament.date.strftime("%Y-%m-%dT%H:%M")
    }
    return jsonify(tournament_data)


@routes_bp.route("/players", methods=['GET'])
def get_players():
    players = Player.query.all()
    player_list = [{'id': player.id, 'name': player.name} for player in players]
    return jsonify(player_list)


@routes_bp.route("/players", methods=['POST'])
def add_player():
    added_player = request.get_json()
    tournament_list = []
    for tournament_id in added_player["tournaments"]:
        tournament = Tournament.query.get(tournament_id)
        if tournament:
            tournament_list.append(tournament)
    player = Player(name=added_player["name"], tournaments=tournament_list)
    db.session.add(player)
    db.session.commit()
    return jsonify({"message": "Player successfully added."})


@routes_bp.route("/players/<int:player_id>", methods=['DELETE'])
def delete_player_by_id(player_id):
    player = Player.query.get(player_id)
    if not player:
        return jsonify({"message": "Player not found."}), 404
    db.session.delete(player)
    db.session.commit()
    return jsonify({"message": "Player deleted successfully."})


@routes_bp.route("/player/<int:player_id>", methods=['GET'])
def get_player_by_id(player_id):
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
    matches = Match.query.all()
    matches_list = [{'id': match.id,
                     'player_1_id': match.participants[0].id if match.participants and len(match.participants) >= 1 else None,
                     'player_2_id': match.participants[1].id if match.participants and len(match.participants) >= 2 else None,
                     'event_id': match.tournament_id,
                     'winner_id': match.winner_id} for match in matches]
    return jsonify(matches_list)


@routes_bp.route("/matches/<int:match_id>", methods=['GET'])
def get_match_by_id(match_id):
    match = models.Match.query.get(match_id)
    if not match:
        return jsonify({"message": "Match not found."}), 404
    match_data = {
        "id": match.id,
        "player_1_id": match.player_1_id,
        "player_2_id": match.player_2_id,
        "event_id": match.event_id,
        "winner_id": match.winner_id
    }
    return jsonify(match_data)


@routes_bp.route("/matches", methods=['POST'])
def add_match():
    added_match = request.get_json()
    match = models.Match(
        player_1_id=added_match["player_1_id"],
        player_2_id=added_match["player_2_id"],
        event_id=added_match["event_id"],
        winner_id=None
    )
    models.db.session.add(match)
    models.db.session.commit()
    return jsonify({"message": "Match successfully added."})


@routes_bp.route("/matches/<int:tournament_id>", methods=['DELETE'])
def delete_matches_by_tournament_id(tournament_id):
    matches = models.Match.query.filter_by(event_id=tournament_id).all()
    if not matches:
        return jsonify({"message": "Matches not found."}), 404
    for match in matches:
        models.db.session.delete(match)
    models.db.session.commit()
    return jsonify({"message": "Matches deleted successfully."})


@routes_bp.route("/tournament/<int:tournament_id>/players", methods=['GET'])
def get_players_by_tournament(tournament_id):
    participants = models.db.session.query(models.Player).join(models.PlayerTournament).filter(
        models.PlayerTournament.event_id == tournament_id).all()
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
