# Visitor Pattern

from abc import ABCMeta, abstractmethod


class AnimalOperation(metaclass=ABCMeta):
    @abstractmethod
    def visit_monkey(self, monkey):
        pass

    @abstractmethod
    def visit_lion(self, lion):
        pass

    @abstractmethod
    def visit_dolphin(self, dolphin):
        pass


class Animal(metaclass=ABCMeta):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def accept(self, operation: AnimalOperation):
        pass


class Monkey(Animal):
    def shout(self):
        print('Ooh oo aa aa!')

    def accept(self, operation: AnimalOperation):
        operation.visit_monkey(self)


class Lion(Animal):
    def roar(self):
        print('Roaaar!')

    def accept(self, operation: AnimalOperation):
        operation.visit_lion(self)


class Dolphin(Animal):
    def speak(self):
        print('Tuut tuttu tuutt!')

    def accept(self, operation: AnimalOperation):
        operation.visit_dolphin(self)


class Speak(AnimalOperation):
    def visit_monkey(self, monkey):
        monkey.shout()

    def visit_lion(self, lion):
        lion.roar()

    def visit_dolphin(self, dolphin):
        dolphin.speak()


monkey = Monkey('George')
lion = Lion('Simba')
dolphin = Dolphin('Winter')

speak = Speak()

monkey.accept(speak)   # Ooh oo aa aa!
lion.accept(speak)     # Roaaar!
dolphin.accept(speak)  # Tuut tutt tuutt!


class Jump(AnimalOperation):
    def visit_monkey(self, monkey):
        print(monkey.name + ' jumped 20 feet high! on to the tree!')

    def visit_lion(self, lion):
        print(lion.name + ' jumped 7 feet! Back on the ground!')

    def visit_dolphin(self, dolphin):
        print(dolphin.name + ' walked on water a little and disappeared')


jump = Jump()

monkey.accept(jump)    # Jumped 20 feet high! on to the tree!
lion.accept(jump)      # Jumped 7 feet! Back on the ground!
dolphin.accept(jump)   # Walked on water a little and disappeared
