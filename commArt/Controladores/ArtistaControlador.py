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
    com_realizadas = ArtistaServicio.obtener_comisiones_realizadas(id_artista)
    if com_realizadas:
        data = [
            {
                "id_comision": c.id_com,
                "descripcion": c.descripcion_com,
                "dibujo": c.dibujo,
                "estado": c.estado,
                "fecha_creacion": c.fecha_creacion,
                "tipo": c.tipo,
                "artista": id_artista,
                "cliente": c.cliente.username
            }
            for c in com_realizadas
        ]
        http = 200
    else:
        data = {"mensaje": "No se encontraron comisiones"}
        http = 404

    return jsonify(data), http

@artista_bp.route('/artistas/<int:id_artista>/categorias', methods=['GET'])
def obtener_categorias(id_artista):
    categorias = ArtistaServicio.obtener_categorias_artista(id_artista)
    if categorias:
        data = [
            {
                "id_categoria": c.id_categoria,
                "nombre_categoria": c.nombre_categoria
            }
            for c in categorias
        ]
        http = 200
    else:
        data = {"mensaje": "No se encontraron categorias"}
        http = 404

    return jsonify(data), http

@artista_bp.route('/artistas/<int:id_artista>/publicaciones', methods=['GET'])
def obtener_publicaciones(id_artista):
    publicaciones = ArtistaServicio.obtener_publicaciones(id_artista)
    if publicaciones:
        data = [
            {
                "id_publicacion": p.id_publicacion,
                "descripcion": p.descripcion_publicacion,
                "dibujo": p.dibujo,
                "fecha_publicacion": p.fecha_publicacion,
                "num_likes": p.num_likes,
                "username": p.artista.usuario.username,
                "artista": id_artista
            }
            for p in publicaciones
        ]
        http = 200
    else:
        data = {"mensaje": "No se encontraron publicaciones"}
        http = 404

    return jsonify(data), http

@artista_bp.route('/artistas/<int:id_artista>/categorias/<int:id_categoria>', methods=['POST'])
def asignar_categoria(id_artista, id_categoria):
    try:
        ArtistaServicio.asignar_categoria(id_artista, id_categoria)
        return jsonify({"mensaje": "Categoría asignada correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@artista_bp.route('/artistas/<int:id_artista>/categorias/<int:id_categoria>', methods=['DELETE'])
def eliminar_categoria(id_artista, id_categoria):
    try:
        ArtistaServicio.desvincular_categoria(id_artista, id_categoria)
        return jsonify({"mensaje": "Categoría eliminada correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@artista_bp.route('/artistas/<int:id_artista>/apuntarse', methods=['POST'])
def apuntarse_comision(id_artista):
    data = request.get_json()
    id_comision = data.get("id_comision")

    if not id_comision:
        data_json = {"error": "ID de comisión requerido"}
        http = 400
    else:
        exito = ArtistaServicio.apuntarse_a_comision(id_artista, id_comision)
        if exito:
            data_json = {
                "id_artista": id_artista,
                "id_comision": id_comision
            }
            http = 200
        else:
            data_json = {
                "mensaje": "No se pudo apuntar (ya apuntado o datos inválidos)"
            }
            http = 400

    return jsonify(data_json), http

@artista_bp.route('/artistas/<int:id_artista>/comisiones-apuntadas', methods=['GET'])
def obtener_comisiones_apuntadas(id_artista):
    comisiones = ArtistaServicio.obtener_comisiones_apuntadas(id_artista)
    return jsonify(comisiones), 200

