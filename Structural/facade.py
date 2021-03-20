# Facade Pattern

class Computer():
    def get_electric_shock(self):
        print('Ouch!')

    def make_sound(self):
        print('Beep beep!')

    def show_loading_screen(self):
        print('Loading..')

    def bam(self):
        print('Ready to be used!')

    def close_everything(self):
        print('Bup bup bup buzzzz!')

    def sooth(self):
        print('Zzzzz')

    def pull_current(self):
        print('Haaah!')


class ComputerFacade():
    def __init__(self, computer: Computer) -> None:
        self._computer = computer

    def turn_on(self):
        self._computer.get_electric_shock()
        self._computer.make_sound()
        self._computer.show_loading_screen()
        self._computer.bam()

    def turn_off(self):
        self._computer.close_everything()
        self._computer.pull_current()
        self._computer.sooth()


computer = ComputerFacade(Computer())
computer.turn_on()
computer.turn_off()
