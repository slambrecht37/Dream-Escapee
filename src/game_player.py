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

    def intro(self):
        print(hp.intro)
        print(hp.playerPromptHelp)

    def prompt(self):
        userInput = input("\nWhat will you do? \n> ")
        self.cmd = userInput.split()

        if len(self.cmd) > 0:
            if self.cmd[0] == 'go':
                self.move()
            elif self.cmd[0] == 'explore':
                self.explore()
            elif self.cmd[0] == 'examine':
                self.examine()
            elif self.cmd[0] == 'take':
                self.take()
            elif self.cmd[0] == 'interact':
                self.interact()
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
                elif rm.room[self.location].nDoor.locked == False:
                    self.location = rm.room[self.location].north
                    #print('The door is unlocked. You go north to room',self.location)
                    print('The door is unlocked. You go north into the next room')
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
                elif rm.room[self.location].eDoor.locked == False:
                    self.location = rm.room[self.location].east
                    #print('The door is unlocked. You go east to room',self.location)
                    print('The door is unlocked. You go east into the next room')
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
                elif rm.room[self.location].sDoor.locked == False:
                    self.location = rm.room[self.location].south
                    #print('The door is unlocked. You go south to room',self.location)
                    print('The door is unlocked. You go south into the next room')
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
                elif rm.room[self.location].wDoor.locked == False:
                    self.location = rm.room[self.location].west
                    #print('The door is unlocked. You go west to room',self.location)
                    print('The door is unlocked. You go west into the next room')
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
                elif rm.room[self.location].uDoor.locked == False:
                    self.location = rm.room[self.location].up
                    #print('The door is unlocked. You go up to room',self.location)
                    print('The door is unlocked. You go up into the room above')
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
                elif rm.room[self.location].dDoor.locked == False:
                    self.location = rm.room[self.location].down
                    #print('The door is unlocked. You go below to room',self.location)
                    print('The door is unlocked. You go down into the room below')
                else:
                    print('''There is a locked door preventing you from going down. Find \
the appropriate key to unlock it''')
            else:
                print('Cannot go down')
        else:
            print('Invalid direction')

    def explore(self):
        #print('explore command selected')
        print(hp.roomDesc[self.location])

    def examine(self):
        obj = self.cmd[1]
        #print('examine command selected')
        found = False
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
                            if it.items[i].name == 'trophy':
                                self.win = True
                                print(hp.win)
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
                        if it.items[i].empty == False:
                            if it.items[i].contents[0] == it.scrapmetal:
                                self.backpack.contents.append(it.statue)
                                self.backpack.contentsNames.append(it.statue.name)
                                it.items[i].emptyFunction()
                            else:
                                it.items[i].emptyFunction()
                        else:
                            print('Nothing happened because the smeltingmold was already empty')
                    elif 'chest' in self.cmd[1] or 'desk' in self.cmd[1] or 'pedestal' in self.cmd[1]:                        
                        if it.items[i].interact(self.backpack.contentsNames) == True:
                            for obj in it.items[i].contents:
                                self.backpack.contents.append(obj)
                                self.backpack.contentsNames.append(obj.name)
                            
                    elif 'door' in self.cmd[1]:
                        it.items[i].singleInteract()

                    else:
                        print("That item doesn't seem to do anything on its own")
                else:
                    print('There is no ', self.cmd[1],'to interact with')
                    
        if len(self.cmd) == 3:
            
##            try:    #still need to check if items in room or in backpack
##                i = it.itemNames.index(self.cmd[1])
##                j = it.itemNames.index(self.cmd[2])
##            except ValueError:
##                i = -1
##                j = -1


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
                elif ('key' in self.cmd[2] or 'ladder' in self.cmd[2]) and 'door' in self.cmd[1]:
                    #print('door/key')
                    it.items[i].interact(it.items[j])
                    
                elif 'furnace' in self.cmd[1] or 'furnace' in self.cmd[2]:
                    if 'furnace' in self.cmd[1]:
                        #print('furnace is first item')
                        it.items[i].interact(it.items[j])
                    elif 'furnace' in self.cmd[2]:
                        #print('furnace is second item')
                        it.items[j].interact(it.items[i])
                        
                elif 'smeltingmold' in self.cmd[1] and 'crucible' in self.cmd[2]:
                    if it.items[j].contents[0].name == 'scrapmetal':
                        #it.items[i].add(it.scrapmetal)
                        it.items[i].add(it.items[j].contents[0])    #change this from being a list
                        it.items[j].emptyFunction()
                elif 'smeltingmold' in self.cmd[2] and 'crucible' in self.cmd[1]:
                    if it.items[i].contents[0].name == 'scrapmetal':
                        #it.items[j].add(it.scrapmetal)
                        it.items[j].add(it.items[i].contents[0])    #change this from being a list
                        it.items[i].emptyFunction()         
                    
                elif 'crucible' in self.cmd[1] or 'crucible' in self.cmd[2]:
                    if 'crucible' in self.cmd[1]:
                        #print("crucible is first item")
                        it.items[i].add(it.items[j])
                    if 'crucible' in self.cmd[2]:
                        #print("crucible is second item")
                        it.items[j].add(it.items[i])
                else:
                    print('There is no interaction between the',self.cmd[1],'and the ',self.cmd[2])
                
            else:
                print('One or both of the entered items are invalid')
                
    def showBackpack(self):
        #print('showBackpack command selected')
        if len(self.backpack.contents) > 0:
            for obj in self.backpack.contentsNames:
                print(obj)
                
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
            else:
                #print('the item exists, however the item is not in the current room')
                return False
        else:
            #print('the item doesnt exist and is not in the current room')
            return False
