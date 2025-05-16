from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Comision(db.Model):
    #Definimos explicitamente el nombre de la tabla
    __tablename__ = 'comisiones'

    #Mapeamos los atributos
    id_com = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion_com = db.Column(db.String, nullable=False)
    estado = db.Column(db.String, nullable=False)
    fecha_creacion = db.Column(db.Date, nullable=False)
    tipo = db.Column(db.String, nullable=False)

    #Relaciones
    #Faltan user cliente y user artista + lista de mensajes
    #id_cliente_com = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    #id_artista_com = db.Column(db.Integer, db.ForeignKey('artistas.id_artista'))

    #Funcion para debugg futuro para imprimir datos en consola
    def __repr__(self):
        return f"<Comision {self.id_com} - {self.estado} - {self.tipo} - {self.fecha_creacion} - {self.descripcion_com} >"