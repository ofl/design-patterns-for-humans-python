# Singleton Pattern

class President():
    def __init__(self) -> None:
        self._name = 'Washington'

    @classmethod
    def get_instance(cls):
        return cls()

    def get_name(self):
        return self._name


president1 = President.get_instance()
print(president1.get_name())

president2 = President.get_instance()
print(president2.get_name())

print(president1 == president2)

president3 = President()
print(president3.get_name())
