from sqlalchemy.orm import joinedload

from Modelos.Notificacion import Notificacion
from extensiones import db

class NotisRepositorio:

    @staticmethod
    def obtener_todo():
        return Notificacion.query.all()

    @staticmethod
    def crear(descripcion,id_usuario):
        notificacion = Notificacion(
            texto=descripcion,
            id_usuario=id_usuario
        )
        db.session.add(notificacion)
        db.session.commit()
        return notificacion

    @staticmethod
    def eliminar(noti_id):
        notificacion = Notificacion.query.get(noti_id)
        operacion_exitosa = False
        if notificacion:
            db.session.delete(notificacion)
            db.session.commit()
            operacion_exitosa = True
        return operacion_exitosa