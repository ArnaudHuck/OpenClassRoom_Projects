from Match_model import Match
from Player_model import Player
from Database import DataBaseController
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Tournament_model import Tournament


class Round:

    def __init__(self, name: str, matches: list[Match]):

        self.name = name
        self.matches = matches

    @staticmethod
    def make(tournament: 'Tournament') -> 'Round':
        name = "Round " + str(len(tournament.list_of_rounds) + 1)
        return Round(name=name, matches=[])

    def serialize(self) -> dict:
        round_info = {'name': self.name, 'list_of_finished_matches': [Match.serialize(match) for match in self.matches]}
        return round_info

    @staticmethod
    def deserialize_round(serialized_round: dict):
        name = serialized_round['name']
        list_of_finished_matches = [Match.deserialize(match) for match in serialized_round['list_of_finished_matches']]
        return Round(name,
                     list_of_finished_matches)

    def run(self, sorted_player_list: list[Player], tournament: 'Tournament'):

        matches: list[Match] = []

        while len(sorted_player_list) > 0:
            match = Match(self.name, sorted_player_list[0], sorted_player_list[1])
            Match.MATCH_NUMBER += 1
            matches.append(match)
            del sorted_player_list[0:2]
        for match in matches:

            match_result = int(input(f"Select the winner of the match {match.player_1} vs {match.player_2}:"
                                     f" 1 = player_1 won, 2 = player_2 won, 3 = draw :"))
            if match_result == 1:
                score_player_1 = 1
                match.score_player_1 = score_player_1
            if match_result == 2:
                score_player_2 = 1
                match.score_player_2 = score_player_2
            if match_result == 3:
                score_player_1 = 0.5
                score_player_2 = 0.5
                match.score_player_1 = score_player_1
                match.score_player_2 = score_player_2

            tournament.participant_score[match.player_1.id] = tournament.participant_score.get(match.player_1.id, 0) + match.score_player_1
            tournament.participant_score[match.player_2.id] = tournament.participant_score.get(match.player_2.id,
                                                                                               0) + match.score_player_2
        return Round(Round.make(tournament).name, matches)

    @staticmethod
    def add_round_to_tournament(name, list_of_finished_matches):
        new_round = Round(name,
                          list_of_finished_matches)
        DataBaseController.add_round_in_db(new_round.serialize())
        return new_round.serialize()

    def __repr__(self):
        return f"{self.matches}"
