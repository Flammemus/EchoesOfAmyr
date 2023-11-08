import random
import time
# import json
from ascii_magic import AsciiArt
from ClassesTbrpg import *
from JsonCode import *

skitterCrab = Enemy("Skitter Crab", hp=25, maxHp=25, damage=5, marks=1, xp=4)
drenchscaleSerpent = Enemy("Drenchscale Serpent", hp=50, maxHp=50, damage=7, marks=2, xp=6)
naridianSiren = Enemy("Naridian Siren", hp=50, maxHp=50, damage=9, marks=2, xp=6)
eldertideLeviathan = Enemy("Eldertide Leviathan", hp=120, maxHp=120, damage=10, marks=6, xp=15)

shamblingUndead = Enemy("Shambling Undead", hp=80, maxHp=80, damage=10, marks=4, xp=9)

windlassShore = Areas("Windlass Shore", safehaven=False, order=1, enemies=[skitterCrab, drenchscaleSerpent, naridianSiren, eldertideLeviathan])
firwoodRetreat = Areas("Firwood Retreat", safehaven=True, order=2, enemies=[])
eldVintasRuins = Areas("Eld Vintas Ruins", safehaven=False, order=3, enemies=[shamblingUndead])

player = Player("TesterGuy", hp=10, maxHp=1000, damage=15, defense=1, eqWeapon="fists", eqArmor="rags", marks=10000, areaName=windlassShore.name, playerClass="Wretched", level=1, xp=0, maxXp=50, skillPoints=0, strength=5, agility=5, willpower=5, hasHorse=True, hasBeenInFirwoodRetreat=True, hasBeenInAncientLibrary=True)
player.chosenClass("Warrior")

steelDagger = Weapons("Steel Dagger", damage=15, cost=40)
mastercraftedSteelDagger = Weapons("Mastercrafted Steel Dagger", damage=20, cost=80)

steelLongsword = Weapons("Steel Longsword", damage=15, cost=40)
mastercraftedSteelLongsword = Weapons("Mastercrafted Steel Longsword", damage=20, cost=80)

oakStaff = Weapons("Oak Staff", damage=15, cost=40)
pineStaff = Weapons("Pine Staff", damage=20, cost=80)

leatherSet = Armor("Leather Wear", defense=5, strength=3, agility=3, willpower=1, cost=50)

lesserHealingPotion = Potion("Lesser Healing Potion", healing=60, cost=1)

def startGame():
    print("")
    print()
    print("@*==========================================*@")
    print("| %%%%%%%%%%%%% Echoes of Amyr %%%%%%%%%%%%% |")
    print("@*==========================================*@"), print()
    print('"new" to create a new character'), print()
    print('"load" (character name) to load that character')
    
    global player


startGame()

