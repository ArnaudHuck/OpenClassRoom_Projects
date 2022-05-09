from Player_model import Player


class PlayerView:

    @staticmethod
    def display_options():
        list_options = ["Add New Player", "Alphabetical sorted list", "Ranking sorted list",
                        "Index sorted list", "Back Home", "Quit"]
        print(f"[N] : {list_options[0]}")
        print(f"[A] : {list_options[1]}")
        print(f"[R] : {list_options[2]}")
        print(f"[D] : {list_options[3]}")
        print(f"[B] : {list_options[4]}")
        print(f"[Q] : {list_options[5]}")

    @staticmethod
    def display_player_list(players: list[Player]):
        for player in players:
            print(player.serialize(), "\n")



