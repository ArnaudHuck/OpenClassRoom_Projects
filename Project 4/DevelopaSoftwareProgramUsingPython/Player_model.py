from Database import DataBaseController


class Player:

    def __init__(self, id=int, first_name="",
                 last_name="", date_of_birth="", gender="", tournament_score=0, current_rank=int()):

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.tournament_score = tournament_score
        self.current_rank = current_rank

    @staticmethod
    def add_player(first_name, last_name, date_of_birth, gender,  current_rank):
        id = DataBaseController.get_len_players_in_db() + 1
        tournament_score = 0

        new_player = Player(id, first_name, last_name,
                            date_of_birth, gender, tournament_score, current_rank)
        DataBaseController.add_player(new_player.serialize())
        return new_player

    @staticmethod
    def get_all_players() -> list['Player']:
        return [Player.deserialize(player) for player in DataBaseController.list_player()]

    @staticmethod
    def deserialize(serialized_player: dict) -> 'Player':
        id = serialized_player["id"]
        first_name = serialized_player["first_name"]
        last_name = serialized_player["last_name"]
        date_of_birth = serialized_player["date_of_birth"]
        gender = serialized_player['gender']
        tournament_score = serialized_player['tournament_score']
        current_rank = serialized_player["current_rank"]
        return Player(id,
                      first_name,
                      last_name,
                      date_of_birth,
                      gender,
                      tournament_score,
                      current_rank,
                      )

    def serialize(self) -> dict:
        player_data = {'id': self.id,
                       'first_name': self.first_name,
                       'last_name': self.last_name,
                       'date_of_birth': self.date_of_birth,
                       'gender': self.gender,
                       'tournament_score': self.tournament_score,
                       'current_rank': self.current_rank}
        return player_data

    @staticmethod
    def get_player(id):
        for player in DataBaseController.list_player():
            if player.__getitem__('id') == id:
                return player
        else:
            print('No match')
