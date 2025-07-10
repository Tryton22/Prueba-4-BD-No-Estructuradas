from pymongo import MongoClient
import pandas as pd
from mongodb_connection import get_mongo_collection


"""
-------------------------------------
            INSERTAR UNO
-------------------------------------
"""
def agregarUnaEncuesta():
    coleccion_mongo, cliente_mongo = get_mongo_collection('aguas_araucania', 'encuestas')
    if coleccion_mongo is None: return

    try:
        usuario = input("Ingrese el usuario al que se realizó la encuesta: ")
        fecha_encuesta = input("Ingrese fecha de la encuesta (YYYY-MM-DD): ")
        cantidad_preguntas = int(input("Ingrese cantidad de preguntas: "))

        preguntas = []
        for i in range(cantidad_preguntas):
            pregunta = input(f"Ingrese pregunta {i+1}: ")
            respuesta = input("Respuesta: ")
            preguntas.append({"pregunta": pregunta, "respuesta": respuesta})

        documento = {
            "usuario":usuario,
            "fecha_encuesta": fecha_encuesta,
            "preguntas": preguntas
        }

        coleccion_mongo.insert_one(documento)
        print("Encuesta agregada correctamente.")
    except Exception as e:
        print(f"Error al agregar encuesta: {e}")
    finally:
        if cliente_mongo: cliente_mongo.close()


"""
-------------------------------------
            LISTAR
-------------------------------------
"""
def listarEncuestas():
    coleccion_mongo, cliente_mongo = get_mongo_collection('aguas_araucania', 'encuestas')
    if coleccion_mongo is None: return

    try:
        print("\n Listado de encuestas:")
        documentos = coleccion_mongo.find()
        if documentos:
            for doc in documentos:
                print(doc)
        else:
            print("No se encontraron encuestas.")
    except Exception as e:
        print(f"Error al listar encuestas: {e}")
    finally:
        if cliente_mongo: cliente_mongo.close()


"""
-------------------------------------
            ACTUALIZAR
-------------------------------------
"""
def actualizarEncuesta():
    coleccion_mongo, cliente_mongo = get_mongo_collection('aguas_araucania', 'encuestas')
    if coleccion_mongo is None: return

    try:
        usuario = input("Ingrese nombre de usuario de la encuesta a actualizar: ")

        encuesta = coleccion_mongo.find_one({'usuario': usuario})
        
        if encuesta:
            print("Encuesta encontrada, actualicemos los datos:")

            nueva_fecha = input("Nueva fecha (YYYY-MM-DD): ")
            cantidad_preguntas = int(input("Cantidad de preguntas: "))

            nuevas_preguntas = []
            for i in range(cantidad_preguntas):
                pregunta = input(f"Pregunta {i+1}: ")
                respuesta = input("Respuesta: ")
                nuevas_preguntas.append({'pregunta': pregunta, 'respuesta': respuesta})

            coleccion_mongo.update_one(
                {'usuario': usuario},
                {'$set': {
                    'fecha_encuesta': nueva_fecha,
                    'preguntas': nuevas_preguntas
                }}
            )
            print("Encuesta actualizada correctamente.")
        else:
            print("No se encontró una encuesta para ese usuario.")
    except Exception as e:
        print(f"Error al actualizar encuesta: {e}")
    finally:
        if cliente_mongo: cliente_mongo.close()


"""
-------------------------------------
            ELIMINAR
-------------------------------------
"""
def eliminarEncuesta():
    coleccion_mongo, cliente_mongo = get_mongo_collection('aguas_araucania', 'encuestas')
    if coleccion_mongo is None: return

    try:
        usuario = input("Ingrese nombre del usuario que realizó la encuesta a eliminar: ")
        resultado = coleccion_mongo.delete_one({'usuario': usuario})

        if resultado.deleted_count > 0:
            print("Encuesta eliminada.")
        else:
            print("No se encontró una encuesta para ese usuario.")
    except Exception as e:
        print(f"Error al eliminar encuesta: {e}")
    finally:
        if cliente_mongo: cliente_mongo.close()


"""
-------------------------------------
            IMPORTAR CSV A MONGODB
-------------------------------------
"""
def importarEncuestas():
    coleccion_mongo, cliente_mongo = get_mongo_collection('aguas_araucania', 'encuestas')
    if coleccion_mongo is None: return

    try:
        ruta_csv = "csv/extraccion_encuestas.csv"
        print(f"Intentando importar datos de CSV '{ruta_csv}' a MongoDB (Encuestas)...")
        df = pd.read_csv(ruta_csv, encoding='utf-8')
        datos = df.to_dict(orient='records')

        if datos:
            coleccion_mongo.insert_many(datos)
            print("Datos de encuestas importados correctamente a MongoDB.")
        else:
            print("El archivo CSV de encuestas está vacío.")
    except FileNotFoundError:
        print(f"Error: El archivo CSV '{ruta_csv}' no se encontró.")
    except Exception as e:
        print(f"Error al importar encuestas desde CSV a MongoDB: {e}")
    finally:
        if cliente_mongo: cliente_mongo.close()

