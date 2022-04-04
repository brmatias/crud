from unicodedata import name
from numpy import delete
import pandas as pd
import mysql.connector as sql

class crud:
    
    def create(tname, collum1, type1, collum2, type2):
        db_connection = sql.connect(host='localhost', database='db', user='user', password='teste')
        dbCursor = db_connection.cursor()
        tableName = tname
        collumName1 = collum1
        typeCollum1 = type1
        collumName2 = collum2
        typeCollum2 = type2
        dbCursor.execute(f'CREATE TABLE {tableName} ({collum1} {type1}, {collum2} {type2})')
        print("Table Created")


    def read():
        db_connection = sql.connect(host='localhost', database='db', user='user', password='teste')
        dbCursor = db_connection.cursor()
        dbCursor.execute('select * from db.pessoas')
        tableRows = dbCursor.fetchall()
        df = pd.DataFrame(tableRows)
        print(df)

    def insert(pname):
        db_connection = sql.connect(host='localhost', database='db', user='user', password='teste')
        dbCursor = db_connection.cursor()
        name = pname
        dbCursor.execute(f'INSERT INTO pessoas (nome) VALUES ("{name}")')
        db_connection.commit()
        print(dbCursor.rowcount, "record inserted.")


    def delete(tname, cname, wdelete):
        db_connection = sql.connect(host='localhost', database='db', user='user', password='teste')
        dbCursor = db_connection.cursor()
        tableName = tname
        collumName = cname
        whereDelete = wdelete
        dbCursor.execute(f'DELETE FROM {tableName} WHERE {collumName}= "{whereDelete}"')
        db_connection.commit()
        print(whereDelete + " as deleted")







