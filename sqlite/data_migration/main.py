import sqlite3

FROM_PATH = '/home/waldis_jr/Documents/Work/Python/wj_a_m_project/wj_a_m/db/wj_a_m_db_old.sqlite'
TO_PATH = '/home/waldis_jr/Documents/Work/Python/wj_a_m_project/wj_a_m/db/wj_a_m_db.sqlite'

from_db = sqlite3.connect(FROM_PATH)
from_cursor = from_db.cursor()

to_db = sqlite3.connect(TO_PATH)
to_cursor = to_db.cursor()

from_cursor.execute('''SELECT t_id, user_name FROM users;''')
for line in from_cursor.fetchall():
    sql = "INSERT INTO users (t_id, user_name) VALUES (?,?)"
    val = (line[0], line[1])
    to_cursor.execute(sql, val)
    to_db.commit()

from_cursor.execute('''SELECT chat_id, chat_name FROM groups;''')
for line in from_cursor.fetchall():
    sql = "INSERT INTO groups (chat_id, chat_name) VALUES (?,?)"
    val = (line[0], line[1])
    to_cursor.execute(sql, val)
    to_db.commit()
