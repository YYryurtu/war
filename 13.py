import random
import time

class Items:
    def __init__(self):
        self.aid = True

class Weapon:
    damage = 0
    durability = 0
    protection = 0

    def attack(self, Unit):
        Unit.HP -= self.damage

    def defense(self):
        pass

    def isAlive(self):
        if self.durability <= 0:
            return False
        else:
            return True

class Luk(Weapon):
    def __init__(self):
        super().__init__()
        self.arrows = 15
        super().damage = 40
        super().durability = 30
        super().protection = 5

    def ArrowsRanOut(self):
        if self.arrows <= 0:
            raise Exception("Arrows ran out")

class Sword(Weapon):
    def __init__(self):
        super().__init__()
        super().damage = 50
        super().durability = 15
        super().protection = 20

class Spear(Weapon):
    def __init__(self):
        super().__init__()
        super().damage = 100
        super().durability = 10
        super().protection = 20

class Axe(Weapon):
    def __init__(self):
        super().__init__()
        super().damage = 30
        super().durability = 35
        super().protection = 15

class Warrior:
    HP = 100
    Armor = 70
    name = "warrior"
    items = Items()

    def useAid(self):
        if self.items.aid:
            self.HP = 100
            self.items.aid = False

    def giveWeapon(self):
        choice = random.randint(0, 3)
        if choice == 1:
            return Sword()
        if choice == 2:
            return Axe()
        if choice == 3:
            return Spear()

    def isAlive(self):
        if self.HP <= 0:
            print(f"Warrior:{self.name} is Dead")
            return False
        elif self.HP == 10:
            self.HP + 50
            self.durability + 5
        else:
            return True

    def Isattack(self, warrior):
        if self.weapon.isAlive():
            warrior.HP -= self.weapon.damage
            self.weapon.durability -= 1
            print(f"\n--Warrior:{warrior.name}-- \n has been attacked by \n --warrior:{self.name}--"
                  f"\nNow --{warrior.name}-- has {warrior.HP} HP"
                  f"\nAnd --{self.name}-- has {self.weapon.durability} durability of weapon\n")
        else:
            print("\nWeapon is broken\n")
            return False

class Archer(Warrior):
    def __init__(self, name):
        super().__init__()
        self.HP = 100
        self.Armor = 150
        self.name = name
        self.weapon = Luk()

class Rider(Warrior):
    def __init__(self, name):
        super().__init__()
        self.HP = 70
        self.Armor = 100
        self.name = name
        self.weapon = Spear()

class Infantryman(Warrior):
    def __init__(self, name, giveWeapon=None):
        super().__init__()
        self.HP = 70
        self.Armor = 100
        self.name = name
        self.weapon = giveWeapon()

class Army:
    def __init__(self):
        self.count_fights = 0
        self.army_1 = []
        self.army_2 = []
        self.initArmy(self.army_1)
        self.initArmy(self.army_2)

    def initArmy(self, army):
        for i in range(0, 2):
            name = input("Enter the name for rider: ")
            army.append(Rider(name))
            name = input("Enter the name for infantryman: ")
            army.append(Infantryman(name))
            name = input("Enter the name for archer: ")
            army.append(Archer(name))
        for warrior in army:
            print(f"{warrior.name}: HP={warrior.HP}, Armor={warrior.Armor}, Weapon={warrior.weapon.__class__.__name__}")

    def game(self):
        while self.army_1 and self.army_2:
            choice = random.randint(1, 2)
            self.count_fights += 1
            print(f"Fight : {self.count_fights}")
            if choice == 1:
                warrior_from_army1 = random.randint(0, len(self.army_1) - 1)
                warrior_from_army2 = random.randint(0, len(self.army_2) - 1)

                if self.army_1[warrior_from_army1].Isattack(self.army_2[warrior_from_army2]):
                    self.army_1.pop(warrior_from_army1)
                else:
                    if self.army_2[warrior_from_army2].isAlive():
                        pass
                    else:
                        self.army_2.pop(warrior_from_army2)
            if choice == 2:
                warrior_from_army1 = random.randint(0, len(self.army_1) - 1)
                warrior_from_army2 = random.randint(0, len(self.army_2) - 1)

                if self.army_2[warrior_from_army2].Isattack(self.army_1[warrior_from_army1]):
                    self.army_2.pop(warrior_from_army2)
                else:
                    if self.army_1[warrior_from_army1].isAlive():
                        pass
                    else:
                        self.army_1.pop(warrior_from_army1)

        if len(self.army_1) <= 0:
            print(f"Army 2 wins!")
        else:
            print(f"Army 1 wins!")

        time.sleep(3)


army = Army()
army.game()
