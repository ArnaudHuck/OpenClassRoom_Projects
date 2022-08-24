from Match_model import Match
from Player_model import Player
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Tournament_model import Tournament


class Round:

    def __init__(self, name: str, matches: list[Match]):

        self.name = name
        self.matches = matches

    @staticmethod
    def make(tournament: 'Tournament') -> 'Round':
        """
        :param tournament: Takes a tournament object
        :return: Returns a round object
        """
        name = "Round " + str(len(tournament.list_of_rounds) + 1)
        return Round(name=name, matches=[])

    def serialize(self) -> dict:
        """
        :return: Return a dict containing all round key, value information
        """
        round_info = {'name': self.name,
                      'list_of_finished_matches':
                          [Match.serialize(match) for match in self.matches]}
        return round_info

    @staticmethod
    def deserialize_round(serialized_round: dict) -> 'Round':
        """
        :param serialized_round: Takes a dict with round key, value information
        :return: Returns a round object
        """
        name = serialized_round['name']
        list_of_finished_matches = [Match.deserialize(match) for match in
                                    serialized_round
                                    ['list_of_finished_matches']]
        return Round(name,
                     list_of_finished_matches)

    # noinspection PyTypeChecker
    def run(self, sorted_player_list: list[Player], tournament: 'Tournament'):
        """
        :param sorted_player_list: Takes a player list previously sorted
        :param tournament: Takes a tournament object
        :return: Returns a round with a list of finished matches and updates
                 participant score
        """

        matches: list[Match] = []
        finished_rounds: list[dict] = [Round.serialize(round) for round in
                                       tournament.list_of_rounds]
        finished_matches: list[Match] = [finished_round
                                         ['list_of_finished_matches']
                                         for finished_round in finished_rounds]

        Match.MATCH_NUMBER = len(finished_matches)

        while len(sorted_player_list) > 0:
            match = Match(self.name, sorted_player_list[0],
                          sorted_player_list[1], 0, 0)
            Match.MATCH_NUMBER += 1
            matches.append(match)
            del sorted_player_list[0:2]
        for match in matches:

            match_result = int(input(f"Select the winner of the match"
                                     f" {match.player_1} vs {match.player_2}:"
                                     f" 1 = player_1 won,"
                                     f" 2 = player_2 won, 3 = draw :"))
            if match_result == 1:
                score_player_1 = 1
                match.score_player_1 = score_player_1
            if match_result == 2:
                score_player_2 = 1
                match.score_player_2 = score_player_2
            if match_result == 3:
                score_player_1 = 0.5  # type: ignore
                score_player_2 = 0.5  # type: ignore
                match.score_player_1 = score_player_1
                match.score_player_2 = score_player_2

            tournament.participant_score[str(match.player_1.id)] =\
                tournament.participant_score.get(
                str(match.player_1.id), 0) + match.score_player_1
            tournament.participant_score[str(match.player_2.id)] =\
                tournament.participant_score.get(
                str(match.player_2.id), 0) + match.score_player_2

        return Round(Round.make(tournament).name, matches)

    def __repr__(self):
        return f"{self.matches}"
