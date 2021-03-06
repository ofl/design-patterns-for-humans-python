# Simple Factory Pattern

from abc import ABCMeta, abstractmethod


class Door(metaclass=ABCMeta):
    @abstractmethod
    def get_width() -> float:
        pass

    @abstractmethod
    def get_height() -> float:
        pass


class WoodenDoor(Door):
    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    def get_width(self) -> float:
        return self._width

    def get_height(self) -> float:
        return self._height


class DoorFactory():
    def make_door(type) -> Door:
        if type == 'big':
            return WoodenDoor(300, 600)
        else:
            return WoodenDoor(100, 200)


normal_size_door = DoorFactory.make_door('normal')
print(normal_size_door.get_width())
print(normal_size_door.get_height())

big_size_door = DoorFactory.make_door('big')
print(big_size_door.get_width())
print(big_size_door.get_height())
