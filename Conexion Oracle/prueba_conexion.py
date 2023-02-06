from tkinter import *
import cx_Oracle
import datetime

root = Tk()
root.title('OLD-CARRIER')
root.iconbitmap('C:/gui/exe/img-acc.ico')
root.geometry("450x400")
root.resizable(0,0)

def MyClick():
    try:
        connection=cx_Oracle.connect(
        user='xxxx',
        password='xxxxxxxx',
        dsn='xx.xxx.xxx.xxx:xxxx/NOMBRE_BD',
        encoding='UTF-8'
        )
        print(connection.version)
        cur = connection.cursor()
        cur.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'yyyymmdd'")
        #cur.execute("select sysdate from dual")
        #rows=cur.fetchall()
        #for row in rows:
        #    print(row)
        cur.callproc('Relacionar_llamadas_fco_v2')
    except Exception as err:
        error = print('Exception raised while executing the procedure', err)
        #error = "Exception raised while executing the procedure"
        myLabel = Label(root, text=err)
        myLabel.pack(pady=10)
    else:
        ok='Procedure execute'
        myLabel = Label(root, text=ok)
        myLabel.pack(pady=10)     

    finally:
        connection.close()
    print("Conexion finalizada.")

myButton = Button(root, text="Generar archivos", command=MyClick)
myButton.pack(pady=10)

root.mainloop()
