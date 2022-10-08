from typing import Callable
from operator import add, sub, mul, truediv


class Calculator:
    def __init__(self, number1: int, number2: int):
        self.number1 = number1
        self.number2 = number2

    def calc(self, operation: Callable):
        return operation(self.number1, self.number2)


c = Calculator(3, 7)
print(c.calc(add))
print(c.calc(sub))
print(c.calc(mul))
print(c.calc(truediv))
print(c.calc(lambda a, b: a**b))
# (1 + 5) / 3**2
