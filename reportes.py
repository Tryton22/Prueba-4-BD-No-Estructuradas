import pandas as pd
from mysql_consultas.conexion import con as connect_mysql
from mongo_consultas.conexion_mongo import get_mongo_collection
from pymongo.errors import ConnectionFailure, PyMongoError
from mysql.connector import Error

def generar_reporte_consolidado():
    """
    Genera un reporte consolidado extrayendo datos de MariaDB y MongoDB.
    """
    print("\n--- Generando Reporte Consolidado ---")
    df_clientes = pd.DataFrame()
    df_reclamos = pd.DataFrame()
    df_respuestas = pd.DataFrame()
    df_comentarios = pd.DataFrame()
    df_analisis = pd.DataFrame()
    df_encuestas = pd.DataFrame()

    # --- Extraer datos de MariaDB ---
    print("Extrayendo datos de MariaDB...")
    mysql_conn = None
    try:
        mysql_conn = connect_mysql()
        if mysql_conn:
            cursor = mysql_conn.cursor(dictionary=True) # Para obtener resultados como diccionarios

            # Clientes
            cursor.execute("SELECT * FROM cliente")
            clientes_data = cursor.fetchall()
            df_clientes = pd.DataFrame(clientes_data)
            print(f" - {len(df_clientes)} clientes cargados desde MariaDB.")

            # Reclamos
            cursor.execute("SELECT * FROM reclamo")
            reclamos_data = cursor.fetchall()
            df_reclamos = pd.DataFrame(reclamos_data)
            print(f" - {len(df_reclamos)} reclamos cargados desde MariaDB.")

            # Respuestas
            cursor.execute("SELECT * FROM respuesta")
            respuestas_data = cursor.fetchall()
            df_respuestas = pd.DataFrame(respuestas_data)
            print(f" - {len(df_respuestas)} respuestas cargadas desde MariaDB.")

    except Error as e:
        print(f"Error al extraer datos de MariaDB: {e}")
    finally:
        if mysql_conn:
            mysql_conn.close()
            print("Conexión a MariaDB cerrada.")

    # --- Extraer datos de MongoDB ---
    print("\nExtrayendo datos de MongoDB...")
    mongo_client = None
    try:
        # Comentarios
        coleccion_comentarios, cliente_comentarios = get_mongo_collection('aguas_araucania', 'comentarios')
        if coleccion_comentarios:
            comentarios_data = list(coleccion_comentarios.find({}))
            df_comentarios = pd.DataFrame(comentarios_data)
            if '_id' in df_comentarios.columns:
                df_comentarios = df_comentarios.drop(columns=['_id'])
            print(f" - {len(df_comentarios)} comentarios cargados desde MongoDB.")
            if cliente_comentarios: cliente_comentarios.close()

        # Análisis de Sentimiento
        coleccion_analisis, cliente_analisis = get_mongo_collection('aguas_araucania', 'analisis_sentimiento')
        if coleccion_analisis:
            analisis_data = list(coleccion_analisis.find({}))
            df_analisis = pd.DataFrame(analisis_data)
            if '_id' in df_analisis.columns:
                df_analisis = df_analisis.drop(columns=['_id'])
            print(f" - {len(df_analisis)} análisis de sentimiento cargados desde MongoDB.")
            if cliente_analisis: cliente_analisis.close()

        # Encuestas
        coleccion_encuestas, cliente_encuestas = get_mongo_collection('aguas_araucania', 'encuestas')
        if coleccion_encuestas:
            encuestas_data = list(coleccion_encuestas.find({}))
            df_encuestas = pd.DataFrame(encuestas_data)
            if '_id' in df_encuestas.columns:
                df_encuestas = df_encuestas.drop(columns=['_id'])
            print(f" - {len(df_encuestas)} encuestas cargadas desde MongoDB.")
            if cliente_encuestas: cliente_encuestas.close()

    except Exception as e: # Captura cualquier error
        print(f"Error al extraer datos de MongoDB: {e}")
    
    # --- Consolidar y Generar Reporte ---
    print("\nConsolidando datos...")

    # 1. Unir clientes con reclamos y respuestas
    df_reporte_mysql = pd.DataFrame()
    if not df_clientes.empty and not df_reclamos.empty:
        df_reporte_mysql = pd.merge(df_clientes, df_reclamos, left_on='id_cliente', right_on='id_cliente', how='left', suffixes=('_cliente', '_reclamo'))
        if not df_respuestas.empty:
            df_reporte_mysql = pd.merge(df_reporte_mysql, df_respuestas, left_on='id_reclamo', right_on='id_reclamo', how='left', suffixes=('_reclamo', '_respuesta'))
    elif not df_clientes.empty:
        df_reporte_mysql = df_clientes
    elif not df_reclamos.empty:
        df_reporte_mysql = df_reclamos
    elif not df_respuestas.empty:
        df_reporte_mysql = df_respuestas

    print("\n--- Reporte de MariaDB (Clientes, Reclamos, Respuestas) ---")
    if not df_reporte_mysql.empty:
        print(df_reporte_mysql.head()) # Muestra las primeras filas
        print(f"\nTotal de filas en reporte MariaDB: {len(df_reporte_mysql)}")
        # Opcional: Exportar a CSV/Excel
        df_reporte_mysql.to_csv('reportes/reporte_mariadb_consolidado.csv', index=False)
        print("Reporte MariaDB consolidado exportado")
    else:
        print("No hay datos de MariaDB para generar el reporte.")

    # 2. Reporte de datos de MongoDB
    print("\n--- Reporte de MongoDB (Comentarios, Análisis de Sentimiento, Encuestas) ---")

    df_reporte_mongodb = pd.DataFrame()
    if not df_comentarios.empty:
        df_reporte_mongodb = df_comentarios
        if not df_analisis.empty:
            df_reporte_mongodb = pd.merge(df_reporte_mongodb, df_analisis, on=['usuario', 'fecha'], how='outer', suffixes=('_comentario', '_analisis'))
        if not df_encuestas.empty:
            df_reporte_mongodb = pd.merge(df_reporte_mongodb, df_encuestas, left_on='usuario', right_on='usuario', how='outer', suffixes=('_coment_analis', '_encuesta'))


    if not df_reporte_mongodb.empty:
        print(df_reporte_mongodb.head())
        print(f"\nTotal de filas en reporte MongoDB: {len(df_reporte_mongodb)}")
        df_reporte_mongodb.to_csv('reportes/reporte_mongodb_consolidado.csv', index=False)
        print("Reporte MongoDB consolidado exportado")
    else:
        print("No hay datos de MongoDB para generar el reporte.")

    print("\nReporte consolidado finalizado.")