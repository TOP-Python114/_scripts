from pathlib import Path
from sys import path, stderr

from configparser import ConfigParser
from mysql.connector import MySQLConnection, Error

DEBUG = True


path_like = str | Path

class PersistenceManager:
    """
    Подключение к серверу MySQL и базе данных по её имени. Обработка запросов.
    Для использования в менеджере контекста.
    """
    db_config_path: path_like = Path(path[0]) / 'db_config.ini'

    @classmethod
    def read_db_config(cls):
        db_config = ConfigParser()
        with open(cls.db_config_path, encoding='utf-8') as filein:
            db_config.read_file(filein)
        return db_config

    def __init__(self, db_name: str, config_path: path_like = None):
        if config_path is not None:
            self.__class__.db_config_path = config_path
        config = self.read_db_config()['Connection']
        try:
            self.connection = MySQLConnection(
                **config,
                database=db_name
            )
            if DEBUG:
                if self.connection.is_connected():
                    print(f'Соединение с "{self.connection.server_host}:{self.connection.server_port}" установлено')
        except Error as e:
            print(e, file=stderr)

    def select_query(self, query: str) -> list[tuple]:
        with self.connection.cursor() as cursor:
            if DEBUG:
                print(cursor)
            cursor.execute(query)
            return cursor.fetchall()

    def insert_query(self, query: str, values: list[tuple] = None) -> None:
        with self.connection.cursor() as cursor:
            if DEBUG:
                print(cursor)
            if values is None:
                cursor.execute(query)
            else:
                cursor.executemany(query, values)
            self.connection.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


# тесты
if __name__ == '__main__':

    db_dir = Path(r'd:\G-Doc\YandexDisk\Job\TOP Academy\Python web\114\scripts\databases\world')


    selects_world = [
        file.read_text()
        for file in db_dir.glob('*.sql')
        if 'example' not in file.name
    ]
    print(*selects_world, sep='\n'*2)

    with PersistenceManager('world') as db_handler:
        for query in selects_world:
            print(db_handler.select_query(query), end='\n\n')


    insert_single_value = (
        "insert into curators"
        "   (name, surname)"
        "values"
        "   ('Боб', 'Дилан')"
    )
    insert_template = (
        "insert into curators"
        "   (name, surname)"
        "values"
        "   (%s, %s)"
    )
    people = [
        ('Джим', 'Хопкинс'),
        ('Капитан', 'Флинт'),
        ('Билл', 'Бонс'),
    ]

    with PersistenceManager('academy') as db_handler:
        db_handler.insert_query(insert_template, people)
        data = db_handler.select_query("""select * from curators""")

    for row in data:
        print(row)

