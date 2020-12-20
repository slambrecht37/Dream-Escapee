#weapons and battles (including enemy(s))

import random
import math

##class Weapon:
##    def __init__(self, name, location, desc, power, accuracy, efficiency, defending):
##        self.name = name
##        self.power = power
##        self.accuracy = accuracy
##        self.efficiency = efficiency
##        self.defending = defending
        
##class PlayerBattle:
##    def __init__(self, name, health, weapon, energy):
##        self.name= name
##        self.health = health
##        self.maxHealth = health
##        self.weapon = weapon
##        self.energy = energy
##        self.maxEnergy = energy
##        self.isDefending = False

class Weapon:
    def __init__(self, name, location, desc, isHidden, canPickUp, power, accuracy, efficiency, defending):
        self.name = name
        self.location = location
        self.desc = desc
        self.isHidden = isHidden
        self.canPickUp = canPickUp
        self.power = power
        self.accuracy = accuracy
        self.efficiency = efficiency
        self.defending = defending

class Enemy:
    def __init__(self, name, health, weapon, energy):
        self.name= name
        self.health = health
        self.maxHealth = health
        self.energy = energy
        self.maxEnergy = energy
        
        self.weapon = weapon
        self.power = weapon.power
        self.accuracy = weapon.accuracy
        self.efficiency = weapon.efficiency
        self.defending = weapon.defending
        
        self.isDefending = False
        self.willDefend = False
        self.awake = False

class Adversary:
    def __init__(self, name, health, weapon, energy):
        self.name= name
        self.health = health
        self.maxHealth = health
        self.energy = energy
        self.maxEnergy = energy
        
        self.weapon = weapon
        self.power = weapon.power
        self.accuracy = weapon.accuracy
        self.efficiency = weapon.efficiency
        self.defending = weapon.defending
        
        self.isDefending = False
        self.willDefend = False

##fistsDesc = 'fists: Your bare fists'
##fists = Weapon('fists', 1, fistsDesc, 2, 10, 10, 3) #25
##
##swordDesc = 'sword: A typical steel sword'
##sword = Weapon('sword', 1, swordDesc, 4, 8, 7, 6) #25
##
##axeDesc = 'axe: A heavy double-bladed battle axe'
##axe = Weapon('axe', 1, axeDesc, 10, 5, 5, 5) #25
##
##hammerDesc = 'hammer: A long, two-handed steel war hammer'
##hammer = Weapon('hammer', 1, hammerDesc, 7, 7, 7, 4) #25
##
##clawsDesc = 'claws: The sharp claws of a goblin'
##
##oldswordDesc = 'oldsword: Old, rusty sword wielded by skeletons'
##
##clubDesc = 'club: a large club used by trolls'
##
##evilSwordDesc = 'evilSword: An ancient sword sporting a wicked blade. Wielded by the King of the Dead'
##
##rpgDesc = 'rpg: An rpg, like what you might find in Call of Duty'
##rpg = Weapon('rpg', 1, rpgDesc, 100, 10, 10, 1)


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.battleOver = False
        self.inp = ''
        random.seed()
        print(self.player.name,'enters into battle against the',self.enemy.name)

    def battlePrompt(self):
        self.inp = input('\nWill you "attack" or "defend"?: ')

    def printStatus(self):
        print(self.player.name,'health: ',self.player.health)
        print(self.player.name,'Energy: ',self.player.energy)
        print(self.enemy.name,'health: ',self.enemy.health)
        print(self.enemy.name,'Energy: ',self.enemy.energy)

    def commence(self):
        while self.battleOver == False:
            self.printStatus()
            self.battlePrompt()
            self.playerAction()
            self.enemyAction()
            self.checkStatus()
            if self.battleOver == True:
                if self.player.health == 0:
                    return False
                if self.enemy.health == 0:
                    return True
            
    def playerAction(self):
        if self.inp == 'attack':
            print('You attack the',self.enemy.name,'with your',self.player.weapon.name)
            dmg = self.generateDmg(self.player)
            if self.generateHit(self.player):
                print('Your attack lands')
                #print('damage dealt: ',dmg)
                self.updateHealth(self.enemy,dmg)
            else:
                print('Your attack misses')
            self.updateEnergy(self.player)

        elif self.inp == 'defend':
            print('You brace yourself for the',self.enemy.name, end = '')
            print("'s attack using your",self.player.weapon.name)
            self.player.isDefending = True
            self.updateEnergy(self.player)

##        elif self.inp == 'run':
##            print('You prepare to run from the battle')
##            self.battleOver = True

