# db2.py

import sqlite3
conn = sqlite3.connect('PY/25/chinook.db')
cursor = conn.cursor()

value = input("Zadej písmeno: ")
value = f'{value}%'
query = "select * from artists where name like ? or name = ?"
cursor.execute(query, (value, 'Test')) # safe parametr do db
print(cursor.fetchall())
