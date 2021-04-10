# Prototype Pattern


class Sheep():
    def __init__(self, name: str, category='Mountain Sheep', color='white'):
        self._name = name
        self._category = category
        self._color = color

    def set_name(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def set_category(self, category: str):
        self._category = category

    def get_category(self) -> str:
        return self._category

    def set_color(self, color: str):
        self._color = color

    def get_color(self) -> str:
        return self._color


original = Sheep('Jolly', 'Shetland Sheep', 'black')
print(original.get_name())
print(original.get_category())
print(original.get_color())

cloned = Sheep('Dolly')
print(cloned.get_name())
print(cloned.get_category())
print(cloned.get_color())

cloned.set_category(original.get_category())
cloned.set_color(original.get_color())
print(cloned.get_name())
print(cloned.get_category())
print(cloned.get_color())
