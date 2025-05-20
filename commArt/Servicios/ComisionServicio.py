from Repositorios.ComisionRepo import ComisionRepositorio

class ComisionServicio:

    @staticmethod
    def listar_categorias():
        return ComisionRepositorio.obtener_todo()

    @staticmethod
    def buscar_categoria(comision_id):
        return ComisionRepositorio.obtener_por_id(comision_id)

    @staticmethod
    def crear_categoria(descripcion,estado,fecha,tipo):
        return ComisionRepositorio.crear(descripcion,estado,fecha,tipo)

    @staticmethod
    def eliminar_categoria(comision_id):
        return ComisionRepositorio.eliminar(comision_id)