from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    #Definimos explicitamente el nombre de la tabla
    __tablename__ = 'usuarios'

    #Mapeamos los atributos
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    correo = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String, nullable=False)
    contrasenia = db.Column(db.String, nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    activo = db.Column(db.Integer, nullable=False)
    #Faltan lista de comisiones solicitadas y lista de seguidores y seguidos + lista de mesajes enviados

    #Relaciones
    artista = db.relationship("Artista", back_populates="usuario", uselist=False, cascade="all, delete")

    #Funcion para debugg futuro para imprimir datos en consola
    def __repr__(self):
        return f"<Usuario {self.username} - {self.correo} - {self.contrasenia} - {self.fecha_nacimiento}>"