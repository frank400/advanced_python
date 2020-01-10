from db import new_connection

with new_connection() as connection:
    if connection.is_connected():
        cursor=connection.cursor()
        cursor.execute('show databases')

        for i,database in enumerate(cursor,start=1):
            print(f'Banco de dados {i}:{database[0]}')
    else:
        print('connection failed!!!!!')