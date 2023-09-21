import random
import time
class Weapon:
    damage = 0
    durability = 0
    protection = 0

    def attack(self, Unit):
        Unit.HP -= self.damage
    def defense(self):
        pass

    def isAlive(self):
        if (self.durability > 0):
            return True
        else:
            raise ("Weapon is broke")

class Luk(Weapon):
    def __init__(self):
        super().__init__()
        self.arrows = 15
        super().damage = 40
        super().durability = 30
        super().protection = 5
    def ArrowsRanOut(self):
        if (self.arrows >= 0):
            return
        else:
            raise ("Arrows ran out")
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

    HP=100
    Armor = 70
    name="warrior"
    def isAlive(self):
        if self.HP <=0:
            print(f"Warrior:{self.name} is Dead")
            return False
        else:
            return True

    def Isattack(self,warrior):
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
    def __init__(self,name):
        super().__init__()
        self.HP = 100
        self.Armor = 150
        self.name = name
        self.weapon = Luk()


class Rider(Warrior):
    def __init__(self,name):
        super().__init__()
        self.HP = 70
        self.Armor = 100
        self.name = name
        self.weapon = Spear()

class Infantryman(Warrior):
    def __init__(self,name):
        super().__init__()
        self.HP = 70
        self.Armor = 100
        self.name = name
        self.weapon = Spear()

    weapon = random.randint(1, 2)
    if weapon == 1:
        def __init__(self):
            self.sword = Sword()
    elif weapon == 2:
        def __init__(self):
            self.spear = Spear()
    elif weapon == 3:
        def __init__(self):
            self.axe = Axe()

class Army:
    army_list1 = []
    for i in range(0, 2):
        name = input("Enter the name for rider: ")

        army_list1.append(Archer(name))
        for archer in army_list1:
            print(f"{archer.name}: HP={archer.HP}, Armor={archer.Armor}, Weapon={archer.weapon.__class__.__name__}")

        army_list1.append(Infantryman(name))
    for infantryman in army_list1:
        print(f"{infantryman.name}: HP={infantryman.HP}, Armor={infantryman.Armor}, Weapon={infantryman.weapon.__class__.__name__}")

        army_list1.append(Rider(name))
    for rider in army_list1:
        print(f"{rider.name}: HP={rider.HP}, Armor={rider.Armor}, Weapon={rider.weapon.__class__.__name__}")
    def __init__(self):
        self.in_infantryman()
        self.in_archer()
        self.in_rider()

    def in_infantryman(self):
        for i in range(3):
            self.army_list1 += Infantryman();
    def in_rider(self):
        for i in range(50):
            self.army_list1 += Rider();
    def in_archer(self):
        for i in range(50):
            self.army_list1 += Archer();

d1 = Army()
print(d1.army_list1)