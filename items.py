class Weapon:
    def __init__(self, name, atk_dmg):
        self.name = name
        self.atk_dmg = atk_dmg
        
    def get_name(self):
        return self.name
    
    def get_damage(self):
        return self.atk_dmg

broken_tractor_blade = Weapon("Tractor Blade", 50)
big_stick = Weapon("Big Stick", 15)