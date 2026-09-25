import random
from enemy import Enemy

class Boss(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, health=200, attackPower=15)
        self.gold = 0
    def attack(self):
        attackstyle = random.randint(1,2)
        if attackstyle==1:
            print("SUPLEX!!")
            return 5 * random.randint(1,4)
        else:
            print("PIERCING GAZE OF BLUE STEEL!!!")
            return self.attack_power() * random.randint(1,2)
    def takeSword(self, Hero):
        """BOSS GOBBOS TAKIN SWOOOORD"""
        self.attack_power= self.attack_power + Hero.attack_power
        Hero.attack_power=0
        print("GIT REKT NOOBIE")

    def take_damage(self, damage):
        damage= damage * .75
        super().take_damage(damage)