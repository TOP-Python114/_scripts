from psycopg2 import connect

conn = connect(
    host='127.0.0.1',
    port='5432',
    user='postgres',
    password='root',
    dbname='airflights'
)
conn.autocommit = True

cur = conn.cursor()

cur.execute(
    """select city,
              airport_name
         from bookings.airports
     order by city"""
)
data = cur.fetchall()

for row in data:
    print(row)
