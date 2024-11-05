import sqlite3

conn = sqlite3.connect('PY/25/chinook.db')
cursor = conn.cursor()

# result = cursor.execute('SELECT * FROM Artists')
# data = result.fetchone()
# print(data)

# query = "INSERT INTO Artists (name) values ('Test')"
# cursor.execute(query)
# conn.commit() # potvrzení příkazu

query = "SELECT * FROM Artists WHERE name = 'Test'"
result = cursor.execute(query)
data = result.fetchone()
print(data)

query = "SELECT * FROM Artists order by ArtistId DESC"
result = cursor.execute(query)
data = result.fetchone()
print(data)

conn.close()
