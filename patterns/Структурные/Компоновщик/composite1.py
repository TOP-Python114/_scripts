from abc import ABC, abstractmethod
from dataclasses import dataclass


class VectorGraphic(ABC):
    @abstractmethod
    def render(self):
        pass


@dataclass
class Line(VectorGraphic):
    name: str
    length: float

    def render(self):
        print(f'{self.name}: {self.length}')


@dataclass
class Text(VectorGraphic):
    name: str
    text: str

    def render(self):
        print(self.text)


class Group(VectorGraphic):
    def __init__(self, name: str):
        self.name = name
        self.__elements: list[VectorGraphic] = []

    @property
    def elements(self):
        return iter(self.__elements)

    def add_elements(self, *args: VectorGraphic):
        self.__elements += list(args)

    def render(self):
        for elem in self.elements:
            elem.render()


line1 = Line('AB', 2)
line2 = Line('BC', 5)
line3 = Line('CD', 2)
line4 = Line('DA', 5)
formula = Text('perimeter', 'P = AB + BC + CD + DA')

line4.render()
formula.render()

print('\n')

figure = Group('perimeter_formula1')
figure.add_elements(line1, line2, formula, line3, line4)
figure.render()
