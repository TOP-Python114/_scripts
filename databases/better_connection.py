from pathlib import Path
from sys import path

from configparser import ConfigParser
from mysql.connector import MySQLConnection


def read_db_config(file_path: str | Path):
    db_config = ConfigParser()
    with open(file_path, encoding='utf-8') as filein:
        db_config.read_file(filein)
    return db_config


db_config_path = Path(path[0]) / 'db_config.ini'
connection_config = read_db_config(db_config_path)['Connection']

conn = MySQLConnection(
    **connection_config,
    database='hospital'
)
conn.autocommit = True

with conn.cursor() as cur:
    cur.execute("show tables")
    print(cur.fetchall())

conn.close()
