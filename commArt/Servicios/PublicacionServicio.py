from Repositorios.PublicacionRepo import PublicacionRepositorio

class CategoriaServicio:

    @staticmethod
    def listar_categorias():
        return PublicacionRepositorio.obtener_todo()

    @staticmethod
    def buscar_categoria(publicacion_id):
        return PublicacionRepositorio.obtener_por_id(publicacion_id)

    @staticmethod
    def crear_categoria(descripcion,dibujo,fecha,nlikes):
        return PublicacionRepositorio.crear(descripcion,dibujo,fecha,nlikes)

    @staticmethod
    def eliminar_categoria(publicacion_id):
        return PublicacionRepositorio.eliminar(publicacion_id)