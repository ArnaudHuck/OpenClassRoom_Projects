from Database import DataBaseController
from Player_model import Player
from Round_model import Round
from typing import List, Dict


class Tournament:

    tournament_in_progress = []

    def __init__(self, id: int, name: str, venue: str, date: str, number_of_rounds: int,
                 time_control: str, description: str, list_of_rounds: list[Round], participant_score: dict[int: int],
                 participant_list: list[Player]):

        if list_of_rounds is None:
            list_of_rounds = []
        self.id = id
        self.name = name
        self.venue = venue
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.time_control = time_control
        self.description = description
        self.list_of_rounds = list_of_rounds
        self.participant_score = participant_score
        self.participant_list = participant_list

    @staticmethod
    def deserialize_tournament(serialized_tournament: dict) -> 'Tournament':
        id = serialized_tournament['id']
        name = serialized_tournament["name"]
        venue = serialized_tournament["venue"]
        date = serialized_tournament["date"]
        number_of_rounds = serialized_tournament["number_of_rounds"]
        time_control = serialized_tournament["time_control"]
        description = serialized_tournament["description"]
        list_of_rounds = serialized_tournament["list_of_rounds"]
        participant_list = serialized_tournament["participant_list"]
        participant_score = serialized_tournament["participant_score"]
        return Tournament(id,
                          name,
                          venue,
                          date,
                          number_of_rounds,
                          time_control,
                          description,
                          list_of_rounds,
                          participant_score,
                          participant_list)

    def serialize(self) -> dict:
        tournament_data = {'id': self.id,
                           'name': self.name,
                           'venue': self.venue,
                           'date': self.date,
                           'number_of_rounds': self.number_of_rounds,
                           'time_control': self.time_control,
                           'description': self.description,
                           'list_of_rounds': [round.serialize() for round in self.list_of_rounds],
                           'participant_score': self.participant_score,
                           'participant_list': [player.serialize() for player in self.participant_list]}
        return tournament_data

    @staticmethod
    def get_all_tournaments() -> list['Tournament']:
        return [Tournament.deserialize_tournament(tournament) for tournament in DataBaseController.list_tournament()]

    @staticmethod
    def get_tournament(id) -> 'Tournament':
        for tournament in DataBaseController.list_tournament():
            if Tournament.deserialize_tournament(tournament).id == id:
                return Tournament.deserialize_tournament(tournament)

    @staticmethod
    def add_tournament(name, venue, date, number_of_rounds, time_control, description,
                       participant_list: List[Player]):
        id = DataBaseController.get_len_tournament_in_db() + 1
        list_of_rounds = []
        participant_score = []
        new_tournament = Tournament(id,
                                    name,
                                    venue,
                                    date,
                                    number_of_rounds,
                                    time_control,
                                    description,
                                    list_of_rounds,
                                    participant_score,
                                    participant_list)
        DataBaseController.add_tournament(new_tournament.serialize())
        Tournament.tournament_in_progress.append(new_tournament.serialize())
        return new_tournament

    def __str__(self):
        return f"id : {self.id} participant score: {self.participant_score} {self.participant_list}"
