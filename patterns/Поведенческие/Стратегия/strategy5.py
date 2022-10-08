from abc import ABC, abstractmethod
from enum import Enum


class GameCharacter:
    def __init__(self):
        self.position: list[float] = [0, 0]

    def move(self, movement_style):
        movement_style(self.position)


class IMove(ABC):
    @staticmethod
    @abstractmethod
    def __call__(position: list[int]):
        pass


class Walk(IMove):
    @staticmethod
    def __call__(position: list[int]):
        position[0] += 1
        print(f'Иду. Новое месторасположение: {position}')


class Run(IMove):
    @staticmethod
    def __call__(position: list[int]):
        position[0] += 2
        print(f'Бегу. Новое месторасположение: {position}')


class Crawl(IMove):
    @staticmethod
    def __call__(position: list[int]):
        position[0] += 0.5
        print(f'Крадусь. Новое месторасположение: {position}')



class MoveStyle(Enum):
    WALK = Walk()
    RUN = Run()
    CRAWL = Crawl()


hero = GameCharacter()
hero.move(MoveStyle.WALK.value)
hero.move(MoveStyle.RUN.value)
hero.move(MoveStyle.CRAWL.value)
