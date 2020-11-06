import sqlite3

conn = sqlite3.connect('users.sqlite')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS test (id int, name varchar(10), days int);''')

# conn.commit()
conn.close()