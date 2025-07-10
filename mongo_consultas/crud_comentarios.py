from pymongo import MongoClient
import pandas as pd
from mongodb_connection import get_mongo_collection 


"""
-------------------------------------
            INSERTAR UNO
-------------------------------------
"""
def agregarUnComentario():
    coleccion_mongo, cliente_mongo = get_mongo_collection('aguas_araucania', 'comentarios')
    if coleccion_mongo is None: return

    try:
        usuario = input("Ingrese nombre de usuario: ")
        fecha = input("Ingrese fecha del comentario (YYYY-MM-DD): ")
        comentario = input("Ingrese comentario: ")
        cantidad_adjuntos = int(input("Cantidad de archivos adjuntos: "))

        adjuntos = []
        for i in range(cantidad_adjuntos):
            nombre_archivo = input(f"Nombre de archivo {i+1}: ")
            url = input("URL del archivo: ")
            adjuntos.append({'nombre_archivo': nombre_archivo, 'url': url})

        documento = {
            'usuario': usuario,
            'fecha': fecha,
            'comentario': comentario,
            'adjuntos': adjuntos
        }

        coleccion_mongo.insert_one(documento)
        print(f"Comentario registrado para usuario: {usuario}")
    except Exception as e:
        print(f"Error al agregar comentario: {e}")
    finally:
        if cliente_mongo: cliente_mongo.close()


"""
-------------------------------------
            LISTAR
-------------------------------------
"""
def listarComentarios():
    coleccion_mongo, cliente_mongo = get_mongo_collection('aguas_araucania', 'comentarios')
    if coleccion_mongo is None: return

    try:
        print("\n Listado de comentarios:")
        documentos = coleccion_mongo.find()
        if documentos:
            for documento in documentos:
                print(documento)
        else:
            print("No se encontraron comentarios.")
    except Exception as e:
        print(f"Error al listar comentarios: {e}")
    finally:
        if cliente_mongo: cliente_mongo.close()


"""
-------------------------------------
            ACTUALIZAR
-------------------------------------
"""
def actualizarComentario():
    coleccion_mongo, cliente_mongo = get_mongo_collection('aguas_araucania', 'comentarios')
    if coleccion_mongo is None: return

    try:
        usuario = input("Ingrese nombre de usuario del comentario a actualizar: ")

        comentario = coleccion_mongo.find_one({'usuario': usuario})
        if comentario:
            print("Comentario encontrado, actualicemos los datos:")

            nueva_fecha = input("Nueva fecha (YYYY-MM-DD): ")
            nuevo_comentario = input("Nuevo comentario: ")
            cantidad_adjuntos = int(input("Cantidad de adjuntos: "))

            nuevos_adjuntos = []
            for i in range(cantidad_adjuntos):
                nombre_archivo = input(f"Nuevo nombre de archivo {i+1}: ")
                url = input("Nueva URL del archivo: ")
                nuevos_adjuntos.append({'nombre_archivo': nombre_archivo, 'url': url})

            coleccion_mongo.update_one(
                {'usuario': usuario},
                {'$set': {
                    'fecha': nueva_fecha,
                    'comentario': nuevo_comentario,
                    'adjuntos': nuevos_adjuntos
                }}
            )
            print("Comentario actualizado correctamente.")
        else:
            print("No se encontró un comentario para ese usuario.")
    except Exception as e:
        print(f"Error al actualizar comentario: {e}")
    finally:
        if cliente_mongo: cliente_mongo.close()


"""
-------------------------------------
            ELIMINAR
-------------------------------------
"""
def eliminarComentario():
    coleccion_mongo, cliente_mongo = get_mongo_collection('aguas_araucania', 'comentarios')
    if coleccion_mongo is None: return

    try:
        usuario = input("Ingrese nombre de usuario del comentario a eliminar: ")
        resultado = coleccion_mongo.delete_one({'usuario': usuario})

        if resultado.deleted_count > 0:
            print("Comentario eliminado.")
        else:
            print("No se encontró un comentario para ese usuario.")
    except Exception as e:
        print(f"Error al eliminar comentario: {e}")
    finally:
        if cliente_mongo: cliente_mongo.close()


"""
-------------------------------------
            IMPORTAR CSV A MONGODB
-------------------------------------
"""
def importarComentarios():
    coleccion_mongo, cliente_mongo = get_mongo_collection('aguas_araucania', 'comentarios')
    if coleccion_mongo is None: return

    try:
        ruta_csv = "csv/extraccion_comentarios.csv"
        print(f"Intentando importar datos de CSV '{ruta_csv}' a MongoDB (Comentarios)...")
        df = pd.read_csv(ruta_csv, encoding='utf-8')
        datos = df.to_dict(orient='records')

        if datos:
            coleccion_mongo.insert_many(datos)
            print("✅ Comentarios importados correctamente a MongoDB.")
        else:
            print("⚠️ El archivo CSV de comentarios está vacío.")
    except FileNotFoundError:
        print(f"Error: El archivo CSV '{ruta_csv}' no se encontró.")
    except Exception as e:
        print(f"Error al importar comentarios desde CSV a MongoDB: {e}")
    finally:
        if cliente_mongo: cliente_mongo.close()