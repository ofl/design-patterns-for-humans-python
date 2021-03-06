# Singleton Pattern

class President():
    _instance = None

    def __init__(self) -> None:
        if self.__class__._instance is not None:
            raise NotImplementedError()
        else:
            self._name = 'Washington'
            self.__class__._instance = self

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()

        return cls._instance

    def get_name(self):
        return self._name


president1 = President.get_instance()
print(president1.get_name())

president2 = President.get_instance()
print(president2.get_name())

print(president1 == president2)

president3 = President()  # => NotImplementedError
print(president3.get_name())
