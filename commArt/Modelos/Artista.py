from Modelos.TablasIntermedias import artista_categoria, solicitud
from extensiones import db

class Artista(db.Model):
    #Definimos explicitamente el nombre de la tabla
    __tablename__ = 'artistas'

    #Mapeamos los atributos
    id_artista = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), primary_key=True)

    #Relaciones
    publicaciones = db.relationship("Publicacion", back_populates="artista", cascade="all, delete-orphan")
    comisiones_realizadas = db.relationship("Comision", back_populates="artista")
    usuario = db.relationship("Usuario", back_populates="artista")
    categorias = db.relationship(
        "Categoria",
        secondary=artista_categoria,
        back_populates="artistas"
    )
    comisiones_solicitadas = db.relationship(
        "Comision",
        secondary=solicitud,
        back_populates="solicitantes"
    )

    #Funcion para debugg futuro para imprimir datos en consola
    def __repr__(self):
        return f"<Artista {self.id_artista} - {self.usuario} >"