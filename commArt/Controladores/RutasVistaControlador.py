from flask import Blueprint, render_template, session, redirect, url_for, request

from Servicios.PublicacionServicio import PublicacionServicio
from Servicios.UsuarioServicio import UsuarioServicio

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
    if 'id_usuario' not in session:
        return redirect(url_for('login')) # Por seguridad, si no hay sesión

    return render_template("comisiones.html")

@vista_bp.route('/notificaciones')
def notificaciones():
    return "<h1>notificaciones en construcción</h1>"

@vista_bp.route('/detalles_perfil')
def detalles_perfil():
    return "<h1>detalles_perfil en construcción</h1>"

@vista_bp.route('/perfil/<int:id_usuario>')
def perfil(id_usuario):
    id_logado = session.get('id_usuario')
    es_logado = id_logado == id_usuario
    sigue = False
    if 'id_usuario' not in session:
        return redirect(url_for('usuario_bp.login'))

    if id_logado and not es_logado:
        sigue = UsuarioServicio.comprobar_si_sigue(id_logado, id_usuario)

    return render_template(
        "perfil.html",
        id_usuario=id_usuario,
        es_logado=bool(id_logado),
        id_logado=id_logado,
        modo_edicion=bool(request.args.get("editar")),
        id_editando=request.args.get("editar_pub", type=int),
        sigue=sigue
    )


@vista_bp.route('/perfil')
def perfil_redirect():
    if 'id_usuario' not in session:
        return redirect(url_for('usuario_bp.login'))  # O una página de error/login
    return redirect(url_for('vista_bp.perfil', id_usuario=session['id_usuario']))

@vista_bp.route('/seleccionar_tags')
def seleccionar_tags():
    if 'id_usuario' not in session:
        return redirect(url_for('login'))

    return render_template('seleccionar_tags.html')

