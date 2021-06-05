# Abstract Factory Pattern

from abc import ABCMeta, abstractmethod
import random


class AbstractProductX(metaclass=ABCMeta):
    @abstractmethod
    def get_description(self) -> None:
        pass


class AbstractProductY(metaclass=ABCMeta):
    @abstractmethod
    def get_description(self) -> None:
        pass


class ConcreteProductX1(AbstractProductX):
    def get_description(self) -> None:
        print('I am a product X1')


class ConcreteProductX2(AbstractProductX):
    def get_description(self) -> None:
        print('I am a product X2')


class ConcreteProductY1(AbstractProductY):
    def get_description(self) -> None:
        print('I am a product Y1')


class ConcreteProductY2(AbstractProductY):
    def get_description(self) -> None:
        print('I am a product Y2')


class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_product_1(self) -> AbstractProductX:
        pass

    @abstractmethod
    def make_product_2(self) -> AbstractProductY:
        pass


class ConcreteFactoryX(AbstractFactory):
    def make_product_1(self) -> AbstractProductX:
        return ConcreteProductX1()

    def make_product_2(self) -> AbstractProductY:
        return ConcreteProductY1()


class ConcreteFactoryY(AbstractFactory):
    def make_product_1(self) -> AbstractProductX:
        return ConcreteProductX2()

    def make_product_2(self) -> AbstractProductY:
        return ConcreteProductY2()


if random.randint(1, 2) == 1:
    factory = ConcreteFactoryX()
else:
    factory = ConcreteFactoryY()

product_1 = factory.make_product_1()
product_2 = factory.make_product_2()
product_1.get_description()
product_2.get_description()
