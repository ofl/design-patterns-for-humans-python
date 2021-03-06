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


class BackOfficeDoor(Door):
    def open(self):
        print('Opening back office door')

    def close(self):
        print('Closing back office door')


class SecuredDoor(Door):
    def __init__(self, door: Door) -> None:
        self._door = door

    def open(self, password: str):
        if self._authenticate(password):
            self._door.open()
        else:
            print('Big no! It ain\'t possible.')

    def close(self):
        self._door.close()

    def _authenticate(self, password: str) -> bool:
        return password == '$ecr@t'


door = SecuredDoor(LabDoor())
door.open('invalid')  # Big no! It ain't possible.

door.open('$ecr@t')  # Opening lab door
door.close()  # Closing lab door

# door.open()  # => TypeError

door = SecuredDoor(BackOfficeDoor())
door.open('invalid')  # Big no! It ain't possible.

door.open('$ecr@t')  # Opening back office door
door.close()  # Closing back office door

# door.open()  # => TypeError
