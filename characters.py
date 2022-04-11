import enum

class Character(object):
    def __init__(self, title, health, atk_dmg):
        self.title = title
        self.health = health
        self.atk_dmg = atk_dmg

    def get_name(self):
        return self.title
    
    def attack(self):
        return self.atk_dmg
    
    def take_damage(self, damage):
        self.health - damage
        
    def is_dead(self):
        return self.health <= 0

class NPC_Types(enum.Enum):
    MONSTER = 1
    HUMAN = 2

class NPC(Character):
    def __init__(self, title, health, atk_dmg, type):
        super().__init__(title, health, atk_dmg)
        self.type = type


cellar_monster = NPC("Cellar Boi", 100, 50, NPC_Types.MONSTER)