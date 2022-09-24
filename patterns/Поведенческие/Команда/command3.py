"""Демонстратор шаблона Команда: компоновщик команд."""

from abc import ABC, abstractmethod
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



class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


@dataclass
class BankAccountCommand(Command):
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
            self.success = False
        else:
            pass


class CompositeBankAccountCommand(Command, list):
    def __init__(self, *commands: Command):
        super().__init__()
        for command in commands:
            self.append(command)

    def execute(self):
        for command in self:
            command.execute()

    def undo(self):
        for command in self[::-1]:
            command.undo()


ba1 = BankAccount(100)
print(f'ba1 {ba1}\n')

ccmds = CompositeBankAccountCommand(
    BankAccountCommand(ba1, Action.DEPOSIT, 100),
    BankAccountCommand(ba1, Action.WITHDRAW, 120)
)
ccmds.execute()
print(f'ba1 {ba1}\n')

ccmds.undo()
print(f'ba1 {ba1}\n')

