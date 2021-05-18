# Visitor Pattern

from abc import ABCMeta, abstractmethod


class AnimalOperation(metaclass=ABCMeta):
    @abstractmethod
    def by_monkey(self, monkey):
        pass

    @abstractmethod
    def by_lion(self, lion):
        pass

    @abstractmethod
    def by_dolphin(self, dolphin):
        pass


class Animal(metaclass=ABCMeta):
    def __init__(self, name) -> None:
        self.name = name


class Monkey(Animal):
    def shout(self):
        print('Ooh oo aa aa!')


class Lion(Animal):
    def roar(self):
        print('Roaaar!')


class Dolphin(Animal):
    def speak(self):
        print('Tuut tuttu tuutt!')


class Speak(AnimalOperation):
    def by_monkey(self, monkey):
        monkey.shout()

    def by_lion(self, lion):
        lion.roar()

    def by_dolphin(self, dolphin):
        dolphin.speak()


monkey = Monkey('George')
lion = Lion('Simba')
dolphin = Dolphin('Winter')

speak = Speak()

speak.by_monkey(monkey)   # Ooh oo aa aa!
speak.by_lion(lion)       # Roaaar!
speak.by_dolphin(dolphin)  # Tuut tutt tuutt!


class Jump(AnimalOperation):
    def by_monkey(self, monkey):
        print(monkey.name + ' jumped 20 feet high! on to the tree!')

    def by_lion(self, lion):
        print(lion.name + ' jumped 7 feet! Back on the ground!')

    def by_dolphin(self, dolphin):
        print(dolphin.name + ' walked on water a little and disappeared')


jump = Jump()

jump.by_monkey(monkey)   # Jumped 20 feet high! on to the tree!
jump.by_lion(lion)       # Jumped 7 feet! Back on the ground!
jump.by_dolphin(dolphin)  # Walked on water a little and disappeared
