from Repositorios.MensajeRepo import MensajeRepositorio

class CategoriaServicio:

    @staticmethod
    def listar_mensajes():
        return MensajeRepositorio.obtener_todo()

    @staticmethod
    def buscar_mensajes(mensaje_id):
        return MensajeRepositorio.obtener_por_id(mensaje_id)

    @staticmethod
    def crear_mensaje(texto,fecha,id_creador,id_comision):
        return MensajeRepositorio.crear(texto,fecha,id_creador,id_comision)

    @staticmethod
    def eliminar_mensaje(mensaje_id):
        return MensajeRepositorio.eliminar(mensaje_id)

    @staticmethod
    def actualizar(mensaje_id, texto):
        return MensajeRepositorio.actualizar(mensaje_id, texto)