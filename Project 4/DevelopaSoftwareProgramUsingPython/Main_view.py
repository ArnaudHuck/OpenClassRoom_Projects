
class MainView:

    @staticmethod
    def home_menu_view():
        """
        :return: Displays the home menu
        """
        list_options = ["Player_menu", "Tournament_menu", "Quit"]
        print(f"[P]: {list_options[0]}")
        print(f"[T]: {list_options[1]}")
        print(f"[Q]: {list_options[2]}")
