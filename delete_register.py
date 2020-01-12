from mysql.connector import ProgrammingError
from db import new_connection


sql_name = 'DELETE FROM contatos WHERE nome = %s'
sql_id = 'DELETE FROM contatos WHERE id = %s'

i = 1
while i:
    op = input('want to delete by name or id: ')
    if op == 'name':
        name = input('Enter a name that you want to delete: ')
        i = 0
    elif op == 'id':
        id_ = input('Enter the id: ')
        i = 0
    else:
        print('Invalid!!!!')

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        if op=='name':
            cursor.execute(sql_name, (name,))
        else:
            cursor.execute(sql_id,(id_,))
        connection.commit()
    except ProgrammingError as e:
        print(f'ERROR: {e.msg}')
    else:
        print(f'{cursor.rowcont} rows in the table | the register was deleted)