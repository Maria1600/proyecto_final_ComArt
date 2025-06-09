from extensiones import db

# Tabla intermedia artista-categoria
artista_categoria = db.Table('categoria_artista',
                             db.Column('id_artista', db.Integer, db.ForeignKey('artistas.id_artista'), primary_key=True),
                             db.Column('id_categoria', db.Integer, db.ForeignKey('categorias.id_categoria'), primary_key=True)
                             )

# Tabla intermedia seguir
seguir = db.Table('seguir',
                  db.Column('id_seguidor', db.Integer, db.ForeignKey('usuarios.id_usuario'), primary_key=True),
                  db.Column('id_seguido', db.Integer, db.ForeignKey('usuarios.id_usuario'), primary_key=True)
                  )

# Tabla intermedia solicitud
solicitud = db.Table('solicitud',
                     db.Column('id_solicitante', db.Integer, db.ForeignKey('artistas.id_artista'), primary_key=True),
                     db.Column('id_comision', db.Integer, db.ForeignKey('comisiones.id_com'), primary_key=True)
                     )

