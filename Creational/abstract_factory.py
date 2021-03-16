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


class DoorFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_door(self) -> Door:
        pass

    @abstractmethod
    def make_fitting_expert(self) -> DoorFittingExpert:
        pass


class WoodenDoorFactory(DoorFactory):
    def make_door(self) -> Door:
        return WoodenDoor()

    def make_fitting_expert(self) -> DoorFittingExpert:
        return Carpenter()


class IronDoorFactory(DoorFactory):
    def make_door(self) -> Door:
        return IronDoor()

    def make_fitting_expert(self) -> DoorFittingExpert:
        return Welder()


wooden_factory = WoodenDoorFactory()
door = wooden_factory.make_door()
expert = wooden_factory.make_fitting_expert()
door.get_description()
expert.get_description()

iron_factory = IronDoorFactory()
door = iron_factory.make_door()
expert = iron_factory.make_fitting_expert()
door.get_description()
expert.get_description()
