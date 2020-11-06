import sqlite3

conn = sqlite3.connect('users.sqlite')
cursor = conn.cursor()

# cursor.execute('''INSERT INTO test (id,name,days) VALUES (2,'Копировать. 😌',29);''')
# conn.commit()

cursor.execute('''SELECT * FROM test;''')
for line in cursor.fetchall():
    print(line[1])


conn.close()
