from game import run_game
from characters import create_character

def main():
    character = create_character()
    run_game(character)

if __name__ == '__main__':
    main()