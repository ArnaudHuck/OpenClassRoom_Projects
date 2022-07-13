import Database
import Player_model
import Player_view
import Player_controller
import Tournament_controller
import Tournament_model
import Round_model
import Match_model
import Main_Controller

# ('Faustine', 'Boudin', '1984.12.06', 'F', 2200)
# ('Henry', 'Huck', '1992.08.04', 'M', 2500)
# ('Alice', 'Charles', '1994.12.07', 'F', 2900)
# ('Gregoris', 'Lassale', '1978.11.18', 'H', 1800)
# ('Philippe', 'Pitou', '1997.10.05', 'H', 1600)
# ('Sabine', 'Foo', '1990.05.12', 'F', 2100)
# ('Benoit', 'Benithon', '1993.08.10', 'H', 2600)
# ('Olivier', 'Dubois', '1979.03.06', 'H', 1900)

# Database.DataBaseController.clean_tournament_database()
# Database.DataBaseController.clean_player_database()
# Database.DataBaseController.clean_round_database()
# Database.DataBaseController.clean_tournament_in_progress_database()
# Database.DataBaseController.clean_tournament_database()

# Player_controller.PlayerController.option_choice()
# Tournament_controller.TournamentController.option_choice()
# tournament = Tournament_controller.StartTournament()
# tournament()

# print(Tournament_model.Tournament.get_all_tournaments_unfinished_or_ended())


Main_Controller.MainController.home_menu()

# chosen_tournament = Tournament_model.Tournament.get_unfinished_tournament(1)
# Tournament_controller.StartTournament.sort_players_next_tours(chosen_tournament)
