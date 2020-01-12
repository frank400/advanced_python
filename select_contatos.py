from mysql.connector.errors import ProgrammingError
from db import new_connection

sql='SELECT*FROM contatos'

with new_connection() as connection:
    try:
        cursor=connection.cursor()
        cursor.execute(sql)
        contatos=cursor.fetchall()
    except ProgrammingError as e:
        print(f'ERROR: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato[2]:2d} - {contato[0]:10s} - Fone : {contato[1]:}')
