"""Демонстратор шаблона Хранитель: сохранение состояний в журнале в атрибуте изменяемого класса."""

from typing import Optional


class Memento:
    def __init__(self, balance: int):
        self.balance = balance


class BankAccount:
    def __init__(self, start_balance: int = 0):
        self._balance = start_balance
        self._changes: list[Memento] = [Memento(start_balance)]
        self._current_state: int = 0

    def deposit(self, amount: int) -> Memento:
        self._balance += amount
        state = Memento(self._balance)
        self._changes += [state]
        self._current_state += 1
        return state

    def withdraw(self, amount: int) -> Memento:
        self._balance -= amount
        self._changes += [state := Memento(self._balance)]
        self._current_state += 1
        return state

    def undo(self) -> Optional[Memento]:
        if self._current_state > 0:
            self._current_state -= 1
            state = self._changes[self._current_state]
            self._balance = state.balance
            return state
        return None

    def redo(self) -> Optional[Memento]:
        if self._current_state < len(self._changes) - 1:
            self._current_state += 1
            state = self._changes[self._current_state]
            self._balance = state.balance
            return state
        return None

    def restore(self, state: Memento):
        self._balance = state.balance
        self._changes = [state]
        self._current_state = 0

    def __str__(self):
        return f'balance: {self._balance}'


ba1 = BankAccount(100)
print(ba1)

ba1.deposit(200)
ba1.deposit(220)
m1 = ba1.withdraw(115)
ba1.deposit(190)
print(ba1)

ba1.undo()
ba1.undo()
ba1.undo()
ba1.undo()
print(ba1)

# лишняя отмена — ничего не произойдёт
ba1.undo()
print(ba1)

ba1.redo()
ba1.redo()
ba1.redo()
ba1.redo()
print(ba1)

# лишний возврат — ничего не произойдёт
ba1.redo()
print(ba1)

# обнуление истории изменений
ba1.restore(m1)
print(ba1)
