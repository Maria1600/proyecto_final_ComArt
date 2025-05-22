from flask import Blueprint, jsonify, request
from Servicios.CategoriaServicio import CategoriaServicio

# Definimos el Blueprint esto sirve para tener cada componente mas organizado
# y por separado, organiza tanto las rutas como la logica
categoria_bp = Blueprint('categoria_bp', __name__)

# Definimos la ruta de esta y el tipo de endpoint
@categoria_bp.route('/categorias', methods=['GET'])
def obtener_todas():
    categorias = CategoriaServicio.listar_categorias()

    #Aqui estamos creado una lista de diccionarios(cada tupla es un diccionario)
    # esto lo que hace es recorrer categoria y cada objeto c se va guardando como
    # un diccionario dentro de la lista
    data = [{"id_categoria": c.id_categoria, "nombre_categoria": c.nombre_categoria}
    for c in categorias]

    # Devolvemos los datos a modo de Json, el 200 es codigo de estado de HTTP que indica que
    # la consulta fue exitosa
    return jsonify(data), 200

# Con <int:id> se indica que lo que va ahi es un int que es el id de categoria
@categoria_bp.route('/categorias/<int:categoria_id>', methods=['GET'])
def obtener_categoria(categoria_id):
    categoria = CategoriaServicio.buscar_categoria(categoria_id)

    if categoria:
        data = {
            "id_categoria": categoria.id_categoria,
            "nombre_categoria": categoria.nombre_categoria
        }
        # 200 es el codigo estandar de http cuando una solicitud se completo correctamente
        http = 200
    else:
        data = {"error": "Categoría no encontrada"}
        # 400 es el codigo estandar de http para cuando ha ocurrido un error interno
        http = 404

    return jsonify(data), http

# Un endpoint POST indica que se estan creando nuevos recursos
@categoria_bp.route('/categorias', methods=['POST'])
def crear_categoria():
    #Aqui se lee el cuerpo Json que le envia el cliente
    data = request.get_json()
    #Extrae el campo concreto del Json
    nombre = data.get("nombre_categoria")

    if nombre:
        nueva = CategoriaServicio.crear_categoria(nombre)
        data_json = {
            "id_categoria": nueva.id_categoria,
            "nombre_categoria": nueva.nombre_categoria
        }
        # 201 es el codigo estandar de http cuando algo ha sido creado
        http = 201
    else:
        data_json = {"error": "Nombre de categoría requerido"}
        # 400 es el codigo estandar de http cuando una peticion ha sido mal formada
        http = 400

    return jsonify(data_json), http

# Un endpoint PUT indica que se estan actualizando compenentes ya existentes
@categoria_bp.route('/categorias/<int:categoria_id>', methods=['PUT'])
def actualizar_categoria(categoria_id):
    data = request.get_json()
    nombre = data.get("nombre_categoria")

    if not nombre:
        data_json = {"error": "Nombre de categoría requerido"}
        http = 400
    else:
        actualizada = CategoriaServicio.actualizar(categoria_id, nombre)

        if actualizada:
            data_json = {
                "id_categoria": actualizada.id_categoria,
                "nombre_categoria": actualizada.nombre_categoria
            }
            http = 200
        else:
            data_json = {"error": "Categoría no encontrada"}
            http = 404

    return jsonify(data_json), http

@categoria_bp.route('/categorias/<int:categoria_id>', methods=['DELETE'])
def eliminar_categoria(categoria_id):
    exito = CategoriaServicio.eliminar_categoria(categoria_id)

    if exito:
        data = {"mensaje": "Categoría eliminada"}
        http = 200
    else:
        data = {"error": "Categoría no encontrada"}
        http = 404

    return jsonify(data), http

@categoria_bp.route('/categorias/<int:categoria_id>/artistas', methods=['GET'])
def obtener_artistas_por_categoria(categoria_id):
    artistas = CategoriaServicio.obtener_artistas_por_categoria(categoria_id)
    if artistas:
        data = [
            {
                "id_artista": a.id_artista,
                "username": a.usuario.username  # asumiendo que tienes relación Artista → Usuario
            }
            for a in artistas
        ]
        http = 200
    else:
        data = {"mensaje": "No se encontraron artistas"}
        http = 404

    return jsonify(data), http
