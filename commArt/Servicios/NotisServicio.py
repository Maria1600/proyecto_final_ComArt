from Repositorios.NotisRepo import NotisRepositorio

class NotisServicio:

    @staticmethod
    def listar_notis():
        return NotisRepositorio.obtener_todo()

    @staticmethod
    def crear_noti(descripcion,id_usuario):
        return NotisRepositorio.crear(descripcion,id_usuario)

    @staticmethod
    def eliminar_noti(noti_id):
        return NotisRepositorio.eliminar(noti_id)