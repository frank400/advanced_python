from db import new_connection


with new_connection() as connection:
    if connection.is_connected():
        cursor=connection.cursor()
        cursor.execute('create database if not exists agenda')
    else:
        print('connection failed!!!')