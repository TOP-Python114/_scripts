from abc import ABC, abstractmethod


class PNGInterface(ABC):
    @abstractmethod
    def draw(self):
        pass


class PNGImage(PNGInterface):
    def __init__(self, image_path):
        self.path = image_path
        self.format = 'raster'

    def draw(self):
        return 'Drawing ' + self.get_image()

    @staticmethod
    def get_image():
        return 'png'


# модуль, который вы нашли для работы с векторными изображениями
# но он не работает с вашим интерфейсом — отсутствует метод draw()
class SVGImage:
    def __init__(self, image_path):
        self.path = image_path
        self.format = 'vector'

    @staticmethod
    def render():
        return 'svg'


class SVGAdapter:
    """Адаптер для растрирования векторных изображений и сопряжения с интерфейсом вывода растровых изображений."""
    def __init__(self, svg: SVGImage):
        self.svg = svg

    def rasterize(self):
        return 'rasterized ' + self.svg.render()

    def draw(self):
        return 'Drawing ' + self.rasterize()



png = PNGImage('picture.png')
print(png.draw())

svg = SVGImage('figure.svg')
svg_raster = SVGAdapter(svg)
print(svg_raster.draw())
