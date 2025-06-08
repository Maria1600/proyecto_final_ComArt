from flask import Blueprint, jsonify, request, session, redirect, url_for
from Servicios.UsuarioServicio import UsuarioServicio

#Blueprint
usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/usuarios', methods=['GET'])
def obtener_todas():
    usuario = UsuarioServicio.listar_usuarios()

    data = [
        {
            "id_usuario": u.id_usuario,
            "es_artista": 1 if u.artista else 0, #Devolvemos 1 si es artista 0 si no
            "correo": u.correo,
            "username": u.username,
            "contrasenia": u.contrasenia,
            "fecha_nacimiento": u.fecha_nacimiento
        }
        for u in usuario
    ]

    return jsonify(data), 200

@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['GET'])
def obtener_usuario(id_usuario):
    usuario = UsuarioServicio.buscar_usuario(id_usuario)

    if usuario:
        #Obtenemos seguidores y seguidos para contarlos
        seguidores = UsuarioServicio.obtener_seguidores(id_usuario)
        seguidos = UsuarioServicio.obtener_seguidos(id_usuario)

        data = {
            "id_usuario": usuario.id_usuario,
            "es_artista": 1 if usuario.artista else 0,
            "correo": usuario.correo,
            "username": usuario.username,
            "descripcion": usuario.descripcion,
            "contrasenia": usuario.contrasenia,
            "fecha_nacimiento": usuario.fecha_nacimiento,
            "n_seguidores": len(seguidores),
            "n_seguidos": len(seguidos)
        }
        http = 200
    else:
        data = {"error": "Usuario no encontrado"}
        http = 404

    return jsonify(data), http

@usuario_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    correo = data.get("correo")
    username = data.get("username")
    contrasenia = data.get("contrasenia")
    fecha = data.get("fecha_nacimiento")
    es_artista = data.get("es_artista", False)

    if correo and username and contrasenia and fecha:

        #Validar si el correo ya esta registrado
        if UsuarioServicio.obtener_por_correo(correo):
            return jsonify({"error": "Este correo ya está registrado"}), 400

        # Validar si el username ya está en uso
        if UsuarioServicio.obtener_por_username(username):
            return jsonify({"error": "El nombre de usuario ya existe"}), 400

        nueva = UsuarioServicio.crear_usuario(correo, username ,contrasenia, fecha, es_artista)

        #Como solo se utiliza para el register
        #Guarda el usuario en la sesión para saber quien es el user logeado en cualquier momento
        session['id_usuario'] = nueva.id_usuario
        session['username'] = nueva.username

        data_json = {
            "id_usuario": nueva.id_usuario,
            "es_artista": 1 if nueva.artista else 0,
            "correo": nueva.correo,
            "username": nueva.username,
            "contrasenia": nueva.contrasenia,
            "fecha_nacimiento": nueva.fecha_nacimiento
        }
        http = 201
    else:
        data_json = {"error": "Parametros invalidos"}
        http = 400

    return jsonify(data_json), http

@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def actualizar_usuario(id_usuario):
    data = request.get_json()
    correo = data.get("correo")
    username = data.get("username")
    descripcion = data.get("descripcion")
    contrasenia = data.get("contrasenia")
    fecha = data.get("fecha_nacimiento")

    if correo and username and fecha:

        actualizada = UsuarioServicio.actualizar(id_usuario, correo, username ,contrasenia, fecha, descripcion)

        if actualizada:
            data_json = {
                "id_usuario": actualizada.id_usuario,
                "es_artista": 1 if actualizada.artista else 0,
                "correo": actualizada.correo,
                "username": actualizada.username,
                "fecha_nacimiento": actualizada.fecha_nacimiento,
                "descripcion": actualizada.descripcion
            }
            http = 200
        else:
            data_json = {"error": "Usuario no encontrada"}
            http = 404

    else:
        data_json = {"error": "Parametros invalidos"}
        http = 400

    return jsonify(data_json), http

@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
    exito = UsuarioServicio.eliminar_usuario(id_usuario)

    if exito:
        data = {"mensaje": "Usuario eliminado"}
        http = 200
    else:
        data = {"error": "Usuario no encontrado"}
        http = 404

    return jsonify(data), http

