class Animal:
    def eating(self):
        pass

class Dog(Animal):
    def eating(self):
        print('I like meat, hehe')

class Parrot(Animal):
    def eating(self):
        print('I like to eat seed, and drink rum like a pirate')

class Lion(Animal):
    def eating(self):
        print('I like to eat other animals, grrr')

class AnimalFactory():
    @classmethod
    def createAnimal(cls, species):
        if species == "lion":
            return Lion()
        if species == "parrot":
            return Parrot()
        if species == "dog":
            return  Dog()
        else:
            raise NameError('Factory can\'t create the given type')

animal_type = input("choose an animal type from the following ( dog, parrot, lion ) :")
animal = AnimalFactory.createAnimal(animal_type)
animal.eating()