from simple_term_menu import TerminalMenu

all_players = []


class Player:
    def __init__(self, first_name, last_name, date_of_birth, sex, rating):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.rating = rating

    def name(self):
        return " ".join([self.first_name, self.last_name])

    def __str__(self):
        return f'{self.name()}({self.rating})'


class View:
    def prompt_for_new_player(self):
        player_first_name = input("Type player first name: ")
        player_last_name = input("Type player last name: ")
        player_date_of_birth = input("Type player date of birth: ")
        player_gender = input("Type player gender M/F: ")
        player_rating = input("Type Rating of the player: ")
        new_player = [player_first_name, player_last_name, player_date_of_birth, player_gender, player_rating]
        if new_player == "":
            return None
        return new_player

    def prompt_player_menu(self):
        main_menu = ["[a] Add Player", "[b] Create Player reports", "[q] quit"]
        sub_menu = ["[a] Alphabetical", "[b] Ranking", "[c] go back"]

        loop = True

        while loop:
            choice = main_menu[TerminalMenu(main_menu, title="player menu").show()]

            if choice == "[a] Add Player":
                self.prompt_for_new_player()

            elif choice == "[b] Create List of Player":
                sub_loop = True
                while sub_loop:
                    choice = sub_menu[TerminalMenu(sub_menu, title="Player Sub menu").show()]

                    if choice == "[a] Alphabetical":
                        print(choice)

                    elif choice == "[b] Ranking":
                        print(choice)

                    elif choice == "[c] go back":
                        sub_loop = False

            elif choice == "[q] quit":
                loop = False


class PlayerController:
    def __init__(self, player, view):
        # Model
        self.players = []
        self.player = player
        # View
        self.view = view

    def add_player(self, first_name, last_name, date_of_birth, sex, rating):
        self.players.append(Player(first_name, last_name, date_of_birth, sex, rating))

    def create_players_list_alphabetical(self):
        return sorted(self.players, key=Player.name)

    def create_players_list_ranking(self):
        return sorted(self.players, key=Player.rating())


