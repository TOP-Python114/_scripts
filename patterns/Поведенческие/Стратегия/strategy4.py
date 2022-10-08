from abc import ABC, abstractmethod
from enum import Enum
from random import choice


class Item(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    LIZARD = 3
    SPOK = 4

    @classmethod
    def rand(cls):
        return choice(list(cls))


class Tie(Exception):
    pass


class Strategy(ABC):
    item: Item

    @staticmethod
    @abstractmethod
    def check(other: Item) -> bool:
        pass


class Rock(Strategy):
    item = Item.ROCK

    # нарушает OCP
    @staticmethod
    def check(other: Item) -> bool:
        if other is Item.PAPER or other is Item.SPOK:
            return False
        if other is Item.SCISSORS or other is Item.LIZARD:
            return True
        if other is Item.ROCK:
            raise Tie


class Paper(Strategy):
    item = Item.PAPER

    # нарушает OCP
    @staticmethod
    def check(other: Item) -> bool:
        if other is Item.SCISSORS or other is Item.LIZARD:
            return False
        if other is Item.ROCK or other is Item.SPOK:
            return True
        if other is Item.PAPER:
            raise Tie


class Scissors(Strategy):
    item = Item.SCISSORS

    # нарушает OCP
    @staticmethod
    def check(other: Item) -> bool:
        if other is Item.ROCK or other is Item.SPOK:
            return False
        if other is Item.PAPER or other is Item.LIZARD:
            return True
        if other is Item.SCISSORS:
            raise Tie


class Lizard(Strategy):
    item = Item.LIZARD

    # нарушает OCP
    @staticmethod
    def check(other: Item):
        if other is Item.ROCK or other is Item.SCISSORS:
            return False
        if other is Item.PAPER or other is Item.SPOK:
            return True
        if other is Item.LIZARD:
            raise Tie


class Spok(Strategy):
    item = Item.LIZARD

    # нарушает OCP
    @staticmethod
    def check(other: Item):
        if other is Item.PAPER or other is Item.LIZARD:
            return False
        if other is Item.SCISSORS or other is Item.ROCK:
            return True
        if other is Item.SPOK:
            raise Tie


class Random(Strategy):
    def __init__(self):
        self.item = Item.rand()

    # нарушает OCP
    def check(self, other: Item):
        if self.item is Item.ROCK:
            return Rock.check(other)
        if self.item is Item.PAPER:
            return Paper.check(other)
        if self.item is Item.SCISSORS:
            return Scissors.check(other)
        if self.item is Item.LIZARD:
            return Lizard.check(other)
        if self.item is Item.SPOK:
            return Spok.check(other)



class Player:
    def __init__(self, name: str, strategy=None):
        self.name = name
        self.change_strategy(strategy)

    def change_strategy(self, strategy=None):
        if strategy is None:
            self.strategy = Random()
        else:
            self.strategy = strategy

    def play(player1, player2: 'Player'):
        try:
            if player1.strategy.check(player2.strategy.item):
                print(f'{player1.name} WINS')
            else:
                print(f'{player2.name} WINS')
        except Tie:
            print('TIE')

    def __str__(self):
        return f'{self.name}: {self.strategy.item.name}'


ivan = Player('Ivan')
serge = Player('Serge')

print(ivan, serge, sep='\n')
ivan.play(serge)
