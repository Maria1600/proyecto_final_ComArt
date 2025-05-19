import os

# Ruta al archivo de la base de datos
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "comisiones.db")

# Configuración de Flask
class Config:
    DATABASE = os.path.join(BASE_DIR, 'comisiones.db')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
