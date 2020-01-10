from mysql.connector import connect
from contextlib import contextmanager

paramns=dict(
    host='localhost',
    port=3306,
    user='root',
    passwd='53489072!@',
    database='agenda'
)

@contextmanager
def new_connection():
    connection = connect(**paramns)
    try:
        yield connection
    finally:
        if (connection and connection.is_connected()):
            connection.close()