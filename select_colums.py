from db import new_connection

sql='SELECT Telefone,Nome FROM contatos'

with new_connection() as connection:
    cursor=connection.cursor()
    cursor.execute(sql)
    contatos=cursor.fetchall()
    
    for contato in contatos:
        print('\t'.join(str(value) for value in contato))