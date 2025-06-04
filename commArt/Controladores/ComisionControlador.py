from flask import Blueprint, jsonify, request
from Servicios.ComisionServicio import ComisionServicio

#Blueprint
comision_bp = Blueprint('comision_bp', __name__)

@comision_bp.route('/api/comisiones', methods=['GET'])
def obtener_todas():
    comision = ComisionServicio.listar_comision()

    data = [
        {
            "id_comision": c.id_com,
            "descripcion": c.descripcion_com,
            "dibujo": c.dibujo,
            "estado": c.estado,
            "fecha_creacion": c.fecha_creacion,
            "tipo": c.tipo,
            "artista": c.artista.usuario.username if c.artista and c.artista.usuario else None,
            #Como el artista puede ser null hay que hacer la comprobacion
            "cliente": c.cliente.username
        }
        for c in comision
    ]

    return jsonify(data), 200

@comision_bp.route('/api/comisiones/<int:id_comision>', methods=['GET'])
def obtener_comision(id_comision):
    comision = ComisionServicio.buscar_comision(id_comision)

    if comision:
        data = {
            "id_comision": comision.id_com,
            "descripcion": comision.descripcion_com,
            "dibujo": comision.dibujo,
            "estado": comision.estado,
            "fecha_creacion": comision.fecha_creacion,
            "tipo": comision.tipo,
            "artista": comision.artista.usuario.username,
            "cliente": comision.cliente.username
        }
        http = 200
    else:
        data = {"error": "Comision no encontrada"}
        http = 404

    return jsonify(data), http

@comision_bp.route('/comisiones/globales', methods=['GET'])
def obtener_comision_por_tipo_sin_asignar():
    comision = ComisionServicio.obtener_global_sin_asigar()

    data = [
        {
            "id_comision": c.id_com,
            "descripcion": c.descripcion_com,
            "estado": c.estado,
            "fecha_creacion": c.fecha_creacion,
            "tipo": c.tipo,
            "cliente": c.cliente.username
        }
        for c in comision
    ]

    print(">> Comisiones globales devueltas:", data)

    return jsonify(data), 200

@comision_bp.route('/comisiones', methods=['POST'])
def crear_comision():
    data = request.get_json()
    descripcion = data.get("descripcion")
    fecha = data.get("fecha_creacion")
    estado = data.get("estado")
    tipo = data.get("tipo")
    id_cliente = data.get("id_cliente")
    id_artista = data.get("id_artista")

    print("DATOS RECIBIDOS:", data)

    if descripcion and fecha and estado and tipo and id_cliente:
        estado_valido = estado in ['En espera']
        tipo_valido = tipo in ['Global', 'Individual']

        if estado_valido and tipo_valido:
            nueva = ComisionServicio.crear_comision(descripcion,estado,fecha,tipo,id_cliente,id_artista)
            data_json = {
                "id_comision": nueva.id_com,
                "descripcion": nueva.descripcion_com,
                "estado": nueva.estado,
                "fecha_creacion": nueva.fecha_creacion,
                "tipo": nueva.tipo,
                "artista": nueva.artista.usuario.username if nueva.artista else None,
                "cliente": nueva.cliente.username
            }
            http = 201
        else:
            data_json = {"error": "Estado o tipo no válidos"}
            http = 400
    else:
        data_json = {"error": "Parametros invalidos"}
        http = 400

    return jsonify(data_json), http

@comision_bp.route('/comisiones/<int:id_comision>', methods=['PUT'])
def actualizar_comision(id_comision):
    data = request.get_json()
    descripcion = data.get("descripcion")
    estado = data.get("estado")

    if descripcion and estado:
        estado_valido = estado in ['Aceptada', 'Rechazada', 'Cancelada', 'En espera', 'En proceso', 'Entregada', 'Terminada']

        if estado_valido:
            actualizada = ComisionServicio.actualizar(id_comision, descripcion, estado)

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
                data_json = {"error": "Comision no encontrada"}
                http = 404
        else:
            data_json = {"error": "Estado no válido"}
            http = 400

    else:
        data_json = {"error": "Parametros invalidos"}
        http = 400

    return jsonify(data_json), http

