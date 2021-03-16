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
    def make_door(width, height) -> Door:
        return WoodenDoor(width, height)


door = DoorFactory.make_door(100, 200)
print(door.get_width())
print(door.get_height())
