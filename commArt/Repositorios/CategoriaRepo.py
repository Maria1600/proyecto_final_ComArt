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