gameLoop = True
while gameLoop:

    def battle(enemy):
        enemy.prepare()

        battleGoing = False

        print("@*======================= Foe Info =======================*@"), print()

        Enemy.showImage(enemy)

        print(), print(f"!!! You encountered a {enemy.name} !!!"), print()

        print(f"{enemy.name} stats:"), print()
        print(f" * {enemy.hp} / {enemy.maxHp} Hp")
        print(f" * {enemy.damage} Dmg")
        print()
        print("Your stats:"), print()
        print(f" * {player.hp} / {player.maxHp} Hp")
        print(f" * {player.damage} dmg"), print()
        print("@*======================*@"), print()

        while battleGoing == False:

            action = input('"sneak off" / "confront"?: ')
            print()
        
            if action == "sneak off":
                print("You successfully sneak away from the foe")
                break

            elif action == "confront":
                battleGoing = True
                print()
                print("@*=====================*@")
                print("| %%%% Battle Info %%%% |")
                print("@*=====================*@")

        while battleGoing:

            print()
            print(f"{enemy.name} {enemy.hp} / {enemy.maxHp}")
            print(f"{player.name} {player.hp} / {player.maxHp}")

            dmgDealtToEnemy = player.attackEnemy(enemy)

            if enemy.hp < 1:

                print()
                print(f"{enemy.name} 0 / {enemy.maxHp}")
                print(player.name, player.hp, "/", player.maxHp)

                print(), print("@*=====================*@"), print()
                print(f"!!! {enemy.name} defeated !!!"), print()
                print(f"You took {enemy.marks} gold marks from the lifeless body of the {enemy.name}")
                print(f"You gained {enemy.xp} / {player.maxXp} xp")
                print()
                print(f"Your hp: {player.hp} / {player.maxHp}")
                player.marks += enemy.marks
                player.xp += enemy.xp

                lvlProcess = True
                while lvlProcess:

                    if player.xp >= player.maxXp:
                        player.level += 1
                        player.xp -= player.maxXp
                        player.maxXp += int(player.level * 33)
                        player.skillPoints += 1

                        print("@*==============================================================================================*@")
                        print("| %%%%% You feel yourself ascendeding to new heights as you level up, gaining a skill point %%%% |")
                        print("@*==============================================================================================*@"), print()

                    if player.xp < player.maxXp:
                        lvlProcess = False


                saveGame(player)
                break

            if player.hp < 1:
                print("You stagger as you feel like prey, barely escaping the grip of death himself as you sprint"), print()
                print("You lost", int(player.marks) / 2, "gold marks in the process")
                player.marks = player.marks / 2

                break

            dmgDealtToPlayer = enemy.attackPlayer(player)

            time.sleep(0.1)

    print("")
    action = input()
    print("")

    if action == "hunt":

        if player.hp > 0:
            if player.areaName == "Windlass Shore":
                battle(random.choice(windlassShore.enemies))

            elif player.areaName == "Firwood Retreat":
                if firwoodRetreat.safehaven == True:
                    print("You should not draw attention to yourself")
            
            elif player.areaName == "Eld Vintas Ruins":
                battle(random.choice(eldVintasRuins.enemies))
        
        else:
            print("Your essence bears wounds, weary traveler. Heed the whispers of nature's boons, and let solace mend your spirit for safety")

    if action == "commands":
        showCommands()
    
    if action == "heal":

        if player.hp < (player.maxHp - lesserHealingPotion.healing):
            player.hp += lesserHealingPotion.healing
        else:
            player.hp = player.maxHp

        print("Used a potion, you have", player.hp, "/", player.maxHp, "hp")

    if action == "stats":
        player.showStats()

    if action.startswith("travel "):
        area_name = action[7:]

        if area_name in Areas.areasList and area_name != player.areaName:

            if player.hasHorse == True:
                player.areaName = area_name
                print(f"You skillfully guide your horse through the rugged tarrain, arriving at {player.areaName}")

            elif player.hasHorse == False:

                if area_name == "Firwood Retreat" or area_name == "Windlass Shore":
                    player.areaName = area_name
                    print("As you walk, Firwood Retreat emerges on the horizon")

                    player.hasHorse = True
                
                else:
                    print("You don't have a horse to your name")
        
        elif area_name not in Areas.areasList:
            print("That place doesn't exist")

        else:
            print("You find yourself already there")


                
    if action == "map":

        for i in Areas.areasList:
            print(i)

    if action == "look around" and player.areaName != "Firwood Retreat":
        print("You should't meddle around, as hostile enemies fills your horizon")

    if player.areaName == "Firwood Retreat":

        if action == "look around":

            if not player.hasBeenInFirwoodRetreat:
                firwoodRetreatIntroDialog()
                print("heiei")
                player.hasBeenInFirwoodRetreat = True

            if player.hasBeenInFirwoodRetreat:
                print("You look around and see the following points of interest:")
                print()
                print(" * Ancient Library")
                print(" * Firwood Forge")
                print(" * Shaman Hut")

        if action.startswith("enter "):
            location = action[6:]

            if location == "Ancient Library":
                inAncientLibrary = True
                while inAncientLibrary:

                    if player.hasBeenInAncientLibrary:
                        print("You return to the ancient library as heavy dark wooden doors close behing you.")
                        print("Familiar librarians greet you with welcoming smiles and nods.")

                        print()
                        actionAncientLibrary = input("Library action: ")
                        print()

                        if actionAncientLibrary == "look around":
                            print("Books fill your horizon.")
                            print("With nothing to do, you take a deep breath, and leave to where you came from")
                            inAncientLibrary = False

                        if actionAncientLibrary == "leave":
                            print("You take a deep breath, and leave to where you came from")
                            inAncientLibrary = False

                    if not player.hasBeenInAncientLibrary:
                        ancientLibraryIntroDialog()

                        while True:

                            if player.playerClass == "Wretched":

                                print()
                                actionChooseClass = input("Choose whose history to delve deeper in: ")
                                print()

                                if actionChooseClass == "Elandor":
                                    player.chosenClass("Magician")

                                elif actionChooseClass == "Thaelen":
                                    player.chosenClass("Warrior")

                                elif actionChooseClass == "Seraph":
                                    player.chosenClass("Theif")

                            if player.playerClass != "Wretched":
                                False

                                print(f"As you embrace the path of the {player.playerClass}, the ancient scrolls unveil the mastery, history,\nand extraordinary feats of your chosen discipline.")
                                print()
                                print(f"@*=== {player.name} the {player.playerClass} ===*@")

                                inAncientLibrary = False
                                player.hasBeenInAncientLibrary = True

                                break

            else:
                print("Place does not exist")



# JSON CODE #

    if action == "characters":
        print("Saved characters:"), print()
        with open(player_data_file, 'r') as file:
            for line in file:
                saved_player = json.load(line)
                print(" ", saved_player['name'])

    if action == "save":
        saveGame(player)
        print("Player data saved successfully!")

    if action.startswith("load "):
        player_name_to_load = action[5:]
        saved_player = load_player(player_name_to_load)
        if(saved_player != 0):
            player.name = saved_player['name']
            player.hp = saved_player['hp']
            player.maxHp = saved_player['maxHp']
            player.damage = saved_player['damage']
            player.defense = saved_player['defense']
            player.marks = saved_player['marks']
            player.playerClass = saved_player['playerClass']
            player.level = saved_player['level']
            player.xp = saved_player['xp']
            player.maxXp = saved_player['maxXp']
            player.areaName = saved_player['areaName']
            player.skillPoints = saved_player['skillPoints']
            player.strength = saved_player['strenght']
            player.agility = saved_player['agility']
            player.willpower = saved_player['willpower']
    if action.startswith("delete "):
        character_name_to_delete = action[7:]
        deleted = delete_character(character_name_to_delete)
        if deleted:
            print(f"Character '{character_name_to_delete}' deleted successfully")
        else:
            print(f"No character found with the name '{character_name_to_delete}'")

    if action == "new":
        player = createNewCharacter(windlassShore)