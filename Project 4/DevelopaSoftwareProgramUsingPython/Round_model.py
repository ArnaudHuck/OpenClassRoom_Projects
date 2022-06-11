from tinydb import where
from Match_model import Match
from Player_model import Player
from Database import DataBaseController


class Round:

    round_in_progress = []

    def __init__(self, name='', list_of_finished_matches=None):

        self.name = name
        self.list_of_finished_matches = list_of_finished_matches
        self.list_of_rounds = []

    def serialize(self) -> dict:
        round_info = {}

        round_info['name'] = self.name
        round_info['list_of_finished_matches'] = self.list_of_finished_matches
        return round_info

    @staticmethod
    def deserialize_round(serialized_round: dict):
        name = serialized_round['name']
        list_of_finished_matches = serialized_round['list_of_finished_matches']
        return Round(name,
                     list_of_finished_matches,)

    def run(self, sorted_player_list: list[Player], tournament_object):
        self.list_of_rounds = []
        self.list_of_finished_matches = []
        self.name = "Round " + str(len(tournament_object.list_of_rounds) + 1)

        while len(sorted_player_list) > 0:
            match_instance = Match(self.name, sorted_player_list[0], sorted_player_list[1])
            Match.MATCH_NUMBER += 1
            self.list_of_rounds.append(match_instance)
            del sorted_player_list[0:2]

        for match in self.list_of_rounds:

            valid_score_player1 = False
            while not valid_score_player1:
                try:
                    score_player1 = float(input(f"Enter the score of {Player.serialize(match.player_1)} :"))
                except Exception:
                    print("You need to enter 0, 0.5 or 1")
                else:
                    match.score_player_1 = float(score_player1)
                    match.player_1.tournament_score += match.score_player_1
                    # DataBaseController.tournament_db.update({"participant_list": match.player_1.tournament_score},
                    #                                         where(Tournament.deserialize_tournament(tournament_object).participant_list == match.player_1))
                    valid_score_player1 = True

            valid_score_player2 = False
            while not valid_score_player2:
                try:
                    score_player2 = float(input(f"Enter the score of {Player.serialize(match.player_2)} :"))
                except Exception:
                    print("You need to enter 0, 0.5 or 1")
                else:
                    match.score_player_2 = float(score_player2)
                    match.player_2.tournament_score += match.score_player_2
                    valid_score_player2 = True

                self.list_of_finished_matches.append(([match.player_1.id, match.score_player_1],
                                                      [match.player_2.id, match.score_player_2]))

        return Round(self.name, self.list_of_finished_matches)

    @staticmethod
    def add_round_to_tournament(name, list_of_finished_matches):
        new_round = Round(name,
                          list_of_finished_matches)
        DataBaseController.add_round_in_db(new_round.serialize())
        return new_round.serialize()
