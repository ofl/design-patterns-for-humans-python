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


computer = Computer()

# turn_on:
computer.get_electric_shock()
computer.make_sound()
computer.show_loading_screen()
computer.bam()

# turn_off:
computer.close_everything()
computer.pull_current()
computer.sooth()
