from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from Controladores.ArtistaControlador import artista_bp
from Controladores.ComisionControlador import comision_bp
from Controladores.MensajeControlador import mensaje_bp
from Controladores.PublicacionControlador import publicacion_bp
from Controladores.UsuarioControlador import usuario_bp
from Controladores.CategoriaControlador import categoria_bp
from config import Config
import os

# Inicializamos SQLAlchemy
db = SQLAlchemy()

# Creamos la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)

# Asociamos la app con la extensión de SQLAlchemy
db.init_app(app)

# Registrar Blueprints
app.register_blueprint(categoria_bp)
app.register_blueprint(publicacion_bp)
app.register_blueprint(mensaje_bp)
app.register_blueprint(comision_bp)
app.register_blueprint(artista_bp)
app.register_blueprint(usuario_bp)

# Solo se inicializa la base si no existe
with app.app_context():
    if not os.path.exists(Config.DATABASE):
        from init_db import init_db
        init_db()

# Ruta de inicio
@app.route('/')
def home():
    return render_template('index.html')

#Rutas

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True)
