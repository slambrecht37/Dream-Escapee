#puzzles for game, figured easier to write them here

import game_help as hp



def leverPuzzle():
    lights = [True, False, False, False, False]
    levers = [True, True, True]
    stage = 1
    win = False
    print(hp.leverPuzzle1)
    print(hp.leverPuzzle2)
    while win == False:
        
        print("\nLight status: ", end = '')
        for obj in lights:
            if obj == True:
                print('ON ', end = '')
            if obj == False:
                print('OFF ', end = '')
                
        print("\nLever status: ", end = '')
        for obj in levers:
            if obj == True:
                print('UP ', end = '')
            if obj == False:
                print('DOWN ', end = '')

        cmd = input('\nWhich lever would you like to move/pull?: ')

        if cmd == 'help':
            print(hp.leverPuzzleHelp)

        elif cmd == 'leave':
            print('You decide to leave the lever machine')
            return False

        else:
            
            try:
                cmd = int(cmd)
            except ValueError:
                cmd = -1

            if 1 <= cmd <= 3:
                levers[cmd - 1] = not(levers[cmd - 1])
            else:
                print('invalid input, please enter a number corresponding to a lever (1, 2, 3)')

            if levers == [False, True, True] and stage == 1: #first stage
                print(hp.leverPuzzle3)
                stage = 2
                lights = [ True, True, False, False, False]
            elif levers == [False, False, True] and stage == 2: #second stage
                print(hp.leverPuzzle3)
                stage = 3
                lights = [ True, True, True, False, False]
            elif levers == [False, False, False] and stage == 3: #third stage
                print(hp.leverPuzzle3)
                stage = 4
                lights = [ True, True, True, True, False]
            elif levers == [True, False, False] and stage == 4: #fourth stage
                stage = 5
                lights = [ True, True, True, True, True]
            else:
                print(hp.leverPuzzle4)
                stage = 1
                levers = [True, True, True]
                lights = [ True, False, False, False, False]

            if lights == [True, True, True, True, True] and stage == 5:
                win = True
                print(hp.leverPuzzle5)
                return True

def numberPuzzle():
    key = hp.numberPuzzleKey
    win = False
    print(hp.numberPuzzleIntro)
    while win == False:

        cmd = input('\nWhat number will you spin the dials to?: ')

        if cmd == 'help':
            print(hp.numberPuzzleHelp)
        elif cmd == 'leave':
            print('You decide to leave the machine.')
            return win
        else:
            try:
                cmd = int(cmd)
            except ValueError:
                cmd = -1
            if  -1 < cmd < 1000:
                if cmd == key:
                    print(hp.numberPuzzleWin)
                    win = True
                    return win
                else:
                    print(hp.numberPuzzleLose)
            else:
                print('Invalid number entry. Enter a number from 000 to 999')



        
