import sqlite3
from sqlite3 import Error

def connect_db() -> sqlite3.Connection:
    """ create a database connection to the SQLite database specified by db_file
        :return: Connection object or None
    """
    try:
        conn = sqlite3.connect("../db/basa.db")
        return conn
    except Error as e:
        print(e)


def create_tables() -> None:
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            begin_date text,
                                            end_date text
                                        ); """

def create_users_table() -> None:
    sql_create_users_table = """CREATE TABLE IF NOT EXISTS users(
                                        userid INT PRIMARY KEY,
                                        first_name TEXT,
                                        second_name TEXT,
                                        id: INT
                                        password TEXT
                                        loging TEXT 
                                        phone TEXT
                                        email TEXT
                                        card_number TEXT
                                        ); """
def create_orders_table() -> None:
    sql_create_users_table = """CREATE TABLE IF NOT EXISTS users(
                                        userid INT PRIMARY KEY,
                                        first_name TEXT,
                                        second_name TEXT,
                                        id: INT
                                        password TEXT
                                        loging TEXT 
                                        phone TEXT
                                        email TEXT
                                        number_card TEXT
                                        ); """

def create_goods_table() -> None:
    sql_create_users_table = """CREATE TABLE IF NOT EXISTS users(
                                        userid INT PRIMARY KEY,
                                        first_name TEXT,
                                        second_name TEXT,
                                        id: INT
                                        password TEXT
                                        loging TEXT 
                                        phone TEXT
                                        email TEXT
                                        number_card TEXT
                                        ); """
def create_order_product_table() -> None:
    sql_create_users_table = """CREATE TABLE IF NOT EXISTS users(
                                        userid INT PRIMARY KEY,
                                        first_name TEXT,
                                        second_name TEXT,
                                        id: INT
                                        password TEXT
                                        loging TEXT 
                                        phone TEXT
                                        email TEXT
                                        number_card TEXT
                                        ); """
