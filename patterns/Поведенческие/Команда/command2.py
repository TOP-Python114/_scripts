"""Демонстратор шаблона Команда: отмена и повтор команд."""

from enum import Enum
from dataclasses import dataclass


class Action(Enum):
    DEPOSIT = 0
    WITHDRAW = 1


class BankAccount:
    """Адресат команд."""
    overdraft_limit: int = -500

    def __init__(self, start_balance: int = 0):
        self._balance = start_balance

    def deposit(self, amount: int) -> None:
        self._balance += amount

    def withdraw(self, amount: int) -> bool:
        if self._balance - amount >= self.overdraft_limit:
            self._balance -= amount
            return True
        return False

    def __str__(self):
        return f'Balance: {self._balance}'


@dataclass
class BankAccountCommand:
    """Команда для различных действий."""
    account: BankAccount
    action: Action
    amount: int
    success: bool = False

    def execute(self):
        if self.action is Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action is Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if self.success:
            if self.action is Action.DEPOSIT:
                self.account.withdraw(self.amount)
            elif self.action is Action.WITHDRAW:
                self.account.deposit(self.amount)
        else:
            pass


ba1 = BankAccount(100)
print(f'ba1 {ba1}')

deposit1 = BankAccountCommand(ba1, Action.DEPOSIT, 50)
deposit1.execute()
print(f'ba1 {ba1}')

withdraw1 = BankAccountCommand(ba1, Action.WITHDRAW, 70)
withdraw1.execute()
print(f'ba1 {ba1}\n')

withdraw1.undo()
print(f'ba1 {ba1}\n')

withdraw2 = BankAccountCommand(ba1, Action.WITHDRAW, 1000)
withdraw2.execute()
print(f'ba1 {ba1}')
withdraw2.undo()
print(f'ba1 {ba1}\n')
