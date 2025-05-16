from flask_sqlalchemy import SQLAlchemy

#Crea instacia de SQLAlchemy para definir el modelo
# db en el futuro se inicializará en app.py con db.init_app(app)
db = SQLAlchemy()

#Creamos una clase que hereda del modelo de la instancia
#Esto indica que estamos representando una tabla de BD
class Categoria(db.Model):
    #Definimos explicitamente el nombre de la tabla
    __tablename__ = 'categorias'

    #Mapeamos los atributos
    id_categoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_categoria = db.Column(db.String, nullable=False, unique=True)

    #Funcion para debugg futuro para imprimir datos en consola
    def __repr__(self):
        return f"<Categoria {self.nombre_categoria}>"