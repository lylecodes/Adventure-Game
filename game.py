import os
from util import bcolors as color
from data import rooms
from items import Weapon


def run_game(mc):
    clear()
    show_instructions()
    current_room = 'Field'
    
    while True:
        room_info = rooms[current_room]
        show_room_info(room_info, current_room) # output current room info to console
        
        move = ''
        
        while move == '': # keep prompting for move while its empty
            move = input('>')
            
        clear()
        
        if move == 'instructions': # user enters instructions
            show_instructions()
            continue
        elif move == 'directions':
            show_directions(room_info)
            continue
        elif move == 'inventory':
            inventory = mc.get_inventory()
            item_names = get_item_names(inventory)
            if len(inventory) > 0:
                print("Inventory: " + ", ".join(item_names) + "\n")
            else:
                print("Inventory is empty\n")
            continue
        
        move_tokens = move.lower().split(" ", 1)
        
        if len(move_tokens) <= 1: # number of commands cannot be 1 beyond this point
            print("Invalid command\n")
            continue;
        
        command = move_tokens[0]
        detail = move_tokens[1]
        
        if command == 'go':
            if detail != 'items' and 'directions' in room_info and detail in room_info['directions']:
                current_room = room_info['directions'][detail]
            else:
                print(f"You can't go {detail}\n")
        elif command == 'get':
            if 'items' in room_info:
                raw_item = get_item_and_update_room(room_info['items'], detail.title())
                if raw_item is not None:
                    mc.add_items_to_inventory([raw_item])
                    print(f"{raw_item.get_name()} added to inventory\n")
                else:
                    print("No such item")
            else:
                print("This room contains no items")
        elif command == 'search':
            if 'searchables' in room_info and detail in room_info['searchables']:
                items_to_add = []
                for item in room_info['searchables'][detail]:
                    items_to_add.append(item)
                mc.add_items_to_inventory(items_to_add)
                del room_info['searchables']
                print("Items added to inventory\n")
            else:
                print("You cannot search that\n")
        elif command == 'attack':
            weapons = get_weapons_from_inventory(mc.get_inventory())
            if len(weapons) <= 0:
                print("You don't have any weapons!\n")
                continue
            if 'npcs' in room_info and len(room_info['npcs']) > 0:
                npc_names = get_npc_names(room_info['npcs'])
                if detail.title() in npc_names:
                    npc = get_npc_from_name(room_info['npcs'], detail.title())
                    mc_won = battle(mc, npc)
                    clear()
                    if mc_won:
                    # if attack_successful(inventory, detail):
                        remove_npc(room_info['npcs'], detail.title())
                        print(f'\n{color.FAIL}{detail.title()} has died{color.ENDC}\n')
                    else:
                        print(f"{color.FAIL}You have died{color.ENDC}\n")
                    input("Press enter to continue")
                    clear()
                else:
                    print(f'You cannot attack {detail}\n')
            else:
                print('There is nobody to attack')

def show_instructions():
    print("Commands:\ngo [direction]\nget [item]\nsearch [searchable]\nattack [npc]\ndirections\ninstructions\n")

def show_room_info(room_info, current_room):
    print(f"You are currently in the {current_room}")
    
    if 'description' in room_info:
        print(room_info['description'] + "\n")
        
    if 'items' in room_info and len(room_info['items']) > 0:
        item_names = []
        for item in room_info['items']:
            item_names.append(item.get_name())
        print("Items seen: " + ", ".join(item_names) + "\n")
        
    if 'npcs' in room_info and len(room_info['npcs']) > 0:
        npc_names = get_npc_names(room_info['npcs'])
        print("You see a " + ", ".join(npc_names) + "\n")


def show_directions(room_info):
        if 'directions' in room_info:
            directions = []
            for key, value in room_info['directions'].items():
                directions.append(key.title() + "-> " + value + "\n");
            print("Directions:\n" + "".join(directions))

def clear():
    os.system('clear')
    
def attack_successful(inventory, npc):
    if npc == 'monster' and 'broken blade' in inventory:
        return True
    return False

def get_npc_names(npc_list):
    npc_names = []
    for npc in npc_list:
        npc_names.append(npc.type.name.title())
    return npc_names

def get_npc_from_name(npc_list, npc_name):
    for npc in npc_list:
        if npc.get_type() == npc_name:
            return npc
    return None

def get_item_names(items_list):
    item_names = []
    for item in items_list:
        item_names.append(item.get_name())
    return item_names

def remove_npc(npc_list, npc_name):
    for npc in npc_list:
        if npc.type.name.title() == npc_name:
            npc_list.remove(npc);
            break;
        else:
            print("Npc could not be removed")

def get_item_and_update_room(items_list, item_name_to_remove):
    for item in items_list:
        if item.get_name() == item_name_to_remove:
            items_list.remove(item)
            return item
    return None

def battle(mc, npc):
    rounds = 0
    mc_dealt = 0
    npc_dealt = 0
    
    while True:
        clear()
        if rounds == 0:
            print(f"You are now battling {npc.get_type()}\n")
        print(f"Your health={mc.get_hp()} | Enemy health={npc.get_hp()}\n")
        print("Choose a weapon to attack with:")
        inventory = mc.get_inventory()
        weapons = get_weapons_from_inventory(inventory)
        
        for idx, weapon in enumerate(weapons):
            print(f"[{idx}] {weapon.get_name()} -> +{weapon.get_damage()} damage")
        print()
        
        choice = ""
        while choice == "":
            choice = input(">")
        
        clear()
        atk_wpn = weapons[int(choice)]
        mc_total_dmg = (atk_wpn.get_damage() + mc.get_atk_dmg())
        mc_dealt = mc_total_dmg
        npc.take_damage(mc_total_dmg)
        rounds += 1
        
        if npc.is_dead():
            return True
        elif mc.is_dead():
            return False
        
        npc_dealt = npc.get_atk_dmg()
        mc.take_damage(npc_dealt)
        
        if npc.is_dead():
            return True
        elif mc.is_dead():
            return False
        
        print(f"\nYou dealt {mc_dealt} damage | Your opponent dealt {npc_dealt} damage\n")
        input("Press enter to continue:\n>")
        
def get_weapons_from_inventory(inventory):
    weapons = []
    for item in inventory:
        if type(item) == Weapon:
            weapons.append(item)
    return weapons