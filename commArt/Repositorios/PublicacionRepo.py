from app import db
from Modelos.Publicacion import Publicacion

class PublicacionRepositorio:

    @staticmethod
    def obtener_todo():
        return Publicacion.query.all()

    @staticmethod
    def obtener_por_id(publicacion_id):
        return Publicacion.query.get(publicacion_id)

    @staticmethod
    def crear(descripcion,dibujo,fecha,nlikes):
        publicacion = Publicacion(
            descripcion_publicacion=descripcion,
            dibujo=dibujo,
            fecha_publicacion=fecha,
            num_likes=nlikes
        )
        db.session.add(publicacion)
        db.session.commit()
        return publicacion

    @staticmethod
    def eliminar(publicacion_id):
        publicacion = Publicacion.query.get(publicacion_id)
        operacion_exitosa = False
        if publicacion:
            db.session.delete(publicacion)
            db.session.commit()
            operacion_exitosa = True
        return operacion_exitosa
