"""Игра Сапёр — демонстратор использования архитектурного подхода MVC с GUI."""
from typing import Optional
from random import randrange as rr


class Cell:
    """Описывает сущность одной клетки игрового поля."""
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column
        self.state: str = 'closed'
        self.mined: bool = False
        self.counter: int = 0

    mark_sequence = ('closed', 'flagged', 'questioned')
    def next_mark(self) -> None:
        """Циклически переключает состояния клетки."""
        if self.state in self.mark_sequence:
            i = self.mark_sequence.index(self.state)
            self.state = self.mark_sequence[(i+1) % len(self.mark_sequence)]

    def open(self) -> None:
        """Переключает клетку в состояние 'открыто'."""
        if self.state != 'flagged':
            self.state = 'opened'


MIN_ROWS = 5
MAX_ROWS = 30

MIN_COLUMNS = 5
MAX_COLUMNS = 30

MIN_MINES = 1
MAX_MINES = 800


# noinspection PyAttributeOutsideInit
class Model:
    """Моделирует игровое поле и игровые действия."""
    def __init__(self):
        self.start_game()

    def start_game(self, rows: int = 15, columns: int = 15, mines: int = 50) -> None:
        """Инициализирует клетки нового игрового поля.

        :param rows: количество строк игрового поля
        :param columns: количество столбцов игрового поля
        :param mines: количество мин на игровом поле
        """
        self.first_step = True
        self.game_over = False

        if MIN_ROWS <= rows <= MAX_ROWS:
            self.rows = rows
        if MIN_COLUMNS <= columns <= MAX_COLUMNS:
            self.columns = columns
        if MIN_MINES <= mines <= MAX_MINES:
            self.mines = mines

        self.table = []
        for i in range(self.rows):
            self.table += [[]]
            for j in range(self.columns):
                self.table[i][j] += [Cell(i, j)]

    def generate_mines(self) -> None:
        """Располагает заданное количество мин на случайных клетках игрового поля."""
        for _ in range(self.mines):
            while True:
                row = rr(self.rows)
                column = rr(self.columns)
                cell = self.table[row][column]
                if cell.state != 'opened' and not cell.mined:
                    cell.mined = True
                    break

    def is_win(self) -> bool:
        """Проверяет, достигнут ли выигрыш."""
        for row in self.table:
            for cell in row:
                if not cell.mined and cell.state not in ('opened', 'flagged'):
                    return False
        return True

    def is_game_over(self) -> bool:
        """Проверяет, случился ли проигрыш."""
        return self.game_over

    def get_cell(self, row: int, column: int) -> Optional[Cell]:
        """Возвращает клетку по заданным индексам, если индексы находятся в заданном диапазоне, иначе None."""
        if 0 <= row < self.rows and 0 <= column < self.columns:
            return self.table[row][column]
        else:
            return None

    def get_cell_neighbours(self, row: int, column: int) -> list[Cell]:
        """Возвращает список клеток, соседних с клеткой, заданной переданными индексами."""
        neighbours = []
        for i in range(row-1, row+2):
            neighbours += [self.get_cell(i, column-1)]
            if i != row:
                neighbours += [self.get_cell(i, column)]
            neighbours += [self.get_cell(i, column+1)]
        return neighbours

    def get_mines_around_cell(self, row: int, column: int) -> int:
        """Подсчитывает и возвращает количество заминированных клеток рядом с клеткой, заданной переданными индексами."""
        neighbours = self.get_cell_neighbours(row, column)
        return sum(1 for cell in neighbours if cell.mined)

    def next_cell_mark(self, row: int, column: int) -> None:
        """Переключает отметку на клетке."""
        cell = self.get_cell(row, column)
        if cell:
            cell.next_mark()

    def open_cell(self, row: int, column: int) -> None:
        """Открывает клетку, проверяет мину, подсчитывает количество мин рядом с открытой, рекурсивно открывает соседние пустые клетки."""
        cell = self.get_cell(row, column)
        if not cell:
            return

        cell.open()

        if cell.mined:
            self.game_over = True
            return

        if self.first_step:
            self.first_step = False
            self.generate_mines()

        cell.counter = self.get_mines_around_cell(row, column)

        if cell.counter == 0:
            neighbours = self.get_cell_neighbours(row, column)
            for n_cell in neighbours:
                if n_cell.state == 'closed':
                    self.open_cell(n_cell.row, n_cell.column)


