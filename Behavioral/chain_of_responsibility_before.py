# Chain of Responsibility Pattern

from abc import ABCMeta


class Account(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._balance = 0
        self._successor

    def pay(self, amount_to_pay: float):
        print('Paid {0} using {1}'.format(
            amount_to_pay, self.__class__.__name__))

    def can_pay(self, amount: float) -> bool:
        return self._balance >= amount


class Bank(Account):
    def __init__(self, balance) -> None:
        self._balance = balance


class Paypal(Account):
    def __init__(self, balance) -> None:
        self._balance = balance


class Bitcoin(Account):
    def __init__(self, balance) -> None:
        self._balance = balance


bank = Bank(100)          # Bank with balance 100
paypal = Paypal(200)      # Paypal with balance 200
bitcoin = Bitcoin(300)    # Bitcoin with balance 300

# Let's try to pay using the first priority i.e. bank
price = 350

if bank.can_pay(price):
    bank.pay(price)
elif paypal.can_pay(price):
    paypal.pay(price)
elif bitcoin.can_pay(price):
    bitcoin.pay(price)
else:
    raise Exception('None of the accounts have enough balance')
