import pandas as pd
import mysql.connector as sql

class crud:
    
    
    def read():
        db_connection = sql.connect(host='localhost', database='db', user='user', password='teste')
        dbCursor = db_connection.cursor()
        dbCursor.execute('select * from db.pessoas')
        tableRows = dbCursor.fetchall()
        df = pd.DataFrame(tableRows)
        print(df)