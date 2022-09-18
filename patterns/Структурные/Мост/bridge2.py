from abc import ABC, abstractmethod


class Material(ABC):
    hits: float
    @abstractmethod
    def __str__(self):
        pass


class Straw(Material):
    hits = 0.75
    def __str__(self):
        return 'straw'


class Wooden(Material):
    hits = 1
    def __str__(self):
        return 'wooden'


class Cobblestone(Material):
    hits = 1.2
    def __str__(self):
        return 'cobblestone'


class Brick(Material):
    hits = 1.5
    def __str__(self):
        return 'brick'



class Building(ABC):
    @abstractmethod
    def show_name(self) -> str:
        pass


class Tower(Building):
    base_hitpoints = 300

    def __init__(self, name: str, material: Material):
        self.name = name
        self.material = material
        self.hitpoints = int(self.base_hitpoints * material.hits)

    def show_name(self) -> str:
        return f'{self.material} tower {self.name}: ' \
               f'{self.hitpoints} HP'


class Wall(Building):
    base_hitpoints = 100

    def __init__(self, name: str, material: Material):
        self.name = name
        self.material = material
        self.hitpoints = int(self.base_hitpoints * material.hits)

    def show_name(self) -> str:
        return f'{self.material} wall {self.name}: ' \
               f'{self.hitpoints} HP'


class Mill(Building):
    base_hitpoints = 150

    def __init__(self, name: str, material: Material):
        self.name = name
        self.material = material
        self.hitpoints = int(self.base_hitpoints * material.hits)

    def show_name(self) -> str:
        return f'{self.material} mill {self.name}: ' \
               f'{self.hitpoints} HP'


wst = Tower(
    'West Watch Tower',
    Cobblestone()
)
print(wst.show_name())

w1 = Wall(
    'West Wall 1',
    Straw()
)
w2 = Wall(
    'West Wall 2',
    Straw()
)
print(w1.show_name(), w2.show_name(), sep='\n')
