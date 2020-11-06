from mysql import connector
import sqlite3

my_db = connector.connect(user='root', host='localhost', database='am_bot', password='08052004')
my_cursor = my_db.cursor()

lite_db = sqlite3.connect('/home/waldis_jr/Documents/Work/Python/wj_a_m_project/wj_a_m/wj_a_m_db.sqlite')
lite_cursor = lite_db.cursor()

my_cursor.execute('select * from users;')
for line in my_cursor.fetchall():
    sql = "INSERT INTO users (t_id, user_name) VALUES (?,?)"
    val = (line[1], line[2])
    try:
        lite_cursor.execute(sql, val)
        lite_db.commit()
    except sqlite3.IntegrityError as e:
        if str(e) == 'UNIQUE constraint failed: users.t_id':
            pass
        else:
            raise e
