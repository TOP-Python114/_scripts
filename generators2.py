from typing import Generator


def counter(start: int, end: int) -> Generator:
    """Генерирует числа в заданном диапазоне."""
    for n in range(start, end):
        yield n
        yield n


cnt = counter(5, 10)
for c in cnt:
    print(c, end=' ')
print()


def inf_count(start: int, step: int = 1) -> Generator:
    while True:
        yield start
        start += step


cnt2 = inf_count(0)
# в cmd используй Ctrl+C, чтобы прервать выполнение скрипта
for n in cnt2:
    print(n)
