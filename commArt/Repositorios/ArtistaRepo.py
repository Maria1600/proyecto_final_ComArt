from sqlalchemy.orm import joinedload

from Modelos import Categoria, Comision
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

    @staticmethod
    def asignar_categoria(id_artista, id_categoria):
        artista = Artista.query.get(id_artista)
        categoria = Categoria.query.get(id_categoria)
        if categoria not in artista.categorias:
            artista.categorias.append(categoria)
        db.session.commit()

    @staticmethod
    def desvincular_categoria(id_artista, id_categoria):
        artista = Artista.query.get(id_artista)
        artista.categorias = [
            c for c in artista.categorias if c.id_categoria != id_categoria
        ]
        db.session.commit()

    @staticmethod
    def apuntarse_a_comision(id_artista, id_comision):
        artista = Artista.query.get(id_artista)
        comision = Comision.query.get(id_comision)
        exito_transaccion = True

        # Validacion si alguno no existe
        if not artista or not comision:
            exito_transaccion = False
        elif artista in comision.solicitantes: # Validacion si ya está apuntado
            exito_transaccion = False
        else:
            comision.solicitantes.append(artista)
            db.session.commit()

        return exito_transaccion

    @staticmethod
    def obtener_ids_comisiones_apuntadas(id_artista):
        artista = Artista.query.get(id_artista)
        return [com.id_com for com in artista.comisiones_solicitadas] if artista else []
