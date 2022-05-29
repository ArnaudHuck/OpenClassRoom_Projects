import time
import copy
from basecontroller import BaseController
from operator import attrgetter
import re
from datetime import date
from datetime import datetime
from Tournament_model import Tournament
from Tournament_view import TournamentView
from Player_model import Player
from Player_view import PlayerView
from operator import itemgetter
from Round_model import Round
from Match_model import Match


class TournamentController(BaseController):

    @staticmethod
    def option_choice():
        TournamentView.display_options()
        user_input = input().capitalize()
        if user_input == "N":
            TournamentController.add_new_tournament()
            BaseController.wait_input()
            return TournamentController.option_choice()
        elif user_input == "L":
            TournamentView.display_tournament_list(Tournament.get_all_tournaments())
            BaseController.wait_input()
            return TournamentController.option_choice()
        elif user_input == "A":
            TournamentView.display_tournament_list(Tournament.get_all_tournaments())
            tournament_id = input("Enter the tournament id you wish to select: ")
            list_player = TournamentController.sort_list_of_player_in_tournament_alphabetically(tournament_id)
            for player in list_player:
                print(player)
            BaseController.wait_input()
            return TournamentController.option_choice()
        elif user_input == "R":
            TournamentView.display_tournament_list(Tournament.get_all_tournaments())
            tournament_id = input("Enter the tournament id you wish to select: ")
            list_player = TournamentController.sort_list_of_player_in_tournament_ranking(tournament_id)
            for player in list_player:
                print(player)
            BaseController.wait_input()
            return TournamentController.option_choice()
        elif user_input == "B":
            pass
        elif user_input == "Q":
            return
        else:
            print('Invalid Input')
            TournamentController.option_choice()

    @staticmethod
    def add_tournament_name():
        valid_tournament_name = False
        while not valid_tournament_name:
            input_tournament_name = input("Tournament name: ").capitalize()
            if input_tournament_name != "":
                valid_tournament_name = True
                return input_tournament_name
            else:
                print("A valid tournament name is required")


    @staticmethod
    def add_tournament_venue():
        valid_tournament_venue = False
        while not valid_tournament_venue:
            input_tournament_venue = input("Tournament venue: ")
            if input_tournament_venue != "":
                valid_tournament_venue = True
                return input_tournament_venue
            else:
                print("A valid tournament venue is required")


    @staticmethod
    def add_tournament_date():
        valid_tournament_date = False
        while not valid_tournament_date:
            input_beginning_tournament_date = input("Tournament beginning date (yyyy.mm.dd): ")
            beginning_date_time_obj = datetime.strptime(input_beginning_tournament_date, '%Y.%m.%d')
            number = re.findall("[0-9]+", input_beginning_tournament_date)
            if len(number) == 3:
                if \
                        len(number[0]) == 4 \
                                and int(number[0]) >= 1900 \
                                and 0 < int(number[1]) < 13 \
                                and 0 < len(number[1]) < 3 \
                                and 0 < int(number[2]) < 32 \
                                and 0 < len(number[2]) < 3:
                    if len(number[1]) == 1:
                        number[1] = str(0) + number[1]
                    if number[1] == "02":
                        if int(number[1]) > 29:
                            return "true"
                    if len(number[2]) == 1:
                        number[2] = str(0) + number[2]
            if beginning_date_time_obj.date() >= date.today():
                input_ending_tournament_date = input("Tournament ending date (yyyy.mm.dd): ")
                if input_ending_tournament_date == "":
                    return input_beginning_tournament_date.__str__()
                else:
                    ending_date_time_obj = datetime.strptime(input_ending_tournament_date, '%Y.%m.%d')
                    number2 = re.findall("[0-9]+", input_ending_tournament_date)
                    if len(number2) == 3:
                        if \
                                    len(number2[0]) == 4 \
                                            and int(number2[0]) >= 1900 \
                                            and 0 < int(number2[1]) < 13 \
                                            and 0 < len(number2[1]) < 3 \
                                            and 0 < int(number2[2]) < 32 \
                                            and 0 < len(number2[2]) < 3:
                            if len(number2[1]) == 1:
                                number2[1] = str(0) + number2[1]
                            if number2[1] == "02":
                                if int(number2[1]) > 29:
                                    return "true"
                            if len(number2[2]) == 1:
                                number2[2] = str(0) + number2[2]
                            if ending_date_time_obj > beginning_date_time_obj:
                                return input_beginning_tournament_date.__str__(), input_ending_tournament_date.__str__()

    @staticmethod
    def add_tournament_number_of_rounds():
        number_of_round = 4
        print("The number of round is set on 4 would you like to change it ? ")

        valid_number = False
        while not valid_number:
            choice = input("Y or N: ")
            if choice == "Y":
                number_of_round = input("Input the desired number of round: ")
                if number_of_round.isdigit():
                    valid_number = True
                else:
                    print("You need to input an integer")
            if choice == "N":
                valid_number = True
        return number_of_round

    @staticmethod
    def add_tournament_time_control():
        time_control = None
        TournamentView.display_tournament_time_control_options()
        user_input = input("Select the tournament time control: ")
        if user_input == "1":
            time_control = "Bullet"
        if user_input == "2":
            time_control = "Blitz"
        if user_input == "3":
            time_control = "Rapid"
        return time_control

    @staticmethod
    def add_tournament_description():
        description = input("Enter the tournament description: ")
        return description

    @staticmethod
    def add_tournament_participant_list() -> list[dict]:
        all_participant = []
        choice = input("Do you wish to add a new player ?  Y/N: ")
        if choice == "Y":
            all_players = TournamentController.sorting_default(Player.get_all_players())
            PlayerView.display_player_list(all_players)
            while not len(all_participant) == 8:
                player_id = input("Enter the player id you wish to add to the tournament: ")
                player_id = int(player_id)
                if player_id <= 0 or player_id > len(all_players):
                    print("You need to input a valid id")
                    BaseController.wait_input()
                    continue
                for player in all_participant:
                    if player.__getitem__('id') == player_id:
                        print("Selected player is already added to the tournament")
                        BaseController.wait_input()
                        continue
                else:
                    added_player = Player.get_player(player_id)
                    all_participant.append(added_player)
                    print(all_participant)
        elif choice == "N":
            return
        else:
            print("Input Y or N")
        return all_participant

    @staticmethod
    def sort_list_of_player_in_tournament_alphabetically(user_input) -> [list[Player]]:
        tournament = Tournament.get_tournament(int(user_input))
        tournament_object = Tournament.deserialize_tournament(tournament)
        list_player = tournament_object.__getattribute__('participant_list')
        new_list = sorted(list_player, key=itemgetter('first_name'))
        return new_list

    @staticmethod
    def sort_list_of_player_in_tournament_ranking(user_input) -> [list[Player]]:
        tournament = Tournament.get_tournament(int(user_input))
        tournament_object = Tournament.deserialize_tournament(tournament)
        list_player = tournament_object.__getattribute__('participant_list')
        new_list = sorted(list_player, key=itemgetter('current_rank'), reverse=True)
        return new_list

    @staticmethod
    def sorting_default(list_players):
        list_players.sort(key=attrgetter("id"))
        return list_players

    @staticmethod
    def add_new_tournament():

        new_tournament = []

        new_tournament.append(TournamentController.add_tournament_name())
        new_tournament.append(TournamentController.add_tournament_venue())
        new_tournament.append(TournamentController.add_tournament_date())
        new_tournament.append(TournamentController.add_tournament_number_of_rounds())
        new_tournament.append(TournamentController.add_tournament_time_control())
        new_tournament.append(TournamentController.add_tournament_description())
        new_tournament.append(TournamentController.add_tournament_participant_list())
        return Tournament.add_tournament(new_tournament[0], new_tournament[1], new_tournament[2], new_tournament[3],
                                         new_tournament[4], new_tournament[5], new_tournament[6])


