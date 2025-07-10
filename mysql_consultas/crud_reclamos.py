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
def insertarReclamo():
    try:
        conexion = con()
        cursor = conexion.cursor()

        id_reclamo = input("Ingrese ID del reclamo: ") 
        fecha_reclamo = input("Ingrese fecha del reclamo (YYYY-MM-DD): ")
        tipo = input("Ingrese tipo de reclamo: ")
        descripcion = input("Ingrese descripción del reclamo: ")
        estado = input("Ingrese estado del reclamo: ")


        sql = "INSERT INTO reclamo (id_reclamo, fecha_reclamo, tipo, descripcion, estado) VALUES (%s, %s, %s, %s, %s)"
        valores = (id_reclamo, fecha_reclamo, tipo, descripcion, estado)
        
        cursor.execute (sql, valores)
        conexion.commit()
        print("Reclamo ingresado correctamente!")
    
    
    except Error as e:
        print(f"Error al ingresar los datos: {e}")
    
    
    cursor.close()
    conexion.close()


"""
-------------------------------------
        INSERTAR VARIOS
-------------------------------------
"""
def agregarMultiplesReclamo():
    try:
        cantidad = int(input("Ingrese cantidad de reclamos a registrar: "))

        conexion = con()
        cursor = conexion.cursor()

        for i in range(cantidad):
            print(f"\nReclamo {i+1}:")
            id_reclamo = input("Ingrese ID del reclamo: ") 
            fecha_reclamo = input("Ingrese fecha del reclamo (YYYY-MM-DD): ")
            tipo = input("Ingrese tipo de reclamo: ")
            descripcion = input("Ingrese descripción del reclamo: ")
            estado = input("Ingrese estado del reclamo: ")

            sql = "INSERT INTO reclamo (id_reclamo, fecha_reclamo, tipo, descripcion, estado) VALUES (%s, %s, %s, %s, %s)"
            valores = (id_reclamo, fecha_reclamo, tipo, descripcion, estado)

            cursor.execute(sql, valores)
            conexion.commit()
        print("Reclamos agregados correctamente.")


    except Error as e:
        print(f"Error al ingresar los datos: {e}")

    cursor.close()
    conexion.close()


"""
-------------------------------------
            ACTUALIZAR
-------------------------------------
"""
def actualizarReclamo():
    try:
        conexion = con()
        cursor = conexion.cursor()

        id_reclamo = input("Ingrese el ID del reclamo que desea actualizar: ")

        tipo = input("Ingrese tipo de reclamo: ")
        descripcion = input("Ingrese descripción del reclamo: ")
        estado = input("Ingrese estado del reclamo: ")


        sql = "UPDATE reclamo SET tipo = %s, descripcion = %s, estado = %s WHERE id_reclamo = %s"
        valores = (tipo, descripcion, estado, id_reclamo)

        cursor.execute(sql, valores)
        conexion.commit()

        if cursor.rowcount > 0:
            #si hay lineas se actualiza el reclamo
            print("El reclamo se actualizó correctamente")
        else:
            print ("reclamo no encontrado.")

    except Error as e:
        print(f"Error al actualizar el reclamo: {e}")


"""
-------------------------------------
            LISTAR
-------------------------------------
"""
def buscarReclamo():
    try:
        conexion = con()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM reclamo")
        reclamos = cursor.fetchall()

        print("\n\n--------LISTADO DE RECLAMOS----------")
        for c in reclamos:
            print(f"ID: {c['id_reclamo']},ID del cliente {c['id_cliente']},\n Fecha: {c['fecha_reclamo']},\n Tipo de Reclamo: {c['tipo']}, descripcion: {c['descripcion']}, estado: {c['estado']}")

    except Error as e:
        print("Ha ocurrido un error: {e}")

    cursor.close()
    conexion.close()


"""
-------------------------------------
            ELIMINAR
-------------------------------------
"""
def eliminarReclamo():
    try:
        conexion = con()
        cursor = conexion.cursor()

        id_reclamo = input("Ingrese ID del reclamo a eliminar: ")

        sql = "DELETE FROM reclamo WHERE id_reclamo = %s"
        valores = (id_reclamo,)

        cursor.execute(sql, valores)
        conexion.commit()

        if cursor.rowcount > 0:
            print("El reclamo ha sido eliminado.")
        else:
            print("Reclamo no encontrado.")

    except Error as e:
        print(f" Error al eliminar el reclamo: {e}")
    

    cursor.close()
    conexion.close()


"""
-------------------------------------
            EXPORTAR
-------------------------------------
"""
def exportarReclamo():
    try:
        conexion = con()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM reclamo")
        resultado = cursor.fetchall()

        # Definir las columnas manualmente, en el orden correcto
        columnas = ['id_reclamo', 'id_cliente', 'fecha_reclamo', 'tipo', 'descripcion', 'estado']

        # Convertir a DataFrame
        dataFrame = pd.DataFrame(resultado, columns=columnas)

        # Mostrar por consola
        print(dataFrame)

        # Exportar CSV
        dataFrame.to_csv('csv/extraccion_reclamos.csv', index=False)
        print("Datos de reclamos exportados correctamente.")
        
    except Error as e:
        print("Error al exportar: {e}")
    
    cursor.close()
    conexion.close()