# Dependency Inversion Principle — Принцип Инверсии Зависимости

from enum import Enum
from abc import abstractmethod


class Relations(Enum):
    """Перечислитель"""
    PARENT = 0
    CHILD = 1

class Person:
    """Информация о человеке"""
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"<Person: {self.name}>"


# интерфейс — прокладка между кодом низкого и верхнего уровней
class RelationshipsBrowser:
    @abstractmethod
    def find_all_children(self, name: str):
        pass


# переменная для аннотации типа
RelationType = list[tuple[Person, Relations, Person]]

class Relationships(RelationshipsBrowser):
    """Хранит информацию об отношениях между людьми."""
    def __init__(self):
        """Хранилище."""
        self.relations: RelationType = []

    def add_relation(self, parent: Person, child: Person):
        self.relations += [
            (parent, Relations.PARENT, child),
            (child, Relations.CHILD, parent)
        ]

    def find_all_children(self, name: str):
        """Низкоуровневая реализация метода для интерфейса, основанная на реализации хранилища."""
        for rel in self.relations:
            if rel[0].name == name and rel[1] == Relations.PARENT:
                yield rel[2]


class Research:
    """Класс верхнего уровня для работы с информацией об отношениях людей."""
    def __init__(self, relations_base: Relationships):
        self.base = relations_base
    
    # нарушение DIP — этот метод через индексацию в данном случае зависит 
    #   от того, как именно реализовано хранилище (списком кортежей) в классе 
    #   низкого уровня
    # def find_all_children(self, name):
    #     for rel in self.base.relations:
    #         if rel[0].name == name and rel[1] == Relations.PARENT:
    #             yield rel[2]
    
    # метод, независимый от способа хранения информации
    def find_all_children(self, name: str):
        return self.base.find_all_children(name)


db = Relationships()
db.add_relation(Person('John'), Person('Matt'))
db.add_relation(Person('John'), Person('Chris'))
db.add_relation(Person('Kate'), Person('Max'))

r = Research(db)
print(*r.find_all_children('John'), sep='\n')
