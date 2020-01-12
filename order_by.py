from db import new_connection

sql="SELECT*from contatos ORDER BY nome ASC"

with new_connection() as connection:
    cursor=connection.cursor()
    cursor.execute(sql)
    
    print('\n'.join(value[0] for value in cursor))