class StartTournament:

    MATCH_PLAYED = []
    ROUNDS_PLAYED = []

    def __call__(self):
        self.sorted_players = []

        self.round = Round()
        self.tournament_object = Tournament.deserialize_tournament(Tournament.get_tournament(id))
        self.sorted_players = self.sort_players_first_tour(self.tournament_object)
        self.tournament_object.list_of_rounds.append(self.round.run(self.sorted_players, self.tournament_object))
        self.save_tournament_statement(self.tournament_object)

        for tour in range(int(self.tournament_object.number_of_rounds) - 1):
            self.sorted_players.clear()
            self.sorted_players = self.sort_players_second_tour((self.tournament_object.list_of_rounds[round]))

    @staticmethod
    def save_tournament_statement(tournament_object):

        round_object = Tournament.deserialize_tournament(tournament_object).list_of_rounds[-1]
        round_serialized = round_object.serialized()
        round_serialized['list_of_finished_matches'] = round_object.list_of_finished_matchs
        round_id = Round.add_round("", round_object.list_of_finished_matchs)
        StartTournament.ROUNDS_PLAYED.append(round_id)

    @staticmethod
    def sort_players_first_tour(tournament: [Tournament]):

        sorted_players = []
        players_instances = []

        for serialized_player in TournamentController.sort_list_of_player_in_tournament_ranking(Tournament.deserialize_tournament(tournament).id):
            player = Player.deserialize(serialized_player)
            players_instances.append(player)

        for player in players_instances:
            player_1 = player
            index_player_1 = players_instances.index(player)

            if index_player_1 + len(Tournament.deserialize_tournament(tournament).participant_list) / 2 < len(Tournament.deserialize_tournament(tournament).participant_list):
                index_player_2 = index_player_1 + int(len(Tournament.deserialize_tournament(tournament).participant_list) / 2)
                player_2 = players_instances[index_player_2]
                sorted_players.append(player_1)
                sorted_players.append(player_2)
                StartTournament.MATCH_PLAYED.append({player_1.id, player_2.id})
            else:
                pass

        return sorted_players
