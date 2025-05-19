from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Publicacion(db.Model):
    #Definimos explicitamente el nombre de la tabla
    __tablename__ = 'publicaciones'

    #Mapeamos los atributos
    id_publicacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion_publicacion = db.Column(db.String)
    dibujo = db.Column(db.String, nullable=False)
    fecha_publicacion = db.Column(db.Date)
    num_likes = db.Column(db.Integer)
    id_artista_publicacion = db.Column(db.Integer, db.ForeignKey('artistas.id_artista'),nullable=False)

    #Relaciones
    artista = db.relationship("Artista", back_populates="publicaciones")

    #Funcion para debugg futuro para imprimir datos en consola
    def __repr__(self):
        return f"<Publicacion {self.id_publicacion} - {self.descripcion_publicacion} - {self.fecha_publicacion} - {self.num_likes} >"