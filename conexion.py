import mysql.connector
from mysql.connector import Error

def con():
    try:
        mydb =mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="actividad2"
    )

        if mydb.is_connected():
            print("Conexion exitosa!!")
        return mydb

    except Error as e:
        print("Error al conectar!")
        return None

mydb= con()
