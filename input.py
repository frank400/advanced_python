from db import new_connection

sql="SELECT*from contatos where nome like %s"

with new_connection() as connection:
    search=input('enter a name that you want search: ')
    args = (f'%{search}%',)
    cursor=connection.cursor()
    cursor.execute(sql,args)
    for x in cursor:
        print(x)