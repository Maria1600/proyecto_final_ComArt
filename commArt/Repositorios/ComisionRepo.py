from datetime import datetime

from sqlalchemy.orm import joinedload

from Modelos.Mensaje import Mensaje
from app import db
from Modelos.Comision import Comision

class ComisionRepositorio:

    @staticmethod
    def obtener_todo():
        return Comision.query.all()

    @staticmethod
    def obtener_por_id(comision_id):
        return Comision.query.get(comision_id)

    @staticmethod
    def crear(descripcion,estado,fecha,tipo,id_cliente,id_artista):
        comision = Comision(
            descripcion_com=descripcion,
            estado=estado,
            fecha_creacion=fecha,
            tipo=tipo,
            id_cliente_com = id_cliente,
            id_artista_com = id_artista
        )
        db.session.add(comision)
        db.session.commit()
        return comision

    @staticmethod
    def eliminar(comision_id):
        comision = Comision.query.get(comision_id)
        operacion_exitosa = False
        if comision:
            db.session.delete(comision)
            db.session.commit()
            operacion_exitosa = True
        return operacion_exitosa

    @staticmethod
    def actualizar(comision_id, new_descripcion, new_estado, new_fecha, new_tipo):
        comision = Comision.query.get(comision_id)
        if comision:
            comision.descripcion_com = new_descripcion,
            comision.estado = new_estado,
            comision.fecha_creacion = new_fecha,
            comision.tipo = new_tipo
            db.session.commit()
        return comision if comision else None

    @staticmethod
    def actualizar_artista_global(comision_id, id_artista):
        comision = Comision.query.get(comision_id)
        if comision and comision.tipo == "Global":
            comision.id_artista_com = id_artista
            db.session.commit()
        return comision if comision else None

    @staticmethod
    def obtener_mensajes(comision_id):
        comision = Comision.query.options(joinedload(Comision.mensajes)).filter_by(id_com=comision_id).first()
        return comision.mensajes if comision else []
