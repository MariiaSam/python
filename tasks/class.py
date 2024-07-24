# 1
'''
Потрібно створити клас Warrior, екземпляри якого матимуть два параметри health = 50, attak = 5
І властивість is alive - True, якщо здоровʼя воїна більше 0

Кожного ходу перший воїн буде вдаряти другого, і цей другий втрачатиме своє в тій самій величині, що і атака першого воїна.
Після цього, якщо ввін ще живий, другий воїн зробить те ж саме із першим.

Поєдинок закінчується смертю одного з них. І якщо перший воїн ще живий, отже іншого біль ше немає

Функція має повертати True, False в іншому випадку

Крім того, ви повинні створити другий тип одиниць – Knight, який має бути підкласом Warrior, але мати підвищену атаку – 7. Також вам потрібно створити функцію fight(), яка ініціюватиме двобій між 2 бійцями та визначатиме найсильніший з них. Поєдинок відбувається за таким принципом:
Кожного ходу перший воїн буде вдаряти по другому, і цей другий втрачатиме своє здоров'я в тій самій величині, що і атака першого воїна. Після цього, якщо він ще живий, другий воїн зробить те ж саме з першим.
Поєдинок закінчується смертю одного з них. Якщо перший воїн ще живий (і, отже, іншого більше немає), функція має повернути True, False в іншому випадку.
'''


class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0

    def loose(self, attack):
        self.health -= self.damage(attack)

    def hit(self, enemy):
        enemy.loose(self.attack)

    def damage(self, attack):
        return attack


class Defender(Warrior):
    def __init__(self, health=60, attack=3, defense=2):
        super().__init__(health, attack)
        self.defense = defense

    def damage(self, attack):
        return attack - self.defense if attack > self.defense else 0


class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        super().__init__(health, attack)


class Vampire(Warrior):
    def __init__(self, health=40, attack=4, vampirism=50):
        super().__init__(health, attack)
        self.vampirism = vampirism

    def hit(self, enemy):
        enemy.loose(self.attack)
        self.health += self.vampirism * enemy.damage(self.attack) / 100


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, unit_count):
        self.units += [unit_type() for i in range(unit_count)]    

class Battle:
    def fight(self, army1, army2):
        while army1.units and army2.units:
            fight_res = fight(army1.units[0], army2.units[0])
            if fight_res:
                army2.units.pop(0)
            else:
                army1.units.pop(0)
        return bool(army1.units)


def fight(unit1, unit2):
    while unit1.is_alive and unit2.is_alive:
        unit1.hit(unit2)
        if unit2.is_alive:
            unit2.hit(unit1)
    return unit1.is_alive


leon = Warrior()
leon.is_alive  # @property
leon.health

alex = Warrior()

chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

# The assert keyword is used when debugging code.
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()
bob = Defender()
mike = Knight()
rog = Warrior()
lancelot = Defender()
eric = Vampire()
adam = Vampire()
richard = Defender()
ogre = Warrior()
assert fight(chuck, bruce) == True
assert fight(dave, carl) == False
assert chuck.is_alive == True
assert bruce.is_alive == False
assert carl.is_alive == True
assert dave.is_alive == False
assert fight(carl, mark) == False
assert carl.is_alive == False
assert fight(bob, mike) == False
assert fight(lancelot, rog) == True
assert fight(eric, richard) == False
assert fight(ogre, adam) == True
# battle tests
my_army = Army()
my_army.add_units(Defender, 2)
my_army.add_units(Vampire, 2)
my_army.add_units(Warrior, 1)
enemy_army = Army()
enemy_army.add_units(Warrior, 2)
enemy_army.add_units(Defender, 2)
enemy_army.add_units(Vampire, 3)
army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Defender, 4)
army_4 = Army()
army_4.add_units(Vampire, 3)
army_4.add_units(Warrior, 2)
battle = Battle()
assert battle.fight(my_army, enemy_army) == False
assert battle.fight(army_3, army_4) == True
print("Coding complete? Let's try tests!")
