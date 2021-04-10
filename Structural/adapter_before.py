# Adapter Pattern

from abc import ABCMeta, abstractmethod


class Lion(metaclass=ABCMeta):
    @abstractmethod
    def roar(self):
        pass


class Dog(metaclass=ABCMeta):
    @abstractmethod
    def bark(self):
        pass


class AfricanLion(Lion):
    def roar(self):
        print('grrrr')


class AsianLion(Lion):
    def roar(self):
        print('ガオー')


class Hunter():
    def hunt(self, lion: Lion):
        lion.roar()


class WildDog(Dog):
    def bark(self):
        print('ワオーン')


hunter = Hunter()

african_lion = AfricanLion()
hunter.hunt(african_lion)

asian_lion = AsianLion()
hunter.hunt(asian_lion)

wild_dog = WildDog()
hunter.hunt(wild_dog)  # => AttributeError
