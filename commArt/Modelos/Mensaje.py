from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Mensaje(db.Model):
    #Definimos explicitamente el nombre de la tabla
    __tablename__ = 'mensajes'

    #Mapeamos los atributos
    id_mensaje = db.Column(db.Integer, primary_key=True, autoincrement=True)
    texto = db.Column(db.String, nullable=False)
    #Aunque este obsoleto el utcnow no nos interesa guardar nada mas la hora y le fecha
    #Si se requiere a futuro zona horaria tambien datetime.now(UTC)
    fecha_creacion_mensaje = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    #Relaciones
    #Faltan user cliente y user artista
    #id_user_creador = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    #id_com_asociada = db.Column(db.Integer, db.ForeignKey('artistas.id_artista'))

    #Funcion para debugg futuro para imprimir datos en consola
    def __repr__(self):
        return f"<Mensaje {self.id_mensaje} - {self.texto} - {self.fecha_creacion_mensaje} >"