"""Пример нарушения и релизации Принципа Единственной Ответственности (SRP)."""

from pathlib import Path
from sys import executable


class Journal:
    """Класс для хранения и взаимодействия с записями."""
    def __init__(self):
        self.entries = []
    
    def add_entry(self, entry):
        if not isinstance(entry, str):
            raise TypeError('можно добавлять только текстовые данные')
        self.entries += [entry]
    
    def del_entry(self, entry):
        try:
            i = self.entries.index(entry)
        except IndexError:
            pass
        else:
            del self.entries[i]
    
    # нарушение приципа единственной ответственности — работа с файловой системой не является ответственностью класса Journal
    # default_path = Path(executable).drive + r'\windows\temp\journal.log'
    # def save_to_file(self, path=None):
        # if not path:
            # path = self.__class__.default_path
        # with open(path, 'a') as fh:
            # print(*self.entries, sep='\n', file=fh)

    def __str__(self):
        return '\n'.join(map(str, self.entries))


class FileManager:
    """Интерфейс, позволяющий осуществлять сохранение объектов в файл."""
    default_path = Path(executable).drive + r'\windows\temp\journal.log'
    @staticmethod
    def save_to_file(object, path=None):
        if not path:
            path = FileManager.default_path
        with open(path, 'a') as fh:
            print(str(object), file=fh)


j = Journal()
for i in range(10, 100, 10):
    j.add_entry(str(i))
# j.save_to_file()
FileManager.save_to_file(j)

journal_path = Path(executable).drive + r'\windows\temp\journal.log'
with open(journal_path) as fh:
    print(fh.read())
