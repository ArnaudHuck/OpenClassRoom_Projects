from tinydb import TinyDB


class DataBaseController:
    db = TinyDB("db.json")
    player_db = db.table("Players")
    tournament_db = db.table("Tournament")
    tournament_in_progress_or_ended_db = db.table("Tournament in progress or ended")
    round_db = db.table("Rounds")
    match_db = db.table("Matches")

    @staticmethod
    def get_tournament(tournament_id: int) -> dict:
        return DataBaseController.tournament_db.get(doc_id=tournament_id)  # type: ignore

    @staticmethod
    def get_unfinished_tournament(tournament_id: int) -> dict:
        return DataBaseController.tournament_in_progress_or_ended_db.get(doc_id=tournament_id)  # type: ignore

    @staticmethod
    def get_len_players_in_db():
        return len(DataBaseController.player_db)

    @staticmethod
    def list_player() -> list:
        return DataBaseController.player_db.all()

    @staticmethod
    def add_player(new_player):
        DataBaseController.player_db.insert(new_player)

    @staticmethod
    def clean_player_database():
        DataBaseController.player_db.truncate()

    @staticmethod
    def list_tournament() -> list:
        return DataBaseController.tournament_db.all()

    @staticmethod
    def get_len_tournament_in_db():
        return len(DataBaseController.tournament_db)

    @staticmethod
    def list_tournament_ended_or_unfinished():
        return DataBaseController.tournament_in_progress_or_ended_db.all()

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
    def add_tournament_in_progress(new_tournament):
        DataBaseController.tournament_in_progress_or_ended_db.insert(new_tournament)

    @staticmethod
    def clean_tournament_in_progress_database():
        DataBaseController.tournament_in_progress_or_ended_db.truncate()
