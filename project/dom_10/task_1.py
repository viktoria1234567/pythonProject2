# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

class Animal:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        pass


class Fish(Animal):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def get_info(self):
        return f'Глубина обитания {self.name} = {self.depth} m'


class Reptiles(Animal):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def get_info(self):
        return f'Длина тела {self.name} = {self.length} m'


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def get_info(self):
        return f'Порода кошки {self.name} = {self.breed}'


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def get_info(self):
        return f'Порода собаки {self.name} = {self.breed}'


class AnimalFactory:
    def __init__(self):
        self.animal_classes = {
            'Fish': Fish,
            'Reptiles': Reptiles,
            'Cat': Cat,
            'Dog': Dog
        }

    def create_animal(self, animal_type, *args):
        if animal_type not in self.animal_classes:
            raise ValueError("Invalid animal type")

        animal_class = self.animal_classes[animal_type]
        return animal_class(*args)


if __name__ == "__main__":
    factory = AnimalFactory()

    fish = factory.create_animal('Fish', 'Goldfish', 0.3)
    reptile = factory.create_animal('Reptiles', 'Snake', 1.5)
    cat = factory.create_animal('Cat', 'Fluffy', 'Persian')
    dog = factory.create_animal('Dog', 'Buddy', 'Labrador')

    print(fish.get_info())
    print(reptile.get_info())
    print(cat.get_info())
    print(dog.get_info())
