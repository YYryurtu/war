import random
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
            return
        else:
            raise ("Weapon is broke")


class Luk(Weapon):
    def __init__(self):
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
        super().damage = 50
        super().durability = 15
        super().protection = 20

class Spear(Weapon):
    def __init__(self):
        super().damage = 100
        super().durability = 10
        super().protection = 20

class Axe(Weapon):
    def __init__(self):
        super().damage = 30
        super().durability = 35
        super().protection = 15

class Warrior:
    HP = 100
    Armor = 50

    def isAlive(self):
        if (self.HP > 0):
            return
        else:
            raise ("Dead")


class Archer(Warrior):
    super().HP -= 30

    def __init__(self):
        self.luk = Luk()


class Rider(Warrior):
    super().HP -= 30
    super().Armor += 10

    def __init__(self):
        self.spear = Spear()

class Infantryman(Warrior):
    super().Armor += 30
    super().HP += 70

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
    army_list = []
    def __init__(self):
        self.in_infantryman()
        self.in_archer()
        self.in_rider()

    def in_infantryman(self):
        for i in range(100):
            self.army_list += Infantryman();
    def in_rider(self):
        for i in range(50):
            self.army_list += Rider();
    def in_archer(self):
        for i in range(50):
            self.army_list += Archer();

d1 = Army()
print(d1.army_list)