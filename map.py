from typing import NoReturn


class Room:
    def __init__(self, room_id: str) -> NoReturn:
        self.room_id = room_id
        self.north = None
        self.east = None
        self.south = None
        self.west = None


class Map:
    def __init__(self) -> NoReturn:
        # Initialize rooms
        self.start = Room('start')
        self.a = Room('a')
        self.b = Room('b')
        self.c = Room('c')
        self.d = Room('d')
        self.e = Room('e')
        self.f = Room('f')
        self.g = Room('g')
        self.h = Room('h')
        self.i = Room('i')
        self.j = Room('j')
        self.end = Room('end')
        
        # Connect all rooms by direction
        self.connect_map()

    def connect_rooms(self, room, north = None, east = None, south = None, west = None):
        room.north = north
        room.east = east
        room.south = south
        room.west = west

    def connect_map(self):
        # Starting room
        self.connect_rooms(self.start, north = self.b, east = self. a)
        # Room A
        self.connect_rooms(self.a, north = self.c, east = self.d, west = self.start)
        # Room B
        self.connect_rooms(self.b, south = self.start, east = self.c)
        # Room C
        self.connect_rooms(self.c, west = self.b, south = self.a, north = self.e)
        # Room D
        self.connect_rooms(self.d, east = self.a)
        # Room E
        self.connect_rooms(self.e, south = self.c, east = self.j, north = self.f)
        # Room F
        self.connect_rooms(self.f, south = self.e, north = self.g, west = self.h)
        # Room G
        self.connect_rooms(self.g, south = self.f, east = self.end)
        # Room H
        self.connect_rooms(self.h, east = self.f, south = self.i)
        # Room I
        self.connect_rooms(self.i, north = self.h)
        # Room J
        self.connect_rooms(self.j, west = self.e)
        # Room end
        self.connect_rooms(self.end, west = self.g)

# Create a map object
my_map = Map()

# Set the current position of the player to the "start" room
current_position = my_map.start

# Map traversal loop
while current_position != my_map.end:
    # Get user direction
    direction = input('Wyd hoe?: N, E, S, W\n')

    # For each direction attempt to change the current position to the room in that direction, if no room exists then give simple message.
    if direction == 'N':
        if current_position.north is not None:
            current_position = current_position.north
            print(f'You are now in room {current_position.room_id}\n')
        else:
            print('You walk into a wall. idiot.\n')
            
    elif direction == 'E':
        if current_position.east is not None:
            current_position = current_position.east
            print(f'You are now in room {current_position.room_id}\n')
        else:
            print('You walk into a wall. idiot.\n')

    elif direction == 'S':
        if current_position.south is not None:
            current_position = current_position.south
            print(f'You are now in room {current_position.room_id}\n')
        else:
            print('You walk into a wall. idiot.\n')

    elif direction == 'W':
        if current_position.west is not None:
            current_position = current_position.west
            print(f'You are now in room {current_position.room_id}\n')
        else:
            print('You walk into a wall. idiot.\n')

# I can now make changes to your code without having to be in liveshare