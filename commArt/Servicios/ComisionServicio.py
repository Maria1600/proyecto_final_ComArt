from Repositorios.ComisionRepo import ComisionRepositorio

class ComisionServicio:

    @staticmethod
    def listar_categorias():
        return ComisionRepositorio.obtener_todo()

    @staticmethod
    def buscar_categoria(comision_id):
        return ComisionRepositorio.obtener_por_id(comision_id)

    @staticmethod
    def crear_categoria(descripcion,estado,fecha,tipo,id_cliente,id_artista):
        return ComisionRepositorio.crear(descripcion,estado,fecha,tipo,id_cliente,id_artista)

    @staticmethod
    def eliminar_categoria(comision_id):
        return ComisionRepositorio.eliminar(comision_id)

    @staticmethod
    def actualizar(comision_id, new_descripcion, new_estado, new_fecha, new_tipo):
        return ComisionRepositorio.actualizar(comision_id, new_descripcion, new_estado, new_fecha, new_tipo)

    @staticmethod
    def actualizar_artista_global(comision_id, id_artista):
        return ComisionRepositorio.actualizar_artista_global(comision_id, id_artista)

    @staticmethod
    def obtener_mensajes(comision_id):
        return ComisionRepositorio.obtener_mensajes(comision_id)