#file to hold game items and classes and the actual objects themselves

#import game_player as pl

class FurnaceStates():
    EMPTY = 0
    FUELED = 1
    LIT = 2
    LOADED = 3
    EMPTIED = 4

class CrucibleStates():
    EMPTY = 0
    FILLED = 1
    INSERTED = 2
    EMPTIED = 3

class SMoldStates():
    EMPTY = 0
    FILLED = 1
    EMPTIED = 2

class Item:     #general item class
    def __init__(self, name, location, desc, isHidden, canPickUp):
        self.name = name
        self.location = location
        self.desc = desc
        self.isHidden = isHidden
        self.canPickUp = canPickUp

class Key(Item):        #to make sure keys are used to unlock containers and not, also includes ladder to attic
    def __init__(self, name, location, desc, isHidden, canPickUp):
        super().__init__(name, location, desc, isHidden, canPickUp)

class Container(Item):      #locked boxes, chests, drawers, etc as well as unlocked desk, etc.
    def __init__(self, name, location, desc, isHidden, canPickUp, heldItem, locked, key = None):
        super().__init__(name, location, desc, isHidden, canPickUp)
        self.key = key if key is not None else None
        self.locked = locked
        self.contents = []
        self.contents.append(heldItem)
        self.alreadyOpened = False

    def interact(self, itemlistNames = None):

        backpackNames = itemlistNames if itemlistNames is not None else None
        
        if self.alreadyOpened == False:
            if self.locked == True:
                if self.name == 'pedestal':
                    inp = input('The pedestal seems to be missing something. Enter the name of an object to place onto it: ')
                else:
                    inp = input('The {0} is locked. Enter the name of a key you possess to try to unlock it: '.format(self.name))

                try:
                    i = backpackNames.index(inp)
                except ValueError:
                    i = -1

                if i > -1:
                    if inp == self.key.name:
                        #print('that is the correct key')
                        self.locked = False
                        self.alreadyOpened = True
                        if self.name == 'pedestal':
                           print('The statue fits snugly into the pedestal. A hidden compartment in the base opens. You add the following items to your backpack: ')
                        else:
                            print('The key works, and the',self.name,'opens. You add the following items to your backpack: ')
                        #now open
                        for obj in self.contents:
                            print(obj.name)
                        return True 
                    else:
                        print('The',inp,'doesnt seem to work with the',self.name)
                        return False               
                else:
                    print('You dont have a',inp,'to use')        
            else:
                self.alreadyOpened = True
                print('The', self.name,'opens. You place the following items in your backpack')
                #now open
                for obj in self.contents:
                        print(obj.name)
                return True
        else:
            print('The',self.name,'has been accessed. You have already taken what was inside')
            return False

    def interact2(self, item):

        if self.alreadyOpened == False:
            if self.locked == True:
                if item.name == self.key.name:
                    self.locked = False
                    self.alreadyOpened = True
                    
                    if self.name == 'pedestal':
                        print('The statue fits snugly into the pedestal. A hidden compartment in the base opens. You add the following items to your backpack: ')
                        
                    else:
                        print('The key works, and the',self.name,'opens. You add the following items to your backpack: ')

                    #now open
                    for obj in self.contents:
                        print(obj.name)
                    return True
                    
                else:
                    print('The',item.name,'doesnt seem to work with the',self.name)
                    return False
            else:
                self.alreadyOpened = True
                if self.name == 'desk': print('You try to open the desk with the',item.name,'but you find it already unlocked. You place the following items in your backpack')
                else: print('The', self.name,'opens. You place the following items in your backpack')
                #now open
                for obj in self.contents:
                    print(obj.name)
                return True
        else:
            print('The', self.name,'has been accessed. You have already taken what was inside')
            return False

