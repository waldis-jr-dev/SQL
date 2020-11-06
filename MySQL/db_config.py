import my_data_for_bd as my_data
import mysql.connector as mysql

user = my_data.user
password = my_data.password
database = my_data.database

db = mysql.connect(host='localhost', user=user, password=password, database=database)
cursor = db.cursor()

# print funcs


def print_tables():
    cursor.execute("SHOW TABLES")
    print(cursor.fetchall())

# tables funcs


def rename_table(table, new_name):
    cursor.execute(f'RENAME TABLE {table} TO {new_name}')


def clear_table(table):
    cursor.execute(f'TRUNCATE TABLE {table}')


def create_table(req):
    cursor.execute(f"CREATE TABLE {req}")


def drop_table(table):
    cursor.execute(f"DROP TABLE {table}")

# columns and lines funcs


def column_count(table):
    return cursor.execute(f"SELECT SUM(*) FROM {table}")


def line_count(table):
    return cursor.execute(f"SELECT COUNT(*) FROM {table}")


def drop_column(table, column_name):
    cursor.execute(f"alter table {table} DROP INDEX {column_name}")


def drop_line(table, line_name):
    cursor.execute(f"alter table {table} where {line_name} = 'whatever'")


def add_column(table, req):
    cursor.execute(f"ALTER TABLE {table} ADD COLUMN {req}")


def rename_column(table, req):
    cursor.execute(f'ALTER TABLE {table} CHANGE {table} {req}')


def modify_column(table, req):
    cursor.execute(f'ALTER TABLE {table} MODIFY {req}')

# return funcs


def table_data(table):
    cursor.execute(f"SELECT * FROM {table}")
    return cursor.fetchall()


def column_data(table):
    cursor.execute(f"SHOW COLUMNS FROM {table}")
    return cursor.fetchall()


def describe_table(table):
    cursor.execute(f"DESCRIBE {table}")
    return cursor.fetchall()
