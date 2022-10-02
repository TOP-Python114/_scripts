"""Демонстратор наблюдателя: наблюдатель с автоматической отменой подписки."""

from abc import ABC


class Observers(list):
    """Список методов наблюдателей."""
    def __call__(self, *args, **kwargs):
        for observer in self:
            observer(*args, **kwargs)


class Observable(ABC):
    def __init__(self):
        self.properties_changed = Observers()


class Person(Observable):
    """Субъект наблюдения."""
    def __init__(self, age: int = 0):
        super().__init__()
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if self.__age == value:
            return
        self.__age = value
        self.properties_changed('age', value)


class TrafficAuthority:
    """Сущность наблюдатель."""
    def __init__(self, person: Person):
        self.person = person
        self.person.properties_changed.append(self.age_changed)

    def age_changed(self, prop_name: str, prop_value: int):
        if prop_name == 'age':
            if prop_value < 16:
                print('Вам запрещено управлять автомобилем.')
            else:
                print('Вам разрешено управлять автомобилем.')
                self.person.properties_changed.remove(self.age_changed)


guy = Person()
gibdd = TrafficAuthority(guy)

for age in (14, 14, 15, 16, 17, 18):
    print(f'{age = }')
    guy.age = age
