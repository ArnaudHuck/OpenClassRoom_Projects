import sys

from Main_view import MainView
from Player_controller import PlayerController
from Tournament_controller import TournamentController


class MainController:
    def __init__(self):
        pass

    @staticmethod
    def home_menu():
        """
        :return: Displays the home menu
        """
        MainView.home_menu_view()
        choice = input("Which menu do you wish to select ?: ")
        if choice == "P":
            PlayerController.option_choice()
        if choice == "T":
            TournamentController.option_choice()
        if choice == "Q":
            sys.exit()
