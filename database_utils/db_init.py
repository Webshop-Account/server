import sqlite3
from sqlite3 import Error


def connect_db() -> sqlite3.Connection:
    conn = None
    try:
        conn = sqlite3.connect("../db/basa.db")
        return conn
    except Error as e:
        print(e)


def create_tables() -> None:
    pass
