from extensiones import db
from Modelos.TablasIntermedias import seguir

class Usuario(db.Model):
    #Definimos explicitamente el nombre de la tabla
    __tablename__ = 'usuarios'

    #Mapeamos los atributos
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    correo = db.Column(db.String, nullable=False, unique=True)
    descripcion = db.Column(db.String)
    username = db.Column(db.String, nullable=False, unique=True)
    contrasenia = db.Column(db.String, nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    activo = db.Column(db.Integer, nullable=False)

    #Relaciones
    artista = db.relationship("Artista", back_populates="usuario", uselist=False, cascade="all, delete")
    seguidos = db.relationship(
        'Usuario',
        secondary=seguir,
        primaryjoin=(seguir.c.id_seguidor == id_usuario),
        secondaryjoin=(seguir.c.id_seguido == id_usuario),
        backref='seguidores'#hace lo mismo del mapeo pero a la inversa y con este nombre
    )#Los joins son consultas para poder sacar las lista de seguidos y seguidores comparando ids
    comisiones_solicitadas = db.relationship("Comision", back_populates="cliente")
    mensajes = db.relationship("Mensaje", back_populates="creador")
    lista_notificaciones = db.relationship(
        "Notificacion",
        back_populates="usuario",
        cascade="all, delete-orphan"
    )

    #Funcion para debugg futuro para imprimir datos en consola
    def __repr__(self):
        return f"<Usuario {self.username} - {self.correo} - {self.contrasenia} - {self.fecha_nacimiento}>"