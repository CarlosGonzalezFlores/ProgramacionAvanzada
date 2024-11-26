from .utils.roles import Rol
class Usuario:
    id: int
    nombre: str
    apellido: str
    usuario:str
    contraseña: str
    rol: Rol

    def __init__(self, id:int, nombre:str, apellido:str, usuario:str, contraseña:str, rol:Rol):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña = contraseña
        self.rol = rol