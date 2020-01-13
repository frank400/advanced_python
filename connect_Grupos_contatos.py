from mysql.connector.errors import ProgrammingError
from db import new_connection

select_group='SELECT id FROM Grupos WHERE descricao= %s '
update_contatos = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s '

contato_Grupo={
    'lucas':'Casa',
    'francisco':'Trabalho',
    'maria':'Casa',
    'valentina':'Trabalho',
    'carol':'Casa',
    'beca':'Trabalho',
    'alex':'Casa',
    'bruno':'Trabalho',
}

with new_connection() as connection:
    try:
        cursor=connection.cursor()
        for nome,grupo in contato_Grupo.items():
            cursor.execute(select_group,(grupo,))
            id_=cursor.fetchone()[0]
            cursor.execute(update_contatos,(id_,nome))
            connection.commit()


    except ProgrammingError as e:
        print(f'ERROR: {e.msg}')
