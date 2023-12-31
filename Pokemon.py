class Pokemon:
    def __init__(self, name, number, generation, type1, type2, species, height,
                 weight, abilities, habilities, hp, attack, defence, spattack, spdefence, speed):
        self.name = name
        self.number = number
        self.generation = generation
        self.type1 = type1
        self.type2 = type2
        self.species = species
        self.height = height
        self.weight = weight
        self.abilities = abilities
        self.habilities = habilities
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.spattack = spattack
        self.spdefence = spdefence
        self.speed = speed
        self.total = int(attack) + int(defence) + int(speed) + int(hp) + int(spattack) + int(spdefence)
        self.legendary = False
        self.mythical = False

    def add_to_list(self, list):
        list.append(self)

    def legendarify(self):
        self.legendary = True

    def myth(self):
        self.mythical = True
