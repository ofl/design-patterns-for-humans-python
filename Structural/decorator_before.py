# Decorator Pattern

from abc import ABCMeta, abstractmethod


class Coffee(metaclass=ABCMeta):
    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


class SimpleCoffee(Coffee):
    def __init__(self) -> None:
        self.cost = 10
        self.description = 'Simple coffee'

    def get_cost(self) -> float:
        return self.cost

    def get_description(self) -> str:
        return self.description

    def add_option(self, option):
        self.cost += option.get_cost()
        self.description += option.get_description()


class MilkCoffeeOption():
    def __init__(self) -> None:
        pass

    def get_cost(self) -> float:
        return 2

    def get_description(self) -> str:
        return ',  milk'


class WhipCoffeeOption():
    def __init__(self) -> None:
        pass

    def get_cost(self) -> float:
        return 5

    def get_description(self) -> str:
        return ',  whip'


class VanillaCoffeeOption():
    def __init__(self) -> None:
        pass

    def get_cost(self) -> float:
        return 3

    def get_description(self) -> str:
        return ',  vanilla'


someCoffee = SimpleCoffee()
print(someCoffee.get_cost())  # 10
print(someCoffee.get_description())  # Simple Coffee

option = MilkCoffeeOption()
someCoffee.add_option(option)
print(someCoffee.get_cost())  # 12
print(someCoffee.get_description())  # Simple Coffee, milk

option = WhipCoffeeOption()
someCoffee.add_option(option)
print(someCoffee.get_cost())  # 17
print(someCoffee.get_description())  # Simple Coffee, milk, whip

option = VanillaCoffeeOption()
someCoffee.add_option(option)
print(someCoffee.get_cost())  # 20
print(someCoffee.get_description())  # Simple Coffee, milk, whip, vanilla
