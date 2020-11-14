#room information

import game_items as it

class Room:
    def __init__(self, roomId, north, east, south, west, up = None, down = None, \
                 nDoor = None, eDoor = None, sDoor = None, wDoor = None, \
                 uDoor = None, dDoor = None):
        self.roomId = roomId
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up if up is not None else 0
        self.down = down if down is not None else 0
        self.nDoor = nDoor if nDoor is not None else it.nonedoor
        self.eDoor = eDoor if eDoor is not None else it.nonedoor
        self.sDoor = sDoor if sDoor is not None else it.nonedoor
        self.wDoor = wDoor if wDoor is not None else it.nonedoor
        self.uDoor = uDoor if uDoor is not None else it.nonedoor
        self.dDoor = dDoor if dDoor is not None else it.nonedoor

room = []

room0 = Room(0, -1, -1, -1, -1)
room1 = Room(1, 2, 0, 9, 0, sDoor = it.largedoor)
room2 = Room(2, 4, 0, 1, 0)
room3 = Room(3, 0, 4, 0, 0, up = 6, uDoor = it.atticdoor)
room4 = Room(4, 7, 5, 2, 3)
room5 = Room(5, 8, 0, 0, 4)
room6 = Room(6, 0, 0, 0, 0, down = 3)
room7 = Room(7, 0, 8, 4, 0)
room8 = Room(8, 0, 0, 5, 7)
room9 = Room(9, 1, 0, 10, 0, sDoor = it.golddoor)
room10 = Room(10, 9, 0, 0, 0)

room.append(room0)
room.append(room1)
room.append(room2)
room.append(room3)
room.append(room4)
room.append(room5)
room.append(room6)
room.append(room7)
room.append(room8)
room.append(room9)
room.append(room10)

print("game_rooms compiles")

