# Singleton Pattern

class President():
    instance = None

    def __new__(cls, *args, **kargs) -> None:
        pass

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = super(President, cls).__new__(cls)

        return cls.instance


president = President()
print(president)

president1 = President.get_instance()
print(president1)

president2 = President.get_instance()
print(president1 == president2)
