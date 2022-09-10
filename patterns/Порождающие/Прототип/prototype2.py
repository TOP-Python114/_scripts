from dataclasses import dataclass, field
from copy import deepcopy


@dataclass
class Hero:
    name: str
    health: int = 250
    army: list = field(default_factory=list)

    def __str__(self):
        return f'{self.name}: {self.health}'


@dataclass
class Prototype:
    health: int = 100

    def __str__(self):
        return f'{self.__class__.__name__}: H={self.health}'

    def clone(self):
        return deepcopy(self)


@dataclass
class Soldier(Prototype):
    stamina: int = 50

    def __str__(self):
        par_str = super().__str__()
        return f'{par_str}, S={self.stamina}'


@dataclass
class Wizard(Prototype):
    mana: int = 35

    def __str__(self):
        par_str = super().__str__()
        return f'{par_str}, M={self.mana}'

@dataclass
class Trader(Prototype):
    charm: int = 10

    def __str__(self):
        par_str = super().__str__()
        return f'{par_str}, C={self.charm}'



zig = Hero('Зигфрид')

sold_prot = Soldier()
wiz_prot = Wizard()
trad_prot = Trader()

prots = (sold_prot, wiz_prot, trad_prot)

for i, j in enumerate((20, 5, 2)):
    for _ in range(j):
        zig.army.append(prots[i].clone())

print(zig)
for man in zig.army:
    print(f'\t{man}')
