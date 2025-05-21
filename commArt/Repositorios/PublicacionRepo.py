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
    def crear(descripcion,dibujo,fecha,nlikes,id_artista):
        publicacion = Publicacion(
            descripcion_publicacion=descripcion,
            dibujo=dibujo,
            fecha_publicacion=fecha,
            num_likes=nlikes,
            id_artista_publicacion=id_artista
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

    @staticmethod
    def actualizar(publicacion_id, new_descripcion, new_dibujo, new_fecha):
        publicacion = Publicacion.query.get(publicacion_id)
        if publicacion:
            publicacion.descripcion_publicacion = new_descripcion,
            publicacion.dibujo = new_dibujo,
            publicacion.fecha_publicacion = new_fecha
            db.session.commit()
        return publicacion if publicacion else None

    @staticmethod
    def add_like(publicacion_id, nlike):
        publicacion = Publicacion.query.get(publicacion_id)
        if publicacion:
            publicacion.num_likes = nlike
            db.session.commit()
        return publicacion if publicacion else None