from Database import DataBaseController
from tinydb import where
from tinydb.operations import set


class Player:

    def __init__(self, id: int, first_name: str,
                 last_name: str, date_of_birth: str, gender: str,
                 current_rank: int):

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.current_rank = current_rank

    @staticmethod
    def add_player(first_name, last_name, date_of_birth, gender,  current_rank):
        """
        :param first_name: Takes the first name of a player
        :param last_name: Takes the last name of the player
        :param date_of_birth: Takes the birthdate of the player
        :param gender: Takes the gender of the player
        :param current_rank: Takes the current score of the player
        :return: Returns a new player and adds it to the DB
        """
        id = DataBaseController.get_len_players_in_db() + 1

        new_player = Player(id, first_name, last_name,
                            date_of_birth, gender, current_rank)
        DataBaseController.add_player(new_player.serialize())
        return new_player

    @staticmethod
    def get_all_players() -> list['Player']:
        """
        :return: Returns a list of all players in the DB
        """
        return [Player.deserialize(player) for player in
                DataBaseController.list_player()]

    @staticmethod
    def deserialize(serialized_player: dict) -> 'Player':
        """
        :param serialized_player: Takes a Player dict with all key,
               value information
        :return: Returns an object of class Player
        """
        id = serialized_player["id"]
        first_name = serialized_player["first_name"]
        last_name = serialized_player["last_name"]
        date_of_birth = serialized_player["date_of_birth"]
        gender = serialized_player['gender']
        current_rank = serialized_player["current_rank"]
        return Player(id,
                      first_name,
                      last_name,
                      date_of_birth,
                      gender,
                      current_rank,
                      )

    def serialize(self) -> dict:
        """
        :return: Returns a dict with all player key, value information
        """
        player_data = {'id': self.id,
                       'first_name': self.first_name,
                       'last_name': self.last_name,
                       'date_of_birth': self.date_of_birth,
                       'gender': self.gender,
                       'current_rank': self.current_rank}
        return player_data

    @staticmethod
    def get_player(id):
        """
        :param id: Takes an int as input
        :return: Returns the matching player in DB
        """
        for player in DataBaseController.list_player():
            if Player.deserialize(player).id == id:
                return Player.deserialize(player)
        else:
            print('No match')

    def __repr__(self):
        return f"{self.id} {self.first_name} {self.last_name} " \
               f"rank : {self.current_rank}"

    @staticmethod
    def update_player_rank(player: 'Player'):
        DataBaseController.player_db.update(set('current_rank',
                                                player.current_rank),
                                            where("id") == player.id)
