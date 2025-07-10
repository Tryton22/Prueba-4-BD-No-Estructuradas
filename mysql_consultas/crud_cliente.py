import csv
import pandas as pd
import mysql.connector
from mysql.connector import Error

from conexion import con


"""
-------------------------------------
            INSERTAR UNO
-------------------------------------
"""
def insertarCliente():
    try:
        conexion = con()
        cursor = conexion.cursor()

        nombre = input("Ingrese el nombre del cliente: ")
        rut = input("Ingrese el RUT del cliente: ")
        direccion = input("Ingrese la dirección del cliente: ")
        correo = input("Ingrese el correo del cliente: ")
        telefono = ("Ingrese el teléfono celular del cliente: ")

        sql = "INSERT INTO clientes (nombre, rut, direccion, correo, telefono) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombre, rut, direccion, correo, telefono)
        
        cursor.execute (sql, valores)
        conexion.commit()
        print("Cliente ingresado correctamente!")
    
    
    except Error as e:
        print(f"Error al ingresar los datos: {e}")
    
    
    cursor.close()
    conexion.close()


"""
-------------------------------------
        INSERTAR VARIOS
-------------------------------------
"""
def agregarMultiplesCliente():
    cantidad = int(input("Ingrese cantidad de clientes a registrar: "))

    conexion = con()
    cursor = conexion.cursor()

    for i in range(cantidad):
        print(f"\nCliente {i+1}:")
        nombre = input("Ingrese nombre: ")
        rut = input("Ingrese RUT: ")
        direccion = input("Ingrese dirección: ")
        correo = input("Ingrese correo: ")
        telefono = input("Ingrese teléfono: ")

        sql = "INSERT INTO cliente (nombre, rut, direccion, correo, telefono) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombre, rut, direccion, correo, telefono)

        cursor.execute(sql, valores)

    conexion.commit()
    print("Clientes agregados correctamente.")
    cursor.close()
    conexion.close()


"""
-------------------------------------
            ACTUALIZAR
-------------------------------------
"""
def actualizarCliente():
    try:
        conexion = con()
        cursor = conexion.cursor()

        id_cliente = input("Ingrese el ID del cliente que desea actualizar: ")

        nueva_direccion = input("Ingrese nueva dirección: ")
        nuevo_correo = input("Ingrese nuevo correo: ")
        nuevo_telefono = input("Ingrese el nuevo teléfono: ")

        sql = "UPDATE cliente SET direccion = %s, correo = %s, telefono = %s WHERE id_cliente = %s"
        valores = (nueva_direccion, nuevo_correo, nuevo_telefono, id_cliente)

        cursor.execute(sql, valores)
        conexion.commit()

        if cursor.rowcount > 0:
            #si hay lineas se actualiza el cliente
            print("El cliente se actualizó correctamente")
        else:
            print ("Cliente no encontrado.")

    except Error as e:
        print(f"Error al actualizar el cliente: {e}")


"""
-------------------------------------
            LISTAR
-------------------------------------
"""
def buscarCliente():
    try:
        conexion = con()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM cliente")
        clientes = cursor.fetchall()

        print("\n\n--------LISTADO DE CLIENTES----------")
        for c in clientes:
            print(f"ID: {c['id_cliente']}, Nombre: {c['nombre']}, RUT: {c['rut']}, Correo: {c['correo']}")

    except Error as e:
        print(f"Ha ocurrido un error: {e}")

    cursor.close()
    conexion.close()


"""
-------------------------------------
            ELIMINAR
-------------------------------------
"""
def eliminarCliente():
    try:
        conexion = con()
        cursor = conexion.cursor()

        id_cliente = input("Ingrese ID del cliente a eliminar: ")

        sql = "DELETE FROM cliente WHERE id_cliente = %s"
        valores = (id_cliente,)

        cursor.execute(sql, valores)
        conexion.commit()

        if cursor.rowcount > 0:
            print("El cliente ha sido eliminado.")
        else:
            print("Cliente no encontrado.")

    except Error as e:
        print(f" Error al eliminar el cliente: {e}")
    

    cursor.close()
    conexion.close()


"""
-------------------------------------
            EXPORTAR
-------------------------------------
"""
def exportarCliente():
    try:
        conexion = con()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM cliente")
        resultado = cursor.fetchall()

        # Definir las columnas manualmente, en el orden correcto
        columnas = ['id_cliente', 'nombre', 'rut', 'direccion', 'correo', 'telefono']

        # Convertir a DataFrame
        dataFrame = pd.DataFrame(resultado, columns=columnas)

        # Mostrar por consola
        print(dataFrame)

        # Exportar CSV
        dataFrame.to_csv('csv/extraccion_clientes.csv', index=False)
        print("Datos de clientes exportados correctamente.")
        
    except Error as e:
        print("Error al exportar: {e}")
    
    cursor.close()
    conexion.close()