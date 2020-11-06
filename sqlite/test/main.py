import sqlite3

conn = sqlite3.connect('test.sqlite')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS test (id int, name varchar(10), days int);''')
# print(cursor.fetchall())

# conn.commit()
conn.close()
