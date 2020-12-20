#puzzles for game, figured easier to write them here

import game_help as hp



def leverPuzzle():
    lights = [True, False, False, False, False]
    levers = [True, True, True]
    stage = 1
    win = False
    winFirstTime = True
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
                winFirstTime = False

            if lights == [True, True, True, True, True] and stage == 5:
                win = True
                print(hp.leverPuzzle5)
                if winFirstTime == True:
                    return 7
                else: return True

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

class GemstonePuzzle():
    def __init__(self):
        self.win = False
        self.slotsStatus = [False, False, False]
        self.slots = [None, None, None]
        self.slotNames = ['first', 'second', 'third']
        self.slotTargets = ['emerald', 'sapphire', 'ruby']
        self.slotID = 0
        
    def interact(self, backpackNames):
        names = backpackNames
        print(hp.gemstonePuzzleIntro)

        while self.win == False:
            if self.slotsStatus[self.slotID] == False:
                print('\nSlot',self.slotID + 1,'status: Empty')
            else: print('\nSlot',self.slotID + 1,'status:',self.slots[self.slotID])
            
            cmd = input('What will you try to put into the {0} hole?: '.format(self.slotNames[self.slotID]))
            if cmd == 'next':
                self.slotID += 1
                if self.slotID >= 3:
                    self.slotID -= 3
            elif cmd == 'leave':
                print('You decide to step away from the machine')
                return self.slotsStatus
            elif cmd == 'backpack':
                for obj in names:
                    print(obj)
            elif cmd == 'help':
                print(hp.gemstonePuzzleHelp)
            else:
                try:
                    i = names.index(cmd)
                except ValueError:
                    i = -1

                if i > -1:
                    item = names[i]

                    if self.slotsStatus[self.slotID] == False: #current slot is empty
                        if item == self.slotTargets[self.slotID]:
                            print('The',cmd,'fits into the slot')
                            self.slots[self.slotID] = item
                            self.slotsStatus[self.slotID] = True
                            self.slotID += 1
                            if self.slotID >= 3:
                                self.slotID -= 3
                            names.remove(item)
                        else:
                            print('The',cmd,'doesnt fit into that slot')
                    else:
                        print('The slot already has been filled')
                else:
                    print('There is no',cmd,'to put into the slot')
            if self.slotsStatus == [True, True, True]:
                self.win = True
                print(hp.gemstonePuzzleWin)
                return self.slotsStatus

#myList = ['emerald', 'sapphire', 'ruby', 'shoe', 'rock', 'stick']
shapemachine = GemstonePuzzle()
#g.interact(myList)

        
