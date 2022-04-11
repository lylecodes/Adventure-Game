import os
from util import bcolors as color
from data import rooms


def run_game():
    show_instructions()
    inventory = []
    current_room = 'Field'
    
    while True:
        room_info = rooms[current_room]
        show_room_info(room_info, current_room) # output current room info to console
        
        move = ''
        
        while move == '': # keep prompting for move while its empty
            move = input('>')
            
        if move == 'instructions': # user enters instructions
            show_instructions()
            continue
        elif move == 'directions':
            show_directions(room_info)
            continue
        elif move == 'inventory':
            show_inventory(inventory)
            continue
        
        move_tokens = move.lower().split(" ", 1)
        
        if len(move_tokens) < 0: # number of commands cannot be 1 beyond this point
            print("Invalid command")
            continue;
        
        command = move_tokens[0]
        detail = move_tokens[1]
        
        if command == 'go':
            if detail != 'items' and 'directions' in room_info and detail in room_info['directions']:
                current_room = room_info['directions'][detail]
            else:
                print(f"You can't go {detail}\n")
        elif command == 'get':
            if 'items' in room_info and detail in room_info['items']:
                inventory.append(detail)
                room_info['items'].remove(detail)
        elif command == 'search':
            if 'searchables' in room_info and detail in room_info['searchables']:
                for item in room_info['searchables'][detail]:
                    inventory.append(item)
                del room_info['searchables']
                print("Items added to inventory\n")
            else:
                print("You cannot search that\n")
        elif command == 'attack':
            if 'npcs' in room_info and len(room_info['npcs']) > 0:
                npc_names = get_npc_names(room_info['npcs'])
                if detail.title() in npc_names:
                    if attack_successful(inventory, detail):
                        remove_npc(room_info['npcs'], detail.title())
                        print(f'{color.FAIL}{detail.title()} has died{color.ENDC}\n')
                    else:
                        print(f"{color.WARNING}Your weapon is not strong enough{color.ENDC}\n")
                else:
                    print(f'You cannot attack {detail}\n')
            else:
                print('There is nobody to attack')

def show_instructions():
    print("Commands:\ngo [direction]\nget [item]\nsearch [searchable]\nattack [npc]\ndirections\ninstructions\n")

def show_room_info(room_info, current_room):
    clear()
    print(f"You are currently in the {current_room}")
    
    if 'description' in room_info:
        print(room_info['description'] + "\n")
        
    if 'items' in room_info and len(room_info['items']) > 0:
        print("Items seen: " + ", ".join(room_info['items']) + "\n")
        
    if 'npcs' in room_info and len(room_info['npcs']) > 0:
        npc_names = get_npc_names(room_info['npcs'])
        print("You see a " + ", ".join(npc_names) + "\n")

def show_inventory(inventory):
    if len(inventory) > 0:
        print("Inventory: " + ", ".join(inventory) + "\n")
    else:
        print("Your inventory is empty.\n")

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

def remove_npc(npc_list, npc_name):
    for npc in npc_list:
        if npc.type.name.title() == npc_name:
            npc_list.remove(npc);
            break;
        else:
            print("Npc could not be removed")
