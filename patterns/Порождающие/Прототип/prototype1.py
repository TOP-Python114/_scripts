from copy import deepcopy
from dataclasses import dataclass


@dataclass
class Address:
    zipcode: str
    city: str
    street: str
    building: str
    office: str

    def __str__(self):
        return f'{self.zipcode}, {self.city}, ' \
               f'{self.street} {self.building}-{self.office}'


class Person:
    def __init__(self,
                 name: str,
                 home_address: Address,
                 office_address: Address,
                 position: str,):
        self.name = name
        self.home_address = home_address
        self.office_address = office_address
        self.position = position

    def __str__(self):
        return f'{self.name.title()} живёт по адресу {self.home_address}, ' \
               f'работает в должности {self.position} ' \
               f'по адресу {self.office_address}'



ivan = Person('Иван Иванович',
              Address('620001', 'Екатеринбург', 'ул. Тенистая', '5', '10'),
              Address('618010', 'Ревда', 'ул. Кремниевая', '118', '213'),
              'Разработчик серверных архитектур')
print(f'\n{ivan}')

yana = deepcopy(ivan)

yana.name = 'Яна Янова'
yana.home_address.street = 'ул. Лучистая'
yana.home_address.building = '25'
yana.home_address.office = '78'
yana.office_address.office = '214'
print(f'\n{yana}')

print(f'\n{ivan}')
