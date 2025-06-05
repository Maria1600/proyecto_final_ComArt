from datetime import datetime
from Repositorios.UsuarioRepo import UsuarioRepositorio
from Servicios.ArtistaServicio import ArtistaServicio


class UsuarioServicio:

    @staticmethod
    def listar_usuarios():
        return UsuarioRepositorio.obtener_todo()

    @staticmethod
    def buscar_usuario(user_id):
        return UsuarioRepositorio.obtener_por_id(user_id)

    @staticmethod
    def obtener_por_correo(correo):
        return UsuarioRepositorio.obtener_por_correo(correo)

    @staticmethod
    def obtener_por_username(username):
        return UsuarioRepositorio.obtener_por_username(username)

    @staticmethod
    def crear_usuario(correo, username ,contrasenia, fecha, es_artista=False):
        if isinstance(fecha, str):
            fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        usuario = UsuarioRepositorio.crear(correo, username, contrasenia, fecha)

        # Si es artista lo creamos
        if es_artista:
            ArtistaServicio.crear_artista(usuario.id_usuario)

        return usuario

    @staticmethod
    def eliminar_usuario(user_id):
        return UsuarioRepositorio.eliminar(user_id)

    @staticmethod
    def actualizar(user_id, correo, username ,contrasenia, fecha, descripcion):
        return UsuarioRepositorio.actualizar(user_id, correo, username ,contrasenia, fecha, descripcion)

    @staticmethod
    def seguir(user_id_a_seguir,id_user_seguidor):
        return UsuarioRepositorio.seguir(user_id_a_seguir,id_user_seguidor)

    @staticmethod
    def dejar_de_seguir(user_id_a_dejar_seguir, id_user_seguidor):
        return UsuarioRepositorio.dejar_de_seguir(user_id_a_dejar_seguir, id_user_seguidor)

    @staticmethod
    def obtener_seguidores(user_id):
        return UsuarioRepositorio.obtener_seguidores(user_id)

    @staticmethod
    def obtener_seguidos(user_id):
        return UsuarioRepositorio.obtener_seguidos(user_id)

    @staticmethod
    def obtener_comisiones_solicitadas(user_id):
        return UsuarioRepositorio.obtener_comisiones_solicitadas(user_id)

    @staticmethod
    def verificar_login(correo,contrasenia):
        return UsuarioRepositorio.verificar_login(correo,contrasenia)

    @staticmethod
    def comprobar_si_sigue(id_usuario, id_objetivo):
        return UsuarioRepositorio.comprobar_si_sigue(id_usuario, id_objetivo)