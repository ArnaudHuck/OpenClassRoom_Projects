from Player_controller import *
from Tournament_controller import *


class Round:
    def __init__(self):
        self.matches = []

    def add_match_result(self):
        self.matches.append(Match)


class Match:
    def __init__(self, p1: Player, p2: Player):
        self.p1, self.p2 = p1, p2


class GameController:
    def __init__(self, round, view, game_evaluator):
        # Model
        self.players = []
        self.round = round
        # View
        self.view = view

        # Controller
        self.game_evaluator = game_evaluator

    def Pairing_players(self):
        ranking_list = []
        for player in self.players:
            ranking_list.append([player[0], player[4]])
            ranking_list.sort(key=operator.itemgetter('rating'))
            middle_index = len(ranking_list)//2
            upper_ranks = ranking_list[:middle_index]
            lower_ranks = ranking_list[middle_index:]

    def run(self):
        while len(self.players) != 8:
            new_player = self.view.prompt_for_new_player()
            if new_player is None and len(self.players) != 8:
                break
            self.add_player(new_player)