# -*- utf-8 -*-


import mysql.connector
from settings import *


def create_book_table():
    server = mysql.connector.connect(user=MYSQL_USER,
                                     password=MYSQL_PASSWORD,
                                     database=MYSQL_DATABASE,
                                     use_unicode=True)
    cursor = server.cursor()
    cursor.execute("DROP TABLE IF EXISTS {0}".format(MYSQL_TABLE))

    sql = """CREATE TABLE {0} (
             isbn  CHAR(20) NOT NULL,
             name  CHAR(20),
             price INT)""".format(MYSQL_TABLE)

    cursor.execute(sql)
    server.commit()
    cursor.close()


if __name__ == '__main__':
    create_book_table()