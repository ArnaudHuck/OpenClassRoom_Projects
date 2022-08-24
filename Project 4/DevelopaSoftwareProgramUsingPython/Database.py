from tinydb import TinyDB


class DataBaseController:
    db = TinyDB("db.json")
    player_db = db.table("Players")
    tournament_db = db.table("Tournament")
    tournament_in_progress_or_ended_db = \
        db.table("Tournament in progress or ended")
    round_db = db.table("Rounds")
    match_db = db.table("Matches")

    @staticmethod
    def get_tournament(tournament_id: int) -> dict:
        """
        :param tournament_id: Takes an int as input
        :return: Returns the tournament matching the input
        """
        return DataBaseController.tournament_db.get(doc_id=tournament_id)

    @staticmethod
    def get_unfinished_tournament(tournament_id: int) -> dict:
        """
        :param tournament_id: Takes an int as input
        :return: Returns the tournament matching the input
        """
        return DataBaseController.tournament_in_progress_or_ended_db. \
            get(doc_id=tournament_id)  # type: ignore

    @staticmethod
    def get_len_players_in_db():
        """
        :return: Returns the number of created player in DB
        """
        return len(DataBaseController.player_db)

    @staticmethod
    def list_player() -> list:
        """
        :return: Returns the list of players in DB
        """
        return DataBaseController.player_db.all()

    @staticmethod
    def add_player(new_player):
        """
        :param new_player: Takes a new player
        :return: Add the new player to the DB
        """
        DataBaseController.player_db.insert(new_player)

    @staticmethod
    def clean_player_database():
        """
        :return: Clean the Player table
        """
        DataBaseController.player_db.truncate()

    @staticmethod
    def list_tournament() -> list:
        """
        :return: Returns the list of tournaments in DB
        """
        return DataBaseController.tournament_db.all()

    @staticmethod
    def get_len_tournament_in_db():
        """
        :return: Returns the number of created tournament in DB
        """
        return len(DataBaseController.tournament_db)

    @staticmethod
    def list_tournament_ended_or_unfinished():
        """
        :return: Returns the list of ended or unfinished tournaments
        """
        return DataBaseController.tournament_in_progress_or_ended_db.all()

    @staticmethod
    def add_tournament(new_tournament):
        """
        :param new_tournament: Takes a new tournament
        :return: Adds the new tournament to the tournament DB
        """
        DataBaseController.tournament_db.insert(new_tournament)

    @staticmethod
    def clean_tournament_database():
        """
        :return: Clean the tournament table
        """
        DataBaseController.tournament_db.truncate()

    @staticmethod
    def add_tournament_in_progress(new_tournament):
        """
        :param new_tournament: Takes a new tournament
        :return: Adds the new tournament to the DB
        """
        DataBaseController.tournament_in_progress_or_ended_db. \
            insert(new_tournament)

    @staticmethod
    def clean_tournament_in_progress_database():
        """
        :return: Clean the tournament in progress table
        """
        DataBaseController.tournament_in_progress_or_ended_db.truncate()
