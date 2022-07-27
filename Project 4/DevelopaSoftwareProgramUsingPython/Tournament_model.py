from Database import DataBaseController
from Player_model import Player
from Round_model import Round
from tinydb import where


class Tournament:

    def __init__(self, id: int, name: str, venue: str, date: str, number_of_rounds: int,
                 time_control: str, description: str, list_of_rounds: list[Round],
                 participant_score: dict[int, float], participant_list: list[Player]):

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
        """
        :param serialized_tournament: Takes a Tournament dict with all key, value information
        :return: Returns an object of Tournament class
        """
        id = serialized_tournament['id']
        name = serialized_tournament["name"]
        venue = serialized_tournament["venue"]
        date = serialized_tournament["date"]
        number_of_rounds = serialized_tournament["number_of_rounds"]
        time_control = serialized_tournament["time_control"]
        description = serialized_tournament["description"]
        list_of_rounds = [Round.deserialize_round(round_dict) for round_dict in serialized_tournament["list_of_rounds"]]
        participant_list = [Player.deserialize(player_dict) for player_dict in
                            serialized_tournament["participant_list"]]
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
        """
        :return: Returns a dict with all Tournament key, value information
        """
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
        """
        :return: Returns a list of tournament
        """
        return [Tournament.deserialize_tournament(tournament) for tournament in DataBaseController.list_tournament()]

    @staticmethod
    def get_tournament(id) -> 'Tournament':
        """
        :param id: Takes an id as input
        :return: Returns the matching tournament in DB
        """
        return Tournament.deserialize_tournament(DataBaseController.get_tournament(id))

    @staticmethod
    def get_unfinished_tournament(id) -> 'Tournament':
        """
        :param id: Takes an id as input
        :return: Returns the matching tournament in DB
        """
        return Tournament.deserialize_tournament(DataBaseController.get_unfinished_tournament(id))

    @staticmethod
    def add_tournament(name, venue, date, number_of_rounds, time_control, description,
                       participant_list: list[Player]):
        """
        :param name: Takes the tournament name
        :param venue: Takes the tournament venue
        :param date: Takes the tournament date
        :param number_of_rounds: Takes the tournament number of rounds
        :param time_control: Takes the tournament time control type
        :param description: Takes the tournament description
        :param participant_list: Takes the tournament player list
        :return: Returns a new tournament and adds it to the DB
        """
        id = DataBaseController.get_len_tournament_in_db() + 1
        list_of_rounds: list[Round] = []
        participant_score: dict = {}
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
        return new_tournament

    @staticmethod
    def get_tournament_rounds(tournament: 'Tournament') -> list[Round]:
        """
        :param tournament: Takes a tournament object
        :return: Returns the tournament list_of_rounds argument
        """
        return tournament.list_of_rounds

    @staticmethod
    def add_tournament_in_progress(tournament: 'Tournament'):
        """
        :param tournament: Takes a tournament object
        :return: if the tournament has not been started yet, adds the tournament in DB
                 if the tournament has been started, updates its list of round argument
        """
        if len(tournament.list_of_rounds) == 1:
            DataBaseController.tournament_in_progress_or_ended_db.insert(tournament.serialize())
        else:
            DataBaseController.tournament_in_progress_or_ended_db.upsert({"list_of_rounds": [Round.serialize(round)
                                                                          for round in tournament.list_of_rounds]},
                                                                         where("id") == tournament.id)

    @staticmethod
    def save_participant_score(tournament: 'Tournament'):
        """
        :param tournament: Takes a tournament object
        :return: Updates its participant score argument
        """
        DataBaseController.tournament_in_progress_or_ended_db.update({'participant_score':
                                                                      tournament.participant_score},
                                                                     where("id") == tournament.id)

    @staticmethod
    def get_all_tournaments_unfinished_or_ended() -> list['Tournament']:
        """
        :return: Returns a list of Tournament from the DB
        """
        return [Tournament.deserialize_tournament(tournament)
                for tournament in DataBaseController.list_tournament_ended_or_unfinished()]

    def __repr__(self):
        return f"id : {self.id} participant score: {self.participant_score} {self.participant_list}"
