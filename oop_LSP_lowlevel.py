"""Модуль низкого уровня"""

# Liskov Substitution Principle — Принцип Подстановки Лисков

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def area(self):
        return self._width * self._height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value


# класс нарушает LSP
class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
    
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value
    
    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value
