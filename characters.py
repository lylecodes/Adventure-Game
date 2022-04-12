import enum

class Character(object):
    def __init__(self, title, health=100, atk_dmg=20):
        self.title = title
        self.health = health
        self.atk_dmg = atk_dmg
        self.inventory = []
        self.equipped_weapon = None

    def get_title(self):
        return self.title
    
    def get_hp(self):
        return self.health
    
    def get_inventory(self):
        return self.inventory
    
    def add_items_to_inventory(self, items):
        for item in items:
            self.inventory.append(item)
    
    def get_atk_dmg(self):
        return self.atk_dmg
    
    def take_damage(self, damage):
        self.health -= damage
        
    def is_dead(self):
        return self.health <= 0

class NPC_Types(enum.Enum):
    MONSTER = 1
    HUMAN = 2

class NPC(Character):
    def __init__(self, title, health, atk_dmg, type):
        super().__init__(title, health, atk_dmg)
        self.type = type
    
    def get_type(self):
        return self.type.name.title()


cellar_monster = NPC("Cellar Boi", 100, 50, NPC_Types.MONSTER)

# print(cellar_monster.get_type())

def create_character():
    name = input("Enter your character's name:\n>")
    return Character(title=name)