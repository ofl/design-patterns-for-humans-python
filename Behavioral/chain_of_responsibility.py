# Chain of Responsibility Pattern

from abc import ABCMeta


class Account(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._balance = 0
        self._successor

    def set_next(self, account):
        self._successor = account

    def pay(self, amount_to_pay: float):
        if self._can_pay(amount_to_pay):
            print('Paid {0} using {1}'.format(
                amount_to_pay, self.__class__))
        elif hasattr(self, '_successor'):
            self._successor.pay(amount_to_pay)
        else:
            raise Exception('None of the accounts have enough balance')

    def _can_pay(self, amount: float) -> bool:
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

bank.set_next(paypal)
paypal.set_next(bitcoin)

# Let's try to pay using the first priority i.e. bank
bank.pay(256)
