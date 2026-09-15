import random
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 120
        self.attack_power = 20
        self.armor = 1
    def attack(self):
        return random.randint(1, self.attack_power)
    def take_damage(self, damage):
        if damage < 5:
            print(self.name + " Dodges!")
            return 
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0
            
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
    def is_alive(self):
            return self.health > 0
    pass
