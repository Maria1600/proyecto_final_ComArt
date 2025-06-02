from sqlalchemy.orm import joinedload
from Modelos.Artista import Artista
from Modelos.Usuario import Usuario
from extensiones import db

class ArtistaRepositorio:

    @staticmethod
    def obtener_todo():
        # Solo obtenemos los usuarios activos por eso hacemos join con usuario para obtenerlo y
        # filtrar con filter en vez de con filter_by ya que tenemos una consulta mas compleja
        # que involucra otras entidades
        return Artista.query.join(Usuario).filter(Usuario.activo == 1).all()

    @staticmethod
    def obtener_por_id(id_artista):
        #Solo se obtiene si el usuario esta activo por eso hacemos join y doble filtro
        return Artista.query.join(Usuario).filter(
            Artista.id_artista == id_artista,
            Usuario.activo == 1
        ).first()

    @staticmethod
    def crear(user_id):
        artista = Artista(
            id_artista = user_id
        )
        db.session.add(artista)
        db.session.commit()
        return artista

    @staticmethod
    def eliminar(id_artista):
        artista = Artista.query.get(id_artista)
        operacion_exitosa = False
        if artista and artista.usuario:
            #Se hace el borrado logico del usuario desde el atributo usuario de artista
            artista.usuario.activo = 0
            db.session.commit()
            operacion_exitosa = True
        return operacion_exitosa

    @staticmethod
    def obtener_comisiones_realizadas(id_artista):
        artista = Artista.query.options(joinedload(Artista.comisiones_realizadas)).filter_by(id_artista=id_artista).first()
        return artista.comisiones_realizadas if artista else []

    @staticmethod
    def obtener_categorias_por_artista(id_artista):
        artista = Artista.query.options(joinedload(Artista.categorias)).filter_by(id_artista=id_artista).first()
        return artista.categorias if artista else []

    @staticmethod
    def obtener_publicaciones(id_artista):
        artista = Artista.query.options(joinedload(Artista.publicaciones)).filter_by(id_artista=id_artista).first()
        return artista.publicaciones if artista else []