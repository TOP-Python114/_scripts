"""Демонстратор шаблона Хранитель: сохранение состояний в отдельных объектах."""

class Memento:
    def __init__(self, balance: int):
        self.balance = balance


class BankAccount:
    def __init__(self, start_balance: int = 0):
        self._balance = start_balance

    def deposit(self, amount: int):
        self._balance += amount
        return Memento(self._balance)

    def withdraw(self, amount: int):
        self._balance -= amount
        return Memento(self._balance)

    def restore(self, state: Memento):
        self._balance = state.balance

    def __str__(self):
        return f'Balance: {self._balance}'


ba1 = BankAccount(100)
print('start', ba1)

m0 = Memento(ba1._balance)

m1 = ba1.deposit(50)
m2 = ba1.withdraw(120)
print(ba1)

ba1.deposit(200)
print(ba1)

ba1.restore(m1)
print(ba1)

ba1.restore(m2)
print(ba1)