class Door(Item):   #door class, (includes attic door) location is room that it can be unlocked from

    endDoorCount = 0
    
    def __init__(self, name, location, desc, isHidden, canPickUp, key, behind = None, locked = True):
        super().__init__(name, location, desc, isHidden, canPickUp)
        self.key = key
        self.locked = locked
        self.behind = behind if behind is not None else 0

    def singleInteract(self, itemlistNames = None):

        backpackNames = itemlistNames if itemlistNames is not None else None
        
        if self.locked:
            if self.name == 'atticdoor':
                print('The atticdoor is too high to reach.')
                inp = input('Enter the name of an item to use to reach the atticdoor: ')
            else:
                print('The',self.name,'is locked')
                inp = input('Enter the name of a key you possess to try to unlock it: ')
            try:
                i = backpackNames.index(inp)
            except ValueError:
                i = -1
            if i > -1:
                #print('chosen item in backpack')
                if inp == self.key.name:
                    self.locked = False
                    if self.name == 'atticdoor':
                        print("You stand the ladder up and it reaches the door to the attic. The ladder seems sturdy enough to climb")
                        return True
                    elif self.name == 'golddoor' or self.name == 'silverdoor' or self.name == 'bronzedoor':
                        print("You insert and turn the key. Sounds of gears turning and metal scraping come from behind the door.")
                        Door.endDoorCount += 1
                        if Door.endDoorCount == 3:
                            print("You hear a dull hum. Suddenly, the gold door swings open to reveal another room")
                        return True
                    elif self.name == 'largedoor':
                        print("You insert and turn the key. The door slowly swings open, revealing another room")
                        return True
                else:
                    if self.name == 'atticdoor':
                        print("That's not going to help you reach the atticdoor")
                    else:
                        print("The",inp,"does not fit into the door's lock")
            else:
                print('You dont have a',inp,'to use')
        else:
            if self.name == 'atticdoor':
                print('The ladder has already been set up to reach the atticdoor')
            else:
                print('The',self.name, 'is unlocked')
                
        if Door.endDoorCount == 3:    #never reached when end doors used since the function returns, moved up there
            print("You hear a dull hum. Suddenly, the gold door swings open to reveal another room")

    def interact(self, obj:Key):
        if self.locked:
            if obj.name == self.key.name:
                self.locked = False
                #print(self.name)
                if self.name == 'golddoor' or self.name == 'silverdoor' or self.name == 'bronzedoor':
                    print("You insert and turn the key. Sounds of gears turning and metal scraping come from behind the door.")
                    Door.endDoorCount += 1
                elif self.name == 'atticdoor':
                    print("You stand the ladder up and it reaches the door to the attic. The ladder seems sturdy enough to climb")
                elif self.name == 'largedoor':
                    print("You insert and turn the key. The door slowly swings open, revealing another room")
            else:
                if self.name == atticdoor:
                    print("That's not going to help you get to the attic door")
                else:            
                    print("The key does not fit into the door's lock")
        else:
            if self.name == atticdoor:
                print("The ladder to get to the attic has already been set up")
            else:
                print("The door is already unlocked")

        if Door.endDoorCount == 3:
            print("You hear a dull hum. Suddenly, the gold door swings open to reveal another room")        

class Consumable(Item):
    def __init__(self, name, location, desc, isHidden, canPickUp, used = False):
        super().__init__(name, location, desc, isHidden, canPickUp)
        self.used = used
        
    def interact(self):
        if self.used == False:
            self.used = True
        else:
            print(self.name,"already used")

class Furnace(Item): #for furnace, since it doesnt fit with other types but has special interactions 

    def __init__(self, name, location, desc, isHidden, canPickUp, fuel):
        super().__init__(name, location, desc, isHidden, canPickUp)
        self.fuel = fuel
        self.isLit = False
        self.isFueled = False
        self.isLoaded = False
        self.state = FurnaceStates.EMPTY

    def interact(self, item):
        if self.state == FurnaceStates.EMPTY:
            if item == self.fuel:
                print('The firewood was placed into the furnace')
                self.state = FurnaceStates.FUELED
            else: print('The furnace has not been fueled or lit yet. Do that before you use it')

        elif self.state == FurnaceStates.FUELED:
            if item.name == 'matches':
                print('You strike a match and use it to light the firewood inside the furnace')
                self.state = FurnaceStates.LIT
            else:
                print('The fuel in the furnace has not been set alight yet. Make sure the furnace is hot before you use it for anything')

        elif self.state == FurnaceStates.LIT:
            if item.name == 'crucible':
                if item.state == CrucibleStates.FILLED:
                    print('You place the filled crucible into the furnace. It seems hot enough to melt the scrapmetal')
                    self.state = FurnaceStates.LOADED
                    item.crucibleInsertFunction()
                else: print('The crucible is empty. There is no point in putting it in the furnace')
            else: print('Its probably not a good idea to place that into the furnace right now')

        elif self.state == FurnaceStates.LOADED:
            if item.name == 'crucible':
                print('The crucible was already placed in the furnace')
            else:
                print('You cannot place that item inside the furnace')

        elif self.state == FurnaceStates.EMPTIED:
            print('You already used the furnace')
            

    def furnaceEmptyFunction(self):
        if self.state == FurnaceStates.LOADED:
            print('You take the crucible out of the furnace')
            self.state = FurnaceStates.EMPTIED

