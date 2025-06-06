import secrets

from flask import Flask, render_template, request, jsonify
from Controladores.ComisionControlador import comision_bp
from Controladores.MensajeControlador import mensaje_bp
from Controladores.PublicacionControlador import publicacion_bp
from Controladores.RutasVistaControlador import vista_bp
from extensiones import db  # cambiamos esto para no generar errores de import circulares
from Controladores.ArtistaControlador import artista_bp
import Modelos  # Esto ejecuta __init__.py de Modelos y carga TODITO
from Controladores.UsuarioControlador import usuario_bp
from Controladores.CategoriaControlador import categoria_bp
from config import Config
import os
from werkzeug.utils import secure_filename


# Creamos la aplicación Flask
app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
#Esto se hace para tener una clave aleatoria para poder utilizar session de manera segura
app.config.from_object(Config)

# Asociamos la app con SQLAlchemy
db.init_app(app)

# Registrar Blueprints
app.register_blueprint(categoria_bp)
app.register_blueprint(publicacion_bp)
app.register_blueprint(mensaje_bp)
app.register_blueprint(comision_bp)
app.register_blueprint(artista_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(vista_bp)

# Inicialización de BD si no existe
with app.app_context():
    if not os.path.exists(Config.DATABASE):
        from init_db import init_db
        from datos_iniciales import insertar_datos  # Importamos los insert
        init_db()               # Crea la estructura con SQL
        insertar_datos(app)      # Despues de crear la bd y su estructura insertamos datos

# Ruta principal la que aparece justo al compilar
@app.route('/')
def home():
    return render_template('login.html')  # ← Se hace predeterminado

# Otras rutas
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/crear_comision')
def crear_comision():
    return render_template('crear_comision.html')

@app.route('/comisiones')
def comisiones():
    return render_template('comisiones.html')

@app.route('/seleccionar_tags')
def seleccionar_tags():
    return render_template('seleccionar_tags.html')

#Ruta para subir imagenes
@app.route('/subir_imagen', methods=['POST'])
def subir_imagen():
    imagen = request.files['imagen']
    if imagen and imagen.filename.lower().endswith(('.png', '.jpg')):
        filename = secure_filename(imagen.filename)
        ruta = os.path.join('static/img', filename)
        imagen.save(ruta)
        data = {"ruta": f"img/{filename}"}
        http = 200
    else:
        data = {"error": "Formato no permitido"}
        http = 400
    return jsonify(data), http

# Ejecutar
if __name__ == '__main__':
    app.run(debug=True)
