# Flyweight Pattern

class KarakTea():
    pass


class TeaMaker():
    def __init__(self) -> None:
        self._available_tea = {}

    def make(self, preference: str):
        if preference not in self._available_tea:
            self._available_tea[preference] = KarakTea()

        return self._available_tea[preference]


class TeaShop():
    def __init__(self, tea_maker: TeaMaker) -> None:
        self._tea_maker = tea_maker
        self._orders = {}

    def take_order(self, teat_type: str, table: int):
        self._orders[table] = self._tea_maker.make(teat_type)

    def serve(self):
        for k in self._orders:
            print('Serving tea to table# ' + str(k))


tea_maker = TeaMaker()
shop = TeaShop(tea_maker)

shop.take_order('less sugar', 1)
shop.take_order('more milk', 2)
shop.take_order('without sugar', 5)

shop.serve()
