from ascii_magic import AsciiArt

class Player:
    def __init__(self, name, hp, maxHp, dmg, eqWeapon, eqArmor, defense, marks, areaName, playerClass, level, xp, maxXp, skillPoints, strength, agility, will, hasHorse, hasBeenInFirwoodRetreat, hasBeenInAncientLibrary):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.dmg = dmg
        self.eqWeapon = eqWeapon
        self.eqArmor = eqArmor
        self.defense = defense
        self.marks = marks
        self.areaName = areaName
        self.playerClass = playerClass
        self.level = level
        self.xp = xp
        self.maxXp = maxXp
        self.skillPoints = skillPoints
        self.strength = strength
        self.agility = agility
        self.will = will
        self.hasHorse = hasHorse
        self.hasBeenInFirwoodRetreat = hasBeenInFirwoodRetreat
        self.hasBeenInAncientLibrary = hasBeenInAncientLibrary

    def chosenClass(self, newClass):
        self.playerClass = newClass

        if self.playerClass == "Wretched":
            self.hp = 100
            self.maxHp = 100

        if self.playerClass == "Thief":
            self.hp = 80
            self.maxHp = 80
        
        if self.playerClass == "Warrior":
            self.hp = 115
            self.maxHp = 115

        if self.playerClass == "Magician":
            self.hp = 70
            self.maxHp = 70
    
    def showStats(self):

        print("@*===", self.name, "the", self.playerClass, "===*@")
        print()
        print("You are currently located in", self.areaName)
        print()
        print("You have:")
        print()
        print(f" * {self.marks} gold marks")
        print(f" * infinite health potions")
        print()
        print(self.hp, "/", self.maxHp, "Hp")
        print()
        print(f"Damage: {self.dmg}")
        print(f"Defense: {self.defense}")
        print()
        print(f"Level: {self.level}")
        print("Xp:", self.xp, "/", self.maxXp)
        print(f"Available skill points: {self.skillPoints}")
        print()
        print(f"Strenght: {self.strength}")
        print(f"Agility: {self.agility}")
        print(f"Willpower: {self.will}")

    def attackEnemy(self, enemy):
        dmgDealtToEnemy = self.dmg
        enemy.hp -= dmgDealtToEnemy
        return dmgDealtToEnemy
    
    
class Areas:
    areasList = []
    def __init__(self, name: str, safehaven: bool, order: int, enemies: list):
        self.name = name
        self.safehaven = safehaven
        self.order = order
        self.enemies = enemies

        Areas.areasList.append(self.name)

class Enemy:
    enemyList = []
    def __init__(self, name, hp, maxHp, dmg, marks, xp):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.dmg = dmg
        self.marks = marks
        self.xp = xp

        Enemy.enemyList.append(self)

    def attackPlayer(self, player):
        dmgDealtToPlayer = self.dmg
        player.hp -= dmgDealtToPlayer
        return dmgDealtToPlayer
    
    def gethp(self):
        return self.hp
    
    def sethp(self):
        self.hp = self.maxHp

    def prepare(self):
        if self.gethp() < 1:
            self.sethp()

    def showImage(self):
        if self.name == "Skitter Crab": 
            skitterCrabImg = AsciiArt.from_image('Images/skitterCrab.png')
            skitterCrabImg.to_terminal(columns=60)

        if self.name == "Eldertide Leviathan":
            eldertideLeviathanImg = AsciiArt.from_image('Images/eldertideLeviathan.png')
            eldertideLeviathanImg.to_terminal(columns=60)

        if self.name == "Drenchscale Serpent":
            drenchscaleSerpentImg = AsciiArt.from_image('Images/drenchscaleSerpent.png')
            drenchscaleSerpentImg.to_terminal(columns=60)
        
        if self.name == "Naridian Siren":
            naridianSirenImg = AsciiArt.from_image('Images/naridianSiren.png')
            naridianSirenImg.to_terminal(columns=60)

        if self.name == "Shambling Undead":
            shamblingUndeadImg = AsciiArt.from_image('Images/shamblingUndead.png')
            shamblingUndeadImg.to_terminal(columns=60)

            

