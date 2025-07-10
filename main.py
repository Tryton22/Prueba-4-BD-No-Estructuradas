# Importar funciones de los módulos CRUD de MariaDB
from mysql_consultas.crud_cliente import insertarCliente, agregarMultiplesCliente, actualizarCliente, buscarCliente, eliminarCliente, exportarCliente
from mysql_consultas.crud_reclamos import insertarReclamo, agregarMultiplesReclamo, actualizarReclamo, buscarReclamo, eliminarReclamo, exportarReclamo
from mysql_consultas.crud_respuestas import insertarRespuesta, agregarMultiplesRespuesta, actualizarRespuesta, buscarRespuesta, eliminarRespuesta, exportarRespuesta

# Importar funciones de los módulos CRUD de MongoDB
from mongo_consultas.crud_analisis_sentimiento import agregarAnalisis, listarAnalisis, actualizarAnalisis, eliminarAnalisis, importarAnalisis as importarAnalisisMongoDB
from mongo_consultas.crud_comentarios import agregarUnComentario, listarComentarios, actualizarComentario, eliminarComentario, importarComentarios as importarComentariosMongoDB
from mongo_consultas.crud_encuestas import agregarUnaEncuesta, listarEncuestas, actualizarEncuesta, eliminarEncuesta, importarEncuestas as importarEncuestasMongoDB

# Importar la función de reporte consolidado
from reportes import generar_reporte_consolidado

# Rutas de los archivos CSV 
CSV_CLIENTES_PATH = 'csv/extraccion_clientes.csv'
CSV_RECLAMOS_PATH = 'csv/extraccion_reclamos.csv'
CSV_RESPUESTAS_PATH = 'csv/extraccion_respuestas.csv'

def menu_clientes():
    while True:
        print("\n--- Menú de Gestión de Clientes (MariaDB) ---")
        print("1. Insertar un cliente")
        print("2. Insertar múltiples clientes")
        print("3. Actualizar un cliente")
        print("4. Listar clientes")
        print("5. Eliminar un cliente")
        print("6. Exportar clientes a CSV")
        print("0. Volver al Menú Principal")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            insertarCliente()
        elif opcion == '2':
            agregarMultiplesCliente()
        elif opcion == '3':
            actualizarCliente()
        elif opcion == '4':
            buscarCliente()
        elif opcion == '5':
            eliminarCliente()
        elif opcion == '6':
            exportarCliente()
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_reclamos():
    while True:
        print("\n--- Menú de Gestión de Reclamos (MariaDB) ---")
        print("1. Insertar un reclamo")
        print("2. Insertar múltiples reclamos")
        print("3. Actualizar un reclamo")
        print("4. Listar reclamos")
        print("5. Eliminar un reclamo")
        print("6. Exportar reclamos a CSV")
        print("0. Volver al Menú Principal")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            insertarReclamo()
        elif opcion == '2':
            agregarMultiplesReclamo()
        elif opcion == '3':
            actualizarReclamo()
        elif opcion == '4':
            buscarReclamo()
        elif opcion == '5':
            eliminarReclamo()
        elif opcion == '6':
            exportarReclamo()
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_respuestas():
    while True:
        print("\n--- Menú de Gestión de Respuestas (MariaDB) ---")
        print("1. Insertar una respuesta")
        print("2. Insertar múltiples respuestas")
        print("3. Actualizar una respuesta")
        print("4. Listar respuestas")
        print("5. Eliminar una respuesta")
        print("6. Exportar respuestas a CSV")
        print("0. Volver al Menú Principal")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            insertarRespuesta()
        elif opcion == '2':
            agregarMultiplesRespuesta()
        elif opcion == '3':
            actualizarRespuesta()
        elif opcion == '4':
            buscarRespuesta()
        elif opcion == '5':
            eliminarRespuesta()
        elif opcion == '6':
            exportarRespuesta()
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_mongodb_operaciones():
    while True:
        print("\n--- Menú de Operaciones MongoDB (Colección 'aguas_araucania') ---")
        print("1. Gestión de Análisis de Sentimiento")
        print("2. Gestión de Comentarios")
        print("3. Gestión de Encuestas")
        print("0. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_analisis_sentimiento()
        elif opcion == '2':
            menu_comentarios()
        elif opcion == '3':
            menu_encuestas()
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_analisis_sentimiento():
    while True:
        print("\n--- Menú Análisis de Sentimiento (MongoDB) ---")
        print("1. Agregar Análisis")
        print("2. Listar Análisis")
        print("3. Actualizar Análisis")
        print("4. Eliminar Análisis")
        print("5. Importar Análisis desde CSV a MongoDB")
        print("0. Volver al Menú de Operaciones MongoDB")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregarAnalisis()
        elif opcion == '2':
            listarAnalisis()
        elif opcion == '3':
            actualizarAnalisis()
        elif opcion == '4':
            eliminarAnalisis()
        elif opcion == '5':
            importarAnalisisMongoDB()
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_comentarios():
    while True:
        print("\n--- Menú Comentarios (MongoDB) ---")
        print("1. Agregar Comentario")
        print("2. Listar Comentarios")
        print("3. Actualizar Comentario")
        print("4. Eliminar Comentario")
        print("5. Importar Comentarios desde CSV a MongoDB")
        print("0. Volver al Menú de Operaciones MongoDB")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregarUnComentario()
        elif opcion == '2':
            listarComentarios()
        elif opcion == '3':
            actualizarComentario()
        elif opcion == '4':
            eliminarComentario()
        elif opcion == '5':
            importarComentariosMongoDB()
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_encuestas():
    while True:
        print("\n--- Menú Encuestas (MongoDB) ---")
        print("1. Agregar Encuesta")
        print("2. Listar Encuestas")
        print("3. Actualizar Encuesta")
        print("4. Eliminar Encuesta")
        print("5. Importar Encuestas desde CSV a MongoDB")
        print("0. Volver al Menú de Operaciones MongoDB")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregarUnaEncuesta()
        elif opcion == '2':
            listarEncuestas()
        elif opcion == '3':
            actualizarEncuesta()
        elif opcion == '4':
            eliminarEncuesta()
        elif opcion == '5':
            importarEncuestasMongoDB()
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL DEL SISTEMA DE GESTIÓN ===")
        print("1. Gestión de Datos MariaDB (Clientes, Reclamos, Respuestas)")
        print("2. Gestión de Datos MongoDB (Análisis, Comentarios, Encuestas)")
        print("3. Generar Reporte Consolidado (MariaDB + MongoDB)")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_mariadb_operaciones()
        elif opcion == '2':
            menu_mongodb_operaciones()
        elif opcion == '3':
            generar_reporte_consolidado()
        elif opcion == '0':
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_mariadb_operaciones():
    while True:
        print("\n--- Menú de Operaciones MariaDB ---")
        print("1. Gestión de Clientes")
        print("2. Gestión de Reclamos")
        print("3. Gestión de Respuestas")
        print("0. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_clientes()
        elif opcion == '2':
            menu_reclamos()
        elif opcion == '3':
            menu_respuestas()
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu_principal()