from datetime import datetime

from sqlalchemy.orm import joinedload
from werkzeug.security import check_password_hash, generate_password_hash

from Modelos import seguir
from Modelos.Usuario import Usuario
from extensiones import db

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
    def obtener_por_correo(correo):
        return Usuario.query.filter_by(correo=correo, activo=1).first()

    @staticmethod
    def obtener_por_username(username):
        return Usuario.query.filter_by(username=username, activo=1).first()

    @staticmethod
    def crear(correo, username ,contrasenia, fecha):
        hash_pass = generate_password_hash(contrasenia)
        usuario = Usuario(
            correo=correo,
            username=username,
            contrasenia=hash_pass,
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
    def actualizar(user_id, correo, username, contrasenia, fecha, descripcion):
        usuario = Usuario.query.get(user_id)
        if not usuario:
            return None

        fecha_f = datetime.strptime(fecha, "%Y-%m-%d").date()
        usuario.correo = correo
        usuario.username = username
        usuario.descripcion = descripcion
        usuario.fecha_nacimiento = fecha_f

        # Solo actualizar la contraseña si viene una nueva
        if contrasenia:
            hash_pass = generate_password_hash(contrasenia)
            usuario.contrasenia = hash_pass

        db.session.commit()
        return usuario


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

    @staticmethod
    def verificar_login(correo, contrasenia):
        usuario = Usuario.query.filter_by(correo=correo, activo=1).first()
        if usuario and check_password_hash(usuario.contrasenia, contrasenia):
            return usuario

    @staticmethod
    def comprobar_si_sigue(id_usuario, id_objetivo):
        #Comprueba si un usuario sigue a un user concreto mirando en la cadena en la tabla intermedia seguir
        return db.session.query(
            db.exists().where(
                (seguir.c.id_seguidor == id_usuario) &
                (seguir.c.id_seguido == id_objetivo)
            )
        ).scalar()
