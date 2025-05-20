from Repositorios.CategoriaRepo import CategoriaRepositorio

class CategoriaServicio:

    @staticmethod
    def listar_categorias():
        return CategoriaRepositorio.obtener_todo()

    @staticmethod
    def buscar_categoria(categoria_id):
        return CategoriaRepositorio.obtener_por_id(categoria_id)

    @staticmethod
    def crear_categoria(nombre_categoria):
        return CategoriaRepositorio.crear(nombre_categoria)

    @staticmethod
    def eliminar_categoria(categoria_id):
        return CategoriaRepositorio.eliminar(categoria_id)