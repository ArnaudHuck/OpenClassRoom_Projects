import Main_Controller
import Database

# Database.DataBaseController.clean_player_database()
# Database.DataBaseController.clean_tournament_in_progress_database()
# Database.DataBaseController.clean_tournament_database()


def main():
    controller = Main_Controller.MainController.home_menu
    controller()


if __name__ == "__main__":
    main()

