import Database
import Player_model
import Player_view
import Player_controller
import Tournament_controller
import Tournament_model
import Round_model

# ('faustine', 'Boudin', '1984.12.06', 'F', 2200)
# ('Henry', 'Huck', '1992.08.04', 'M', 2500)
# ('Alice', 'Charles', '1994.12.07', 'F', 2900)
# ('Gregoris', 'Lassale', '1978.11.18', 'H', 1800)
# ('Philippe', 'Pitou', '1997.10.05', 'H', 1600)
# ('Sabine', 'Foo', '1990.05.12', 'F', 2100)
# ('Benoit', 'Benithon', '1993.08.10', 'H', 2600)
# ('Olivier', 'Dubois', '1979.03.06', 'H', 1900)

# Player_model.Player.add_player('Sabine', 'Foo', '1990.05.12', 'F', 2100)
# print(Database.DataBaseController.get_len_players_in_db())
# All_players = Player_model.Player.get_all_players()
# A = (Player_model.DataBaseController.list_player())
# B = Database.DataBaseController.get_player('Henry', 'Huck', '1992.08.04')
# print(A)
# print(B)
# Database.DataBaseController.clean_tournament_database()

# Player_controller.PlayerController.option_choice()

# print(Player_model.Player.get_all_players())
# Tournament_controller.TournamentController.add_tournament_participant_list()
# Tournament_controller.TournamentController.option_choice()
# Tournament_controller.TournamentController.add_new_tournament()
# Tournament_model.Tournament.get_all_tournaments()

# print(Player_model.Player.deserialize(({'id': 1, 'first_name': 'faustine', 'last_name': 'Boudin', 'date_of_birth': '1984.12.06', 'gender': 'F', 'current_rank': 2200})))
# print(Database.DataBaseController.list_tournament())
# Database.DataBaseController.clean_tournament_database()

# print(Tournament_controller.TournamentController.sort_list_of_player_in_tournament_alphabetically(1))

# Tournament_controller.StartTournament.sort_players_second_tour(Tournament_model.Tournament.deserialize_tournament(Tournament_model.Tournament.get_tournament(1)).list_of_rounds)

# print(Tournament_controller.StartTournament.sort_players_first_tour(Tournament_model.Tournament.get_tournament(1)))

# print(Tournament_model.Tournament.deserialize_tournament(Tournament_model.Tournament.get_tournament(1)).list_of_rounds)

# tournament = Tournament_controller.StartTournament()
# tournament()


# round = Round_model.Round()
# finished_first_round = (round.run(Tournament_controller.StartTournament.sort_players_first_tour(Tournament_model.Tournament.get_tournament(1)), Tournament_model.Tournament.deserialize_tournament(Tournament_model.Tournament.get_tournament(1))))
# print(Round_model.Round.serialize(finished_first_round))

# second_round = Tournament_controller.StartTournament.sort_players_next_tours(finished_first_round)
# print(second_round)

tournament = Tournament_controller.StartTournament()
tournament()

# print(Tournament_model.Tournament.get_tournament(1))

# Database.DataBaseController.clean_round_database()
