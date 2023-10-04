import math
from datetime import datetime
from api.models.match import Match
from api.models.player import Player

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
    },
    {
        "id": "9oi9ce1a-5566-3353-856c-9a3620c0531b",
        "result_text": None,
        "is_winner": False,
        "status": None,
        "name": "Soma"
    }
    # {
    #     "id": "9oi9ce1a-8888-3353-856c-9a3620c0531b",
    #     "result_text": None,
    #     "is_winner": False,
    #     "status": None,
    #     "name": "Erik"
    # },
    # {
    #     "id": "9oi9ce1a-6543-3353-856c-9a3620c0531b",
    #     "result_text": None,
    #     "is_winner": False,
    #     "status": None,
    #     "name": "Csilla"
    # }
]  # 14

player_objects = []

for player_data in mock_player_list:
    player = Player(**player_data)
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


def create_brackets(player_list, tournament_id):
    matches = []
    match_counter = (2 ** math.ceil(math.log2(len(player_list)))) / 2  # 8
    opponent_count = len(player_objects) - match_counter
    match_id = 1
    next_match_id = 1

    # First round matches
    for match in range(int(match_counter)):
        if opponent_count > 0:
            matches.append(create_match(tournament_id, round_id=1, match_id=match_id,
                                        next_match_id=int(next_match_id),
                                        player_1=player_list.pop(0),
                                        player_2=player_list.pop(0)))
            opponent_count -= 1
            match_id += 1
            next_match_id += 0.5
        else:
            participant = player_list.pop(0)
            participant.status = 'WALK_OVER'
            matches.append(create_match(tournament_id=tournament_id, round_id=1, match_id=match_id,
                                        next_match_id=int(next_match_id),
                                        player_1=participant))
            match_id += 1
            next_match_id += 0.5
    match_counter /= 2

    # Advanced round matches
    round_id = 2
    next_match_id = 1
    while match_counter > 1:
        match_id = 1
        for count in range(int(match_counter)):
            matches.append(create_match(tournament_id=tournament_id, round_id=round_id, match_id=match_id,
                                        next_match_id=int(next_match_id)))
            match_id += 1
            next_match_id += 0.5
        round_id += 1
        match_counter /= 2

    # Create final match
    final_match = create_match(tournament_id=tournament_id, round_id=round_id, match_id=1,
                               next_match_id=int(next_match_id))
    final_match.next_match_id = None
    matches.append(final_match)

    return matches


organised_matches = create_brackets(player_objects, 1)
for game in organised_matches:
    print(game)
