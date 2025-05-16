from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Artista(db.Model):
    #Definimos explicitamente el nombre de la tabla
    __tablename__ = 'artistas'

    #Mapeamos los atributos
    id_artista = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), primary_key=True)
    #Faltan lista de publicaciones y lista de tags y lista de comisiones realizadas

    #Relaciones
    usuario = db.relationship("Usuario", back_populates="artista")

    #Funcion para debugg futuro para imprimir datos en consola
    def __repr__(self):
        return f"<Artista {self.id_artista} - {self.usuario} >"