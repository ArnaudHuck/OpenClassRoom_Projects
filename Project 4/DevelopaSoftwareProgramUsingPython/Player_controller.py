import sys

from basecontroller import BaseController
from operator import attrgetter
import re
from Player_model import Player
from Player_view import PlayerView
from main import main
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Main_Controller import MainController


class PlayerController(BaseController):

    @staticmethod
    def option_choice():
        """
        :return: Returns the entry matching the user's input
        """
        PlayerView.display_options()
        user_input = input().capitalize()
        if user_input == 'A':
            PlayerController.new_player()
            return PlayerController.option_choice()
        elif user_input == 'B':
            player_list = PlayerController.sorting_alphabetical(Player.get_all_players())
            PlayerView.display_player_list(player_list)
            PlayerController.wait_input()
            PlayerController.option_choice()
        elif user_input == 'C':
            player_list = PlayerController.sorting_rank(Player.get_all_players())
            PlayerView.display_player_list(player_list)
            PlayerController.wait_input()
            PlayerController.option_choice()
        elif user_input == 'D':
            player_list = PlayerController.sorting_default(Player.get_all_players())
            PlayerView.display_player_list(player_list)
            PlayerController.wait_input()
            PlayerController.option_choice()
        elif user_input == "E":
            PlayerController.change_player_rank()
        elif user_input == "F":
            MainController.home_menu()
        elif user_input == 'H':
            main()
        elif user_input == "Q":
            sys.exit()
        else:
            print('Invalid Input')
            PlayerController.option_choice()

    @staticmethod
    def sorting_default(list_players):
        """
        :param list_players: Takes a list of Players
        :return: Returns the list sorted by id
        """
        list_players.sort(key=attrgetter("id"))
        return list_players

    @staticmethod
    def sorting_alphabetical(list_players: list[Player]):
        """
        :param list_players: Takes a list of Players
        :return: Returns the list sorted by last name
        """
        list_players.sort(key=attrgetter("last_name", "first_name",
                                         "current_rank", "id"))
        return list_players

    @staticmethod
    def sorting_rank(list_players: list[Player]):
        """
        :param list_players: Takes a list of Players
        :return: Returns the list sorted by ranking
        """
        list_players.sort(key=attrgetter("current_rank"), reverse=True)
        return list_players

    @staticmethod
    def add_first_name():
        """
        :return: Returns the user's input after checking consistency
        """
        valid_first_name = False
        while not valid_first_name:
            input_first_name = input("First name : ").capitalize()
            if input_first_name != "":
                valid_first_name = True
            else:
                print("A valid first name is required")
        return input_first_name

    @staticmethod
    def add_last_name():
        """
        :return: Returns the user's input after checking consistency
        """
        valid_last_name = False
        while not valid_last_name:
            input_last_name = input("Last name : ").capitalize()
            if input_last_name != "":
                valid_last_name = True
            else:
                print("A valid last name is required")
        return input_last_name

    @staticmethod
    def add_date_birth():
        """
        :return: Returns the user's input after checking consistency
        """
        valid_birthdate = False
        while not valid_birthdate:
            input_date_birth = input("Date of birth (yyyy.mm.dd) : ")
            number = re.findall("[0-9]+", input_date_birth)
            if len(number) == 3:
                if \
                        len(number[0]) == 4 and int(number[0]) >= 1900 and 0 < int(number[1]) < 13 \
                        and 0 < len(number[1]) < 3 and 0 < int(number[2]) < 32 and 0 < len(number[2]) < 3:
                    if len(number[1]) == 1:
                        number[1] = str(0) + number[1]
                    if number[1] == "02":
                        if int(number[1]) > 29:
                            return "true"
                    if len(number[2]) == 1:
                        number[2] = str(0) + number[2]
                    valid_birthdate = True
                else:
                    print("A valid birthdate is required")
            else:
                print("A valid birthdate is required")
        return input_date_birth

    @staticmethod
    def add_gender():
        """
        :return: Returns the user's input after checking consistency
        """
        valid_gender = False
        while not valid_gender:
            input_gender = input("Gender (m/f) : ").capitalize()
            if input_gender == "M" or input_gender == "F":
                valid_gender = True
            else:
                print("A valid gender is required")
        return input_gender

    @staticmethod
    def add_current_rank():
        """
        :return: Returns the user's input after checking consistency
        """
        valid_rank = False
        while not valid_rank:
            input_current_rank = input("Current Rank : ")
            number = re.findall("[0-9]+", input_current_rank)
            if len(number) == 1:
                if 0 < int(number[0]):
                    valid_rank = True
            else:
                print("A valid rank is required")
        return int(input_current_rank)

    @staticmethod
    def new_player():
        """
        :return: Returns an object containing all previous inputs
        """

        new_player = []

        new_player.append(PlayerController.add_first_name())
        new_player.append(PlayerController.add_last_name())
        new_player.append(PlayerController.add_date_birth())
        new_player.append(PlayerController.add_gender())
        new_player.append(PlayerController.add_current_rank())
        return Player.add_player(new_player[0], new_player[1], new_player[2], new_player[3], new_player[4])

    @staticmethod
    def change_player_rank():
        """
        :return: User selects the player he wants to modify the score, then inputs the new score which is updated in db
        """
        player_list = PlayerController.sorting_default(Player.get_all_players())
        PlayerView.display_player_list(player_list)
        choice = input("Enter the player id you wish to modify: ")
        player = Player.get_player(int(choice))
        if player is None:
            print("The player does not exists")
            BaseController.wait_input()
            PlayerController.change_player_rank()
        else:
            print(player)
            BaseController.wait_input()
            choice = input("Do you want to modify the current rank ? (Y/N): ")
            if choice == "Y":
                print(f'What is the new rank of {player.first_name}?:')
                valid_rank = False
                while not valid_rank:
                    new_rank = input("Enter the new rank value: ")
                    number = re.findall("[0-9]+", new_rank)
                    if len(number) == 1:
                        if 0 < int(number[0]):
                            valid_rank = True
                            player.current_rank = int(new_rank)
                            print(player)
                            Player.update_player_rank(player)
                    else:
                        print("A valid rank is required")
                        continue
            elif choice == "N":
                PlayerController.option_choice()
            else:
                print("You need to enter Y or N")
                BaseController.wait_input()









