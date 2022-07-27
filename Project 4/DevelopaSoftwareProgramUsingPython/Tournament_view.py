from Tournament_model import Tournament
from Round_model import Round


class TournamentView:

    @staticmethod
    def display_options():
        """
        :return: Displays the Tournament menu
        """
        list_options = ["Create new tournament", "List all tournaments",
                        "Alphabetical list players in a tournament", "Ranking list players in a tournament",
                        "List of rounds in tournament", "Start_new_tournament", "Resume_tournament", "Quit"]
        print(f"[A] : {list_options[0]}")
        print(f"[B] : {list_options[1]}")
        print(f"[C] : {list_options[2]}")
        print(f"[D] : {list_options[3]}")
        print(f"[E] : {list_options[4]}")
        print(f"[F] : {list_options[5]}")
        print(f"[G] : {list_options[6]}")
        print(f"[Q] : {list_options[7]}")

    @staticmethod
    def display_tournament_list(tournaments: list[Tournament]):
        """
        :param tournaments: Takes a list of tournaments
        :return: Returns the main information of each tournament in the list
        """
        for tournament in tournaments:
            print(tournament.name, tournament.date, "\n")

    @staticmethod
    def display_tournament_time_control_options():
        """
        :return: Displays the time control options
        """
        list_options = ["Bullet", "Blitz", "Rapid"]
        print(f"[1] : {list_options[0]}")
        print(f"[2] : {list_options[1]}")
        print(f"[3] : {list_options[2]}")

    @staticmethod
    def display_tournament_list_of_rounds(list_of_rounds: list[Round]):
        """
        :param list_of_rounds: Takes a list of rounds
        :return: Displays the rounds information for each round in the list
        """
        for round in list_of_rounds:
            print(round.name, round.matches, "\n")

    @staticmethod
    def display_tournament_unfinished():
        """
        :return: Displays a list of tournament that has at least one played round
        """
        for tournament in Tournament.get_all_tournaments_unfinished_or_ended():
            if len(tournament.list_of_rounds) < tournament.number_of_rounds:
                print(tournament.id, tournament.name, tournament.date, "\n")
