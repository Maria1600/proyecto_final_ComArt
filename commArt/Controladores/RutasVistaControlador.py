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

