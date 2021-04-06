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


normal_size_door = WoodenDoor(100, 200)
print(normal_size_door.get_width())
print(normal_size_door.get_height())

big_size_door = WoodenDoor(300, 600)
print(big_size_door.get_width())
print(big_size_door.get_height())
