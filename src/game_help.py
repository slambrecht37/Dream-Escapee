#help and desc strings so as not to clutter other files

playerPromptHelp = '''Your goal is to find the trophy room and pick up the trophy.
Valid commands:
\ngo <north, etc> or up/down (depending on location) : move around map
\nexplore : give description of current room, including objects of interest. Use command 'explore auto' to enable automatic exploring whenever you enter a room.
\nexamine <item> : examine an item in the room or in your backpack
\ntake <item> : pick up an item from the room and put it in your backpack'
\ninteract <item> <item(optional)> : interact with/use up to 2 items that
are in the room or in your backpack
\nbackpack : print the contents of your backpack
\nhelp : prints available commands at any time
Review the README.txt file associated with the game for more in-depth help'''

intro = '''Welcome to Dream Escapee!
If you have any questions about what to do or how things work, type 'help' at any time.
You can also look through the README file associated with the game.
Your main goal is to find the trophy room. Once inside, picking up the trophy will win the game.
Enjoy!'''

storyIntro = ''' '''

win = '''\nYou pick up the mysterious trophy and marvel at its beauty. Suddenly, the trophy glows an incredible and intense golden color. \
Startled, you drop the trophy, and it clangs across the floor. It continues to glow, and continues to get brighter. You shield your eyes, but it barely helps. Just \
as the light becomes unbearable bright, everything goes dark.

Am I dead? Did I die? Confused, you slowly open your eyes. Everything seems fine, amazingly, except you are . . . \
somewhere else. You sit up in a panic, only to realize that your are lying in your bed. It was all a dream. Relieved, you roll over to go back to sleep, but something \
catches your eye across the room. The sun was reflecting bizarrely off of something near the end of your bed. You rub your eyes to get a better look, but what you see \
alarms you. There, sitting neatly on your desk, was that mysterious trophy.'''

roomDesc = []

room0Desc = 'filler room to fill array'
room1Desc = '''A large empty room. There are some doors/doorways connected to it.
To the north is a doorway to another room. To the south is a large metal door.'''
room2Desc = '''A mostly empty room. In one corner is a large machine with 3 levers coming out of it.
To the north there is a doorway to another room, and to the south is a doorway to another room.'''
room3Desc = '''A small room with a door in the ceiling to the attic. On one wall is a strange machine \
with 3 spinnable dials, each able to show digits 0-9
To the east is a doorway to another room. There is a closed door in the ceiling that goes up to the attic.'''
room4Desc = '''An office room. There is a wooden desk in the center, surrounded by a chair, filing cabinets, and the like.
To each of the north, east, south, and west there is a doorway leading to another room.'''
room5Desc = '''A storage room. There are random items and piles of junk all over the place.
To the north and to the west are doorways to other rooms.'''
room6Desc = '''A cramped attic. There is a wooden chest on one side with a keyhole in the front.
There is a door in the floor down to another room.'''
room7Desc = '''A bizarre room. The walls, floor, and ceiling are made of marble. Against one wall are three stone pedestals, \
two of which have a small metal statue of an angel. Maybe its missing a third statue?
There are doorways to other rooms to the south and east.'''
room8Desc = '''The boiler room. There is an industrial-looking furnace on one side. A few other items are strewn around the room.
There are doorways to other rooms to the south and west.'''
room9Desc = '''An empty room. There are 3 doors: a bronze one, a silver one, and a gold one. All have a slot for a key.
To the east is a large bronze-colored door, to the west is a large silver-colored door, and to the south is a large gold-colored door. \
To the north is a large metal door.'''
room10Desc = '''Another empty room. In the center of the room is an altar of sorts, with a golden trophy sitting on top.
To the north is a gold-colored door to another room.'''

roomDesc.append(room0Desc)
roomDesc.append(room1Desc)
roomDesc.append(room2Desc)
roomDesc.append(room3Desc)
roomDesc.append(room4Desc)
roomDesc.append(room5Desc)
roomDesc.append(room6Desc)
roomDesc.append(room7Desc)
roomDesc.append(room8Desc)
roomDesc.append(room9Desc)
roomDesc.append(room10Desc)

leverPuzzleDesc = '''levermachine: An unusual machine. Three levers stick out of the front, and a row of 5 lights runs across the top \
There doesn't seem to be any cables running into it for power, and there doesn't seem to be any way into the machine. On the front is a small coin slot.'''
leverPuzzleHelp = '''Enter a number from 1 to 3 to select a lever to move. Type 'leave' to step away from the machine.'''
leverPuzzle1 = '''\nYou approach the strange lever machine. All 3 levers are in the 'up' position, and each is able to be moved into \
the down position. There is also a series of 5 lights on the front face of the machine, all of which are off.'''
leverPuzzle2 = '''You push the coin into the coin slot on the front of the machine. The sound of grinding gears comes from inside \
the machine. The first light in the series of 5 turns on.
Enter help at anytime to see options.'''
leverPuzzle3 = '''You pull the lever. Mechanical sounds come from inside of the machine. The next light turns on.'''
leverPuzzle4 = '''You pull the lever. Suddenly, all levers return to the 'up' state and all lights turn off. After a few seconds, \
the first light on the machine turns back on. Looks like you have to try again'''
leverPuzzle5 = '''You pull the lever. The last light turns on, and the usual whirring of gears is accompanied by a shrill scraping noise \
as a small drawer opens up, revealing a heavy steel key. You take the key and put it into your backpack.'''

numberPuzzleKey = 789
numberPuzzleDesc = '''numbermachine: A large boxy machine. There are 3 dials on the front, each able to show a number from 0 to 9. There are not any \
other obvious features of the machine.'''
numberPuzzleHelp = '''Enter a number from 0 to 999 into the machine. Type 'leave' to step away from the machine'''
numberPuzzleIntro = '''You approach the number machine. There is no hole for a key, so spinning the number dials to the right sequence must do something.
Enter help at anytime to see options.'''
numberPuzzleLose = 'Nothing happened. Must have been the wrong number.'
numberPuzzleWin = 'After entering the number, the machine whirs. Suddenly, a small compartment opens up, holding a bronze-colored key. \
You take the key and put it in your backpack'

#print('game_help compiles')
