from db import new_connection
from mysql.connector import ProgrammingError
table_contatos='''
    create table if not exists contatos(Nome VARCHAR(50),Telefone VARCHAR(40))
'''

table_emails='''
    CREATE TABLE IF NOT EXISTS emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        Dono VARCHAR(50)
    )
'''
with new_connection() as connection:
    try:
        cursor=connection.cursor()
        cursor.execute(table_contatos)
        cursor.execute(table_emails)
    except ProgrammingError as e:
        print(f'Error: {e.msg}')