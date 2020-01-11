from db import new_connection
from mysql.connector import ProgrammingError

with new_connection() as connection:
    try:
        cursor=connection.cursor()
        cursor.execute('SHOW TABLES')
        for i,table in enumerate(cursor,start=1):
            print(f'{i} : {table[0]}')
    except ProgrammingError as e:
        print(f'ERROR: {e}')