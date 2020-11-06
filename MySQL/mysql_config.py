from Private.MySQL import my_data
import mysql.connector as mysql

user = my_data.db_user_name()
password = my_data.db_user_password()

db = mysql.connect(host='localhost', user=user, password=password)
cursor = db.cursor()


def print_databases():
    cursor.execute('SHOW DATABASES')
    print(cursor.fetchall())


def create_database(db_name):
    cursor.execute(f"CREATE DATABASE [IF NOT EXISTS] {db_name}")


# def drop_database(db_name):
#     cursor.execute(f"DROP DATABASE [IF EXISTS] {db_name}")
