from enum import Enum
from math import cos, sin


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    # плохой вариант
    # def __init__(self,
    #              a: float,
    #              b: float,
    #              system: CoordinateSystem = CoordinateSystem.CARTESIAN):
    #     if system is CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system is CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = a * sin(b)

    # хороший вариант
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @staticmethod
    def cartesian(x: int, y: int) -> 'Point':
        """Создаёт объект точки, заданной декартовыми координатами.

        :param x координата оси абсцисс
        :param y координата оси ординат
        """
        return Point(x, y)

    @staticmethod
    def polar(rho: float, phi: float) -> 'Point':
        """Создаёт объект точки, заданной полярными координатами.

        :param rho (ρ) радиальная компонента
        :param phi (φ) азимут (в радианах)
        """
        x = rho * cos(phi)
        y = rho * sin(phi)
        return Point(x, y)

    def __repr__(self):
        return f"<{self.__class__.__name__}: x={self.x}, y={self.y}>"

    def __str__(self):
        return f"({self.x}; {self.y})"


p_zero = Point(0, 0)
p1 = Point(1, 3)
# p2 = Point(4, 0.5, CoordinateSystem.POLAR)
p2 = Point.polar(4, 0.5)
p3 = Point.cartesian(6, 10)

print(p_zero, p1, p2, p3, sep='\n')
