from Player_model import Player


class Match:

    MATCH_NUMBER = 1

    def __init__(self, name='', player_1=Player, player_2=Player, score_player_1=float, score_player_2=float):
        self.name = "Match " + str(Match.MATCH_NUMBER)
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2



