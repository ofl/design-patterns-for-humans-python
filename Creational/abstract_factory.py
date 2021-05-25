# Abstract Factory Pattern

from abc import ABCMeta, abstractmethod


class AbstractDoor(metaclass=ABCMeta):
    @abstractmethod
    def get_description(self) -> None:
        pass


class ConcreteWoodenDoor(AbstractDoor):
    def get_description(self) -> None:
        print('I am a wooden door')


class ConcreteIronDoor(AbstractDoor):
    def get_description(self) -> None:
        print('I am a iron door')


class AbstractDoorFactory(metaclass=ABCMeta):
    @abstractmethod
    def get_description(self) -> None:
        pass


class ConcreteFactoryWelder(AbstractDoorFactory):
    def get_description(self) -> None:
        print('I can only fit iron doors')


class ConcreteFactoryCarpenter(AbstractDoorFactory):
    def get_description(self) -> None:
        print('I can only fit wooden doors')


class AbstractDoorFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_door(self) -> AbstractDoor:
        pass

    @abstractmethod
    def make_fitting_expert(self) -> AbstractDoorFactory:
        pass


class ConcreteWoodenDoorFactory(AbstractDoorFactory):
    def make_door(self) -> AbstractDoor:
        return ConcreteWoodenDoor()

    def make_fitting_expert(self) -> AbstractDoorFactory:
        return ConcreteFactoryCarpenter()


class ConcreteIronDoorFactory(AbstractDoorFactory):
    def make_door(self) -> AbstractDoor:
        return ConcreteIronDoor()

    def make_fitting_expert(self) -> AbstractDoorFactory:
        return ConcreteFactoryWelder()


wooden_factory = ConcreteWoodenDoorFactory()
door = wooden_factory.make_door()
expert = wooden_factory.make_fitting_expert()
door.get_description()
expert.get_description()

iron_factory = ConcreteIronDoorFactory()
door = iron_factory.make_door()
expert = iron_factory.make_fitting_expert()
door.get_description()
expert.get_description()
