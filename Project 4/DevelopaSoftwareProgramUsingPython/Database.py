from tinydb import TinyDB, where, Query


class DataBaseController:
    db = TinyDB("db.json")
    player_db = db.table("Players")
    tournament_db = db.table("Tournament")
    round_db = db.table("Rounds")
    match_db = db.table("Matches")

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
    def clean_player_database():
        DataBaseController.player_db.truncate()

    @staticmethod
    def list_tournament() -> list[dict]:
        return DataBaseController.tournament_db.all()

    @staticmethod
    def get_len_tournament_in_db():
        return len(DataBaseController.tournament_db)

    @staticmethod
    def add_tournament(new_tournament):
        DataBaseController.tournament_db.insert(new_tournament)

    @staticmethod
    def clean_tournament_database():
        DataBaseController.tournament_db.truncate()

    @staticmethod
    def clean_round_database():
        DataBaseController.round_db.truncate()

    @staticmethod
    def add_round_in_db(new_round):
        DataBaseController.round_db.insert(new_round)



