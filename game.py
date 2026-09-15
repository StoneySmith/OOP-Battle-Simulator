from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Iron Square"

def battle(hero: Hero, enemy: Goblin):
        while hero.is_alive() and enemy.is_alive():
          hero_damage = hero.attack()
          enemy.take_damage(hero_damage)
          if enemy.is_alive:
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)

        if hero.is_alive():
             print(f"{hero.name} wins!")
        else:
             print(f"{enemy.name} wins!")

    

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")
    
    goblin = Goblin("Gribble")
    goblin2 = Goblin("Gronkle")
    print("But no hero has answered the call... yet.")
    heroName = input("What is your Hero's name?")
    hero = Hero(heroName)
    print(f"{heroName} enters the arena with {hero.health} health.")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    firstAttack = hero.attack()
    goblin.take_damage(firstAttack)
    if goblin.is_alive():
            hero.take_damage(goblin.attack())
    battle(hero,goblin)
    


if __name__ == "__main__":
    main()
