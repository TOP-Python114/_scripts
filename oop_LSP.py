"""Модуль верхнего уровня"""

# Liskov Substitution Principle — Принцип Подстановки Лисков

from oop_LSP_lowlevel import Rectangle, Square


def high_level_function(shape: Rectangle):
    w = shape.width
    shape.height = 10
    area_expected = w*10
    print(f"Ождиаемая площадь: {area_expected}, "
          f"полученная через метод: {shape.area}")


rect1 = Rectangle(2, 3)
high_level_function(rect1)

square1 = Square(3)
high_level_function(square1)
