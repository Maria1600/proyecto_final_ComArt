from flask import Blueprint, jsonify, request

from Servicios.MensajeServicio import MensajeServicio

#Blueprint
publicacion_bp = Blueprint('mensaje_bp', __name__)

@publicacion_bp.route('/mensajes', methods=['GET'])
def obtener_todas():
    mensajes = MensajeServicio.listar_mensajes()

    data = [
        {
            "id_mensaje": m.id_mensaje,
            "texto": m.texto,
            "fecha_creacion": m.fecha_creacion_mensaje,
            "creador": m.creador.username,
            "comision": m.id_com_asociada
        }
        for m in mensajes
    ]

    return jsonify(data), 200

@publicacion_bp.route('/mensajes/<int:id_mensaje>', methods=['GET'])
def obtener_mensaje(id_mensaje):
    mensaje = MensajeServicio.buscar_mensaje(id_mensaje)

    if mensaje:
        data = {
            "id_mensaje": mensaje.id_mensaje,
            "texto": mensaje.texto,
            "fecha_creacion": mensaje.fecha_creacion_mensaje,
            "creador": mensaje.creador.username,
            "comision": mensaje.id_com_asociada
        }
        http = 200
    else:
        data = {"error": "Mensaje no encontrado"}
        http = 404

    return jsonify(data), http

@publicacion_bp.route('/mensajes', methods=['POST'])
def crear_mensaje():
    data = request.get_json()
    texto = data.get("texto")
    id_creador = data.get("id_creador")
    fecha = data.get("fecha_creacion")
    id_comision = data.get("id_comision")

    if texto and id_creador and fecha and id_comision:
        nueva = MensajeServicio.crear_mensaje(texto,fecha,id_creador,id_comision)
        data_json = {
            "id_mensaje": nueva.id_mensaje,
            "texto": nueva.texto,
            "fecha_creacion": nueva.fecha_creacion_mensaje,
            "creador": nueva.creador.username,
            "comision": nueva.id_com_asociada
        }
        http = 201
    else:
        data_json = {"error": "Parametros invalidos"}
        http = 400

    return jsonify(data_json), http

@publicacion_bp.route('/mensajes/<int:id_mensaje>', methods=['PUT'])
def actualizar_publicacion(id_mensaje):
    data = request.get_json()
    texto = data.get("texto")

    if texto:
        actualizada = MensajeServicio.actualizar(id_mensaje, texto)

        if actualizada:
            data_json = {
                "id_mensaje": actualizada.id_mensaje,
                "texto": actualizada.texto,
                "fecha_creacion": actualizada.fecha_creacion_mensaje,
                "creador": actualizada.creador.username,
                "comision": actualizada.id_com_asociada
            }
            http = 200
        else:
            data_json = {"error": "Mensaje no encontrado"}
            http = 404

    else:
        data_json = {"error": "Parametros invalidos"}
        http = 400


    return jsonify(data_json), http

@publicacion_bp.route('/mensajes/<int:id_mensaje>', methods=['DELETE'])
def eliminar_mensaje(id_mensaje):
    exito = MensajeServicio.eliminar_mensaje(id_mensaje)

    if exito:
        data = {"mensaje": "Mensaje eliminado"}
        http = 200
    else:
        data = {"error": "Mensaje no encontrado"}
        http = 404

    return jsonify(data), http

