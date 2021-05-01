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


floor_light = FloorLight()
tv = TV()
air_conditioner = AirConditioner()

smart_speaker = SmartSpeaker()
smart_speaker.append_device(floor_light)
smart_speaker.append_device(tv)
smart_speaker.append_device(air_conditioner)

smart_speaker.good_morning(3, 20)
