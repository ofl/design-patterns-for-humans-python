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


class SmartSpeaker():
    def __init__(self) -> None:
        self._devices = []

    def append_device(self, device):
        self._devices.append(device)

    def good_morning(self, channel: int, temp: input):
        print('おはよう')
        for device in self._devices:
            if type(device) is TV:
                device.turn_on(channel)
            elif type(device) is AirConditioner:
                device.turn_on(temp)
            else:
                device.turn_on()


class Human:
    def __init__(self, smart_speaker) -> None:
        self.smart_speaker = smart_speaker

    def set_up_smart_speaker(self):
        floor_light = FloorLight()
        tv = TV()
        air_conditioner = AirConditioner()

        self.smart_speaker.append_device(floor_light)
        self.smart_speaker.append_device(tv)
        self.smart_speaker.append_device(air_conditioner)

    def say_good_morning(self):
        self.smart_speaker.good_morning(3, 20)


smart_speaker = SmartSpeaker()
human = Human(smart_speaker)
human.set_up_smart_speaker()
human.say_good_morning()
