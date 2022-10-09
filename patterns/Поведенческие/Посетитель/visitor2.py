from abc import ABC
from typing import Callable, Type


class Expression(ABC):
    """Описывает объекты математических выражений."""
    pass


class FloatExpression(Expression):
    def __init__(self, value: float):
        self.value = value


class AdditionExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right


_methods = {}

def visitor(arg_type: Type[Expression]) -> Callable:
    """Определяет объект класса, с которым должен работать декорируемый метод."""

    def decorator(method_object: Callable) -> Callable:
        """Сохраняет декорируемый метод в словарь по ключу – имени класса объекта, с которым работает метод."""
        _methods[arg_type.__name__] = method_object

        def _wrapper(instance_object, object_to_process: Expression) -> None:
            """Получает из словаря нужный метод в зависимости от класса объекта, с которым должен работать метод."""
            key = object_to_process.__class__.__name__
            method = _methods[key]
            return method(instance_object, object_to_process)

        return _wrapper

    return decorator



class ExpressionPrinter:
    """Посетитель объектов выражения, накапливающий в буфере строковое представление объектов выражения."""
    def __init__(self):
        self.buffer = []

    def __str__(self):
        return ''.join(self.buffer)

    @visitor(FloatExpression)
    def visit(self, fe: FloatExpression):
        self.buffer.append(str(fe.value))

    @visitor(AdditionExpression)
    def visit(self, ae: AdditionExpression):
        self.buffer.append('(')
        self.visit(ae.left)
        self.buffer.append(' + ')
        self.visit(ae.right)
        self.buffer.append(')')


# 1 + (2 + 3)
expr1 = AdditionExpression(
    FloatExpression(1),
    AdditionExpression(
        FloatExpression(2),
        FloatExpression(3)
    )
)
printer = ExpressionPrinter()
printer.visit(expr1)
print(printer)
