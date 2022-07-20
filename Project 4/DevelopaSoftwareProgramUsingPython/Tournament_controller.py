import sys

from basecontroller import BaseController
from operator import attrgetter
import re
from datetime import date
from datetime import datetime
from Tournament_model import Tournament
from Tournament_view import TournamentView
from Player_model import Player
from Player_view import PlayerView
from Round_model import Round
from typing import Optional
from Match_model import Match


class TournamentController(BaseController):

    @staticmethod
    def option_choice():
        TournamentView.display_options()
        user_input = input().capitalize()
        if user_input == "A":
            TournamentController.add_new_tournament()
            BaseController.wait_input()
            return TournamentController.option_choice()
        elif user_input == "B":
            TournamentView.display_tournament_list(Tournament.get_all_tournaments())
            BaseController.wait_input()
            return TournamentController.option_choice()
        elif user_input == "C":
            TournamentView.display_tournament_list(Tournament.get_all_tournaments())
            tournament_id = input("Enter the tournament id you wish to select: ")
            list_player = TournamentController.sort_list_of_player_in_tournament_alphabetically(tournament_id)
            for player in list_player:
                print(player)
            BaseController.wait_input()
            return TournamentController.option_choice()
        elif user_input == "D":
            TournamentView.display_tournament_list(Tournament.get_all_tournaments())
            tournament_id = input("Enter the tournament id you wish to select: ")
            list_player = TournamentController.sort_list_of_player_in_tournament_ranking(tournament_id)
            for player in list_player:
                print(player)
            BaseController.wait_input()
            return TournamentController.option_choice()
        elif user_input == "E":
            TournamentView.display_tournament_list(Tournament.get_all_tournaments())
            tournament_id = input("Enter the tournament id you wish to select: ")
            TournamentView.display_tournament_list_of_rounds(Tournament.get_tournament_rounds
                                                             (Tournament.get_tournament(tournament_id)))
            BaseController.wait_input()
            return TournamentController.option_choice()
        elif user_input == "F":
            tournament = StartTournament()
            tournament()
        elif user_input == "G":
            StartTournament.resume_tournament()
        elif user_input == "Q":
            sys.exit()
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
                        len(number[0]) == 4 and int(number[0]) >= 1900 and 0 < int(number[1]) < 13 \
                        and 0 < len(number[1]) < 3 and 0 < int(number[2]) < 32 and 0 < len(number[2]) < 3:
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
                                len(number2[0]) == 4 and int(number2[0]) >= 1900 and 0 < int(number2[1]) < 13 \
                                and 0 < len(number2[1]) < 3 and 0 < int(number2[2]) < 32 and 0 < len(number2[2]) < 3:
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
    def add_tournament_participant_list() -> Optional[list[Player]]:
        all_participant: list[Player] = []
        choice = input("Do you wish to add a new player ?  Y/N: ")
        if choice == "Y":
            all_players = TournamentController.sorting_default(Player.get_all_players())
            PlayerView.display_player_list(all_players)
            while not len(all_participant) == 8:
                player_id = int(input("Enter the player id you wish to add to the tournament: "))
                if player_id <= 0 or player_id > len(all_players):
                    print("You need to input a valid id")
                    BaseController.wait_input()
                    continue
                for player in all_participant:
                    if int(player_id) == player.id:
                        print("Selected player is already added to the tournament")
                        BaseController.wait_input()
                        continue
                else:
                    added_player = Player.get_player(player_id)
                    all_participant.append(added_player)
                    print(all_participant)
        elif choice == "N":
            return None
        else:
            print("Input Y or N")
        return all_participant

    @staticmethod
    def sort_list_of_player_in_tournament_alphabetically(user_input) -> list[Player]:
        tournament = Tournament.get_tournament(int(user_input))
        list_player = tournament.participant_list
        new_list = sorted(list_player, key=lambda player: player.last_name)
        return new_list

    @staticmethod
    def sort_list_of_player_in_tournament_ranking(user_input) -> list[Player]:
        tournament = Tournament.get_tournament(int(user_input))
        list_player = tournament.participant_list
        new_list = sorted(list_player, key=lambda player: player.current_rank, reverse=True)
        return new_list

    @staticmethod
    def sorting_default(list_players):
        list_players.sort(key=attrgetter("id"))
        return list_players

    @staticmethod
    def add_new_tournament():

        new_tournament = [TournamentController.add_tournament_name(), TournamentController.add_tournament_venue(),
                          TournamentController.add_tournament_date(),
                          TournamentController.add_tournament_number_of_rounds(),
                          TournamentController.add_tournament_time_control(),
                          TournamentController.add_tournament_description(),
                          TournamentController.add_tournament_participant_list()]

        return Tournament.add_tournament(new_tournament[0], new_tournament[1], new_tournament[2], new_tournament[3],
                                         new_tournament[4], new_tournament[5], new_tournament[6])


