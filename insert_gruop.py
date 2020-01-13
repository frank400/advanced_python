from mysql.connector.errors import ProgrammingError
from db import new_connection

sql = 'INSERT INTO Grupos (descricao) VALUES (%s) '
args=(('Casa',),('Trabalho',))

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.executemany(sql, args)
        connection.commit()

    except ProgrammingError as e:
        print(f'ERROR: {e.msg}')
      
