# Bridge Pattern

from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name: str, salary: float) -> None:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def set_salary(self, salary):
        pass

    @abstractmethod
    def get_salary(self) -> float:
        pass

    @abstractmethod
    def get_roles(self) -> list:
        pass


class Developer(Employee):
    def __init__(self, name: str, salary: float) -> None:
        self._name = name
        self._salary = salary
        self._roles = []

    def get_name(self) -> str:
        return self._name

    def set_salary(self, salary):
        self._salary = salary

    def get_salary(self) -> str:
        return self._salary

    def get_roles(self) -> list:
        return self._roles


class Designer(Employee):
    def __init__(self, name: str, salary: float) -> None:
        self._name = name
        self._salary = salary
        self._roles = []

    def get_name(self) -> str:
        return self._name

    def set_salary(self, salary):
        self._salary = salary

    def get_salary(self) -> str:
        return self._salary

    def get_roles(self) -> list:
        return self._roles


class Organization():
    def __init__(self) -> None:
        self._employees = []

    def add_employee(self, employee: Employee):
        self._employees.append(employee)

    def get_net_salaries(self):
        net_salary = 0

        for employee in self._employees:
            net_salary += employee.get_salary()

        return net_salary


john = Developer('John Doe', 12000)
jane = Designer('Jane Doe', 15000)

organization = Organization()
organization.add_employee(john)
organization.add_employee(jane)

print(organization.get_net_salaries())
