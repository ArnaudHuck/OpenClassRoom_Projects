from Player_model import Player
from typing import Any


class Match:

    MATCH_NUMBER = 1

    def __init__(self, name: str, player_1: Player, player_2: Player, score_player_1: float = 0, score_player_2: float = 0):
        self.name = "Match " + str(Match.MATCH_NUMBER)
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def __repr__(self):
        return f"{self.player_1} --VS-- {self.player_2}"

    def serialize(self) -> dict:
        return {"player_1": Player.serialize(self.player_1),
                "player_2": Player.serialize(self.player_2),
                "score_player_1": self.score_player_1,
                "score_player_2": self.score_player_2}

    @staticmethod
    def deserialize(serialized_match) -> 'Match':
        player_1 = serialized_match["player_1"]
        player_2 = serialized_match["player_2"]
        score_player_1 = serialized_match["score_player_1"]
        score_player_2 = serialized_match["score_player_2"]
        return Match(player_1,
                     player_2,
                     score_player_1,
                     score_player_2)