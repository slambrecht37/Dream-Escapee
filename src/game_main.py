#main file for running the code

import game_player as pl

## Your end goal is to find the trophy room and pick up the trophy.
## Type help at any time for simple instructions and guidance.
## View the README file associated with this game for more in-depth info.

player = pl.Player()
player.intro()
while player.win == False:
    player.prompt()
    