class Weapons:
    def __init__(self, name, dmgBonus, cost):
        self.name = name
        self.dmg_bonus = dmgBonus
        self.cost = cost

class Armor:
    def __init__(self, name, defBonus, strBonus, agiBonus, willBonus, cost):
        self.name = name
        self.def_bonus = defBonus
        self.strBonus = strBonus
        self.agiBonus = agiBonus
        self.willBonus = willBonus
        self.cost = cost

class Potion:
    def __init__(self, name, healingValue, cost):
        self.name = name
        self.healingValue = healingValue
        self.cost = cost

def showCommands():
    print("@*=== commands ===*@"), print()
    print("hunt              - Discover a menacing presence, ready to battle")
    print("heal              - Rejuvenate with your healing potion's magic")
    print("stats             - Review your character's details")
    print("map               - Explore your local map in detail")
    print("travel (location) - Eplore the marked location on your map")
    print("look around       - Explore the surroundings in the city")
    print("enter (location)  - Enter desired building or place in your current area")
    print("commands          - Discover more actions on the logbook's reverse")
    print()
    print("characters              - View all saved characters")
    print("save                    - Save your current progress")
    print("load (character name)   - Load that specific character")
    print("delete (character name) - Delete that character from the save file")

def introDialog():
    print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
    print("=======================================================================================================")
    print()
    print("As the tempestuous waves tossed Eolh's Call, a ship renowned for its voyages into uncharted waters.")
    print("You clung to a piece of the wreckage, fighting against the relentless sea.")
    print("The ship, once a beacon of hope, now shattered against the unforgiving rocks.")
    print("Desperately, you kicked and swam, your strength waning as the cold sea gnawed at your resolve.")
    print("And then, through the tumult, your fingers grazed the gritty, comforting touch of land—Windlass Shores.")
    print()
    print("=======================================================================================================")
    print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
    print()

def introCommands():
    print("As you wash ashore upon the enigmatic Windlass Shores,")
    print("amidst the remnants of the ill-fated ship, you stumble upon an ancient logbook,")
    print("whispering secrets of a world unknown.")
    print("A mere vessel, you now hold the key to your destiny.")

    print("")

    print('hunt', "    - Discover a menacing presence, ready to battle")
    print('heal', "    - Rejuvenate with your healing potion's magic")
    print('stats', "   - Review your character's details")
    print()
    print('commands', "- Discover more actions on the logbook's reverse")

def choosingOfClass():
    print("As you arrive at the ancient library, you're welcomed by the librarians.\nThey sense your potential and offer guidance.\nThree paths unfold, and you must decide your calling.\nWill you become a formidable Warrior, a cunning Thief, or a masterful Magician?")

def firwoodRetreatIntroDialog():
    print("You enter Firwood Retreat, a tranquil village within a dense forest.")
    print("In the village's heart lies the Ancient Library, an imposing structure surrounded by towering trees.")
    print("Inside, you can explore a vast collection of knowledge and choose your class, shaping your unique path.")
    print("To the east stands the Firwood Forge, a bustling blacksmith's shop, and to the west, you find the Shaman's Hut, where a mystical aura fills the air.")
    print()

def ancientLibraryIntroDialog():
    print("Stepping into the Ancient Library, a hushed realm of boundless knowledge awaits.")
    print("Three towering statues of revered masters, carved from stone, guard the entrance.")
    print("Each master commands their own domain within these hallowed halls.")
    print("To the left, the statue of Elandor Stormweaver, the Grand Wizard, beckons with shelves of arcane tomes.")
    print("On the right, Thaelen Ironclad, the Grand Warrior, stands watch over an armory of legendary texts.")
    print("In the center, Seraphina Shadowsong, the Grand Thief, presides over secrets hidden within volumes of intrigue.")
    print("Your journey in wisdom and adventure begins here, among these guardians of lore.")
    print()
    print("You look around and see the following points of interest:")
    print()
    print(" * Elandor Stormweaver the Grand Wizard")
    print(" * Thaelen Ironclad the Mighty Warrior")
    print(" * Seraph Song the Invisible Theif")
    print()
    print("Choose whose history to delve deeper in, adventurer")
    print()
    print('"Elandor / Thaelen / Seraph"')
