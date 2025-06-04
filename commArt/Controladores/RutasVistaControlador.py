from flask import Blueprint, render_template, session, redirect, url_for

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

@vista_bp.route('/crear_comision', defaults={'id_artista': None})
@vista_bp.route('/abrir_comision/<int:id_artista>')
def crear_comision(id_artista):
    es_global = id_artista is None
    id_cliente = session.get("id_usuario")

    if not id_cliente:
        return redirect(url_for('login'))  # Por seguridad, si no hay sesión

    return render_template(
        "crear_comision.html",
        es_global=es_global,
        id_artista=id_artista,
        id_cliente=id_cliente
    )

@vista_bp.route('/comisiones')
def comisiones():
    return "<h1>comisiones en construcción</h1>"

@vista_bp.route('/notificaciones')
def notificaciones():
    return "<h1>notificaciones en construcción</h1>"

@vista_bp.route('/perfil')
def perfil():
    return "<h1>Perfil en construcción</h1>"