@comision_bp.route('/comisiones/<int:id_comision>', methods=['DELETE'])
def eliminar_comision(id_comision):
    exito = ComisionServicio.eliminar_comision(id_comision)

    if exito:
        data = {"mensaje": "Comision eliminada"}
        http = 200
    else:
        data = {"error": "Comision no encontrada"}
        http = 404

    return jsonify(data), http

@comision_bp.route('/comisiones/<int:id_comision>/artista', methods=['PUT'])
def asignar_artista(id_comision):
    data = request.get_json()
    id_artista = data.get("id_artista")

    if not id_artista:
        data_json = {"error": "Falta el ID del artista"}
        http = 400
    else:
        comision = ComisionServicio.actualizar_artista_global(id_comision, id_artista)

        if comision:
            data_json = {
                "id_publicacion": comision.id_publicacion,
                "descripcion": comision.descripcion_publicacion,
                "dibujo": comision.dibujo,
                "fecha_publicacion": comision.fecha_publicacion,
                "num_likes": comision.num_likes,
                "artista": comision.artista.usuario.username
            }
            http = 200
        else:
            data_json = {"error": "Comisión no encontrada o no es de tipo Global"}
            http = 404

    return jsonify(data_json), http

@comision_bp.route('/comisiones/<int:id_comision>/estado', methods=['PUT'])
def actualizar_estado(id_comision):
    data = request.get_json()
    estado = data.get("estado")

    if not estado:
        data_json = {"error": "Falta el estado"}
        http = 400
    else:
        estado_valido = estado in ['Aceptada', 'Rechazada', 'Cancelada', 'En espera', 'En proceso', 'Entregada', 'Terminada']

        if estado_valido:
            comision = ComisionServicio.actualizar_estado(id_comision, estado)

            if comision:
                data_json = {
                    "id_comision": comision.id_com,
                    "descripcion": comision.descripcion_com,
                    "estado": comision.estado,
                    "fecha_creacion": comision.fecha_creacion,
                    "tipo": comision.tipo,
                    "artista": comision.artista.usuario.username if comision.artista else None,
                    "cliente": comision.cliente.username
                }
                http = 200
            else:
                data_json = {"error": "Comisión no encontrada"}
                http = 404
        else:
            data_json = {"error": "Estado no válido"}
            http = 400

    return jsonify(data_json), http

@comision_bp.route('/comisiones/<int:id_comision>/dibujo', methods=['PUT'])
def entregar_dibujo(id_comision):
    data = request.get_json()
    dibujo = data.get("dibujo")

    if not dibujo:
        data_json = {"error": "Falta el dibujo"}
        http = 400
    else:
        comision = ComisionServicio.cargar_dibujo_a_bd(id_comision, dibujo)

        if comision:
            data_json = {
                "id_publicacion": comision.id_publicacion,
                "descripcion": comision.descripcion_publicacion,
                "dibujo": comision.dibujo,
                "fecha_publicacion": comision.fecha_publicacion,
                "num_likes": comision.num_likes,
                "artista": comision.artista.usuario.username
            }
            http = 200
        else:
            data_json = {"error": "Comisión no encontrada"}
            http = 404

    return jsonify(data_json), http

@comision_bp.route('/comisiones/<int:id_comision>/mensaje', methods=['GET'])
def obtener_mensajes(id_comision):
    mensajes = ComisionServicio.obtener_mensajes(id_comision)
    if mensajes:
        data = [
            {
                "creador": m.creador.username,
                "mensaje": m.texto,
                "fecha": m.fecha_creacion_mensaje
            }
            for m in mensajes
        ]
        http = 200
    else:
        data = {"mensaje": "No se encontraron mensajes"}
        http = 404

    return jsonify(data), http

@comision_bp.route('/comisiones/usuario/<int:id_usuario>', methods=['GET'])
def obtener_comisiones_usuario(id_usuario):
    comisiones = ComisionServicio.obtener_comisiones_de_usuario(id_usuario)
    data = [
        {
            "id_comision": c.id_com,
            "descripcion": c.descripcion_com,
            "dibujo": c.dibujo,
            "estado": c.estado,
            "fecha_creacion": c.fecha_creacion,
            "tipo": c.tipo,
            "artista": c.artista.usuario.username if c.artista and c.artista.usuario else None,
            #Como el artista puede ser null hay que hacer la comprobacion
            "cliente": c.cliente.username
        }
        for c in comisiones
    ]

    return jsonify(data), 200