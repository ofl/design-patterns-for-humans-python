# Simple Factory Pattern(https://github.com/kamranahmedse/design-patterns-for-humans)

from abc import ABCMeta, abstractmethod


class Door(metaclass=ABCMeta):
    @abstractmethod
    def getWidth() -> float:
        pass

    @abstractmethod
    def getHeight() -> float:
        pass


class WoodenDoor(Door):
    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height
        # super().__init__()

    def getWidth(self) -> float:
        return self._width

    def getHeight(self) -> float:
        return self._height


class DoorFactory():
    def makeDoor(width, height) -> Door:
        return WoodenDoor(width, height)


door = DoorFactory.makeDoor(100, 200)
print(door.getWidth())
print(door.getHeight())
