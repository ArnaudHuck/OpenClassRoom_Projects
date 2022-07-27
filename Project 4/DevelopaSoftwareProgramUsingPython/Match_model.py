from Player_model import Player


class Match:

    MATCH_NUMBER = 1

    def __init__(self, name: str, player_1: Player, player_2: Player, score_player_1: float, score_player_2: float):
        self.name = "Match " + str(Match.MATCH_NUMBER)
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def __repr__(self):
        return f"{self.player_1} --VS-- {self.player_2}"

    def serialize(self) -> dict:
        """
        :return: Returns a dict containing all match keu, value information
        """
        return {"name": self.name,
                "player_1": Player.serialize(self.player_1),
                "player_2": Player.serialize(self.player_2),
                "score_player_1": self.score_player_1,
                "score_player_2": self.score_player_2}

    @staticmethod
    def deserialize(serialized_match) -> 'Match':
        """
        :param serialized_match: Takes a dict containing all match key, value information
        :return: Returns a round object
        """
        name = serialized_match["name"]
        player_1 = Player.deserialize(serialized_match["player_1"])
        player_2 = Player.deserialize(serialized_match["player_2"])
        score_player_1 = serialized_match["score_player_1"]
        score_player_2 = serialized_match["score_player_2"]
        return Match(name,
                     player_1,
                     player_2,
                     score_player_1,
                     score_player_2)