##        elif self.inp == 'win':
##            print('you win')
##            self.battleOver = True

        else:
            print('invalid entry')
            
    def enemyAction(self):
        if self.enemy.health > 0:
            if self.enemy.willDefend == False:
                if (self.enemy.energy/self.enemy.maxEnergy) <= 0.8: #enemy will block next turn to regain energy
                    self.enemy.willDefend = True
                    self.enemy.isDefending = True
                dmg = self.generateDmg(self.enemy)
                if self.generateHit(self.enemy):
                    print("The enemy's attack lands")
                    #print('enemy strike for',dmg,'damage')
                    self.updateHealth(self.player,dmg)
                else:
                    print("The enemy's attack misses")
            else:
                self.enemy.willDefend = False
            self.updateEnergy(self.enemy)
            if self.enemy.isDefending == True and self.enemy.willDefend == False:
                self.enemy.isDefending = False

    def generateDmg(self, entity):           
        pwr = entity.weapon.power
        enrg = entity.energy
        mxEnrg = entity.maxEnergy
        energyMod = (enrg/mxEnrg) * 0.4 + 0.6   #energyMod minimum of 0.6
        dmg = math.floor(pwr * energyMod * random.uniform(0.75,1.6))
        if dmg < 1: dmg = 1
        return dmg
    
    def generateHit(self, entity):
        acc = entity.weapon.accuracy
        x = random.uniform(0,10)
        if x > acc: return False
        else: return True

    def updateEnergy(self, entity):
        enrg = entity.energy
        mxEnrg = entity.maxEnergy
        
        if entity.isDefending == True and entity.willDefend == False:
            entity.energy += 5
            print(entity.name,'regains some energy from defending')
        else:
            eff = entity.weapon.efficiency
            nrg = math.ceil((7-.75*eff) * random.uniform(0.9,1.1))
            if nrg < 1: nrg = 1
            print(entity.name,'energy used: ',nrg)
            entity.energy -= nrg

        if entity.energy < 0: entity.energy = 0
        if entity.energy > entity.maxEnergy: entity.energy = entity.maxEnergy
            
    def updateHealth(self, entity, dmg):
        print('The attack is for',dmg,'damage')
        if entity.isDefending:
            dfnmod = (1.25 - (0.1 * entity.weapon.defending)) * random.uniform(0.9, 1.1)
            dmg = math.floor(dmg * dfnmod)
            print(entity.name,'defends, taking', dmg, 'damage')
            #print('defend mod: ',dfnmod)
            #print('By defending yourself, you only took',dmg,'damage and regained 3 energy')
        entity.health -= dmg
        
        if entity.health < 0: entity.health = 0

    def checkStatus(self):
        if self.player.health == 0:
            print('You died.')
            self.battleOver = True
        if self.enemy.health == 0:
            print('The',self.enemy.name,'died. You win')
            self.battleOver = True
        if self.player.isDefending:
            self.player.isDefending = False

#Weapons
fistsDesc = 'fists: Your bare fists. Quick and manueverable, but lacking in power and defense'
swordDesc = 'sword: A typical steel sword. Easy to wield and to defend with, while still able to deal decent damage'
axeDesc = 'axe: A heavy double-bladed battle axe. Able to deal massive damage, but its size makes it hard to wield'
hammerDesc = 'hammer: A long, two-handed steel war hammer. Its power and wieldability make it a formidable weapon, but it does not lend itself well to defense'

clawsDesc = 'claws: The sharp claws of a goblin'
oldswordDesc = 'oldsword: Old, rusty sword wielded by skeletons'
clubDesc = 'club: a large club used by trolls'

rpgDesc = 'rpg: An rpg, like what you might find in Call of Duty. Just aim and pull the trigger, and your enemies will cease to exist'

fists = Weapon('fists', 1, fistsDesc, True, True, 2, 10, 10, 3) #25
sword = Weapon('sword', 9, swordDesc, True, True, 4, 8, 7, 6) #25
axe = Weapon('axe', 9, axeDesc, True, True, 10, 5, 5, 5) #25
hammer = Weapon('hammer', 9, hammerDesc, True, True, 7, 7, 7, 4) #25

claws = Weapon('claws', 12, clawsDesc, True, True, 3, 8, 8, 2)
oldsword = Weapon('oldsword', 11, oldswordDesc, True, True, 5, 6, 5, 4)
club = Weapon('club', 10, clubDesc, True, True, 7, 5, 4, 3)

rpg = Weapon('rpg', 1, rpgDesc, True, True, 100, 10, 10, 1)

#Enemies
goblin = Enemy('goblin', 20, claws, 20)
skeleton = Enemy('skeleton', 20, oldsword, 15)
troll = Enemy('troll', 25, club, 15)
        
##y = 0
##while y == 0:
##    for x in range(0,10):
##        print(math.ceil((7-0.75*x)*random.uniform(0.9,1.1)))
##    y = int(input('continue?: '))
    

##player = Adversary('steve', 1, fists, 20)
##goblin = Adversary('goblin', 100, axe, 20)
##battle = Battle(player, goblin)
##battle.commence()
