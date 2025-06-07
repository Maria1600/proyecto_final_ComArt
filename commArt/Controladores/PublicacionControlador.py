from datetime import datetime

from flask import Blueprint, jsonify, request
from Servicios.PublicacionServicio import PublicacionServicio

#Blueprint
publicacion_bp = Blueprint('publicacion_bp', __name__)

@publicacion_bp.route('/publicaciones', methods=['GET'])
def obtener_todas():
    publicaciones = PublicacionServicio.listar_publicacion()

    data = [
        {
            "id_publicacion": p.id_publicacion,
            "descripcion": p.descripcion_publicacion,
            "dibujo": p.dibujo,
            "fecha_publicacion": p.fecha_publicacion,
            "num_likes": p.num_likes,
            "artista": p.artista.usuario.username,
            "id_artista": p.artista.id_artista
        }
        for p in publicaciones
    ]

    return jsonify(data), 200

@publicacion_bp.route('/publicaciones/<int:id_publicacion>', methods=['GET'])
def obtener_publicacion(id_publicacion):
    publicacion = PublicacionServicio.buscar_publicacion(id_publicacion)

    if publicacion:
        data = {
            "id_publicacion": publicacion.id_publicacion,
            "descripcion": publicacion.descripcion_publicacion,
            "dibujo": publicacion.dibujo,
            "fecha_publicacion": publicacion.fecha_publicacion,
            "num_likes": publicacion.num_likes,
            "artista": publicacion.artista.usuario.username
        }
        http = 200
    else:
        data = {"error": "Publicacion no encontrada"}
        http = 404

    return jsonify(data), http

@publicacion_bp.route('/publicaciones', methods=['POST'])
def crear_publicacion():
    data = request.get_json()
    descripcion = data.get("descripcion")
    dibujo = data.get("dibujo")
    fecha_str = data.get("fecha_publicacion")
    nlikes = data.get("nlikes", 0)
    id_artista = data.get("id_artista")

    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return jsonify({"error": "Fecha inválida"}), 400

    if descripcion and dibujo and fecha and id_artista:
        nueva = PublicacionServicio.crear_publicacion(descripcion,dibujo,fecha,nlikes,id_artista)
        data_json = {
            "id_publicacion": nueva.id_publicacion,
            "descripcion": nueva.descripcion_publicacion,
            "dibujo": nueva.dibujo,
            "fecha_publicacion": nueva.fecha_publicacion,
            "num_likes": nueva.num_likes,
            "artista": nueva.artista.usuario.username
        }
        http = 201
    else:
        data_json = {"error": "Parametros invalidos"}
        http = 400

    return jsonify(data_json), http

@publicacion_bp.route('/publicaciones/<int:id_publicacion>', methods=['PUT'])
def actualizar_publicacion(id_publicacion):
    data = request.get_json()
    descripcion = data.get("descripcion")

    if descripcion:
        actualizada = PublicacionServicio.actualizar(id_publicacion, descripcion)

        if actualizada:
            data_json = {
                "id_publicacion": actualizada.id_publicacion,
                "descripcion": actualizada.descripcion_publicacion,
                "dibujo": actualizada.dibujo,
                "fecha_publicacion": actualizada.fecha_publicacion,
                "num_likes": actualizada.num_likes,
                "artista": actualizada.artista.usuario.username
            }
            http = 200
        else:
            data_json = {"error": "Publicacion no encontrada"}
            http = 404

    else:
        data_json = {"error": "Parametros invalidos"}
        http = 400


    return jsonify(data_json), http

@publicacion_bp.route('/publicaciones/<int:id_publicacion>', methods=['DELETE'])
def eliminar_publicacion(id_publicacion):
    exito = PublicacionServicio.eliminar_publicacion(id_publicacion)

    if exito:
        data = {"mensaje": "Publicacion eliminada"}
        http = 200
    else:
        data = {"error": "Publicacion no encontrada"}
        http = 404

    return jsonify(data), http

@publicacion_bp.route('/publicaciones/<int:publicacion_id>/like', methods=['PUT'])
def agregar_like(publicacion_id):
    publicacion = PublicacionServicio.add_like(publicacion_id)

    if publicacion:
        data = {
            "id_publicacion": publicacion.id_publicacion,
            "num_likes": publicacion.num_likes
        }
        http = 200
    else:
        data = {"error": "Publicación no encontrada"}
        http = 404

    return jsonify(data), http
