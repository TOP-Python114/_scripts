from mysql.connector import MySQLConnection
from pprint import pprint

# создание и настройка объекта подключения
connection = MySQLConnection(
    host='127.0.0.1',
    port='3300',
    user='root',
    password='root',
    database='academy'
)
connection.autocommit = True

# создание объекта курсора
cursor = connection.cursor()

# выполнение запроса — данные, возвращённые сервером, будут записаны в объект курсор
cursor.execute(
    """select * from Lectures"""
)

# первый вариант изъятия данных из объекта курсора
# data = cursor.fetchall()
# pprint(data)

# второй вариант изъятия данных из объекта курсора
for line in cursor:
    print(line)

# закрытие объектов курсора и подключения — освобождение потоков
cursor.close()
connection.close()
