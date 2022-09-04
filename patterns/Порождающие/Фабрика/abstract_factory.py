from abc import ABC, abstractmethod


class Drink(ABC):
    DRINK = True
    @abstractmethod
    def drink(self):
        pass

class Tea(Drink):
    def drink(self):
        print('Чай вкусный')

class Coffee(Drink):
    def drink(self):
        print('Я не люблю кофе')


class DrinkFactory(ABC):
    @staticmethod
    @abstractmethod
    def prepare(amount: int):
        pass

class TeaFactory(DrinkFactory):
    @staticmethod
    def prepare(amount: int):
        """Имитация сложного процесса настройки объекта."""
        print('Кипятим воду')
        print(f'Кладём в чашку {amount // 20} г чайных листьев')
        print(f'Наливаем в чашку {amount} мл кипятка')
        return Tea()

class CoffeeFactory(DrinkFactory):
    @staticmethod
    def prepare(amount: int):
        """Имитация сложного процесса настройки объекта."""
        print(f'Кладём в турку {amount // 100} ч.л. молотого кофе')
        print(f'Наливаем в турку {amount} мл холодной воды')
        print('Держим кофе на слабом огне до закипания')
        return Coffee()


def make_drink(kind: str):
    """Возвращает определённое количество напитка нужного типа."""
    if kind.lower() in ('tea', 'чай'):
        return TeaFactory.prepare(200)
    elif kind.lower() in ('coffee', 'кофе'):
        return CoffeeFactory.prepare(50)
    else:
        return None

# what_do_you_want = input('Чай / Кофе ? ')
# hot_drink = make_drink(what_do_you_want)
# hot_drink.drink()



from enum import Enum
from inspect import getmembers, isclass, isabstract
from sys import modules

# разберите этот класс самостоятельно
class HotDrinkMachine:
    """Сбор информации о генерируемом объекте и возврат объекта."""
    AvailableDrinks = Enum(
        'AvailableDrinks',
        [
            pair[0]
            for pair in getmembers(
                modules[__name__],
                lambda obj: isclass(obj)
                            and getattr(obj, 'DRINK', False)
                            and not isabstract(obj)
            )
        ]
    )
    factories = {}
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for drink in self.AvailableDrinks:
                self.factories[drink] = eval(drink.name + 'Factory')()

    def print_drinks(self) -> None:
        """Отображение доступных напитков."""
        print('Напитки:')
        for drink in self.AvailableDrinks:
            print(f"{drink.value}. {drink.name}")

    def choose_drink(self) -> int:
        """Запрос к пользователю: вид напитка."""
        lf = len(self.AvailableDrinks)
        return int(input(f' > выберите напиток (1–{lf}): '))

    def choose_amount(self) -> int:
        """Запрос к пользователю: объём напитка."""
        return int(input(' > укажите объём (мл): '))

    def make_drink(self) -> Drink:
        """Генерация нужного объекта."""
        self.print_drinks()
        idx = self.choose_drink()
        amount = self.choose_amount()
        return self.factories[self.AvailableDrinks(idx)].prepare(amount)


hdm = HotDrinkMachine()
hdm.make_drink().drink()
