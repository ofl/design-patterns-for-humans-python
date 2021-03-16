# Adapter Pattern

from abc import ABCMeta, abstractmethod


class Lion(metaclass=ABCMeta):
    @abstractmethod
    def roar(self):
        pass


class AfricanLion(Lion):
    def roar(self):
        print('grrrr')


class AsianLion(Lion):
    def roar(self):
        print('がおー')


class Hunter():
    def hunt(self, lion: Lion):
        lion.roar()


class WildDog():
    def bark(self):
        print('わんわん')


class WildDogAdapter(Lion):
    def __init__(self, dog: WildDog) -> None:
        self._dog = dog

    def roar(self):
        self._dog.bark()


hunter = Hunter()

african_lion = AfricanLion()
hunter.hunt(african_lion)

asian_lion = AsianLion()
hunter.hunt(asian_lion)

wild_dog = WildDog()
wild_dog_adapter = WildDogAdapter(wild_dog)
hunter.hunt(wild_dog_adapter)
