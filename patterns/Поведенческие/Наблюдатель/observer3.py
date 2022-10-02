"""Демонстратор наблюдателя: вызываемый список наблюдателей."""

from dataclasses import dataclass


class Observers(list):
    def __call__(self, *args, **kwargs):
        for observer in self:
            observer(*args, **kwargs)


@dataclass
class Person:
    name: str
    address: str

    def __post_init__(self):
        self.falls_ill = Observers()

    def catch_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name: str, address: str):
    print(f'{name} нуждается в докторе по адресу {address}')



ivan = Person('Иван', 'пр. Ленина 72')

ivan.falls_ill.append(
    lambda name, address: print(f'{name} заболел')
)
ivan.falls_ill.append(call_doctor)

ivan.catch_cold()

