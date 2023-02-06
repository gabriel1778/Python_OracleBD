from multiprocessing import connection
import cx_Oracle

try:
    connection=cx_Oracle.connect(
        user='xxxxxx',
        password='xxxxxxxx',
        dsn='xx.xxx.xxx.xxx:XXXX/XXXX',
        encoding='UTF-8'

    )
    print(connection.version)
    cursor=connection.cursor()
    cursor.execute("SELECT secuencia, comando FROM SIA_DAEMON WHERE ROWNUM =1")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexion finalizada.")
