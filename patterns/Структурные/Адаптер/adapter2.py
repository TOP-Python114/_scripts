from abc import ABC, abstractmethod


class PNGInterface(ABC):
    @abstractmethod
    def draw(self):
        pass


class PNGImage(PNGInterface):
    def __init__(self, image_path):
        self.path = image_path
        self.format = image_path.rsplit('.', 1)[-1].upper()
        self.type = 'raster'

    def draw(self):
        return 'Drawing ' + self.get_image()

    @staticmethod
    def get_image():
        return 'png'


class BMPImage:
    def __init__(self, image_path=None):
        self.path = image_path
        self.format = 'BMP'
        self.type = 'raster'

    @staticmethod
    def get_image():
        return 'bmp'


class SVGImage:
    def __init__(self, image_path):
        self.path = image_path
        self.format = image_path.rsplit('.', 1)[-1].upper()
        self.type = 'vector'

    @staticmethod
    def render():
        return 'svg'


class UnknownImageType(Exception):
    pass

class UnknownImageFormat(Exception):
    pass


class ImageAdapter(PNGInterface):
    def __init__(self, image_obj):
        self.image = image_obj

    def rasterize(self):
        return BMPImage()

    def bmp_to_png(self, image_obj):
        if image_obj.format == 'BMP':
            return 'converted ' + image_obj.get_image()
        else:
            raise UnknownImageFormat

    def draw(self):
        if self.image.type == 'vector':
            return 'Drawing ' + self.bmp_to_png(self.rasterize())
        elif self.image.type == 'raster':
            return 'Drawing ' + self.image.get_image()
        else:
            raise UnknownImageType


png = PNGImage('picture.png')
svg = SVGImage('figure.svg')

png_prep = ImageAdapter(png)
svg_prep = ImageAdapter(svg)

print(png_prep.draw())
print(svg_prep.draw())
