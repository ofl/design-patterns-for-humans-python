# Command Pattern

from abc import ABCMeta, abstractmethod


class Bulb():
    def turn_on(self):
        print("Bulb has been lit")

    def turn_off(self):
        print("Darkness")


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def redo(self):
        pass


class TurnOn(Command):
    def __init__(self, bulb: Bulb) -> None:
        self._bulb = bulb

    def execute(self):
        self._bulb.turn_on()

    def undo(self):
        self._bulb.turn_off()

    def redo(self):
        self.execute()


class TurnOff(Command):
    def __init__(self, bulb: Bulb) -> None:
        self._bulb = bulb

    def execute(self):
        self._bulb.turn_off()

    def undo(self):
        self._bulb.turn_on()

    def redo(self):
        self.execute()


class RemoteControl():
    def submit(self, command: Command):
        command.execute()


bulb = Bulb()

turn_on = TurnOn(bulb)
turn_off = TurnOff(bulb)

remote = RemoteControl()
remote.submit(turn_on)  # Bulb has been lit!
remote.submit(turn_off)  # Darkness!
