# Abstract Factory Pattern

from abc import ABCMeta, abstractmethod


class Door(metaclass=ABCMeta):
    @abstractmethod
    def get_description(self) -> None:
        pass


class WoodenDoor(Door):
    def get_description(self) -> None:
        print('I am a wooden door')


class IronDoor(Door):
    def get_description(self) -> None:
        print('I am a iron door')


class DoorFittingExpert(metaclass=ABCMeta):
    @abstractmethod
    def get_description(self) -> None:
        pass


class Welder(DoorFittingExpert):
    def get_description(self) -> None:
        print('I can only fit iron doors')


class Carpenter(DoorFittingExpert):
    def get_description(self) -> None:
        print('I can only fit wooden doors')


door = WoodenDoor()
expert = Carpenter()
door.get_description()
expert.get_description()

door = IronDoor()
expert = Welder()
door.get_description()
expert.get_description()
