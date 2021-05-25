# Abstract Factory Pattern

class WoodenDoor():
    def get_description(self):
        print('I am a wooden door')


class IronDoor():
    def get_description(self):
        print('I am a iron door')


class Welder():
    def get_description(self):
        print('I can only fit iron doors')


class Carpenter():
    def get_description(self):
        print('I can only fit wooden doors')


class WoodenDoorFactory():
    def make_door(self):
        return WoodenDoor()

    def make_fitting_expert(self):
        return Carpenter()


class IronDoorFactory():
    def make_door(self):
        return IronDoor()

    def make_fitting_expert(self):
        return Welder()


wooden_factory = WoodenDoorFactory()
door = wooden_factory.make_door()
expert = wooden_factory.make_fitting_expert()
door.get_description()
expert.get_description()

iron_factory = IronDoorFactory()
door = iron_factory.make_door()
expert = iron_factory.make_fitting_expert()
door.get_description()
expert.get_description()
