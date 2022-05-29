from Player_controller import PlayerController


class MainController:

    def __init__(self):

        self.player_controller = PlayerController(self)

    def get_unserial_list_players(self):
        return self.player_controller.get_unserial_list_of_player()

    def get_unserial_players_participants(self, players_participants_in_db):
        return self.player_controller \
            .get_unserial_players_participants(players_participants_in_db)
