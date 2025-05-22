from app import db

class Comision(db.Model):
    #Definimos explicitamente el nombre de la tabla
    __tablename__ = 'comisiones'

    #Mapeamos los atributos
    id_com = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion_com = db.Column(db.String, nullable=False)
    dibujo = db.Column(db.String)
    estado = db.Column(db.String, nullable=False)
    fecha_creacion = db.Column(db.Date, nullable=False)
    tipo = db.Column(db.String, nullable=False)
    id_cliente_com = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_artista_com = db.Column(db.Integer, db.ForeignKey('artistas.id_artista'))

    #Relaciones
    #Faltan lista de mensajes
    artista = db.relationship("Artista", back_populates="comisiones_realizadas")
    cliente = db.relationship("Usuario", back_populates="comisiones_solicitadas")
    mensajes =  db.relationship("Mensaje", back_populates="comision_asociada")

#Funcion para debugg futuro para imprimir datos en consola
    def __repr__(self):
        return f"<Comision {self.id_com} - {self.estado} - {self.tipo} - {self.fecha_creacion} - {self.descripcion_com} >"