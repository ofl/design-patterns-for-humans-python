# Builder Pattern

class Burger():
    def __init__(self, size, cheese, pepperoni, lettuce, tomato) -> None:
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.lettuce = lettuce
        self.tomato = tomato


burger = Burger(14, True, True, False, True)

print('size: ' + str(burger.size))
print('cheese: ' + str(burger.cheese))
print('tomato: ' + str(burger.tomato))
print('lettuce: ' + str(burger.lettuce))
print('pepperoni: ' + str(burger.pepperoni))
