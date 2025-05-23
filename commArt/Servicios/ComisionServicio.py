from Repositorios.ComisionRepo import ComisionRepositorio

class ComisionServicio:

    @staticmethod
    def listar_comision():
        return ComisionRepositorio.obtener_todo()

    @staticmethod
    def buscar_comision(comision_id):
        return ComisionRepositorio.obtener_por_id(comision_id)

    @staticmethod
    def crear_comision(descripcion,estado,fecha,tipo,id_cliente,id_artista):
        return ComisionRepositorio.crear(descripcion,estado,fecha,tipo,id_cliente,id_artista)

    @staticmethod
    def eliminar_comision(comision_id):
        return ComisionRepositorio.eliminar(comision_id)

    @staticmethod
    def actualizar(comision_id, new_descripcion, new_estado):
        return ComisionRepositorio.actualizar(comision_id, new_descripcion, new_estado)

    @staticmethod
    def actualizar_artista_global(comision_id, id_artista):
        return ComisionRepositorio.actualizar_artista_global(comision_id, id_artista)

    @staticmethod
    def actualizar_estado(comision_id, estado):
        return ComisionRepositorio.actualizar_estado(comision_id, estado)

    @staticmethod
    def cargar_dibujo_a_bd(comision_id, dibujo):
        return ComisionRepositorio.cargar_dibujo_a_bd(comision_id, dibujo)

    @staticmethod
    def obtener_mensajes(comision_id):
        return ComisionRepositorio.obtener_mensajes(comision_id)