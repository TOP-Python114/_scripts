"""Компонент Модель (MVC) — работа с файлом."""

from dataclasses import dataclass
from pathlib import Path
from sys import path
from json import load as jload
import re

from pprint import pprint

SCRIPT_DIR = Path(path[0])
data_path = SCRIPT_DIR / 'people.json'


@dataclass
class Person:
    name: str
    age: int
    email: str
    phone: str
    country: str
    langs: list[str]

    def __str__(self):
        return self.name

    @staticmethod
    def get_all() -> tuple['Person', ...]:
        with open(data_path, 'r', encoding='utf-8') as f_in:
            data = jload(f_in)
        results = ()
        for person in data:
            person['langs'] = person['langs'].split()
            results += (Person(**person), )
        return results

    def does_speak(self, lang: str) -> bool:
        if re.match(r'^[A-Z]{2}$', lang):
            return lang in self.langs
        else:
            raise ValueError("'lang' should be an uppercase two-letter code")


if __name__ == '__main__':
    people = Person.get_all()
    print(len(people))
    print(people[-1].does_speak('KZ'))
    print(people[-1].does_speak('english'))
