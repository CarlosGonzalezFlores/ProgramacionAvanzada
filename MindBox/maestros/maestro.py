from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol
class Maestro (Usuario):
    rfc: str
    sueldo: float


    def __init__(self, numero_controlM: str, nombre: str, apellido: str, rfc: str, sueldo: float, contraseña: str):
        super().__init__(numero_control=numero_controlM, nombre=nombre, apellido=apellido, contraseña=contraseña, rol=Rol.MAESTRO)
        self.rfc = rfc
        self.sueldo = sueldo

    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"\n - Número de control: {self.numero_controlM}, Nombre completo: {nombre_completo}, RFC: {self.rfc}, Sueldo: {self.sueldo}"
        return info 