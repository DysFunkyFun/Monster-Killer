from player import Player

# Store current game state
# Contains all game variables
class GameState(object):

    def __init__(self) -> None:

        # values for the progression of the game
        self.start_player_health = 100
        self.monster_kill_count = 0
        self.kill_count_goal = 5

        self.player = Player(self.start_player_health)

    def is_game_over(self) -> bool:
        if self.player.health <= 0 or self.player.kill_count >= self.kill_count_goal:
            return True
        return False