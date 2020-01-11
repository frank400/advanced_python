from db import new_connection
from mysql.connector import ProgrammingError

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute('DROP TABLE emails')
    except ProgrammingError as e:
        print(f'ERROR: {e.msg}')
