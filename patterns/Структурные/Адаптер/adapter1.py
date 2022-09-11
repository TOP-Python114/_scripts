from abc import ABC, abstractmethod


class RasterInterface(ABC):
    @abstractmethod
    def draw(self):
        pass


class RasterImage(RasterInterface):
    def __init__(self, image_path):
        self.path = image_path

    def draw(self):
        return 'Drawing ' + self.get_image()

    @staticmethod
    def get_image():
        return 'png'


# модуль, который вы нашли для работы с векторными изображениями
# но он не работает с вашим интерфейсом — отсутствует метод draw()
class VectorImage:
    def __init__(self, image_path):
        self.path = image_path

    @staticmethod
    def render():
        return 'svg'


class VectorAdapter:
    """Адаптер для растрирования векторных изображений и сопряжения с интерфейсом вывода растровых изображений."""
    def __init__(self, svg: VectorImage):
        self.svg = svg

    def rasterize(self):
        return 'rasterized ' + self.svg.render()

    def draw(self):
        return 'Drawing ' + self.rasterize()



png = RasterImage('picture.png')
print(png.draw())

svg = VectorImage('figure.svg')
svg_raster = VectorAdapter(svg)
print(svg_raster.draw())
