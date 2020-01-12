from db import new_connection

sql="SELECT*from contatos where telefone='34233-4123'"

with new_connection() as connection:
    cursor=connection.cursor()
    cursor.execute(sql)
    for x in cursor:
        print(x)