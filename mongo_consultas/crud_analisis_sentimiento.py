from pymongo import MongoClient
import pandas as pd
from conexion_mongo import get_mongo_collection

"""
-------------------------------------
            INSERTAR UNO
-------------------------------------
"""
def agregarAnalisis():
    coleccion_mongo, cliente_mongo = get_mongo_collection('aguas_araucania', 'analisis_sentimiento')
    if coleccion_mongo is None: return
    try:
        usuario = input("Ingrese nombre de usuario: ")
        origen = input("Ingrese origen (ej: 'twitter', 'facebook'): ")
        fecha = input("Ingrese fecha del comentario (YYYY-MM-DD): ")
        comentario = input("Ingrese comentario: ")
        sentimiento = input("Ingrese sentimiento (positivo / neutro / negativo): ")
        score = float(input("Ingrese puntaje de sentimiento (entre -1.0 y 1.0): "))

        documento = {
            'usuario': usuario,
            'origen': origen,
            'fecha': fecha,
            'comentario': comentario,
            'sentimiento': sentimiento,
            'score': score
        }

        coleccion_mongo.insert_one(documento)
        print(f"Análisis registrado para usuario: {usuario}")
    except Exception as e:
        print(f"Error al agregar análisis: {e}")
    finally:
        if cliente_mongo: cliente_mongo.close()


"""
-------------------------------------
            LISTAR
-------------------------------------
"""
def listarAnalisis():
    coleccion_mongo, cliente_mongo = get_mongo_collection('aguas_araucania', 'analisis_sentimiento')
    if coleccion_mongo is None: return

    try:
        print("\n Listado de análisis de sentimiento:")
        documentos = coleccion_mongo.find()
        if documentos:
            for documento in documentos:
                print(documento)
        else:
            print("No se encontraron análisis de sentimiento.")
    except Exception as e:
        print(f"Error al listar análisis: {e}")
    finally:
        if cliente_mongo: cliente_mongo.close()

"""
-------------------------------------
            ACTUALIZAR
-------------------------------------
"""
def actualizarAnalisis():
    coleccion_mongo, cliente_mongo = get_mongo_collection('aguas_araucania', 'analisis_sentimiento')
    if coleccion_mongo is None: return

    try:
        usuario = input("Ingrese nombre de usuario del análisis a actualizar: ")

        analisis = coleccion_mongo.find_one({'usuario': usuario})
        if analisis:
            print("Análisis encontrado, actualicemos los datos:")

            nuevo_origen = input("Nuevo origen (ej: 'twitter', 'facebook'): ")
            nueva_fecha = input("Nueva fecha (YYYY-MM-DD): ")
            nuevo_comentario = input("Nuevo comentario: ")
            nuevo_sentimiento = input("Nuevo sentimiento (positivo / neutro / negativo): ")
            nuevo_score = float(input("Nuevo puntaje de sentimiento (entre -1.0 y 1.0): "))

            coleccion_mongo.update_one(
                {'usuario': usuario},
                {'$set': {
                    'origen': nuevo_origen,
                    'fecha': nueva_fecha,
                    'comentario': nuevo_comentario,
                    'sentimiento': nuevo_sentimiento,
                    'score': nuevo_score
                }}
            )
            print("Análisis actualizado correctamente.")
        else:
            print("No se encontró un análisis para ese usuario.")
    except Exception as e:
        print(f"Error al actualizar análisis: {e}")
    finally:
        if cliente_mongo: cliente_mongo.close()

"""
-------------------------------------
            ELIMINAR
-------------------------------------
"""
def eliminarAnalisis():
    coleccion_mongo, cliente_mongo = get_mongo_collection('aguas_araucania', 'analisis_sentimiento')
    if coleccion_mongo is None: return

    try:
        usuario = input("Ingrese nombre de usuario del análisis a eliminar: ")
        resultado = coleccion_mongo.delete_one({'usuario': usuario})

        if resultado.deleted_count > 0:
            print("Análisis eliminado.")
        else:
            print("No se encontró un análisis para ese usuario.")
    except Exception as e:
        print(f"Error al eliminar análisis: {e}")
    finally:
        if cliente_mongo: cliente_mongo.close()

"""
-------------------------------------
            IMPORTAR
-------------------------------------
"""
def importarAnalisis():
    coleccion_mongo, cliente_mongo = get_mongo_collection('aguas_araucania', 'analisis_sentimiento')
    if coleccion_mongo is None: return

    try:
        ruta_csv = "csv/extraccion_analisis_sentimiento.csv"
        print(f"Intentando importar datos de CSV '{ruta_csv}' a MongoDB (Análisis de Sentimiento)...")
        df = pd.read_csv(ruta_csv, encoding='utf-8')
        datos = df.to_dict(orient='records')

        if datos:
            coleccion_mongo.insert_many(datos)
            print("Análisis importados correctamente a MongoDB.")
        else:
            print("El archivo CSV de análisis de sentimiento está vacío.")
    except FileNotFoundError:
        print(f"Error: El archivo CSV '{ruta_csv}' no se encontró.")
    except Exception as e:
        print(f"Error al importar análisis desde CSV a MongoDB: {e}")
    finally:
        if cliente_mongo: cliente_mongo.close()
