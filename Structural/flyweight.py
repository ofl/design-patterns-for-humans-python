# Flyweight Pattern

class KarakTea():
    def __init__(self, tea_type) -> None:
        print(f'Making {tea_type} tea')
        self.name = tea_type


class TeaMaker():
    def __init__(self) -> None:
        self._available_tea = {}

    def make(self, preference: str):
        if preference not in self._available_tea:
            self._available_tea[preference] = KarakTea(preference)

        return self._available_tea[preference]


class TeaShop():
    def __init__(self, tea_maker: TeaMaker) -> None:
        self._tea_maker = tea_maker
        self._orders = {}

    def take_order(self, tea_type: str, table: int):
        self._orders[table] = self._tea_maker.make(tea_type)

    def serve(self):
        for k, v in self._orders.items():
            print(f'Serving {v.name} tea to table# ' + str(k))


tea_maker = TeaMaker()
shop = TeaShop(tea_maker)

shop.take_order('less sugar', 1)
shop.take_order('more milk', 2)
shop.take_order('more milk', 3)
shop.take_order('without sugar', 5)
shop.take_order('less sugar', 7)

print('---------------------')

shop.serve()
