from commands import Commands
from events import Events
from util import Util
from gamestate import GameState
from mapping import Map
from mapping import Room
import random

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


class EventsManager(object):

    def __init__(self, game_state: GameState) -> None:
        self.game_state = game_state
        self.events = {
            1: Events.ENCOUNTER,
            2: Events.WEAPON,
            3: Events.ITEM
        }
        self.events_map = {
            Events.ENCOUNTER: self.encounter,
            Events.WEAPON: self.weapon,
            Events.ITEM: self.item
        }
    
    
    def get_command(self) -> Commands:
        idx = Util.ask_query('What\'s your next move? (Type \'4\' for options.)', [str(c) for c in self.commands.keys()])
        return self.commands[idx + 1]
        
    
    
    def exec_command(self, command: Commands) -> None:
        command_func = self.command_map[command]
        command_func()

    
    def choose_event(self) -> int:
       evt_choice = random.choice(list(Events))
       return evt_choice
    
    
    def encounter(self):
        print('Encounter!')
    
    def weapon(self):
        print('Weapon!')
   
    def item(self):
        print('Item!')
    
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