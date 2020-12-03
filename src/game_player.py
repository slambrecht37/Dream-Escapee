#player information

import game_items as it
import game_rooms as rm
import game_help as hp
import game_puzzle as pz

class Player:
    def __init__(self):
        self.backpack = it.Backpack()
        self.location = 1
        self.win = False
        self.numberMachineComplete = False
        self.leverMachineComplete = False
        self.cmd = ''
        self.exploreAuto = False

    def intro(self):
        print(hp.intro)
        print(hp.playerPromptHelp)

    def prompt(self):
        userInput = input("\nWhat will you do? \n> ")
        self.cmd = userInput.split()

        if len(self.cmd) > 0:
            if self.cmd[0] == 'go':
                if len(self.cmd) == 2: self.move()
                else: print("Invalid number of arguments. 'go' supports 1 argument.")
            elif self.cmd[0] == 'explore':
                if len(self.cmd) == 1 or len(self.cmd) == 2: self.explore()
                else: print("Invalid number of arguments. 'explore' supports 0 or 1 argument(s).")
            elif self.cmd[0] == 'examine':
                if len(self.cmd) == 2: self.examine()
                else: print("Invalid number of arguments. 'examine' supports 1 argument.")
            elif self.cmd[0] == 'take':
                if len(self.cmd) == 2: self.take()
                else: print("Invalid number of arguments. 'take' supports 1 argument.")
            elif self.cmd[0] == 'interact':
                if len(self.cmd) == 2 or len(self.cmd) == 3: self.interact()
                else: print("Invalid number of arguments. 'interact' supports 1 or 2 arguments.")
            elif self.cmd[0] == 'backpack':
                self.showBackpack()
            elif self.cmd[0] == 'help':
                print(hp.playerPromptHelp)
            else:
                print('Invalid command entered. Type help at any time to see available commands')

    def move(self):
        #print('move command selected')
        if self.cmd[1] == 'north':
            if rm.room[self.location].north > 0:
                if rm.room[self.location].nDoor == it.nonedoor:
                    self.location = rm.room[self.location].north
                    #print('Now in room',self.location)
                    print('You go into the room to the north')
                    if self.exploreAuto: self.explore()
                elif rm.room[self.location].nDoor.locked == False:
                    self.location = rm.room[self.location].north
                    #print('The door is unlocked. You go north to room',self.location)
                    print('The door is unlocked. You go north into the next room')
                    if self.exploreAuto: self.explore()
                else:
                    print('''There is a locked door preventing you from going north. Find \
the appropriate key to unlock it''')  
            else:
                print('Cannot go north')
                
        elif self.cmd[1] == 'east':
            if rm.room[self.location].east > 0:
                if rm.room[self.location].eDoor == it.nonedoor:
                    self.location = rm.room[self.location].east
                    #print('Now in room',self.location)
                    print('You go into the room to the east')
                    if self.exploreAuto: self.explore()
                elif rm.room[self.location].eDoor.locked == False:
                    self.location = rm.room[self.location].east
                    #print('The door is unlocked. You go east to room',self.location)
                    print('The door is unlocked. You go east into the next room')
                    if self.exploreAuto: self.explore()
                else:
                    print('''There is a locked door preventing you from going east. Find \
the appropriate key to unlock it''')
            else:
                print('Cannot go east')
                
        elif self.cmd[1] == 'south':
            if rm.room[self.location].south > 0:
                if rm.room[self.location].sDoor == it.nonedoor:
                    self.location = rm.room[self.location].south
                    #print('Now in room',self.location)
                    print('You go into the room to the south')
                    if self.exploreAuto: self.explore()
                elif rm.room[self.location].sDoor.locked == False:
                    self.location = rm.room[self.location].south
                    #print('The door is unlocked. You go south to room',self.location)
                    print('The door is unlocked. You go south into the next room')
                    if self.exploreAuto: self.explore()
                else:
                    print('''There is a locked door preventing you from going south. Find \
the appropriate key to unlock it''')
            else:
                print('Cannot go south')
                
        elif self.cmd[1] == 'west':
            if rm.room[self.location].west > 0:
                if rm.room[self.location].wDoor == it.nonedoor:
                    self.location = rm.room[self.location].west
                    #print('Now in room',self.location)
                    print('You go into the room to the west')
                    if self.exploreAuto: self.explore()
                elif rm.room[self.location].wDoor.locked == False:
                    self.location = rm.room[self.location].west
                    #print('The door is unlocked. You go west to room',self.location)
                    print('The door is unlocked. You go west into the next room')
                    if self.exploreAuto: self.explore()
                else:
                    print('''There is a locked door preventing you from going west. Find \
the appropriate key to unlock it''')
            else:
                print('Cannot go west')
                
        elif self.cmd[1] == 'up':
            if rm.room[self.location].up > 0:
                if rm.room[self.location].uDoor == it.nonedoor:
                    self.location = rm.room[self.location].up
                    #print('Now in room',self.location)
                    print('You go into the room above')
                    if self.exploreAuto: self.explore()
                elif rm.room[self.location].uDoor == it.atticdoor:
                    if it.atticdoor.locked == True:
                        print('The atticdoor is too high to reach.')
                    else:
                        self.location = rm.room[self.location].up
                        print('You use the ladder to reach the atticdoor. You go up into the room above')
                        if self.exploreAuto: self.explore()
                elif rm.room[self.location].uDoor.locked == False:
                    self.location = rm.room[self.location].up
                    #print('The door is unlocked. You go up to room',self.location)
                    print('The door is unlocked. You go up into the room above')
                    if self.exploreAuto: self.explore()
                else:
                    print('''There is a locked door preventing you from going up. Find \
the appropriate key to unlock it''')
            else:
                print('Cannot go up')
                
        elif self.cmd[1] == 'down':
            if rm.room[self.location].down > 0:
                if rm.room[self.location].dDoor == it.nonedoor:
                    self.location = rm.room[self.location].down
                    #print('Now in room',self.location)
                    print('You go into the room below')
                    if self.exploreAuto: self.explore()
                elif rm.room[self.location].dDoor == it.atticdoor:
                    self.location = rm.room[self.location].down
                    print('You climb down the ladder into the room below.')
                    if self.exploreAuto: self.explore()
                elif rm.room[self.location].dDoor.locked == False:
                    self.location = rm.room[self.location].down
                    #print('The door is unlocked. You go below to room',self.location)
                    print('The door is unlocked. You go down into the room below')
                    if self.exploreAuto: self.explore()
                else:
                    print('''There is a locked door preventing you from going down. Find \
the appropriate key to unlock it''')
            else:
                print('Cannot go down')
        else:
            print('Invalid direction')

    def explore(self):
        #print('explore command selected')
        if len(self.cmd) == 1:
            print(hp.roomDesc[self.location])
            if not(rm.room[self.location].items == []):
                print('Objects in room: ')
                for obj in rm.room[self.location].items:
                    print(obj.name)
        elif len(self.cmd) == 2:
            if self.cmd[1] == 'auto':
                self.exploreAuto = not(self.exploreAuto)
                if self.exploreAuto: print('explore auto enabled')
                else: print('explore auto disabled')
            elif self.cmd[1] == 'north' or self.cmd[1] == 'east' or self.cmd[1] == 'south' or self.cmd[1] == 'west'or self.cmd[1] == 'up' or self.cmd[1] == 'down':
                print(hp.roomDesc[self.location])
                if not(rm.room[self.location].items == []):
                    print('Objects in room: ')
                    for obj in rm.room[self.location].items:
                        print(obj.name)
            else:
                print('Invalid argument')

    def examine(self):
        obj = self.cmd[1]
        #print('examine command selected')
        found = False

        if obj == 'levermachine':
            found = True
            print(hp.leverPuzzleDesc)
        elif obj == 'numbermachine':
            found = True
            print(hp.numberPuzzleDesc)
            
        if len(self.backpack.contents) > 0:
            #print("checking backpack")
            try:
                i = self.backpack.contentsNames.index(obj)
            except ValueError:
                i = -1
                #print(obj,"not in backpack")
            if i > -1:
                #print(obj,"in backpack")
                found = True
                print(self.backpack.contents[i].desc)
        if found == False:
            #print("checking room")
            try:
                i = it.itemNames.index(obj)
            except ValueError:
                i = -1
                #print(obj,"not in any room")
            if i > -1:
                #print(obj,"is in a room")
                if it.items[i].isHidden == False:
                    if it.items[i].location == self.location:
                        #print(obj,"is in current room")
                        found = True
                        print(it.items[i].desc)
                    if it.items[i] == it.golddoor or it.items[i] == it.atticdoor or it.items[i] == it.largedoor:
                        if self.location == it.items[i].behind:
                            found = True
                            print(it.items[i].desc)
                    
        if found == False:
            print("There is no",obj,"to examine")
            

    def take(self):
        obj = self.cmd[1]
        #print('take command selected')
        
        if obj == 'numbermachine' or obj == 'levermachine':
            print(obj,'cannot be picked up')

        try:
            i = it.itemNames.index(obj)
        except ValueError:
            i = -1

        if i > -1:
            
            #print(obj,"exists somewhere")
            if not(self.inBackpack(obj)):
            #print(obj,'is not in backpack already')
                if it.items[i].isHidden == False:
                    if it.items[i].canPickUp == True:                
                        if it.items[i].location == self.location:
                            print(obj,"placed in backpack")
                            self.backpack.contentsNames.append(it.items[i].name)
                            self.backpack.contents.append(it.items[i])
                            rm.room[self.location].items.remove(it.items[i])
                            if it.items[i].name == 'trophy':
                                self.win = True
                                print(hp.win)
                                f = input('\nCongrats on finishing the game! Press ENTER to close out of the window.')
                        else:
                            print("There is no",obj,"to pick up")
                    else:
                        print(obj,'can not be picked up') 
                else:
                    print("There is no",obj,"to pick up")
            else:
                print(obj,'already in backpack')
        else:
            print("There is no",obj,"to pick up")
                
    def interact(self):
        #print('interact command selected')
        if len(self.cmd) == 2:
            #print('interact 1')

            if self.cmd[1] == 'levermachine':
                #print('lever puzzle')
                if self.location == 2:
                    if self.leverMachineComplete == False:                        
                        inp = input('The machine is off, but there seems to be a coin slot on the side. Maybe its creator took inspiration from \
game machines. An arcade coin or something similar would probably work. What item will you try to use with the machine?: ')
                        try:
                            i = self.backpack.contentsNames.index(inp)
                        except ValueError:
                            i = -1
                        if i > -1:
                            if inp == 'coin':
                                if pz.leverPuzzle() == True:
                                    self.leverMachineComplete = True
                                    self.backpack.contentsNames.append(it.heavykey.name)
                                    self.backpack.contents.append(it.heavykey)
                                    self.backpack.contentsNames.remove('coin')
                                    self.backpack.contents.remove(it.coin)
                            else:
                                print("The",inp,"doesn't seem to work with the machine")
                        else:
                            print('There is no',inp,'to use. You step away from the machine')    
                    else:
                        print("You already solved this machine's puzzle")
                else:
                    print('There is no levermachine to interact with here')
                
            elif self.cmd[1] == 'numbermachine':
                #print('number puzzle')
                if self.location == 3:
                    if self.numberMachineComplete == False:
                        if pz.numberPuzzle() == True:
                            self.numberMachineComplete = True
                            self.backpack.contentsNames.append(it.bronzekey.name)
                            self.backpack.contents.append(it.bronzekey)
                    else:
                        print("You already solved this machine's puzzle")
                else:
                    print('There is no numbermachine to interact with here')
            else:
                if self.inBackpack(self.cmd[1]) == True:
                    i = self.backpack.contentsNames.index(self.cmd[1])
                elif self.inCurrentRoom(self.cmd[1]) == True:
                    i = it.itemNames.index(self.cmd[1])
                else:
                    i = -1

                if i > -1:
                    if 'smeltingmold' in self.cmd[1]:
                        if it.items[i].state == it.SMoldStates.FILLED:
                            self.backpack.contentsNames.append('statue')
                            self.backpack.contents.append(it.statue)
                            it.items[i].interact()
                        else:
                            it.items[i].interact()

                    elif 'chest' in self.cmd[1] or 'desk' in self.cmd[1] or 'pedestal' in self.cmd[1]:                        
                        if it.items[i].interact(self.backpack.contentsNames) == True:
                            for obj in it.items[i].contents:
                                self.backpack.contents.append(obj)
                                self.backpack.contentsNames.append(obj.name)
                            if it.items[i].name == 'pedestal':
                                self.backpack.contentsNames.remove('statue')
                                self.backpack.contents.remove(it.statue)
                            
                    elif 'door' in self.cmd[1]:
                        if it.items[i].singleInteract(self.backpack.contentsNames):
                            if it.items[i].name == 'atticdoor':
                                self.backpack.contentsNames.remove('ladder')
                                self.backpack.contents.remove(it.ladder)
                    else:
                        print("That item doesn't seem to do anything on its own")
                else:
                    print('There is no ', self.cmd[1],'to interact with')
                    
        elif len(self.cmd) == 3:
            
