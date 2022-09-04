from math import cos, sin


class Point:
    class Factory:
        @staticmethod
        def cartesian(x: float, y: float) -> 'Point':
            """Создаёт объект точки, заданной декартовыми координатами."""
            new = Point()
            new.x = round(x, 1)
            new.y = round(y, 1)
            new.r = round((x**2 + y**2)**0.5, 1)
            return new

        @staticmethod
        def polar(rho: float, phi: float) -> 'Point':
            """Создаёт объект точки, заданной полярными координатами."""
            new = Point()
            new.x = round(rho * cos(phi), 1)
            new.y = round(rho * sin(phi), 1)
            return new

    # экземпляр фабрики в пространстве имён объекта класса
    factory = Factory()
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<{self.__class__.__name__}: x={self.x}, y={self.y}>"

    def __str__(self):
        return f"({self.x}; {self.y})"


p0 = Point()
p1 = Point.factory.cartesian(3.5, 1.9)
p2 = Point.factory.polar(4, 0.5)
p3 = Point(3.5, 1.9)

for i in range(4):
    print(globals()[f'p{i}'])
