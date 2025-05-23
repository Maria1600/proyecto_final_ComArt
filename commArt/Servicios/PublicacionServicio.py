from Repositorios.PublicacionRepo import PublicacionRepositorio

class PublicacionServicio:

    @staticmethod
    def listar_publicacion():
        return PublicacionRepositorio.obtener_todo()

    @staticmethod
    def buscar_publicacion(publicacion_id):
        return PublicacionRepositorio.obtener_por_id(publicacion_id)

    @staticmethod
    def crear_publicacion(descripcion,dibujo,fecha,nlikes,id_artista):
        return PublicacionRepositorio.crear(descripcion,dibujo,fecha,nlikes,id_artista)

    @staticmethod
    def eliminar_publicacion(publicacion_id):
        return PublicacionRepositorio.eliminar(publicacion_id)

    @staticmethod
    def actualizar(publicacion_id, new_descripcion, new_dibujo, new_fecha):
        return PublicacionRepositorio.actualizar(publicacion_id, new_descripcion, new_dibujo, new_fecha)

    @staticmethod
    def add_like(publicacion_id):
        return PublicacionRepositorio.add_like(publicacion_id)