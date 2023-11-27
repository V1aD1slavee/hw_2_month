import sqlite3


def create_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection


def create_table(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)


sql_create_table = """
CREATE TABLE IF NOT EXISTS products (
id INTENGER PRIMERY KEY,
product_title VAR CHAR (200) NOT NULL,
price DOUBLE (3,3) NOT NULL DEFAULT 0.0,
quantity INTENGER NOT NULL DEFAULT 0
);
"""


connection = create_connection("hw.db")

create_table(connection, sql_create_table)
