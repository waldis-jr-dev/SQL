import passwords
import mysql.connector as mysql

db = mysql.connect(host=passwords.MYSQL_host,
                   user=passwords.MySQL_user,
                   password=passwords.MySQL_password)
cursor = db.cursor()


def print_databases():
    cursor.execute('SHOW DATABASES')
    print(cursor.fetchall())


def create_database(db_name):
    cursor.execute(f"CREATE DATABASE [IF NOT EXISTS] {db_name}")


# def drop_database(db_name):
#     cursor.execute(f"DROP DATABASE [IF EXISTS] {db_name}")
