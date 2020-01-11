from db import new_connection
from mysql.connector.errors import ProgrammingError

sql='INSERT INTO contatos (nome,telefone) values(%s,%s)'
args=(('lucas','34233-4123'),
    ('alex','34233-4123'),
    ('bruno','34233-4123'),
    ('maria','34233-4123'),
    ('valentina','34233-4123'),
    ('carol','34233-4123'),
    ('beca','34233-4123'),)

with new_connection() as connection:
    try:
        cursor=connection.cursor()
        cursor.executemany(sql,args)
        connection.commit()
    except ProgrammingError as e:
        print(f'ERROR: {e}')
