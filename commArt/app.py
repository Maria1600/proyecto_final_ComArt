import os
from flask import Flask, render_template
from config import Config
from init_db import init_db

# Crear la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)  # Cargar configuración desde config.py

# Llamar a init_db para asegurarse de que la base de datos esté lista
if not os.path.exists(Config.DATABASE):
    init_db()  # Ejecuta la función para crear la base de datos

# Ruta de inicio
@app.route('/')
def home():
    return render_template('index.html')

# Aquí ejemplo de otra ruta
@app.route('/artistas')
def artistas():
    return render_template('artistas_list.html')

# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True)
