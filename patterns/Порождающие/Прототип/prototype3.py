from random import choice as ch
from string import ascii_letters as asl
from time import sleep
from copy import deepcopy
from datetime import datetime as dt


class Prototype:
    def __init__(self, field_len: int):
        self.field1 = ''.join(ch(asl) for _ in range(field_len-2))
        self.field2 = ''.join(ch(asl) for _ in range(field_len-1))
        self.field3 = ''.join(ch(asl) for _ in range(field_len))
        self.field4 = ''.join(ch(asl) for _ in range(field_len+1))
        self.field5 = ''.join(ch(asl) for _ in range(field_len+2))
        sleep(2.5)

    def clone(self):
        return deepcopy(self)


def cur_mins():
    print(f'{dt.now():%M мин %S с %f}\b\b\b мс')


print('Старт:', end=' ')
cur_mins()

inst1 = Prototype(25)
print('Создан первый экземпляр:', end=' ')
cur_mins()

for _ in range(100):
    inst1.clone()
print('Созданы клоны:', end=' ')
cur_mins()
