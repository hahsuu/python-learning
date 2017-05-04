
class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("subclass must implement abstract method")


class Cat(Animal):
    def __init__(self,name):
        super(Cat, self).__init__(name)

    def talk(self):
        return 'Meow!'


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)

    def talk(self):
        return 'Woof woof'


animals = [Cat('Missy'),
           Dog('Lassie')]


for animal in animals:
    print(animal.name)
    print(animal.talk())



