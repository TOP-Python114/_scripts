from abc import ABC


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


class ExpressionPrinter:
    """Формирует строку для объекта выражения."""
    @classmethod
    # метод нарушает OCP
    def print(cls, buffer: list, expression: Expression):
        """Записывает в буфер строковое представление элементов выражения, осуществляя рекурсивный обход элементов выражения."""
        if isinstance(expression, FloatExpression):
            buffer.append(str(expression.value))
        elif isinstance(expression, AdditionExpression):
            buffer.append('(')
            cls.print(buffer, expression.left)
            buffer.append(' + ')
            cls.print(buffer, expression.right)
            buffer.append(')')
        else:
            raise NotImplementedError


# 1 + (2 + 3)
expr1 = AdditionExpression(
    FloatExpression(1),
    AdditionExpression(
        FloatExpression(2),
        FloatExpression(3)
    )
)
# объект посетитель
expr_buffer = []
ExpressionPrinter.print(expr_buffer, expr1)
print(''.join(expr_buffer))
