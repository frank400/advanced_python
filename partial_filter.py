from db import new_connection

sql="SELECT*from contatos where nome like 'a%'"

with new_connection() as connection:
    cursor=connection.cursor()
    cursor.execute(sql)
    for x in cursor:
        print(x)