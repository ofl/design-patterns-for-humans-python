# Iterator Pattern

class RadioStation():
    def __init__(self, frequency: float) -> None:
        self._frequency = frequency

    def get_frequency(self):
        return self._frequency

    def show_frequency(self):
        print('My frequency is:' + str(self.get_frequency()))


class StationList():
    def __init__(self) -> None:
        self._stations: list[RadioStation] = []
        self._counter: int = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._valid():
            value = self._stations[self._counter]
            self._counter += 1
            return value
        else:
            raise StopIteration()

    def add_station(self, station: RadioStation):
        self._stations.append(station)

    def remove_station(self, to_remove: RadioStation):
        to_remove_frequency = to_remove.get_frequency()
        removed = list(filter(
            lambda x: x.get_frequency() != to_remove_frequency, self._stations)
        )
        self._stations = removed

    def current(self) -> RadioStation:
        return self._stations[self._counter]

    def rewind(self):
        self._counter = 0

    def _valid(self):
        return 0 <= self._counter < len(self._stations)


station_list = StationList()

station_list.add_station(RadioStation(89))
station_list.add_station(RadioStation(101))
station_list.add_station(RadioStation(102))
station_list.add_station(RadioStation(103.2))

station_list.remove_station(RadioStation(102))

for station in station_list:
    print(station.get_frequency())

station_list.rewind()

station_list.current().show_frequency()

next(station_list)
next(station_list)

station_list.current().show_frequency()
