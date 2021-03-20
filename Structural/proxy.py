# Proxy Pattern

from abc import ABCMeta, abstractmethod


class Door(metaclass=ABCMeta):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass


class LabDoor(Door):
    def open(self):
        print('Opening lab door')

    def close(self):
        print('Closing lab door')


class SecuredDoor(Door):
    def __init__(self, door: Door) -> None:
        self._door = door

    def open(self, password: str):
        if self.authenticate(password):
            self._door.open()
        else:
            print('Big no! It ain\'t possible.')

    def authenticate(self, password: str) -> bool:
        return password == '$ecr@t'

    def close(self):
        self._door.close()


door = SecuredDoor(LabDoor())
door.open('invalid')  # Big no! It ain't possible.

door.open('$ecr@t')  # Opening lab door
door.close()  # Closing lab door
