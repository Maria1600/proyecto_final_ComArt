from Modelos.TablasIntermedias import artista_categoria
from extensiones import db

#Creamos una clase que hereda del modelo de la instancia
#Esto indica que estamos representando una tabla de BD
class Categoria(db.Model):
    #Definimos explicitamente el nombre de la tabla
    __tablename__ = 'categorias'

    #Mapeamos los atributos
    id_categoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_categoria = db.Column(db.String, nullable=False, unique=True)

    #Relacion N:M
    artistas = db.relationship(
        "Artista",
        secondary=artista_categoria,
        back_populates="categorias"
    )

    #Funcion para debugg futuro para imprimir datos en consola
    def __repr__(self):
        return f"<Categoria {self.nombre_categoria}>"