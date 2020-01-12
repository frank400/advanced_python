from mysql.connector import ProgrammingError
from db import new_connection

sql = "UPDATE contatos SET nome='francisco' WHERE id = 6"

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
    except ProgrammingError as e:
        print(f'ERROR: {e.msg}')
    else:
        print('success!!!')