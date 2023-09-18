import math
import random
from datetime import datetime

import models
from models import Player, Match, Tournament, db

mock_player_list = [
    {
        "id": "c016cb2a-fdd9-4c40-a81f-0cc6bdf4b9cc",
        "result_text": None,
        "is_winner": False,
        "status": None,
        "name": "Zoli"
    },
    {
        "id": "9ea9ce1a-4794-4553-856c-9a3620c0531b",
        "result_text": None,
        "is_winner": False,
        "status": None,
        "name": "Peti"
    },
    {
        "id": "c016cb2a-fdd9-4c57-a81f-0cc6bdf4b9cc",
        "result_text": None,
        "is_winner": False,
        "status": None,
        "name": "Imi"
    },
    {
        "id": "9ea9ce1a-4794-7153-856c-9a3620c0531b",
        "result_text": None,
        "is_winner": False,
        "status": None,
        "name": "Feri"
    },
    {
        "id": "c016cb2a-fdd9-4c40-a54f-0cc6bdf4b9cc",
        "result_text": None,
        "is_winner": False,
        "status": None,
        "name": "Geza"
    },
    {
        "id": "9ea9ce1a-4729-4553-856c-9a3620c0531b",
        "result_text": None,
        "is_winner": False,
        "status": None,
        "name": "Roli"
    },
    {
        "id": "c088cb2a-fdd9-4c40-a81f-0cc6bdf4b9cc",
        "result_text": None,
        "is_winner": False,
        "status": None,
        "name": "Liza"
    },
    {
        "id": "9ea9ce1a-4345-4553-856c-9a3620c0531b",
        "result_text": None,
        "is_winner": False,
        "status": None,
        "name": "Karcsi"
    },
    {
        "id": "c016cb2a-fdd9-4c40-a23f-0cc6bdf4b9cc",
        "result_text": None,
        "is_winner": False,
        "status": None,
        "name": "Kata"
    },
    {
        "id": "9ea9ce1a-4794-4553-958c-9a3620c0531b",
        "result_text": None,
        "is_winner": False,
        "status": None,
        "name": "Eszter"
    },
    {
        "id": "c016cb2a-fdd9-4c50-a77f-0cc6bdf4b9cc",
        "result_text": None,
        "is_winner": False,
        "status": None,
        "name": "Samu"
    },
    {
        "id": "9ea9ce1a-4794-3333-856c-9a3620c0531b",
        "result_text": None,
        "is_winner": False,
        "status": None,
        "name": "Ati"
    },
    {
        "id": "9ea9ce1a-5566-3353-856c-9a3620c0531b",
        "result_text": None,
        "is_winner": False,
        "status": None,
        "name": "Ede"
    }
]

player_objects = []

for player_data in mock_player_list:
    player = Player(**player_data)
    # Append the Player object to the list
    player_objects.append(player)


def create_match(tournament_id, round_id, match_id, player_1=None, player_2=None, next_match_id=None, winner_id=None,
                 state=None):
    return Match(
        id=int(f"{tournament_id}{round_id:02d}{match_id:02d}"),
        tournament_id=tournament_id,
        winner_id=winner_id,
        state=state,
        start_time=datetime.now(),
        tournament_round_text=round_id,
        next_match_id=int(f"{tournament_id}{round_id + 1:02d}{next_match_id:02d}"),
        participants=[player_1, player_2]
    )


def organize_matches(player_list, tournament_id):
    matches = []
    first_round_bracket_count = 2 ** math.floor(math.log2(len(player_list)))
    preround_players = random.sample(player_list, len(player_list) - (first_round_bracket_count * 2 - len(player_list)))
    empty_first_round_matches_count = int(len(preround_players) / 2 - first_round_bracket_count / 2)
    player_list = [player for player in player_list if player not in preround_players]
    preround_match_count = 0

    # Organize preround matches
    round_id, match_id = 0, 1
    preround_players_copy = preround_players.copy()
    while len(preround_players_copy) >= 2:
        if empty_first_round_matches_count > 0:
            for count in range(empty_first_round_matches_count):
                matches.append(create_match(tournament_id, round_id, match_id,
                                            next_match_id=match_id if match_id <= int(first_round_bracket_count/2)
                                            else int(first_round_bracket_count/2),
                                            player_1=preround_players_copy.pop(0),
                                            player_2=preround_players_copy.pop(0)))
        # if match_id == 1:
        #     next_match_id = match_id
        # else:
        #     if match_id % 2 == 0:
        #         next_match_id = int(match_id / 2)
        #     else:
        #         next_match_id = int((match_id + 1) / 2)

        preround_match_count += 1
        match_id += 1

    # Organize first round matches
    round_id, match_id = 1, 1
    for count in range(int(first_round_bracket_count / 2)):
        if match_id == 1:
            next_match_id = match_id
        else:
            if match_id % 2 == 0:
                next_match_id = int(match_id / 2)
            else:
                next_match_id = int((match_id + 1) / 2)
        if player_list:
            matches.append(create_match(tournament_id, round_id, match_id, next_match_id=next_match_id,
                                        player_1=player_list.pop(0)))
            match_id += 1
        else:
            matches.append(create_match(tournament_id, round_id, match_id, next_match_id=next_match_id))
            match_id += 1
    for number in range(int(len(player_list) / 2)):
        if match_id == 1:
            next_match_id = match_id
        else:
            if match_id % 2 == 0:
                next_match_id = int(match_id / 2)
            else:
                next_match_id = int((match_id + 1) / 2)
        matches.append(create_match(tournament_id, round_id, match_id, next_match_id=next_match_id,
                                    player_1=player_list.pop(0),
                                    player_2=player_list.pop(0)))
        match_id += 1

    # Organize advanced round matches
    round_id, match_id = 2, 1
    while first_round_bracket_count >= 2:
        match_id = 1
        for _ in range(round(round(first_round_bracket_count) / 4)):
            if match_id == 1:
                next_match_id = match_id
            else:
                if match_id % 2 == 0:
                    next_match_id = int(match_id / 2)
                else:
                    next_match_id = int((match_id + 1) / 2)
            matches.append(create_match(tournament_id, round_id, match_id, next_match_id=next_match_id))
            match_id += 1
        first_round_bracket_count = first_round_bracket_count / 2
        round_id += 1

    return matches


organized_matches = organize_matches(player_objects, 1)
for game in organized_matches:
    print(game)

# match_id if match_id == 1 else (match_id // 2 if match_id % 2 == 0 else (match_id + 1) // 2)

# Increasing match|_id with 0.5 in every iteration, and rounding it down, should solve next_match_id issues.
# Last match id has to be null. When creating advanced round matches check if it's the last match.

