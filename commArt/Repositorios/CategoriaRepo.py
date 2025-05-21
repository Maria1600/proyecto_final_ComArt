from sqlalchemy.orm import joinedload

from app import db
from Modelos.Categoria import Categoria

class CategoriaRepositorio:

    @staticmethod
    def obtener_todo():
        return Categoria.query.all()

    @staticmethod
    def obtener_por_id(categoria_id):
        return Categoria.query.get(categoria_id)

    @staticmethod
    def crear(nom_categoria):
        categoria = Categoria(nombre_categoria=nom_categoria)
        db.session.add(categoria)
        db.session.commit()
        return categoria

    @staticmethod
    def eliminar(categoria_id):
        categoria = Categoria.query.get(categoria_id)
        operacion_exitosa = False
        if categoria:
            db.session.delete(categoria)
            db.session.commit()
            operacion_exitosa = True
        return operacion_exitosa

    @staticmethod
    def actualizar(categoria_id, nom_categoria):
        categoria = Categoria.query.get(categoria_id)
        if categoria:
            categoria.nombre_categoria = nom_categoria
            db.session.commit()
        return categoria if categoria else None

    def obtener_artistas_por_categoria(categoria_id):
        #Hacemos una consulta para buscar los artistas de una categoria en concreto
        # .options sirve para modificar el cpmportamiento de la consulta cuando se hace join
        # joinedload es parecido a hacer un join en SQL y el filter_by como un WHERE
        categoria = Categoria.query.options(joinedload(Categoria.artistas)).filter_by(id_categoria=categoria_id).first()
        # Lo siguiente retorna la lista y si no devuelve una cadena vacía
        return categoria.artistas if categoria else []