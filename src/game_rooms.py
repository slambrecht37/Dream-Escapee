#room information

import game_items as it
import game_battle as bt

class Room:
    def __init__(self, roomId, north, east, south, west, up = None, down = None, \
                 nDoor = None, eDoor = None, sDoor = None, wDoor = None, \
                 uDoor = None, dDoor = None, items = None, enemy = None):
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
        self.items = items if items is not None else []
        self.enemy = enemy if enemy is not None else None

room = []

room1Items = [it.largedoor]
room2Items = [it.levermachine]
room3Items = [it.atticdoor, it.numbermachine]
room4Items = [it.book, it.desk, it.matches]
room5Items = [it.firewood, it.ladder, it.silverkey, it.scrapmetal]
room6Items = [it.atticdoor, it.chest]
room7Items = [it.pedestal]
room8Items = [it.crucible, it.furnace, it.oldkey, it.smeltingmold]
room9Items = [it.weaponcase, it.bronzedoor, it.golddoor, it.largedoor, it.silverdoor]
room10Items = [it.ruby]
room11Items = [it.emerald]
room12Items = [it.sapphire]
room13Items = [it.shapemachine]

room0 = Room(0, -1, -1, -1, -1)
room1 = Room(1, 2, 0, 9, 0, sDoor = it.largedoor, items = room1Items)
room2 = Room(2, 4, 0, 1, 0, items = room2Items)
room3 = Room(3, 0, 4, 0, 0, up = 6, uDoor = it.atticdoor, items = room3Items)
room4 = Room(4, 7, 5, 2, 3, items = room4Items)
room5 = Room(5, 8, 0, 0, 4, items = room5Items)
room6 = Room(6, 0, 0, 0, 0, down = 3, dDoor = it.atticdoor, items = room6Items)
room7 = Room(7, 0, 8, 4, 0, items = room7Items)
room8 = Room(8, 0, 0, 5, 7, items = room8Items)
room9 = Room(9, 1, 12, 10, 11, eDoor = it.bronzedoor, sDoor = it.golddoor, wDoor = it.silverdoor, items = room9Items)
room10 = Room(10, 9, 0, 13, 0, items = room10Items, enemy = bt.troll)
room11 = Room(11, 0, 9, 0, 0, items = room11Items, enemy = bt.skeleton)
room12 = Room(12, 0, 0, 0, 9, items = room12Items, enemy = bt.goblin)
room13 = Room(13, 10, 0, 0, 0, items = room13Items)

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
room.append(room11)
room.append(room12)
room.append(room13)

#print("game_rooms compiles")

