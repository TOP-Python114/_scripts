"""Игра Сапёр — демонстратор использования архитектурного подхода MVC с GUI."""


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


