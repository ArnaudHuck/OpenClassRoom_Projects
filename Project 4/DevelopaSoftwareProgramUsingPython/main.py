import operator
import datetime
from dataclasses import dataclass


@dataclass
class Player:
    first_name : str
    last_name : str
    date_of_birth : datetime
    sex : str
    rating : int

    def __str__(self):
        return f'{self.first_name}{self.last_name}({self.rating})'


class Tournament:
    def __init__(self, name, venue, date, rounds, players, time_control, description,  number_of_rounds=4):
        self.name = name
        self.venue = venue
        self.date = date
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description
        self.number_of_rounds = number_of_rounds


class Round:
    def __init__(self):
        self.list_of_match = []


class Match:
    def __init__(self, pair_of_players):
        self.pair_of_player =


class View:
    def prompt_for_new_player(self):
        player_first_name = input("Type player first name: ")
        player_last_name = input("Type player last name: ")
        player_date_of_birth = input("Type player date of birth: ")
        player_gender = input("Type player gender M/F: ")
        player_rating = input("Type name of the player [1:8]: ")
        new_player = [player_first_name, player_last_name, player_date_of_birth, player_gender, player_rating]
        if new_player == "":
            return None
        return new_player


class GameController:
    def __init__(self, tournament, view, game_evaluator):
        # Model
        self.players = []
        self.tournament = tournament
        # View
        self.view = view

        # Controller
        self.game_evaluator = game_evaluator

    def create_tournament(self):
        pass

    def add_player(self, first_name, last_name, date_of_birth, sex, rating):
        self.players.append(Player(first_name, last_name, date_of_birth, sex, rating))

    def sort_player_by_rank(self):
        ranking_list = []
        for player in self.players:
            ranking_list.append([player[0], player[4]])
            ranking_list.sort(key=operator.itemgetter('rating'))
            middle_index = len(ranking_list)//2
            upper_ranks = ranking_list[:middle_index]
            lower_ranks = ranking_list[middle_index:]
            return upper_ranks, lower_ranks

    def run(self):
        while len(self.players) != 8:
            new_player = self.view.prompt_for_new_player()
            if new_player is None and len(self.players) != 8:
                break
            self.add_player(new_player)














