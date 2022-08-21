from pprint import pprint


def counter(start: int, end: int):
    """Генерирует числа в заданном диапазоне."""
    for n in range(start, end):
        yield n


cnt = counter(5, 10)
print(f'{cnt = }')
print(f'{type(cnt) = }\n')

pprint(dir(cnt))

print(f'\n{cnt.__next__() = }')
print(f'{cnt.__next__() = }')
print(f'{cnt.__next__() = }')
print(f'{cnt.__next__() = }')
print(f'{cnt.__next__() = }')
try:
    print(f'{next(cnt)}')
except StopIteration:
    print('StopIteration: генераторная функция завершила работу\n')

print('cnt = counter(5, 10)')
cnt = counter(5, 10)
print(list(cnt))
print(list(cnt))
