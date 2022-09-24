"""Демонстратор шаблона Команда: отмена и повтор команд."""

from enum import Enum
from dataclasses import dataclass


class Action(Enum):
    DEPOSIT = 0
    WITHDRAW = 1


class BankAccount:
    overdraft_limit: int = -500

    def __init__(self, start_balance: int = 0):
        self._balance = start_balance

    def deposit(self, amount: int):
        self._balance += amount

    def withdraw(self, amount: int):
        self._balance -= amount

    def __str__(self):
        return f'Balance: {self._balance}'


@dataclass
class BankAccountCommand:
    account: BankAccount
    action: Action
    amount: int

    def execute(self):
        if self.action is Action.DEPOSIT:
            self.account.deposit(self.amount)
        elif self.action is Action.WITHDRAW:
            self.account.withdraw(self.amount)


ba1 = BankAccount(100)
print(f'ba1 {ba1}\n')

deposit1 = BankAccountCommand(ba1, Action.DEPOSIT, 50)
deposit1.execute()
print(f'ba1 {ba1}\n')

withdraw1 = BankAccountCommand(ba1, Action.WITHDRAW, 70)
withdraw1.execute()
print(f'ba1 {ba1}\n')
