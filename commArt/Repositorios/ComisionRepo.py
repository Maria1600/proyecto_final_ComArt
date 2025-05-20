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
    def crear(descripcion,estado,fecha,tipo):
        comision = Comision(
            descripcion_com=descripcion,
            estado=estado,
            fecha_creacion=fecha,
            tipo=tipo
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
