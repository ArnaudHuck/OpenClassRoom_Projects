from Player_model import Player
from typing import Any


class Match:

    MATCH_NUMBER = 1

    def __init__(self, name: Any, player_1: Player, player_2: Player, score_player_1: float = 0, score_player_2: float = 0):
        self.name = "Match " + str(Match.MATCH_NUMBER)
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def __str__(self):
        return f"{self.name} : {self.player_1} --VS-- {self.player_2}."
