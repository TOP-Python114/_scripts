# существующая объектная модель: Vector, Raster
# наша объектная модель: square, triangle, circle, ...

from dataclasses import dataclass

@dataclass
class VectorSquare:
    name: str
    def render(self):
        return f'vector square {self.name}'

@dataclass
class RasterSquare:
    name: str
    def render(self):
        return f'raster square {self.name}'

# class VectorTriangle
# class RasterTriangle
# class VectorCircle
# class RasterCircle
# ...
# увеличение количества фигур и/или количества интерфейсов приведёт к взрывному росту количества необходимых классов


class IVector:
    """Интерфейс для отображения объекта в векторном виде.

    Адаптер для существующего интерфейса Vector.
    Мост для нашей объектной модели, использующей интерфейс Vector.
    """
    @staticmethod
    def render(image):
        """Полиморфный метод."""
        return f'vector {image}'


class IRaster:
    """Интерфейс для отображения объекта в растровом виде.

    Адаптер для существующего интерфейса Raster.
    Мост для нашей объектной модели, использующей интерфейс Raster.
    """
    @staticmethod
    def render(image):
        """Полиморфный метод."""
        return f'raster {image}'


class Shape:
    """Базовый класс геометрических фигур, использующий мосты для отображения с помощью различных интерфейсов."""
    def __init__(self, renderer: IVector | IRaster):
        self._interface = renderer

    def draw(self):
        return self._interface.render(self.__class__.__name__)


class Square(Shape):
    pass

class Triangle(Shape):
    pass

class Circle(Shape):
    pass


render_vector = IVector()
render_raster = IRaster()

sq1 = Square(render_raster)
tr1 = Triangle(render_raster)
tr2 = Triangle(render_vector)
cr1 = Circle(render_vector)

for shape in (sq1, tr1, tr2, cr1):
    print(shape.draw())
