from db import new_connection
from mysql.connector.errors import ProgrammingError

sql = 'INSERT INTO contatos (Nome,Telefone) values(%s,%s)'
args = ('Lucas', '94122-3123')

with new_connection() as connection:
    try:
        cursor=connection.cursor()
        cursor.execute(sql,args)
        connection.commit()
    except ProgrammingError as e:
        print(f'ERROR: {e.msg}')
