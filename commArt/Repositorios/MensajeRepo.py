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
    def crear(texto,fecha,id_creador,id_comision):
        mensaje = Mensaje(
            texto=texto,
            fecha_creacion_mensaje = fecha,
            id_user_creador = id_creador,
            id_com_asociada = id_comision
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

    @staticmethod
    def actualizar(mensaje_id, texto):
        mensaje = Mensaje.query.get(mensaje_id)
        if mensaje:
            mensaje.texto = texto
            db.session.commit()
        return mensaje if mensaje else None