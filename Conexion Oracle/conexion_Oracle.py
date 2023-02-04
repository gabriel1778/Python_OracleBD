from multiprocessing import connection
import cx_Oracle

try:
    connection=cx_Oracle.connect(
        user='inter',
        password='bidu39cola',
        dsn='10.204.166.109:1521/INTERP',
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