from flask import Blueprint, render_template

#Esto es para que flask encuentre las rutas mas facil
vista_bp = Blueprint('vista_bp', __name__)

@vista_bp.route('/inicio')
def inicio():
    return render_template('inicio.html')

@vista_bp.route('/login')
def login():
    return render_template('login.html')

@vista_bp.route('/register')
def mostrar_registro():
    return render_template("register.html")

@vista_bp.route('/crear_comision')
def crear_comision():
    return "<h1>crear_comision en construcción</h1>"

@vista_bp.route('/comisiones')
def comisiones():
    return "<h1>comisiones en construcción</h1>"

@vista_bp.route('/notificaciones')
def notificaciones():
    return "<h1>notificaciones en construcción</h1>"

@vista_bp.route('/perfil')
def perfil():
    return "<h1>Perfil en construcción</h1>"
