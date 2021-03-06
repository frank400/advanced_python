from collections import defaultdict
from db import new_connection
from mysql.connector.errors import ProgrammingError

sql='''
    SELECT
        Grupos.descricao as grupo,
        contatos.nome as contato
    FROM contatos
    INNER JOIN Grupos ON contatos.grupo_id=Grupos.id
    ORDER BY grupo, contato
'''

with new_connection() as connection:
    try:
        cursor=connection.cursor(dictionary=True)
        cursor.execute(sql)
        contatos=cursor.fetchall()
    except ProgrammingError as e:
        print(f'ERROR: {e.msg}')
    else:
        agruop=defaultdict(list)
        for contato in contatos:
            agruop[contato['grupo']].append(contato['contato'])
        
        print(agruop)
