from commands import Commands
from events import Events
from util import Util
from gamestate import GameState

class CommandsManager(object):
    
    def __init__(self, game_state: GameState) -> None:
        self.game_state = game_state
        self.commands = {
            1: Commands.MOVE,
            2: Commands.ATTACK,
            3: Commands.FLEE,
            4: Commands.SHOW
        }
        self.command_map = {
            Commands.MOVE: self.move,
            Commands.ATTACK: self.attack,
            Commands.FLEE: self.flee,
            Commands.SHOW: self.show_commands
        }

    def get_command(self) -> Commands:
        idx = Util.ask_query('What\'s your next move? (Type \'4\' for options.)', [str(c) for c in self.commands.keys()])
        return self.commands[idx + 1]
        
    def exec_command(self, command: Commands) -> None:
        command_func = self.command_map[command]
        command_func()

    def get_event(self, event: Events) -> str:
        ...

    def move(self):
        print('MOVE')

    def attack(self):
        print('ATTACK')
        
    def flee(self):
        print('FLEE')

    def show_commands(self):
        print('''

*----------------*
|    COMMANDS    |
*----------------*
|                |          
|   1: Move      |
|   2: Attack    |
|   3: Flee      |
|                |
*----------------*
        
        ''')