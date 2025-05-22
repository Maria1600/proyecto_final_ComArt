from sqlalchemy.orm import joinedload
from Modelos.Usuario import Usuario
from app import db

class UsuarioRepositorio:

    @staticmethod
    def obtener_todo():
        #Solo obtenemos los usuarios activos
        return Usuario.query.filter_by(activo=1).all()

    @staticmethod
    def obtener_por_id(user_id):
        #Solo se obtiene si el usuario esta activo
        return Usuario.query.filter_by(id_usuario=user_id, activo=1).first()

    @staticmethod
    def crear(correo, username ,contrasenia, fecha):
        usuario = Usuario(
            correo=correo,
            username=username,
            contrasenia=contrasenia,
            fecha_nacimiento=fecha,
            activo = 1
        )
        #Al crear un usuario este se activa por defecto
        db.session.add(usuario)
        db.session.commit()
        return usuario

    @staticmethod
    def eliminar(user_id):
        usuario = Usuario.query.get(user_id)
        operacion_exitosa = False
        if usuario:
            #Hacemos solo el borrado logico del usuario
            usuario.activo = 0
            db.session.commit()
            operacion_exitosa = True
        return operacion_exitosa

    @staticmethod
    def actualizar(user_id, correo, username ,contrasenia, fecha):
        usuario = Usuario.query.get(user_id)
        if usuario:
            usuario.correo=correo,
            usuario.username=username,
            usuario.contrasenia=contrasenia,
            usuario.fecha_nacimiento=fecha
            db.session.commit()
        return usuario if usuario else None

    @staticmethod
    def seguir(user_id_a_seguir,id_user_seguidor):
        seguidor = Usuario.query.get(id_user_seguidor)
        seguido = Usuario.query.get(user_id_a_seguir)
        exito_transaccion = True

        #Si uno de los dos no existe lo damos por invalido
        if not seguidor or not seguido:
            exito_transaccion = False

        #Si ya lo esta siguiendo lo damos por invalido
        if seguido in seguidor.seguidos:
            exito_transaccion = False

        #Append cambia atomaticamente la lista de seguidos de seguidor y viceversa
        seguidor.seguidos.append(seguido)
        db.session.commit()
        return exito_transaccion

    @staticmethod
    def dejar_de_seguir(user_id_a_dejar_seguir, id_user_seguidor):
        seguidor = Usuario.query.get(id_user_seguidor)
        seguido = Usuario.query.get(user_id_a_dejar_seguir)
        exito_transaccion = True

        #Si uno de los dos no existe lo damos por invalido
        if not seguidor or not seguido:
            exito_transaccion = False

        #Si de verdad lo esta siguiendo continuamos
        if seguido in seguidor.seguidos:
            #Append cambia atomaticamente la lista de seguidos de seguidor y viceversa
            seguidor.seguidos.remove(seguido)
            db.session.commit()
        else:
            exito_transaccion = False

        return exito_transaccion

    @staticmethod
    def obtener_seguidores(user_id):
        usuario = Usuario.query.options(joinedload(Usuario.seguidores)).filter_by(id_usuario=user_id).first()
        return usuario.seguidores if usuario else []

    @staticmethod
    def obtener_seguidos(user_id):
        usuario = Usuario.query.options(joinedload(Usuario.seguidos)).filter_by(id_usuario=user_id).first()
        return usuario.seguidos if usuario else []

    @staticmethod
    def obtener_comisiones_solicitadas(user_id):
        usuario = Usuario.query.options(joinedload(Usuario.comisiones_solicitadas)).filter_by(id_usuario=user_id).first()
        return usuario.comisiones_solicitadas if usuario else []
