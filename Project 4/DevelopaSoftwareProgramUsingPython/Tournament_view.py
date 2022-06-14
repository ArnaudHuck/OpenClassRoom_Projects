from Tournament_model import Tournament
from Player_model import Player


class TournamentView:

    @staticmethod
    def display_options():
        list_options = ["Create new tournament", "List all tournaments",
                        "Alphabetical list players in a tournament", "Ranking list players in a tournament",
                        "Back Home", "Quit"]
        print(f"[N] : {list_options[0]}")
        print(f"[L] : {list_options[1]}")
        print(f"[A] : {list_options[2]}")
        print(f"[R] : {list_options[3]}")
        print(f"[B] : {list_options[4]}")
        print(f"[Q] : {list_options[5]}")

    @staticmethod
    def display_tournament_list(tournaments: list[Tournament]):
        for tournament in tournaments:
            print(tournament, "\n")

    @staticmethod
    def display_tournament_time_control_options():
        list_options = ["Bullet", "Blitz", "Rapid"]
        print(f"[1] : {list_options[0]}")
        print(f"[2] : {list_options[1]}")
        print(f"[3] : {list_options[2]}")
