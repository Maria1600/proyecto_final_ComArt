import sqlite3
from config import DB_PATH

#Funcion para inicializar la BD
def init_db():

    # Conectar a la base de datos (la crea si no existe)
    conn = sqlite3.connect(DB_PATH)

    # Crear el cursor para ejecutar comandos SQL
    cursor = conn.cursor()

    # Crear las tablas si no existen
    #EJEMPLO DE TABLA
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS artistas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT,
        fecha_nacimiento <TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Confirmar los cambios (guardar los datos)
    conn.commit()

    # Cerrar la conexión
    conn.close()

    print("Base de datos inicializada correctamente.")