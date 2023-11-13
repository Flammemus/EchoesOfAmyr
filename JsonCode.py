from ClassesTbrpg import *
import os
import json

player_data_file = "player_data.json"

def save_player_data(player_data):
    # Read existing data from the file
    existing_data = []
    if os.path.exists(player_data_file):
        with open(player_data_file, 'r') as file:
            existing_data = json.load(file)

    # Check if the player already exists and update the data
    player_exists = False
    for saved_player in existing_data:
        if saved_player['name'] == player_data['name']:
            saved_player.update(player_data)
            player_exists = True
            break

    # If the player doesn't exist, add the data to the existing data
    if not player_exists:
        existing_data.append(player_data)

    # Write all the data back to the file
    with open(player_data_file, 'w') as file:
        json.dump(existing_data, file)

def load_player(player_name):
    with open(player_data_file, 'r') as file:
        lines = json.load(file)
        for line in lines:

            if line['name'] == player_name:
                saved_player = line
                print(f"Player data for {player_name} loaded successfully!")

                return saved_player

        print(f"No saved data found for {player_name}.")
        return 0

def saveGame(player):
    player_data = {
        'name': player.name,
        'hp': player.hp,
        'maxHp': player.maxHp,
        'damage': player.damage,
        'defense': player.defense,
        'marks': player.marks,
        'areaName': player.areaName,
        'playerClass': player.playerClass,
        'level': player.level,
        'xp': player.xp,
        'maxXp': player.maxXp,
        'skillPoints': player.skillPoints,
        'strength': player.strength,
        'agility': player.agility,
        'willpower': player.willpower
    }
    save_player_data(player_data)

def delete_character(character_name):
    with open(player_data_file, 'r') as file:
        # lines = file.readlines()
        lines = json.load(file)

    deleted = False
    with open(player_data_file, 'w') as file:
        for line in lines:
            # saved_player = json.loads(line)
            if line['name'] == character_name:
                deleted = True
                lines.remove(line)
            # else:
                # json.dump(saved_player, file)
                # file.write('\n')
        json.dump(lines,file)



    return deleted
    

def createNewCharacter():
    while True:

            introDialog()

            player_name = input("Do you remember your name, adventurer?: ")

            with open(player_data_file) as file:
                existing_data = json.load(file)
                for line in existing_data:
                    # saved_player = json.loads(line)
                    if line['name'] == player_name:
                        print(), print("This name is already taken. Please choose a different name"), print()
                        break
                    
                else:
                    print()
                    introCommands()
                    player = Player(player_name, hp=100, maxHp=100, damage=15, defense=0, eqWeapon="fists", eqArmor="rags", marks=4, areaName="Windlass Shore", playerClass="Wretched", level=1, xp=0, maxXp=50, skillPoints=0, strength=5, agility=5, willpower=5, hasHorse=False, hasBeenInFirwoodRetreat=False, hasBeenInAncientLibrary=False)
                    return player