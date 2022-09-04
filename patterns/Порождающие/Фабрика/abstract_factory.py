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
