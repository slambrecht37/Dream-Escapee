
# Dream Escapee

This game was created by myself (Sam Lambrecht) as a personal project. This is a text-based, escape-style game, and you win once you find the trophy room and take the trophy from its stand.


# Technical Aspects of DE and How to Run DE

This game was coded using Python 3.8.6 (which was the most recent release when development started). In order to run the game, you must download/install Python version 3.8.6 or newer from <https://www.python.org/downloads/>. 
To play this game, make sure that all files of the name game_xxxx.py are in the same folder. Once an adequate version of Python is installed, open IDLE (should be named IDLE (Python 3.x.x 32/64-bit). From the top bar select File>Open and open game_main.py. From game_main.py go to the top bar and select Run>Run Module. This will start the game with the prompt 'What will you do?' followed by a '>' symbol, and it will wait for you to enter a command. Alternatively, the game can be run by navigating to the folder containing the game files and double-clicking game_main.py.


# Command How-to

When entering commands, keep all entries in lowercase. For any command that takes arguments, the command name and the argument(s) should be seperate by a space. For any arguments that are items, be sure to type the item's name EXACTLY as it appears in the world. For instance, if you explore a room and find and object called smallkey and want to examine it, use >examine smallkey instead of >examine small key.


# Controls/Commands

The game allows for 6 different commands to move around and interact with the world:

go <arg>:
The 'go' command is used to move around the world. Valid arguments for this command are north, south, east, and west, as well as up and down. You will not always be able to travel in all directions, and you will be notified if you are able to travel in your specified direction.
Example usage: 
>go north
You head north and find yourself in another room
	
explore:
The 'explore' command is used to explore your current location. It will return a description of where you are, including information about objects in the room as well as which directions lead to other rooms. The explore command can also be used to automatically explore a room when entering it be entering 'explore auto'.
Example usage:
>explore
A small room with several pieces of furniture.
There are doorways to the south and east that lead to other rooms. There is a wooden door to the west.
Objects: sofa, chair, table, desk, shelf, book, woodendoor
Another example:
>explore auto
explore auto enabled ->When enabled, this will automatically explore a room when entering so the user doesn't have to repeatedly use explore
	
examine <arg>:
The 'examine' command is used to examine a particular item in your backpack or in the current room. It will return a description of the item. Valid arguments to this function are the names of items as they appear in the world.
Example usage:
>examine chair
chair: A simple wooden chair of sturdy construction.

take <arg>:
The 'take' command is used to take a particular item in the current room and place it in your backpack. Not every item is able to be placed in the backpack. Valid arguments to this function are the names of items as they appear in the world.
Example usage:
>take book
You place the book in your backpack.
	
backpack:
The 'backpack' command is used to print the contents of your backpack.
Example usage:
>backpack
Current backpack contents:
book
jacket
pencil
smallkey
bucket

interact <arg> (<arg>):
The 'interact' command is the most important one in the game. It is used to interact with up to 2 objects. Each object must be in the current room or in your backpack in order to interact with it. Valid arguments to this function are the names of items as they appear in the world. Keep in mind: not every item can be interacted with by itself. Most objects (doors, things with keys, etc.) only require 'interact <object>' to work, and you will be prompted for a key/item to use the object. Other objects require the command of the form 'interact <object> <object>' to do something.
Example usage:
>interact bucket sink
You use the sink the fill the bucket up with water
>interact desk
The desk is unlocked. You place the following item(s) in your bag:
pencilcase








 
###### HINTS BELOW #####









##### FINAL WARNING #####





heavykey: 
Use ladder to get up to atticdoor, use oldkey with chest in attic to get coin, use coin with levermachine to receive heavykey
interact ladder atticdoor, interact chest (then enter oldkey when prompted), interact levermachine (enter coin when prompted)

bronzekey:
Read note in desk for dial number, use that number on numbermachine to receive bronzekey
interact desk, interact numbermachine

silverkey:
Find in room 5
take silverkey

goldkey:
put firewood inside furnace, then use matches to light furnace. Put the scrapmetal into the crucible then place the crucible into the furnace. Take the crucible out and pour the molten metal into the smeltingmold. Then remove the cast statue from the smelting mold. Use the statue to open the pedestal. Receive the goldkey.
interact furnace firewood, interact furnace matches, interact crucible scrapmetal, interact crucible furnace, interact crucible smeltingmold, interact smeltingmold, interact pedestal (enter statue when prompted)

Use heavykey to unlock large door. Use bronze/silver/goldkey to unlock bronze/silver/golddoor. Take each gem behind each door. This will trigger a different battle each time. Win each battle to successfully place the gems in your backpack. Go south through the room with the golddoor to the room with the shapemachine. Place gems in this order: emerald, sapphire, ruby. Take trophy to win.
