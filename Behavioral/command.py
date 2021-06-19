from abc import ABCMeta, abstractmethod


class Invoker:
    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()


class Command(metaclass=ABCMeta):
    def __init__(self, receiver):
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    def execute(self):
        self._receiver.action()


class ReceiverA:
    def action(self):
        print('receiver A action')


class ReceiverB:
    def action(self):
        print('receiver B action')


class ReceiverC:
    def action(self):
        print('receiver C action')


class Client:
    def __init__(self, invoker) -> None:
        self.invoker = invoker

    def set_up(self):
        receiver_a = ReceiverA()
        concrete_command_a = ConcreteCommand(receiver_a)
        receiver_b = ReceiverB()
        concrete_command_b = ConcreteCommand(receiver_b)
        receiver_c = ReceiverC()
        concrete_command_c = ConcreteCommand(receiver_c)

        self.invoker.store_command(concrete_command_a)
        self.invoker.store_command(concrete_command_b)
        self.invoker.store_command(concrete_command_c)

    def execute(self):
        self.invoker.execute_commands()


invoker = Invoker()
client = Client(invoker)
client.set_up()

client.execute()
