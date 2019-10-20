class Animal:
    total_number_of_animal = 0

    def __init__(self):
        Animal.total_number_of_animal += 1


class Dog(Animal):

    def __init__(self, name, species):
        super().__init__()
        self.name = name
        self.species = species


class Cat(Animal):

    def __init__(self, name, species):
        super().__init__()
        self.name = name
        self.species = species




