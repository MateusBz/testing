class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'hau hau. Jestem {self.name}.'

    def rename(self, new_name):
        self.name = new_name


dog_1 = Dog('Azor')
print(dog_1.speak())

dog_2 = Dog('Rex')
print(dog_2.speak())
dog_2.rename('Reksio')
print(dog_2.speak())
