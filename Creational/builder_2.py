# Builder Pattern

from abc import ABCMeta, abstractmethod


class Product():
    def __init__(self, builder) -> None:
        self.size = builder.size
        self.cheese = builder.cheese
        self.pepperoni = builder.pepperoni
        self.lettuce = builder.lettuce
        self.tomato = builder.tomato


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def add_pepperoni(self):
        pass

    @abstractmethod
    def add_lettuce(self):
        pass

    @abstractmethod
    def add_cheese(self):
        pass

    @abstractmethod
    def add_tomato(self):
        pass


class ConcreteBuilder(Builder):
    def __init__(self, size: int) -> None:
        self.size = size
        self.cheese = False
        self.pepperoni = False
        self.lettuce = False
        self.tomato = False

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_lettuce(self):
        self.lettuce = True
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_tomato(self):
        self.tomato = True
        return self

    def get_result(self) -> Product:
        return Product(self)


class Director():
    def __init__(self, builder) -> None:
        self.builder = builder

    def construct(self):
        return self.builder.add_cheese().add_lettuce().add_pepperoni().get_result()


director = Director(ConcreteBuilder(16))
burger = director.construct()

print('size: ' + str(burger.size))
print('cheese: ' + str(burger.cheese))
print('tomato: ' + str(burger.tomato))
print('lettuce: ' + str(burger.lettuce))
print('pepperoni: ' + str(burger.pepperoni))
