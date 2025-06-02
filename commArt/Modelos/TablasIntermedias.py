from extensiones import db

# Tabla intermedia artista-categoria
artista_categoria = db.Table('categoria_artista',
                             db.Column('id_artista', db.Integer, db.ForeignKey('artistas.id_artista'), primary_key=True),
                             db.Column('id_categoria', db.Integer, db.ForeignKey('categorias.id_categoria'), primary_key=True)
                             )

# Tabla intermedia seguir
seguir = db.Table('seguir',
                  db.Column('seguidor_id', db.Integer, db.ForeignKey('usuarios.id_usuario'), primary_key=True),
                  db.Column('seguido_id', db.Integer, db.ForeignKey('usuarios.id_usuario'), primary_key=True)
                  )
