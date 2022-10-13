class Player(object):

    def __init__(self, start_player_health: int) -> None:
        self.health = start_player_health
        self.kill_count = 0