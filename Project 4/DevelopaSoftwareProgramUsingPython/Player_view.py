from Player_model import Player


class PlayerView:

    @staticmethod
    def display_options():
        """
        :return: Displays the PLayer Menu
        """
        list_options = ["Add New Player", "Alphabetical sorted list", "Ranking sorted list",
                        "Index sorted list", "Modify player rank", "Home menu", "Quit"]
        print(f"[A] : {list_options[0]}")
        print(f"[B] : {list_options[1]}")
        print(f"[C] : {list_options[2]}")
        print(f"[D] : {list_options[3]}")
        print(f"[E] : {list_options[4]}")
        print(f"[H] : {list_options[5]}")
        print(f"[Q] : {list_options[6]}")

    @staticmethod
    def display_player_list(players: list[Player]):
        """
        :param players: Takes a Player list
        :return: Displays main info for each player in the list
        """
        for player in players:
            print(player.serialize(), "\n")
