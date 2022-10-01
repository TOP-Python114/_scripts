"""Демонстратор шаблона Хранитель: инфраструктура для работы с состояниями."""

from dataclasses import dataclass, field


@dataclass
class CharacterState:
    """Состояние персонажа.

    Хранитель (memento)
    """
    health: int
    level: int
    inventory: list[str]
    position: dict[str, int]

    def __str__(self):
        return (f'X={self.position["x"]} Y={self.position["y"]},'
                f' HP{self.health}, LVL{self.level},'
                f' INV: ' + ', '.join(self.inventory))


@dataclass
class Character:
    """Персонаж игры.

    Инициатор (originator)
    """
    name: str
    health: int = 10
    level: int = 1
    inventory: list[str] = field(default_factory=list)
    position: dict[str, int] = field(default_factory=dict, init=False)

    def __post_init__(self):
        self.name = self.name.title()
        self.position = {'x': 0, 'y': 0}

    def __str__(self):
        return f'{self.name}: HP{self.health}, LVL{self.level}'

    def move(self, delta_x: int = 1, delta_y: int = 1):
        self.position['x'] += delta_x
        self.position['y'] += delta_y

    def hit(self):
        self.health -= 1

    def progress(self):
        self.level += 1

    def get_item(self, item: str):
        self.inventory += [item]

    def drop_item(self, item: str):
        self.inventory.remove(item)

    @property
    def state(self) -> CharacterState:
        return CharacterState(
            self.health,
            self.level,
            self.inventory.copy(),
            self.position.copy()
        )

    @state.setter
    def state(self, ch_state: CharacterState):
        self.health = ch_state.health
        self.level = ch_state.level
        self.inventory = ch_state.inventory
        self.position = ch_state.position


class SaveLoadMenu:
    """Управление состояниями персонажа: сохранение и загрузка состояний.

    Опекун (caretaker)
    """
    def __init__(self, character: Character):
        self.character = character
        self._saves: list[CharacterState] = []

    def save(self) -> None:
        self._saves += [self.character.state]

    def _show_saves(self) -> None:
        print(f'\nСохранения для {self.character.name}:')
        for i, save in enumerate(self._saves, 1):
            print(f'\t{i}. {save}')

    def _get_slot_number(self) -> int:
        while True:
            inp = input(' номер слота > ')
            if inp.isdecimal():
                inp = int(inp) - 1
                if 0 <= inp < len(self._saves):
                    break
                else:
                    print('... вводите цифры, соответствующие номеру слота ...')
            else:
                print('... вводите символы цифр ...')
        return inp

    def load(self):
        self._show_saves()
        i = self._get_slot_number()
        self.character.state = self._saves[i]



hero = Character('Люк Скайуокер')
menu = SaveLoadMenu(hero)
print(hero)

hero.move(3, 5)
hero.hit()
hero.hit()
hero.hit()
hero.progress()

menu.save()
print(hero)

hero.move(2, -1)
hero.get_item('бластер')
hero.move(1, -1)
hero.hit()
hero.hit()
hero.move(-4, 4)

menu.save()
print(hero)

menu.load()
print(hero)
