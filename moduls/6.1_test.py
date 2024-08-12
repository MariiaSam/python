class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health

    def attack(self, other_pokemon):
        # Pikachu attacks Charmander!
        print(f"{self.name} attacks {other_pokemon.name}!")

    def dodge(self):
        # Pikachu dodged the attack!
        print(f"{self.name} dodged the attack!")

    def evolve(self, new_form):
        # Pikachu is evolving into Raichu!
        print(f"{self.name} is evolving into {new_form}!")
        self.name = new_form


# Створення об'єкта Pikachu
pikachu = Pokemon("Pikachu", "Electric", 100)

# Використання методів
pikachu.attack(Pokemon("Charmander", "Fire", 100))
pikachu.dodge()
pikachu.evolve("Raichu")