class StartTournament:
    MATCH_PLAYED: list[Match] = []
    ROUNDS_PLAYED: list[Round] = []

    def __call__(self):
        self.sorted_players: list[Player] = []

        print(Tournament.get_all_tournaments())
        self.tournament = Tournament.get_tournament(int(input("Enter the tournament id you wish to start: ")))
        self.round = Round.make(self.tournament)
        self.sorted_players = self.sort_players_first_tour(self.tournament)
        self.tournament.list_of_rounds.append(self.round.run(self.sorted_players, self.tournament))
        self.tournament.save_participant_score(self.tournament)
        self.tournament.add_tournament_in_progress(self.tournament)
        self.leave_or_stay()

        for round_index in range(self.tournament.number_of_rounds - 1):
            self.sorted_players.clear()
            self.sorted_players = self.sort_players_next_tours(self.tournament)
            self.tournament.list_of_rounds.append(self.round.run(self.sorted_players, self.tournament))
            self.tournament.save_participant_score(self.tournament)
            self.tournament.add_tournament_in_progress(self.tournament)
            self.leave_or_stay()
        print(self.who_is_winner(self.tournament.participant_score))

    @staticmethod
    def has_match_been_not_played(test_match: set[int], list_of_finished_matches: list[Match]):
        for match in list_of_finished_matches:
            match_set = {match.player_1.id, match.player_2.id}
            if test_match == match_set:
                return True
            else:
                continue
        return False

    @staticmethod
    def sort_players_first_tour(tournament: Tournament):

        sorted_players: list[Player] = []
        players_instances: list[Player] = []

        for player in TournamentController.sort_list_of_player_in_tournament_ranking(tournament.id):
            players_instances.append(player)

        for player in players_instances:
            player_1 = player
            index_player_1 = players_instances.index(player)

            if index_player_1 + len(tournament.participant_list) / 2 < len(tournament.participant_list):
                index_player_2 = index_player_1 + int(len(tournament.participant_list) / 2)
                player_2 = players_instances[index_player_2]
                sorted_players.append(player_1)
                sorted_players.append(player_2)
                StartTournament.MATCH_PLAYED.append(Match(Match.MATCH_NUMBER, player_1, player_2, 0, 0))  # type: ignore
                print(StartTournament.MATCH_PLAYED)
            else:
                pass

        return sorted_players

    @staticmethod
    def sort_players_next_tours(tournament: Tournament):

        players_id_and_score: list[dict] = []
        players_instance: list[Player] = []
        players_sorted_by_score: list[Player] = []
        match_to_try = set()

        players = tournament.participant_list
        player_score_list = tournament.participant_score
        for key in player_score_list:
            for player in players:
                if int(key) == player.id:
                    players_id_and_score.append({"player_id": player.id, "player_rank": player.current_rank,
                                                 "player_score": player_score_list[key]})

        sorted_new_list = sorted(players_id_and_score, key=lambda x: (x['player_score'], x['player_rank']),
                                 reverse=True)
        print(sorted_new_list)
        for player_dict in sorted_new_list:
            players_sorted_by_score.append(Player.get_player(player_dict['player_id']))

        for player_1 in players_sorted_by_score:

            if player_1 in players_instance:
                continue
            else:
                try:
                    player_2 = players_sorted_by_score[players_sorted_by_score.index(player_1) + 1]
                except Exception:
                    break

            match_to_try.add(player_2.id)
            match_to_try.add(player_1.id)

            while StartTournament.has_match_been_not_played(match_to_try, StartTournament.MATCH_PLAYED) is True:
                print(f"The match {player_1} versus {player_2} already took place")
                match_to_try.remove(player_2.id)
                try:
                    player_2 = players_sorted_by_score[players_sorted_by_score.index(player_2) + 1]
                except Exception:
                    break
                match_to_try.add(player_2.id)
                continue

            else:
                print(f"Adding match {player_1} versus {player_2}")
                players_instance.append(player_1)
                players_instance.append(player_2)
                players_sorted_by_score.pop(players_sorted_by_score.index(player_2))
                StartTournament.MATCH_PLAYED.append(Match(Match.MATCH_NUMBER, player_1, player_2, 0, 0))  # type: ignore
                match_to_try.clear()
        return players_instance

    @staticmethod
    def who_is_winner(participant_final_scores: dict[int, float]) -> str:

        new_value = max(participant_final_scores, key=participant_final_scores.get)  # type: ignore
        return f'{Player.get_player(new_value)} is the big winner'

    @staticmethod
    def resume_tournament():

        sorted_players = []
        TournamentView.display_tournament_unfinished()
        BaseController.wait_input()
        valid_entry = False
        while not valid_entry:
            choice = input("Which tournament do you wish to resume?: ")
            try:
                int(choice)
                valid_entry = True
            except Exception:
                print("You need to enter a valid tournament id")
            else:
                chosen_tournament = Tournament.get_unfinished_tournament(choice)
                for finished_round in chosen_tournament.list_of_rounds:
                    for match in finished_round.matches:
                        StartTournament.MATCH_PLAYED.append(Match(Match.MATCH_NUMBER, match.player_1, match.player_2,
                                                                  match.score_player_1, match.score_player_2))

                for round in range(int(chosen_tournament.number_of_rounds) - len(chosen_tournament.list_of_rounds)):
                    sorted_players.clear()
                    sorted_players = StartTournament.sort_players_next_tours(chosen_tournament)
                    tournament_round = Round.make(chosen_tournament)
                    chosen_tournament.list_of_rounds.append(tournament_round.run(sorted_players, chosen_tournament))
                    Tournament.save_participant_score(chosen_tournament)
                    Tournament.add_tournament_in_progress(chosen_tournament)
                    StartTournament.leave_or_stay()
                print(StartTournament.who_is_winner(chosen_tournament.participant_score))

    @staticmethod
    def leave_or_stay():
        print("Do you wish to leave the current tournament ?")
        valid_choice = False
        while not valid_choice:
            choice = input("Enter: Y or N: ")
            if choice == "Y":
                valid_choice = True
                sys.exit()
            elif choice == "N":
                valid_choice = True
                break
            else:
                print("You need to enter Y or N")
