from db import new_connection
from mysql.connector import ProgrammingError
table_grupos='''
    create table if not exists Grupos(
        id INT AUTO_INCREMENT PRIMARY KEY,
        descricao VARCHAR(50)
    )
'''
create_foreign_key_contatos='''
    ALTER TABLE contatos ADD grupo_id INT
'''

alter_contatos='''
    ALTER TABLE contatos ADD FOREIGN KEY (grupo_id)
    REFERENCES Grupos(id)
'''

with new_connection() as connection:
    try:
        cursor=connection.cursor()
        cursor.execute(table_grupos)
        cursor.execute(create_foreign_key_contatos)
        cursor.execute(alter_contatos)
    except ProgrammingError as e:
        print(f'Error: {e.msg}')