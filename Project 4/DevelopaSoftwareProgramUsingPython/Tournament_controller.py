from datetime import datetime
from dataclasses import dataclass
from typing import Tuple, List
from simple_term_menu import TerminalMenu
from Player_controller import Player


@dataclass
class Tournament:
    name: str
    venue: str
    date: Tuple[datetime]
    rounds: []
    players: List[Player]
    time_control: str
    description: str
    number_of_rounds: int


class View:
    def prompt_for_new_tournament(self):
        tournament_name = input("Type tournament name: ")
        tournament_venue = input("Type tournament venue: ")
        tournament_date = input("Type tournament date: ")
        tournament_rounds = input("Type tournament rounds: ")
        tournament_players = input("Type tournament players: ")
        tournament_time_control = input("Type tournament time control: [Blitz/Rapid/Bullet] ?")
        tournament_description = input("Type tournament description: ")
        tournament_number_of_rounds = input("Type tournament number of rounds: ")
        tournament = [tournament_name, tournament_venue, tournament_date, tournament_rounds, tournament_players,
                      tournament_time_control, tournament_description, tournament_number_of_rounds]
        return tournament

    def prompt_tournament_menu(self):
        main_menu = ["[a] Create new tournament", "[b] Create tournament reports", "[q] quit"]
        sub_menu = ["[a] Alphabetical", "[b] Ranking", "[c] go back"]

        loop = True

        while loop:
            choice = main_menu[TerminalMenu(main_menu, title="Tournament menu").show()]

            if choice == "[a] Create new tournament":
                self.prompt_for_new_tournament()

            elif choice == "[b] Create tournament reports":
                sub_loop = True
                while sub_loop:
                    choice = sub_menu[TerminalMenu(sub_menu, title="Tournament sub menu").show()]

                    if choice == "[a] Alphabetical":
                        print(choice)

                    elif choice == "[b] Ranking":
                        print(choice)

                    elif choice == "[c] go back":
                        sub_loop = False

            elif choice == "[q] quit":
                loop = False


class GameController:
    def __init__(self, tournament, view, game_evaluator):
        # Model
        self.tournament = tournament
        # View
        self.view = view

        # Controller
        self.game_evaluator = game_evaluator

    def create_tournament(self):
        pass


view = View()
view.prompt_tournament_menu()
