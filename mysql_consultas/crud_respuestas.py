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
def insertarRespuesta():
    try:
        conexion = con()
        cursor = conexion.cursor()

        id_respuesta = input("Ingrese ID del respuesta: ") 
        id_reclamo = input("Ingrese el ID del reclamo contestado")
        fecha_respuesta = input("Ingrese fecha del respuesta (YYYY-MM-DD): ")
        detalle_respuesta = input("Ingrese tipo de respuesta: ")
        responsable = input("Ingrese descripción del respuesta: ")
        

        sql = "INSERT INTO respuesta (id_respuesta, id_reclamo, fecha_respuesta, detalle_respuesta, responsable) VALUES (%s, %s, %s, %s, %s)"
        valores = (id_respuesta,id_reclamo,fecha_respuesta, detalle_respuesta, responsable)
        
        cursor.execute (sql, valores)
        conexion.commit()
        print("Respuesta ingresada correctamente!")
    
    
    except Error as e:
        print(f"Error al ingresar los datos: {e}")
    
    
    cursor.close()
    conexion.close()


"""
-------------------------------------
        INSERTAR VARIOS
-------------------------------------
"""
def agregarMultiplesRespuesta():
    try:
        cantidad = int(input("Ingrese cantidad de respuestas a registrar: "))

        conexion = con()
        cursor = conexion.cursor()

        for i in range(cantidad):
            print(f"\nRespuesta {i+1}:")
            id_respuesta = input("Ingrese ID del respuesta: ") 
            id_reclamo = input("Ingrese el ID del reclamo contestado")
            fecha_respuesta = input("Ingrese fecha del respuesta (YYYY-MM-DD): ")
            detalle_respuesta = input("Ingrese tipo de respuesta: ")
            responsable = input("Ingrese descripción del respuesta: ")
            

            sql = "INSERT INTO respuesta (id_respuesta, id_reclamo, fecha_respuesta, detalle_respuesta, responsable) VALUES (%s, %s, %s, %s, %s)"
            valores = (id_respuesta,id_reclamo,fecha_respuesta, detalle_respuesta, responsable)
            


            cursor.execute(sql, valores)
            conexion.commit()
        print("Respuestas agregadas correctamente.")


    except Error as e:
        print(f"Error al ingresar los datos: {e}")

    cursor.close()
    conexion.close()


"""
-------------------------------------
            ACTUALIZAR
-------------------------------------
"""
def actualizarRespuesta():
    try:
        conexion = con()
        cursor = conexion.cursor()

        id_respuesta = input("Ingrese el ID de la respuesta que desea actualizar: ")

        detalle_respuesta = input("Ingrese tipo de respuesta: ")
        responsable = input("Ingrese descripción del respuesta: ")


        sql = "UPDATE respuesta SET detalle_respuesta = %s, responsable = %s WHERE id_respuesta = %s"
        valores = (detalle_respuesta, responsable, id_respuesta)

        cursor.execute(sql, valores)
        conexion.commit()

        if cursor.rowcount > 0:
            #si hay lineas se actualiza el reclamo
            print("La respuesta se actualizó correctamente")
        else:
            print ("Respuesta no encontrada.")

    except Error as e:
        print(f"Error al actualizar la respuesta: {e}")


"""
-------------------------------------
            LISTAR
-------------------------------------
"""
def buscarRespuesta():
    try:
        conexion = con()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM respuesta")
        respuestas = cursor.fetchall()

        print("\n\n--------LISTADO DE respuestaS----------")
        for c in respuestas:
            print(f"ID: {c['id_respuesta']}, id_reclamo: {c['id_reclamo']}, fecha_respuesta: {c['fecha_respuesta']}, detalle_respuesta: {c['detalle_respuesta']}, responsable {c['responsable']}")

    except Error as e:
        print("Ha ocurrido un error: {e}")

    cursor.close()
    conexion.close()


"""
-------------------------------------
            ELIMINAR
-------------------------------------
"""
def eliminarRespuesta():
    try:
        conexion = con()
        cursor = conexion.cursor()

        id_respuesta = input("Ingrese ID de la respuesta a eliminar: ")

        sql = "DELETE FROM respuesta WHERE id_respuesta = %s"
        valores = (id_respuesta,)

        cursor.execute(sql, valores)
        conexion.commit()

        if cursor.rowcount > 0:
            print("La respuesta ha sido eliminada.")
        else:
            print("respuesta no encontrada.")

    except Error as e:
        print(f" Error al eliminar la respuesta: {e}")
    

    cursor.close()
    conexion.close()


"""
-------------------------------------
            EXPORTAR
-------------------------------------
"""
def exportarRespuesta():
    try:
        conexion = con()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM respuesta")
        resultado = cursor.fetchall()

        # Definir las columnas manualmente, en el orden correcto
        columnas = ['id_respuesta', 'id_reclamo', 'fecha_respuesta', 'detalle_respuesta', 'responsable']

        # Convertir a DataFrame
        dataFrame = pd.DataFrame(resultado, columns=columnas)

        # Mostrar por consola
        print(dataFrame)

        # Exportar CSV
        dataFrame.to_csv('csv/extraccion_respuestas.csv', index=False)
        print("Datos de respuestas exportados correctamente")
        
    except Error as e:
        print("Error al exportar: {e}")
    
    cursor.close()
    conexion.close()