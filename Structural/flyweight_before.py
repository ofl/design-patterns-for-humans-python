# Flyweight Pattern

class KarakTea():
    def __init__(self, tea_type) -> None:
        print(f'Making {tea_type} tea')
        self.name = tea_type


class TeaShop():
    def __init__(self) -> None:
        self._orders = {}

    def take_order(self, tea_type: str, table: int):
        self._orders[table] = KarakTea(tea_type)

    def serve(self):
        for k, v in self._orders.items():
            print(f'Serving {v.name} tea to table# ' + str(k))


shop = TeaShop()

shop.take_order('less sugar', 1)
shop.take_order('more milk', 2)
shop.take_order('more milk', 3)
shop.take_order('without sugar', 5)
shop.take_order('less sugar', 7)

print('---------------------')

shop.serve()
