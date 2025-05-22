import sqlite3
from config import DB_PATH
#from Modelos.Usuario import Usuario
#from Modelos.Artista import Artista
#from Modelos.Categoria import Categoria
#from Modelos.Comision import Comision
#from Modelos.Mensaje import Mensaje
#from Modelos.Publicacion import Publicacion
#from Modelos.TablasIntermedias import TablasIntermedias

#Funcion para inicializar la BD
def init_db():

    #Por mantener la estructura y tod0 el rollo aun esto no se va ha hacer pero como ya estan
    #terminados los mapeados con hacer imports de cada uno y poner lo siguiente bastaria:
    #db.create_all()

    # Conectar a la base de datos (la crea si no existe)
    conn = sqlite3.connect(DB_PATH)

    # Crear el cursor para ejecutar comandos SQL
    cursor = conn.cursor()

    # --------------------------- Crear las tablas si no existen ------------------------------------

    #Tabla de usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        correo TEXT UNIQUE NOT NULL,
        username TEXT NOT NULL,
        contrasenia TEXT NOT NULL,
        fecha_nacimiento TIMESTAMP NOT NULL,
        activo INTEGER CHECK(activo IN (1,0)) NOT NULL
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

    #Tabla intermedia seguir
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS seguir (
        id_seguidor INTEGER NOT NULL,
        id_seguido INTEGER NOT NULL,
        PRIMARY KEY (id_seguidor, id_seguido),
        FOREIGN KEY (id_seguidor) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
        FOREIGN KEY (id_seguido) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
    )
    """)

    #Tabla de comisiones
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comisiones (
        id_com INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion_com TEXT NOT NULL,
        dibujo TEXT,
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

    #Tabla intermedia de Artistas-Categorias
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categoria_artista (
        id_artista INTEGER NOT NULL,
        id_categoria INTEGER NOT NULL,
        PRIMARY KEY (id_artista, id_categoria),
        FOREIGN KEY (id_artista) REFERENCES artistas(id_artista) ON DELETE CASCADE,
        FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria) ON DELETE CASCADE
    )
    """)

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