@usuario_bp.route('/usuarios/<int:id_usuario>/seguidores', methods=['GET'])
def obtener_seguidores(id_usuario):
    usuarios = UsuarioServicio.obtener_seguidores(id_usuario)
    if usuarios:
        data = [
            {
                "id_usuario": u.id_usuario,
                "username": u.username,
                "es_artista": 1 if u.artista else 0
            }
            for u in usuarios
        ]
        http = 200
    else:
        data = {"mensaje": "No se encontraron seguidores"}
        http = 404

    return jsonify(data), http

@usuario_bp.route('/usuarios/<int:id_usuario>/seguidos', methods=['GET'])
def obtener_seguidos(id_usuario):
    usuarios = UsuarioServicio.obtener_seguidos(id_usuario)
    if usuarios:
        data = [
            {
                "id_usuario": u.id_usuario,
                "username": u.username,
                "es_artista": 1 if u.artista else 0
            }
            for u in usuarios
        ]
        http = 200
    else:
        data = {"mensaje": "No se encontraron seguidos"}
        http = 404

    return jsonify(data), http

@usuario_bp.route('/usuarios/<int:id_usuario>/comisiones_solicitadas', methods=['GET'])
def obtener_comisiones_solicitadas(id_usuario):
    com_solicitadas = UsuarioServicio.obtener_comisiones_solicitadas(id_usuario)
    if com_solicitadas:
        data = [
            {
                "id_comision": c.id_com,
                "descripcion": c.descripcion_com,
                "dibujo": c.dibujo,
                "estado": c.estado,
                "fecha_creacion": c.fecha_creacion,
                "tipo": c.tipo,
                "artista": c.artista.usuario.username,
                "cliente": id_usuario
            }
            for c in com_solicitadas
        ]
        http = 200
    else:
        data = {"mensaje": "No se encontraron com_solicitadas"}
        http = 404

    return jsonify(data), http

@usuario_bp.route('/usuarios/<int:id_usuario>/seguir/<int:user_id_a_seguir>', methods=['POST'])
def seguir_usuario(id_usuario, user_id_a_seguir):
    exito = UsuarioServicio.seguir(user_id_a_seguir, id_usuario)

    if exito:
        data = {"mensaje": "Usuario seguido correctamente"}
        http = 200
    else:
        data = {"mensaje": "No se pudo seguir al usuario"}
        http = 404

    return jsonify(data), http

@usuario_bp.route('/usuarios/<int:id_usuario>/dejar_de_seguir/<int:user_id_a_dejar_de_seguir>', methods=['POST'])
def dejar_de_seguir_usuario(id_usuario, user_id_a_dejar_de_seguir):
    exito = UsuarioServicio.dejar_de_seguir(user_id_a_dejar_de_seguir, id_usuario)

    if exito:
        data = {"mensaje": "Usuario dejado de seguir correctamente"}
        http = 200
    else:
        data = {"mensaje": "No se pudo dejar de seguir al usuario"}
        http = 404

    return jsonify(data), http

@usuario_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    correo = data.get("correo")
    contrasenia = data.get("contrasenia")

    if correo and contrasenia:
        usuario = UsuarioServicio.verificar_login(correo, contrasenia)
        if usuario:
            #Guarda el usuario en la sesión para saber quien es el user logeado en cualquier momento
            session['id_usuario'] = usuario.id_usuario
            session['username'] = usuario.username

            data_json = {
                "id_usuario": usuario.id_usuario,
                "correo": usuario.correo,
                "username": usuario.username
            }
            http = 200
        else:
            data_json = {"error": "Credenciales inválidas"}
            http = 401
    else:
        data_json = {"error": "Faltan campos obligatorios"}
        http = 400

    return jsonify(data_json), http

@usuario_bp.route('/logout')
def logout():
    session.clear()  # Elimina todos los datos de sesión
    return redirect(url_for('vista_bp.login'))  # Redirige al login

@usuario_bp.route('/usuarios/<int:id_usuario>/sigue_a/<int:id_objetivo>', methods=['GET'])
def comprobar_si_sigue(id_usuario, id_objetivo):
    sigue = UsuarioServicio.comprobar_si_sigue(id_usuario, id_objetivo)

    if sigue is None:
        data = {"error": "Error al comprobar seguimiento"}
        http = 400
    else:
        data = {"sigue": sigue}
        http = 200

    return jsonify(data), http