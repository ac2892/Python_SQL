import sqlite3

try:
    sqliteConnection = sqlite3.connect('./DB/test.db')
    cursor = sqliteConnection.cursor()
    print("Database Successfully Connected to SQLite")

    sqlite_select_Query = "select * from tbl_Items where Item_ID = 1;"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print(record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")