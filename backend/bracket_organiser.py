import math
import random
from models import Match, db


def create_match(event_id, round_id, match_id, next_match_id=None, player_1_id=None, player_2_id=None):
    return Match(
        id=int(f"{event_id}{round_id:02d}{match_id:02d}"),
        next_match_id=int(f"{event_id}{round_id + 1:02d}{next_match_id or round(match_id / 2) + 1:02d}"),
        player_1_id=player_1_id,
        player_2_id=player_2_id,
        event_id=event_id
    )


def organize_matches(player_list, event_id):
    matches = []
    first_round_bracket_count = 2 ** math.floor(math.log2(len(player_list)))
    preround_players = random.sample(player_list, (len(player_list) - first_round_bracket_count) * 2)
    first_round_players = list(set(player_list) - set(preround_players))

    # Organize preround matches
    round_id, match_id = 0, 1
    while len(preround_players) >= 2:
        matches.append(create_match(event_id, round_id, match_id, next_match_id=match_id,
                                    player_1_id=preround_players.pop(0)["id"],
                                    player_2_id=preround_players.pop(0)["id"]))
        match_id += 1

    # Organize first round matches
    round_id, match_id = 1, 1
    for _ in range(len(preround_players) // 2):
        matches.append(create_match(event_id, round_id, match_id, next_match_id=match_id,
                                    player_1_id=preround_players.pop(0)["id"],
                                    player_2_id=preround_players.pop(0)["id"]))
        match_id += 1

    # Organize advanced round matches
    round_id, match_id = 2, 1
    while first_round_bracket_count >= 2:
        for _ in range(first_round_bracket_count // 2):
            matches.append(create_match(event_id, round_id, match_id, next_match_id=match_id))
            match_id += 1
        first_round_bracket_count //= 2
        round_id += 1

    return matches


def add_matches_to_database(matches):
    db.session.add_all(matches)
    db.session.commit()