class Vessel(Item):
    def __init__(self, name, location, desc, isHidden, canPickUp):
        super().__init__(name, location, desc, isHidden, canPickUp)
        self.empty = True
        self.contents = None
        self.state = 0 #empty for all situations        

    def interact(self, argItem = None):

        item = argItem if argItem is not None else None
        
        if self.name == 'crucible':
            if self.state == CrucibleStates.EMPTY:
                if item.name == 'scrapmetal':
                    print('You place the bits of scrapmetal into the crucible. The amount of scrapmetal seems a perfect fit for the crucible')
                    self.state = CrucibleStates.FILLED
                    self.contents = item
                elif item.name == 'smeltingmold':
                    print('The crucible is empty. There is nothing to pour into the smeltingmold')
                else: print('Its probably not a good idea to place that in the crucible')
                
            elif self.state == CrucibleStates.FILLED:
                if item.name == 'smeltingmold':
                    print('You should probably melt the metal before pouring it into the smeltingmold')
                else:
                    print('That is not going to do anything with the filled crucible')
                
            elif self.state == CrucibleStates.INSERTED:
                if item.name == 'smeltingmold':
                    if item.state == SMoldStates.EMPTY:
                        print('You pour the molten metal from the crucible into the smeltingmold. It should be cool enough to extract from the smeltingmold soon')
                        self.state = CrucibleStates.EMPTIED
                        item.interact(self.contents)
                        self.contents = None
                    else: print('The molten metal cannot be poured into the smelting mold because the smeltingmold already has something in it')
                else: print('That object has no use with the crucible while the crucible is full of molten metal')

            elif self.state == CrucibleStates.EMPTIED:
                if item.name == 'smeltingmold':
                    print('You already poured the molten metal from the crucible into the smeltingmold')
                else:
                    print('You already used the crucible. You do not need it to use it again')

        elif self.name == 'smeltingmold':
            if self.state == SMoldStates.EMPTY:
                if not(item == None):
                    if item.name == 'scrapmetal':
                        self.contents = item
                        self.state = SMoldStates.FILLED
                    else:
                        print('That probably shouldnt be placed into the smeltingmold')
                else: print('The smeltingmold has no use by itself right now')

            elif self.state == SMoldStates.FILLED:
                if self.contents.name == 'scrapmetal':
                    print('''You open the smeltingmold and use some clamps to move the cast object into some water to cool it off. You pull the object \
out to see it is a small metal statue of an angel. You place the statue in your backpack.''')
                self.state = SMoldStates.EMPTIED
                self.contents = None

            elif self.state == SMoldStates.EMPTIED:
                print('You already used the smeltingmold')

    def crucibleInsertFunction(self):
        if self.name == 'crucible':
            self.state = CrucibleStates.INSERTED

class Backpack:
    def __init__(self):
        self.contentsNames = []
        self.contents = []
        
    def add(item):
        contentsNames.append(item.name)
        contents.append(item)        

itemNames = []
items = []

#Items (not any more specific)
matchesDesc = 'matches: A book of matches'
bookDesc = '''book: A worn book. The faded title reads, "Smelting and Casting for Dummies." You open it and read a couple pages:
. . . . .
Smelting boils down (pun intended) to 4 basic steps:
Step 1: Ensure that your smelting furnace is sufficiently hot.
Step 2: Place your crucible containing your casting metal into the furnace.
Step 3: Pour the molten metal from the crucible into the desired mold.
Step 4: Once the metal solidifies, extract the casted item from the mold.
If you can remember these 4 steps, you are on your way to becoming a seasoned metalsmith. In fact, you are already better than the worker who caused the Great Slag Disaster of 1869.
. . . . .'''
noteDesc = 'note: A small slip of paper. It reads "Combo: 789"'
trophyDesc = 'trophy: A golden goblet encrusted with jewels'

matches = Item('matches', 4, matchesDesc, False, True)
book = Item('book', 4, bookDesc, False, True)
note = Item('note', 4, noteDesc, True, True)    #hidden so can't be picked up anyway because isHidden supercedes canPickUp
trophy = Item('trophy', 10, trophyDesc, False, True)
levermachine = Item('levermachine', 2, 'levermachine desc', False, False)
numbermachine = Item('numbermachine', 3, 'numbermachine desc', False, False)

itemNames.append('matches')
itemNames.append('book')
itemNames.append('note')
itemNames.append('trophy')

items.append(matches)
items.append(book)
items.append(note)
items.append(trophy)

#Keys
nonekeyDesc = 'no key -> if you read this let me know as this shouldnt ever happen'
bronzekeyDesc = 'bronzekey: A heavy bronze key'
silverkeyDesc = 'silverkey: A heavy silver key'
goldkeyDesc = 'goldkey: A heavy gold key'
coinDesc = 'coin: A shiny gold arcade-style coin'
oldkeyDesc = 'oldkey: A small key. It is weathered and rusty, obviously old'
ladderDesc = 'ladder: A normal ladder. Could probably extend to 20+ feet high'
heavykeyDesc = 'heavykey: A heavy steel key'
smallkeyDesc = 'smallkey: A small metal key. It looks like it might go to a desk drawer'
statueDesc = 'statue: A small metal statue of an angel'