#       return [Player.serialize(player) for player in sorted_players]

    @staticmethod
    def sort_players_second_tour(round_instance):
        player = Player()
        players = []
        players_sorted_by_score = []
        players_sorted_flat = []
        players_instance = []
        match_to_try = set()

        for match in Round.deserialize_round(round_instance).list_of_rounds:
            print(match)
            for player in match:
                players.append(player)

        players_sorted_by_score = copy.copy(players)

        for player in players_sorted_by_score:
            players_sorted_flat.append(player[0])

        players_sorted_by_score.clear()

        # Sort players by score, if score are equals, sort by rank.
        players_instance.sort(key=attrgetter("tournament_score", 'ranking'), reverse=True)

        for player_1 in players_instance:

            if player_1 in players_sorted_by_score:
                continue
            else:
                try:
                    player_2 = players_instance[players_instance.index(player_1) + 1]
                except Exception:
                    break

            match_to_try.add(player_1.player_id)
            match_to_try.add(player_2.player_id)

            while match_to_try in StartTournament.MATCH_PLAYED:  # compare match_to_try with matchs already played
                print(f"Le match {player_1} CONTRE {player_2} a déjà eu lieu")
                time.sleep(1)
                match_to_try.remove(player_2.player_id)
                try:
                    player_2 = players_instance[players_instance.index(player_2) + 1]
                except Exception:
                    break
                match_to_try.add(player_2)
                continue

            else:
                print(f"Ajout du match {player_1} CONTRE {player_2}")
                players_sorted_by_score.append(player_1)
                players_sorted_by_score.append(player_2)
                players_instance.pop(players_instance.index(player_2))
                StartTournament.MATCH_PLAYED.append({player_1.player_id, player_2.player_id})
                match_to_try.clear()
                time.sleep(1)

        return players_sorted_by_score
