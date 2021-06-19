# Command Pattern

from abc import ABCMeta, abstractmethod


class FloorLight():
    def turn_on(self):
        print("フロアライトをつけた")


class TV():
    def __init__(self) -> None:
        self._channel = 1

    def turn_on(self, channel: int):
        self._channel = channel
        print(f"テレビをつけて{self._channel}チャンネルにした")


class AirConditioner():
    def __init__(self) -> None:
        self._temp = 24

    def turn_on(self, temp: int):
        self._temp = temp
        print(f"エアコンをつけて{self._temp}度にした")


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class FloorLightCommand(Command):
    def __init__(self, floor_light: FloorLight) -> None:
        self._floor_light = floor_light

    def execute(self):
        self._floor_light.turn_on()


class TVCommand(Command):
    def __init__(self, tv: TV, channel: int) -> None:
        self._tv = tv
        self._channel = channel

    def execute(self):
        self._tv.turn_on(self._channel)


class AirConditionerCommand(Command):
    def __init__(self, air_conditioner: AirConditioner, temp: int) -> None:
        self._air_conditioner = air_conditioner
        self._temp = temp

    def execute(self):
        self._air_conditioner.turn_on(self._temp)


class SmartSpeaker():
    def __init__(self) -> None:
        self._commands = []

    def append_command(self, command: Command):
        self._commands.append(command)

    def good_morning(self):
        print('おはよう')
        for command in self._commands:
            command.execute()


class Human:
    def __init__(self, smart_speaker) -> None:
        self.smart_speaker = smart_speaker

    def set_up_smart_speaker(self):
        floor_light = FloorLight()
        tv = TV()
        air_conditioner = AirConditioner()

        command_1 = FloorLightCommand(floor_light)
        self.smart_speaker.append_command(command_1)
        command_2 = TVCommand(tv, 3)
        self.smart_speaker.append_command(command_2)
        command_3 = AirConditionerCommand(air_conditioner, 20)
        self.smart_speaker.append_command(command_3)

    def say_good_morning(self):
        self.smart_speaker.good_morning()


smart_speaker = SmartSpeaker()
human = Human(smart_speaker)
human.set_up_smart_speaker()
human.say_good_morning()