##            try:    #still need to check if items in room or in backpack
##                i = it.itemNames.index(self.cmd[1])
##                j = it.itemNames.index(self.cmd[2])
##            except ValueError:
##                i = -1
##                j = -1



            if 'levermachine' in self.cmd[1] or 'levermachine' in self.cmd[2]:
                if 'levermachine' in self.cmd[1] and 'levermachine' in self.cmd[2]:
                    print('Nice try, levermachine-ception has no power here')
                
                elif 'levermachine' in self.cmd[1]:
                    if self.location == 2:
                        if self.leverMachineComplete == False:
                            if self.inBackpack(self.cmd[2]) == True:
                                x = it.itemNames.index(self.cmd[2])
                            else:
                                x = -1
                            if x > -1:
                                if it.items[x].name == 'coin':
                                    if pz.leverPuzzle() == True:
                                        self.leverMachineComplete = True
                                        self.backpack.contentsNames.append(it.heavykey.name)
                                        self.backpack.contents.append(it.heavykey)
                                        self.backpack.contentsNames.remove('coin')
                                        self.backpack.contents.remove(it.coin)
                                else: print('The',self.cmd[2],'doesnt seem to work with the levermachine')
                            else: print("There is no",self.cmd[2],"to use")
                        else: print("You already solved this machine's puzzle")
                    else: print('There is no levermachine to interact with here')

                elif 'levermachine' in self.cmd[2]:
                    if self.location == 2:
                        if self.leverMachineComplete == False:
                            if self.inBackpack(self.cmd[1]) == True:
                                x = it.itemNames.index(self.cmd[1])
                            else:
                                x = -1
                            if x > -1:
                                if it.items[x].name == 'coin':
                                    if pz.leverPuzzle() == True:
                                        self.leverMachineComplete = True
                                        self.backpack.contentsNames.append(it.heavykey.name)
                                        self.backpack.contents.append(it.heavykey)
                                        self.backpack.contentsNames.remove('coin')
                                        self.backpack.contents.remove(it.coin)
                                else: print('The',self.cmd[1],'doesnt seem to work with the levermachine')
                            else: print("There is no",self.cmd[1],"to use")
                        else: print("You already solved this machine's puzzle")
                    else: print('There is no levermachine to interact with here')              

            else:
                if self.inBackpack(self.cmd[1]) == True or self.inCurrentRoom(self.cmd[1]) == True:
                    i = it.itemNames.index(self.cmd[1])
                else:
                    i = -1

                if self.inBackpack(self.cmd[2]) == True or self.inCurrentRoom(self.cmd[2]) == True:
                    j = it.itemNames.index(self.cmd[2])
                else:
                    j = -1
                    
                if i > -1 and j > -1:
                    if ('key' in self.cmd[1] or 'ladder' in self.cmd[1]) and 'door' in self.cmd[2]:
                        #print('key/door')
                        it.items[j].interact(it.items[i])
                        if it.items[i].name == 'ladder' and it.items[j].name == 'atticdoor':
                            self.backpack.contentsNames.remove('ladder')
                            self.backpack.contents.remove(it.ladder)
                    elif ('key' in self.cmd[2] or 'ladder' in self.cmd[2]) and 'door' in self.cmd[1]:
                        #print('door/key')
                        it.items[i].interact(it.items[j])
                        if it.items[j].name == 'ladder' and it.items[i].name == 'atticdoor':
                            self.backpack.contentsNames.remove('ladder')
                            self.backpack.contents.remove(it.ladder)
                        
                    elif 'furnace' in self.cmd[1] or 'furnace' in self.cmd[2]:
                        if 'furnace' in self.cmd[1] and 'furnace' in self.cmd[2]:
                            print("Nice try, but 'furnace-ception' has no power here")
                        
                        elif 'furnace' in self.cmd[1]:
                            #print('furnace is first item')
                            it.items[i].interact(it.items[j])
                            if it.items[j].name == 'firewood' and it.items[i].state == it.FurnaceStates.FUELED:
                                self.backpack.contentsNames.remove('firewood')
                                self.backpack.contents.remove(it.firewood)
                                
                        elif 'furnace' in self.cmd[2]:
                            #print('furnace is second item')
                            it.items[j].interact(it.items[i])
                            if it.items[i].name == 'firewood' and it.items[j].state == it.FurnaceStates.FUELED:
                                self.backpack.contentsNames.remove('firewood')
                                self.backpack.contents.remove(it.firewood)

                    elif 'crucible' in self.cmd[1] or 'crucible' in self.cmd[2]:

                        if 'crucible' in self.cmd[1] and 'crucible' in self.cmd[2]:
                            print("Nice try, but 'crucible-ception' has no power here")
                
                        elif 'crucible' in self.cmd[1]:
                            if it.items[i].state == it.CrucibleStates.INSERTED and it.items[j].name == 'smeltingmold':
                                f = it.itemNames.index('furnace')
                                it.items[f].furnaceEmptyFunction()
                                it.items[i].interact(it.items[j])
                            elif it.items[i].state == it.CrucibleStates.EMPTY and it.items[j].name == 'scrapmetal':
                                it.items[i].interact(it.items[j])
                                self.backpack.contentsNames.remove('scrapmetal')
                                self.backpack.contents.remove(it.scrapmetal)
                            else:
                                it.items[i].interact(it.items[j])

                        elif 'crucible' in self.cmd[2]:
                            if it.items[j].state == it.CrucibleStates.INSERTED and it.items[i].name == 'smeltingmold':
                                f = it.itemNames.index('furnace')
                                it.items[f].furnaceEmptyFunction()
                                it.items[j].interact(it.items[i])
                            elif it.items[j].state == it.CrucibleStates.EMPTY and it.items[i].name == 'scrapmetal':
                                it.items[j].interact(it.items[i])
                                self.backpack.contentsNames.remove('scrapmetal')
                                self.backpack.contents.remove(it.scrapmetal)
                            else:
                                it.items[j].interact(it.items[i])
                                
                    elif 'chest' in self.cmd[1] or 'pedestal' in self.cmd[1] or 'desk' in self.cmd[1]:
                        if it.items[i].interact2(it.items[j]) == True:
                            for obj in it.items[i].contents:
                                self.backpack.contentsNames.append(obj.name)
                                self.backpack.contents.append(obj)
                            if it.items[i].name == 'pedestal':
                                self.backpack.contentsNames.remove('statue')
                                self.backpack.contents.remove(it.statue)


                    elif 'chest' in self.cmd[2] or 'pedestal' in self.cmd[2] or 'desk' in self.cmd[2]:
                        if it.items[j].interact2(it.items[i]) == True:
                            for obj in it.items[j].contents:
                                self.backpack.contentsNames.append(obj.name)
                                self.backpack.contents.append(obj)
                            if it.items[j].name == 'pedestal':
                                self.backpack.contentsNames.remove('statue')
                                self.backpack.contents.remove(it.statue)
                        
                    
                    else:
                        print('There is no interaction between the',self.cmd[1],'and the',self.cmd[2])                
                else:
                    if i == -1: print('There is no',self.cmd[1],'to use')
                    if j == -1: print('There is no',self.cmd[2],'to use')
                
    def showBackpack(self):
        #print('showBackpack command selected')
        if len(self.backpack.contents) > 0:
            for obj in self.backpack.contentsNames:
                print(obj)
        else: print('Backpack is empty')
                
    def inBackpack(self,cmdString):
        try:
            i = self.backpack.contentsNames.index(cmdString)
        except ValueError:
            i = -1
        if i > -1:
            #print('the item is in the backpack')
            return True
        else:
            #print('item is not in backpack')
            return False
        
    def inCurrentRoom(self,cmdString):
        try:
            i = it.itemNames.index(cmdString)
        except ValueError:
            i = -1
        if i > -1:
            if it.items[i].location == self.location:
                #print('item is in the current room')
                return True
            elif it.items[i] == it.golddoor or it.items[i] == it.atticdoor or it.items[i] == it.largedoor:
                if it.items[i].behind == self.location:
                    return True
            else:
                #print('the item exists, however the item is not in the current room')
                return False
        else:
            #print('the item doesnt exist and is not in the current room')
            return False
