from sqlalchemy import create_engine

import re
from pprint import pprint

# шаблон строки для подключения к БД:
# [DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]
mysql_server = 'mysql+mysqlconnector://root:root@127.0.0.1:3300'

# создание объекта движка
engine = create_engine(mysql_server + '/academy')

# изучение атрибутов объекта движка
# for attr in dir(engine):
#     if not re.fullmatch(r'__.*__', attr):
#         value = getattr(engine, attr)
#         print(f"{attr}\n\t{type(value)}\n\t{value}\n")

# метод execute() возвращает объект курсора
cursor = engine.execute("""select * from curators""")
data = cursor.fetchall()
cursor.close()
pprint(data)


print('\n')


psql_server = 'postgresql+psycopg2://postgres:root@127.0.0.1:5432'

engine = create_engine(psql_server + '/airflights')
with engine.execute("""select * from bookings.aircrafts""") as cursor:
    data = cursor.fetchall()
pprint(data)


print('\n')


sqlite_file = 'sqlite:///db.sqlite'

engine = create_engine(sqlite_file)
with engine.execute("""select * from author""") as cursor:
    data = cursor.fetchall()
pprint(data)

