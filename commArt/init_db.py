import sqlite3
from config import DB_PATH

#Funcion para inicializar la BD
def init_db():

    # Conectar a la base de datos (la crea si no existe)
    conn = sqlite3.connect(DB_PATH)

    # Crear el cursor para ejecutar comandos SQL
    cursor = conn.cursor()

    # --------------------------- Crear las tablas si no existen ------------------------------------

    #Tabla de usuarios LUEGO SE LE PONE CHECK A EL DNI ESTA EN PROCESAMIENTO (DEBATIENDO CONMIGO MISMA SI)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        dni TEXT UNIQUE NOT NULL,
        correo TEXT UNIQUE NOT NULL,
        username TEXT NOT NULL,
        contraseña TEXT NOT NULL,
        fecha_nacimiento TIMESTAMP NOT NULL,
        activo INTEGER CHECK(activo IN (1,0))
    )
    """)

    #Tabla entidad debil artistas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS artistas (
        id_artista INTEGER PRIMARY KEY,
        FOREIGN KEY (id_artista) REFERENCES usuarios(id_usuario)
            ON DELETE CASCADE
    )
    """)

    #HACE FALTA CREAR TABLA INTERMEDIA PARA HACER LA RELACION DE SI MISMO DE USUARIO SEGUIR

    #Tabla de comisiones
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comisiones (
        id_com INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion_com TEXT NOT NULL,
        estado TEXT CHECK(estado IN ('Aceptada','Rechazada','Cancelada','En espera','En proceso', 'Terminada')) NOT NULL,
        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        tipo TEXT CHECK(tipo IN ('Global','Individual')) NOT NULL,
        id_cliente_com INTEGER NOT NULL,
        id_artista_com INTEGER,
        FOREIGN KEY (id_cliente_com) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
        FOREIGN KEY (id_artista_com) REFERENCES artistas(id_artista) ON DELETE CASCADE
    )
    """)

    #Tabla de mensajes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mensajes (
        id_mensaje INTEGER PRIMARY KEY AUTOINCREMENT,
        texto TEXT NOT NULL,
        fecha_creacion_mensaje TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        id_user_creador INTEGER NOT NULL,
        id_com_asociada INTEGER NOT NULL,
        FOREIGN KEY (id_user_creador) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
        FOREIGN KEY (id_com_asociada) REFERENCES comisiones(id_com) ON DELETE CASCADE
    )
    """)

    #Tabla de tags/categorias
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categorias (
        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_categoria TEXT UNIQUE NOT NULL
    )
    """)

    #HAY QUE CREAR TABLA INTERMEDIA PARA RELACION N:M DE ARTISTAS Y CATEGORIAS

    #Tabla de publicacion
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publicaciones (
        id_publicacion INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_publicacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        dibujo TEXT,
        descripcion_publicacion TEXT,
        num_likes INTEGER,
        id_artista_publicacion INTEGER NOT NULL,
        FOREIGN KEY (id_artista_publicacion) REFERENCES artistas(id_artista)
            ON DELETE CASCADE
    )
    """)

    # Confirmar los cambios (guardar los datos)
    conn.commit()

    # Cerrar la conexión
    conn.close()

    print("Base de datos inicializada correctamente.")