from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable


class Item(ABC):
    # @abstractmethod
    # def return_price(self):
    #     pass
    def return_price(self):
        return f'{self.price} ₽'


@dataclass
class Phone(Item):
    price: int

    # def return_price(self):
    #     return f'{self.price} ₽'


@dataclass
class Charger(Item):
    price: int

    # def return_price(self):
    #     return f'{self.price} ₽'


@dataclass
class Earphones(Item):
    price: int

    # def return_price(self):
    #     return f'{self.price} ₽'


@dataclass()
class Box(Item):
    contents: Iterable

    def return_price(self):
        price = 0
        for obj in self.contents:
            price += obj.price
        return f'{price} ₽'


smartphone1 = Phone(52450)
print(f'Стоимость смартфона без аксессуаров: {smartphone1.return_price()}')

package = Box([
    smartphone1,
    Charger(2350),
    Earphones(7500)
])
print(f'Стоимость смартфона с аксессуарами: {package.return_price()}')
