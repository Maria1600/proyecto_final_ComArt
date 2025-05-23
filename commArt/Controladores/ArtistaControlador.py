from flask import Blueprint, jsonify, request
from Servicios.ArtistaServicio import ArtistaServicio

#Blueprint
artista_bp = Blueprint('artista_bp', __name__)

@artista_bp.route('/artistas', methods=['GET'])
def obtener_todas():
    artista = ArtistaServicio.listar_artista()

    data = [
        {
            "id_artista": a.id_artista,
            "correo": a.usuario.correo,
            "username": a.usuario.username,
            "contrasenia": a.usuario.contrasenia,
            "fecha_nacimiento": a.usuario.fecha_nacimiento
        }
        for a in artista
    ]

    return jsonify(data), 200

@artista_bp.route('/artistas/<int:id_artista>', methods=['GET'])
def obtener_artista(id_artista):
    artista = ArtistaServicio.buscar_artista(id_artista)

    if artista:
        data = {
            "id_artista": artista.id_artista,
            "correo": artista.usuario.correo,
            "username": artista.usuario.username,
            "contrasenia": artista.usuario.contrasenia,
            "fecha_nacimiento": artista.usuario.fecha_nacimiento
        }
        http = 200
    else:
        data = {"error": "Artista no encontrado"}
        http = 404

    return jsonify(data), http

@artista_bp.route('/artistas', methods=['POST'])
def crear_artista():
    data = request.get_json()
    id_user = data.get("id_usuario")

    if id_user :
        nueva = ArtistaServicio.crear_artista(id_user)
        data_json = {
            "id_artista": nueva.id_artista,
            "correo": nueva.usuario.correo,
            "username": nueva.usuario.username,
            "contrasenia": nueva.usuario.contrasenia,
            "fecha_nacimiento": nueva.usuario.fecha_nacimiento
        }
        http = 201
    else:
        data_json = {"error": "Parametros invalidos"}
        http = 400

    return jsonify(data_json), http

@artista_bp.route('/artistas/<int:id_artista>', methods=['DELETE'])
def eliminar_artista(id_artista):
    exito = ArtistaServicio.eliminar_artista(id_artista)

    if exito:
        data = {"mensaje": "Artista eliminado"}
        http = 200
    else:
        data = {"error": "Artista no encontrado"}
        http = 404

    return jsonify(data), http

@artista_bp.route('/artistas/<int:id_artista>/comisiones_realizadas', methods=['GET'])
def obtener_comisiones_realizadas(id_artista):
    artista = ArtistaServicio.obtener_comisiones_realizadas(id_artista)
    if artista:
        data = [
            {
                "id_comision": a.comisiones_realizadas.id_com,
                "descripcion": a.comisiones_realizadas.descripcion_com,
                "dibujo": a.comisiones_realizadas.dibujo,
                "estado": a.comisiones_realizadas.estado,
                "fecha_creacion": a.comisiones_realizadas.fecha_creacion,
                "tipo": a.comisiones_realizadas.tipo,
                "artista": a.id_artista,
                "cliente": a.comisiones_realizadas.cliente.username
            }
            for a in artista
        ]
        http = 200
    else:
        data = {"mensaje": "No se encontraron comisiones"}
        http = 404

    return jsonify(data), http

@artista_bp.route('/artistas/<int:id_artista>/categorias', methods=['GET'])
def obtener_categorias(id_artista):
    artista = ArtistaServicio.obtener_categorias_artista(id_artista)
    if artista:
        data = [
            {
                "id_categoria": a.categorias.id_categoria,
                "nombre_categoria": a.categorias.nombre_categoria
            }
            for a in artista
        ]
        http = 200
    else:
        data = {"mensaje": "No se encontraron categorias"}
        http = 404

    return jsonify(data), http

@artista_bp.route('/artistas/<int:id_artista>/publicaciones', methods=['GET'])
def obtener_publicaciones(id_artista):
    artista = ArtistaServicio.obtener_publicaciones(id_artista)
    if artista:
        data = [
            {
                "id_publicacion": a.publicaciones.id_publicacion,
                "descripcion": a.publicaciones.descripcion_publicacion,
                "dibujo": a.publicaciones.dibujo,
                "fecha_publicacion": a.publicaciones.fecha_publicacion,
                "num_likes": a.publicaciones.num_likes,
                "artista": a.id_artista
            }
            for a in artista
        ]
        http = 200
    else:
        data = {"mensaje": "No se encontraron publicaciones"}
        http = 404

    return jsonify(data), http