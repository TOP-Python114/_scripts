from abc import ABC, abstractmethod
from enum import Enum


class ListStrategy(ABC):
    @abstractmethod
    def start(self, buffer):
        pass

    @abstractmethod
    def add_item(self, buffer, item: str):
        pass

    @abstractmethod
    def end(self, buffer):
        pass


class Html(ListStrategy):
    def start(self, buffer):
        buffer.append('<ul>')

    def add_item(self, buffer, item: str):
        buffer.append(f'    <li>{item}</li>')

    def end(self, buffer):
        buffer.append('</ul>')


class Markdown(ListStrategy):
    def start(self, buffer):
        pass

    def add_item(self, buffer, item: str):
        buffer.append(f' * {item}')

    def end(self, buffer):
        pass


class OutputListStrategy(Enum):
    HTML = 1
    MARKDOWN = 2


class TextProcessor:
    def __init__(self, list_strategy: ListStrategy = Html()):
        self.strategy = list_strategy
        self.buffer: list[str] = []

    def set_items(self, item: str, *items: str):
        items = (item, ) + items
        self.strategy.start(self.buffer)
        for item in items:
            self.strategy.add_item(self.buffer, item)
        self.strategy.end(self.buffer)

    def set_output_strategy(self, output: OutputListStrategy):
        if output is OutputListStrategy.HTML:
            self.strategy = Html()
        elif output is OutputListStrategy. MARKDOWN:
            self.strategy = Markdown()

    def __str__(self):
        return '\n'.join(self.buffer)



menu_elements = ['File', 'Edit', 'View']

tp = TextProcessor()
tp.set_items(*menu_elements)
print(tp)

tp.set_output_strategy(OutputListStrategy.MARKDOWN)
tp.buffer.clear()

tp.set_items(*menu_elements)
print(tp)
