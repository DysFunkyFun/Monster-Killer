from gamestate import GameState
from cmdsmanager import CommandsManager
from commands import Commands
from util import Util
from cmdsmanager import EventsManager

class Game(object):

    def __init__(self, game_state: GameState, commands_manager: CommandsManager):
        self.game_state = game_state
        self.commands_manager = commands_manager
        self.events_manager = events_manager

    def step(self):
        
        # Ask the player for a command
        command: Commands = self.commands_manager.get_command()

        
        
        # Execute command
        self.commands_manager.exec_command(command)
        
        
        # Run chance for event, this is where we'll determine after the command what happens.
        
