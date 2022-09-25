# event broker
# CQS (command and query selector)

from abc import ABC, abstractmethod
from enum import Enum


class WhatToQuery(Enum):
    ATTACK = 0
    DEFENSE = 1


class Event(list):
    def __call__(self, *args, **kwargs):
        for function in self:
            function(*args, **kwargs)


class Query:
    def __init__(self,
                 creature_name: str,
                 what_to_query: WhatToQuery,
                 default_value: int):
        self.creature_name = creature_name
        self.what_to_query = what_to_query
        self.value = default_value


class Game:
    """Брокер событий."""
    def __init__(self):
        self.queries = Event()

    def perform_query(self,
                      sender: 'Creature',
                      query: Query):
        self.queries(sender, query)


class Creature:
    def __init__(self,
                 game: Game,
                 name: str,
                 initial_attack: int,
                 initial_defense: int):
        self.game = game
        self.name = name
        self.initial_attack = initial_attack
        self.initial_defense = initial_defense

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f'{self.name}: A={self.attack} / D={self.defense}'


class CreatureModifier(ABC):
    def __init__(self, game: Game, creature: Creature):
        self.game = game
        self.creature = creature
        self.game.queries.append(self.handle)

    @abstractmethod
    def handle(self, sender: Creature, query: Query):
        pass

    def remove_from_queries(self):
        self.game.queries.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender: Creature, query: Query):
        if self.creature.name == sender.name:
            if query.what_to_query is WhatToQuery.ATTACK:
                query.value *= 2


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self, sender: Creature, query: Query):
        if self.creature.name == sender.name:
            if query.what_to_query is WhatToQuery.DEFENSE:
                query.value += 1



new_game = Game()
goblin = Creature(new_game, 'Strong Goblin', 3, 2)
print(goblin)

dam = DoubleAttackModifier(new_game, goblin)
print(goblin)

dam.remove_from_queries()
print(goblin)
