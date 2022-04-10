import os
from data import rooms


def run_game():
    show_instructions()
    inventory = []
    current_room = 'Field'
    while True:
        show_room_info(current_room) # output current room info to console
        room_info = rooms[current_room]
        move = ''
        
        while move == '': # keep prompting for move while its empty
            move = input('>')
            
        if move == 'instructions': # user enters instructions
            show_instructions()
            continue
        
        move_tokens = move.lower().split(" ", 1)
        
        if len(move_tokens) < 0:
            print("Invalid command")
            continue;
        
        command = move_tokens[0]
        detail = move_tokens[1]
        
        if command == 'go':
            if detail != 'items' and detail in room_info:
                current_room = room_info[detail]
            else:
                print(f"You can't go {detail}\n")
        elif command == 'get':
            if 'items' in room_info and detail in room_info['items']:
                inventory.append(detail)
                room_info['items'].remove(detail)
    
def show_instructions():
    print("Commands: go [direction], get [item], instructions\n")

def show_room_info(current_room):
    clear()
    room_info = rooms[current_room]
    print(f"You are currently in the {current_room}\n")
    if 'items' in room_info:
        print("Items: ")
        for item in room_info['items']:
            print(item + ', ')
    print()

def clear():
    os.system('clear')