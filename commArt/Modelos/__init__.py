#Este archivo es como una inicializacion de los modelos basicamente inicializa un paquete en
# Python esto lo hacemos para evitar errores de referencias circulares
from .Usuario import Usuario
from .Artista import Artista
from .Categoria import Categoria
from .Comision import Comision
from .Mensaje import Mensaje
from .Publicacion import Publicacion
from .TablasIntermedias import artista_categoria, seguir