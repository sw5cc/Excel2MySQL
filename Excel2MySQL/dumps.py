# -*- utf-8 -*-


import mysql.connector
from openpyxl import load_workbook
from settings import *


def insert_record(isbn, name, price):
    server = mysql.connector.connect(user=MYSQL_USER,
                                     password=MYSQL_PASSWORD,
                                     database=MYSQL_DATABASE,
                                     use_unicode=True)
    cursor = server.cursor()
    cursor.execute('insert into book (isbn, name, price) values (%s, %s, %s)', [isbn, name, price])
    server.commit()
    cursor.close()


def xls2db(path):
    wb = load_workbook(filename=path, read_only=True)

    # :type: list of :class:`openpyxl.worksheet.worksheet.Worksheet`
    wss = wb.worksheets
    for ws in wss:
        for row in ws.rows:
            book = []
            for cell in row:
                book.append(cell.value)
            if book is not None:
                insert_record(book[0], book[1], book[2])