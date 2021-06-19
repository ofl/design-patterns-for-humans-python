# Builder Pattern

class Burger():
    def __init__(self, builder) -> None:
        self.size = builder.size
        self.cheese = builder.cheese
        self.pepperoni = builder.pepperoni
        self.lettuce = builder.lettuce
        self.tomato = builder.tomato


class BurgerBuilder():
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

    def build(self) -> Burger:
        return Burger(self)


burger = BurgerBuilder(14)\
    .add_cheese()\
    .add_lettuce()\
    .add_pepperoni()\
    .build()

print('size: ' + str(burger.size))
print('cheese: ' + str(burger.cheese))
print('tomato: ' + str(burger.tomato))
print('lettuce: ' + str(burger.lettuce))
print('pepperoni: ' + str(burger.pepperoni))
