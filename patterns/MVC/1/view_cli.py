"""Компонент Представление (MVC) — интерфейс командной строки."""

from time import sleep
from typing import Collection

import re


def start_view() -> None:
    print('Приветствую в Демонстраторе MVC!')
    sleep(2)


def ask_if_show_all() -> str:
    prompt = 'Хотите вывести всю информацию из БД [д/н]?\n'
    while True:
        inp = input(prompt)
        if re.match(r'^[днyn]$', inp):
            break
    return inp


def show_all_view(data: Collection) -> None:
    print(f'В БД всего {len(data)} элементов')
    for elem in data:
        print(elem)
    sleep(10)


def end_view() -> None:
    print('Пока!')
    sleep(2)
