import random
from enemy import Enemy

class Goblin(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, health=100, attackPower=7)
        self.gold = 0
    def stealGold(self, Hero):
        """GOBBOS TAKIN GOOOOLD"""
        self.gold = self.gold + Hero.gold
        Hero.gold = 0
        print("GIT REKT NOOB")