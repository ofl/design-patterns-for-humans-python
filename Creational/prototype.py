# Prototype Pattern

import copy


class Sheep():
    def __init__(self, name: str, category: str = 'Mountain Sheep') -> None:
        self.name = name
        self.category = category

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_category(self, category: str):
        self.category = category

    def get_category(self) -> str:
        return self.category


original = Sheep('Jolly')
print(original.get_name())
print(original.get_category())

cloned = copy.copy(original)
cloned.set_name('Dolly')
print(cloned.get_name())
print(cloned.get_category())
