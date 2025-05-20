from app import db
from Modelos.Mensaje import Mensaje

class MensajeRepositorio:

    @staticmethod
    def obtener_todo():
        return Mensaje.query.all()

    #CUIDADO QUE EN PYTHON HAY UNA FUNCION ID Y SI SE PONE SOLO ESO SE RALLA
    @staticmethod
    def obtener_por_id(mensaje_id):
        return Mensaje.query.get(mensaje_id)

    @staticmethod
    def crear(texto,fecha):
        mensaje = Mensaje(
            texto=texto,
            fecha_creacion_mensaje = fecha
        )
        db.session.add(mensaje)
        db.session.commit()
        return mensaje

    @staticmethod
    def eliminar(mensaje_id):
        mensaje = Mensaje.query.get(mensaje_id)
        operacion_exitosa = False
        if mensaje:
            db.session.delete(mensaje)
            db.session.commit()
            operacion_exitosa = True
        return operacion_exitosa
