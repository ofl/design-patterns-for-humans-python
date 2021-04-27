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

    def secure_open(self, password):
        if self._authenticate(password):
            self.open()
        else:
            print('Big no! It ain\'t possible.')

    def _authenticate(self, password: str) -> bool:
        return password == '$ecr@t'


class BackOfficeDoor(Door):
    def open(self):
        print('Opening back office door')

    def close(self):
        print('Closing back office door')

    def secure_open(self, password):
        if self._authenticate(password):
            self.open()
        else:
            print('Big no! It ain\'t possible.')

    def _authenticate(self, password: str) -> bool:
        return password == '$ecr@t'


door = LabDoor()
door.secure_open('invalid')  # Big no! It ain't possible.

door.secure_open('$ecr@t')  # Opening lab door
door.close()  # Closing lab door

door.open()  # Opening lab door

door = BackOfficeDoor()
door.secure_open('invalid')  # Big no! It ain't possible.

door.secure_open('$ecr@t')  # Opening back office door
door.close()  # Closing back office door

door.open()  # Opening back office door
