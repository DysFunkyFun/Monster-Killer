from game import Game
from gamestate import GameState
from cmdsmanager import CommandsManager

class Main(object):

    @staticmethod
    def run():

        # Initialize game variables
        game_state = GameState()
        commands_manager = CommandsManager(game_state)

        # Start main game loop
        game = Game(game_state, commands_manager)
        while not game_state.is_game_over():
            game.step()
        

Main.run()