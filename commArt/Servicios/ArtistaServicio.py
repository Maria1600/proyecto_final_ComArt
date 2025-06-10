from Repositorios.ArtistaRepo import ArtistaRepositorio

class ArtistaServicio:

    @staticmethod
    def listar_artista():
        return ArtistaRepositorio.obtener_todo()

    @staticmethod
    def buscar_artista(id_artista):
        return ArtistaRepositorio.obtener_por_id(id_artista)

    @staticmethod
    def crear_artista(user_id):
        return ArtistaRepositorio.crear(user_id)

    @staticmethod
    def eliminar_artista(id_artista):
        return ArtistaRepositorio.eliminar(id_artista)

    @staticmethod
    def obtener_comisiones_realizadas(id_artista):
        return ArtistaRepositorio.obtener_comisiones_realizadas(id_artista)

    @staticmethod
    def obtener_categorias_artista(id_artista):
        return ArtistaRepositorio.obtener_categorias_por_artista(id_artista)

    @staticmethod
    def obtener_publicaciones(id_artista):
        return ArtistaRepositorio.obtener_publicaciones(id_artista)

    @staticmethod
    def asignar_categoria(id_artista, id_categoria):
        return ArtistaRepositorio.asignar_categoria(id_artista, id_categoria)

    @staticmethod
    def desvincular_categoria(id_artista, id_categoria):
        return ArtistaRepositorio.desvincular_categoria(id_artista, id_categoria)

    @staticmethod
    def apuntarse_a_comision(id_artista, id_comision):
        return ArtistaRepositorio.apuntarse_a_comision(id_artista, id_comision)

    @staticmethod
    def obtener_comisiones_apuntadas(id_artista):
        return ArtistaRepositorio.obtener_ids_comisiones_apuntadas(id_artista)
