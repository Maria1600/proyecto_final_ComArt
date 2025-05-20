from Repositorios.MensajeRepo import MensajeRepositorio

class CategoriaServicio:

    @staticmethod
    def listar_mensajes():
        return MensajeRepositorio.obtener_todo()

    @staticmethod
    def buscar_mensajes(mensaje_id):
        return MensajeRepositorio.obtener_por_id(mensaje_id)

    @staticmethod
    def crear_categoria(texto,fecha):
        return MensajeRepositorio.crear(texto,fecha)

    @staticmethod
    def eliminar_categoria(mensaje_id):
        return MensajeRepositorio.eliminar(mensaje_id)