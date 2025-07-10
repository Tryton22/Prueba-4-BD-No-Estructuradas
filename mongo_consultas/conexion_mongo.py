from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def get_mongo_collection(db_name, collection_name, host='localhost', port=27017):
    """
    Establece una conexión a MongoDB y retorna una colección específica.
    """
    try:
        client = MongoClient(host, port)
        client.admin.command('ping') # Verifica la conexión
        db = client[db_name]
        collection = db[collection_name]
        print(f"Conexión a MongoDB (DB: {db_name}, Colección: {collection_name}) exitosa.")
        return collection, client # Devolvemos también el cliente para poder cerrarlo
    except ConnectionFailure as e:
        print(f"Error de conexión a MongoDB: Asegúrate de que MongoDB esté en ejecución y accesible en {host}:{port}. Error: {e}")
        return None, None
    except Exception as e:
        print(f"Ocurrió un error inesperado al conectar a MongoDB: {e}")
        return None, None
