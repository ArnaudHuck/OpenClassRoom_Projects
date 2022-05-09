from tinydb import TinyDB, where, Query


class DataBaseController:
    db = TinyDB("db.json")
    player_db = db.table("Players")

    def __init__(self):
        self.players = []

    @staticmethod
    def get_len_players_in_db():
        return len(DataBaseController.player_db)

    @staticmethod
    def list_player() -> list[dict]:
        return DataBaseController.player_db.all()

    @staticmethod
    def add_player(new_player):
        DataBaseController.player_db.insert(new_player)

    @staticmethod
    def clean_database():
        DataBaseController.player_db.truncate()

    @staticmethod
    def get_player(player_first_name, player_last_name, player_birthdate):
        for player in DataBaseController.list_player():
            if player.__getitem__('first_name') == player_first_name \
                    and player.__getitem__('last_name') == player_last_name \
                    and player.__getitem__('date_of_birth') == player_birthdate:
                return player
        else:
            print('No match')





