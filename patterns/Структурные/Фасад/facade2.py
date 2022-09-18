"""Моделирование симуляции."""

from random import shuffle
from typing import MutableSequence


class Hawk:
    """Модель ястреба."""
    def __init__(self):
        self.name = 'H'
        self.alive = True
        self.reproducing = False

    def __str__(self):
        return self.name

    @staticmethod
    def move() -> str:
        return 'attack'

    @staticmethod
    def reproduce() -> 'Hawk':
        return Hawk()


class Dove:
    """Модель голубя."""
    def __init__(self):
        self.name = 'D'
        self.alive = True
        self.reproducing = True

    def __str__(self):
        return self.name

    @staticmethod
    def move() -> str:
        return 'defend'

    @staticmethod
    def reproduce() -> 'Dove':
        return Dove()


def iteration(species: list[Hawk, Dove]) -> list[Hawk, Dove]:
    half = len(species) // 2
    part1 = species[:half]
    part2 = species[half:]

    for a1, a2 in zip(part1, part2):
        move1, move2 = a1.move(), a2.move()

        if move1 == 'attack':
            if move2 == 'attack':
                # два ястреба
                a1.alive = False
                a2.alive = False
            elif move2 == 'defend':
                # ястреб и голубь
                a1.reproducing = True
                a2.alive = False
        elif move1 == 'defend':
            if move2 == 'attack':
                # голубь и ястреб
                a1.alive = False
                a2.reproducing = True
            elif move2 == 'defend':
                # два голубя
                a1.reproducing = False
                a2.reproducing = False

    species = []
    for animal in part1 + part2:
        if animal.alive:
            species.append(animal)
            if animal.reproducing:
                species.append(animal.reproduce())

    return species


class Simulation:
    """Предоставляет интерфейс для работы с симуляциями."""
    def __init__(self, hawk_number: int, dove_number: int):
        self.population = []
        for _ in range(hawk_number):
            self.population.append(Hawk())
        for _ in range(dove_number):
            self.population.append(Dove())
        shuffle(self.population)

    def iterate(self) -> bool:
        """Выполняет один шаг симуляции. Возвращает True, если в популяции остались животные. Иначе — False"""
        self.population = iteration(self.population)
        shuffle(self.population)
        return bool(self.population)

    def show_animals(self):
        return ' '.join(
            str(animal)
            for animal in self.population
        )


hawks, doves = 5, 20
s = Simulation(hawks, doves)
print(f'Начало: {hawks}/{doves}\n{s.show_animals()}\n')

for _ in range(7):
    s.iterate()
    print(s.show_animals())
