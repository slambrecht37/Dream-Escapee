#file to hold game items and classes and the actual objects themselves

#import game_player as pl

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

class Door(Item):   #door class, (includes attic door) location is room that it can be unlocked from

    endDoorCount = 0
    
    def __init__(self, name, location, desc, isHidden, canPickUp, key, behind = None, locked = True):
        super().__init__(name, location, desc, isHidden, canPickUp)
        self.key = key
        self.locked = locked
        self.behind = behind if behind is not None else 0

    def singleInteract(self):
        if self.locked:
            print('The',self.name,'is locked')
        else:
            print('The',self.name, 'is unlocked')

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
    def __init__(self, name, location, desc, isHidden, canPickUp, fuel, isLit = False, isFueled = False):
        super().__init__(name, location, desc, isHidden, canPickUp)
        self.fuel = fuel
        self.isLit = isLit
        self.isFueled = isFueled

    def interact(self, item):
        if item == self.fuel:
            print('The firewood was placed into the furnace')
            item.used = True
            self.isFueled = True
        elif item.name == 'matches':
            if self.isFueled == True:
                print('You strike a match and use it to light the firewood inside the furnace')
                self.isLit = True
            else:
                print('There is no fuel in the furnace to light with the matches. Add fuel and try again')
        elif item.name == 'crucible':
            if self.isLit == True:
                if item.empty == False:
                    if item.contents[0].name == 'scrapmetal':
                        print("You place the filled crucible inside the furnace. The furnace seems hot enough to melt the scrapmetal")
                        print("HINT: The next command should be 'interact crucible smeltingmold'")
                        item.contents[0].used = True
                    else:
                        print("That's probably not a good idea")
                else:
                    print("The crucible is empty. There is no point in putting in the furnace")
            else:
                print("The furnace is not lit, so nothing will happen with the crucible")
        else:
            print('invalid combination of items')

class Vessel(Item):
    def __init__(self, name, location, desc, isHidden, canPickUp,empty):
        super().__init__(name, location, desc, isHidden, canPickUp)
        self.empty = empty
        self.contents = []

    def add(self, item):
        self.contents.append(item)
        self.empty = False
        #print(item.name,"placed in",self.name)
        if self.name == 'crucible' and item.name == 'scrapmetal' and item.used == False:
            print('You place the bits of scrapmetal into the crucible. The amount of scrapmetal seems a perfect fit for the crucible')
        if self.name == 'smeltingmold' and item.name == 'scrapmetal' and item.used == True:
            print('You take the crucible and pour the molten metal into the smeltingmold') #describe acquisistion of statue
            
    def emptyFunction(self):
        print(self.name,"emptied")
        if self.name == 'smeltingmold' and self.contents[0].name == 'scrapmetal' and self.contents[0].used == True:
            #print("here is statue, meine fraulein")
            print('''You open the smeltingmold and use some clamps to move the cast object into some water to cool it off. You pull the object \
out to see it is a small metal statue of an angel. You place the statue in your backpack.''')
        self.contents = []
        self.empty = True

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
noteDesc = 'note: A small slip of paper. It reads "Combo: 789"'
trophyDesc = 'trophy: A golden goblet encrusted with jewels'

matches = Item('matches', 4, matchesDesc, False, True)
note = Item('note', 4, noteDesc, True, True)    #hidden so can't be picked up anyway because isHidden supercedes canPickUp
trophy = Item('trophy', 10, trophyDesc, False, True)

itemNames.append('matches')
itemNames.append('note')
itemNames.append('trophy')

items.append(matches)
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
smeltingmoldDesc = 'smeltingmold: A bulky cermic mold used for casting molten metal. It looks to be in the shape of a winged humanoid'
crucibleDesc = 'crucible: A heavy ceramic crucible'

smeltingmold = Vessel('smeltingmold', 8, smeltingmoldDesc, False, False, True)
crucible = Vessel('crucible', 8, crucibleDesc, False, False, True)

itemNames.append('smeltingmold')
itemNames.append('crucible')

items.append(smeltingmold)
items.append(crucible)
        
print("game_items compiles")
        