nonekey = Key('nonekey', 0, nonekeyDesc, True, False)
bronzekey = Key('bronzekey', 3, bronzekeyDesc, True, True)    #found in numberpuzzle, used for bronze door
silverkey = Key('silverkey', 5, silverkeyDesc, False, True)   #found in room 5, used for silver door
goldkey = Key('goldkey', 7, goldkeyDesc, True, True)         #found from angel statue stuff, used for gold door
coin = Key('coin', 6, coinDesc, True, True)                   #found in chest in attic, used for lever machine
oldkey = Key('oldkey', 8, oldkeyDesc, False, True)            #found on floor of room 8, used for chest in attic
ladder= Key('ladder', 5, ladderDesc, False, True)             #found onfloor of room 5, used for attic door
heavykey = Key('heavykey', 2, heavykeyDesc, True, True)       #found in lever puzzle, used for for large door in room 1
statue = Key('statue',8, statueDesc, True, True)

itemNames.append('bronzekey')
itemNames.append('silverkey')
itemNames.append('goldkey')
itemNames.append('coin')
itemNames.append('oldkey')
itemNames.append('ladder')
itemNames.append('heavykey')
itemNames.append('statue')

items.append(bronzekey)
items.append(silverkey)
items.append(goldkey)
items.append(coin)
items.append(oldkey)
items.append(ladder)
items.append(heavykey)
items.append(statue)

#Containers
deskDesc = 'desk: A large wooden desk with many drawers'
chestDesc = 'chest: An old wooden chest, resembling a small treasure chest'
pedestalDesc = 'pedestal: A stone pedestal with a recess in the top, as if something was meant to sit there'

desk = Container('desk', 4, deskDesc, False, False, note, False)
chest = Container('chest', 6, chestDesc, False, False, coin, True, oldkey)
pedestal = Container('pedestal', 7, pedestalDesc, False, False, goldkey, True, statue) 

itemNames.append('desk')
itemNames.append('chest')
itemNames.append('pedestal')

items.append(desk)
items.append(chest)
items.append(pedestal)

#Doors
bronzedoorDesc = 'bronzedoor: A sturdy bronze-colored door with a lock'
silverdoorDesc = 'silverdoor: A sturdy silver-colored door with a lock'
golddoorDesc = 'golddoor: A sturdy gold-colored door with a lock'
atticdoorDesc = 'atticdoor: A small wooden door set in the ceiling'
largedoorDesc = 'largedoor: A large steel door with a large key hole'
nonedoorDesc = 'no door -> if you read this let me know since this shouldnt ever happen'

bronzedoor = Door('bronzedoor', 9, bronzedoorDesc, False, False, bronzekey)
silverdoor = Door('silverdoor', 9, silverdoorDesc, False, False, silverkey)
golddoor = Door('golddoor', 9, golddoorDesc, False, False, goldkey, 10)
atticdoor = Door('atticdoor', 3, atticdoorDesc, False, False, ladder, 6)
largedoor = Door('largedoor', 1, largedoorDesc, False, False, heavykey, 9)
nonedoor = Door('nonedoor', 0, nonedoorDesc, True, False, nonekey, locked = False)

itemNames.append('bronzedoor')
itemNames.append('silverdoor')
itemNames.append('golddoor')
itemNames.append('atticdoor')
itemNames.append('largedoor')

items.append(bronzedoor)
items.append(silverdoor)
items.append(golddoor)
items.append(atticdoor)
items.append(largedoor)

#Consumables
scrapmetalDesc = 'scrapmetal: A pile of metal scrap. It seems lightweight, probably used for smelting'
firewoodDesc = 'firewood: Some firewood. It looks dry enough to burn'

firewood = Consumable('firewood', 5, firewoodDesc, False, True)
scrapmetal = Consumable('scrapmetal', 5, scrapmetalDesc, False, True)

itemNames.append('firewood')
itemNames.append('scrapmetal')

items.append(firewood)
items.append(scrapmetal)

#Furnace
furnaceDesc = 'furnace: A foundry furnace, capable of reaching hundreds of degrees F'

furnace = Furnace('furnace', 8, furnaceDesc, False, False, firewood)

itemNames.append('furnace')

items.append(furnace)

#Vessels
smeltingmoldDesc = 'smeltingmold: A bulky ceramic mold used for casting molten metal. It looks to be in the shape of a winged humanoid'
crucibleDesc = 'crucible: A heavy ceramic crucible'

smeltingmold = Vessel('smeltingmold', 8, smeltingmoldDesc, False, False)
crucible = Vessel('crucible', 8, crucibleDesc, False, False)

itemNames.append('smeltingmold')
itemNames.append('crucible')

items.append(smeltingmold)
items.append(crucible)
        
#print("game_items compiles")
        

