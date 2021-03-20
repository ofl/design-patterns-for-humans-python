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
    def get_cost(self) -> float:
        return 10

    def get_description(self) -> str:
        return 'Simple coffee'


class MilkCoffee(Coffee):
    def __init__(self, coffee: Coffee) -> None:
        self._coffee = coffee

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 2

    def get_description(self) -> str:
        return self._coffee.get_description() + ',  milk'


class WhipCoffee(Coffee):
    def __init__(self, coffee: Coffee) -> None:
        self._coffee = coffee

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 5

    def get_description(self) -> str:
        return self._coffee.get_description() + ',  whip'


class VanillaCoffee(Coffee):
    def __init__(self, coffee: Coffee) -> None:
        self._coffee = coffee

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 3

    def get_description(self) -> str:
        return self._coffee.get_description() + ',  vanilla'


someCoffee = SimpleCoffee()
print(someCoffee.get_cost())  # 10
print(someCoffee.get_description())  # Simple Coffee

someCoffee = MilkCoffee(someCoffee)
print(someCoffee.get_cost())  # 12
print(someCoffee.get_description())  # Simple Coffee, milk

someCoffee = WhipCoffee(someCoffee)
print(someCoffee.get_cost())  # 17
print(someCoffee.get_description())  # Simple Coffee, milk, whip

someCoffee = VanillaCoffee(someCoffee)
print(someCoffee.get_cost())  # 20
print(someCoffee.get_description())  # Simple Coffee, milk, whip, vanilla
