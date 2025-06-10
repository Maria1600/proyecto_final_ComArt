from extensiones import db

class Notificacion(db.Model):
    #Definimos explicitamente el nombre de la tabla
    __tablename__ = 'notificaciones'

    #Mapeamos los atributos
    id_noti = db.Column(db.Integer, primary_key=True, autoincrement=True)
    texto = db.Column(db.String, nullable=False)
    id_usuario = db.Column('id_usuario', db.Integer, db.ForeignKey('usuarios.id_usuario'))

    #Relaciones
    usuario = db.relationship("Usuario", back_populates="lista_notificaciones")


#Funcion para debugg futuro para imprimir datos en consola
    def __repr__(self):
        return f"<Notiss {self.id_noti} - {self.texto} - {self.id_usuario}>"