"""Модуль 2"""

from module1 import M1

import module1

M2 = 200

print([
    name
    for name in globals().keys()
    if not name.startswith('__')
])

print(f'{M1 = }')
M1 = 150
print(f'{M1 = }')

print(f'{module1.M1 = }\n')

module1.M1 = 175
print(f'{module1.M1 = }')

print(f'{M1 = }\n')


