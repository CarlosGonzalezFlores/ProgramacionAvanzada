from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol
class Coordinador(Usuario):
    sueldo: float
    rfc: str
    años_antiguedad: int


    def __init__(self, numero_control: str, nombre: str, apellido: str, rfc: str, sueldo: float, contraseña: str, años_antiguedad: int):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contraseña=contraseña, rol=Rol.COORDINADOR)
        self.rfc = rfc
        self.sueldo = sueldo
        self.años_antiguedad = años_antiguedad

    #def mostrar_info_maestro(self):
        #nombre_completo = f"{self.nombre} {self.apellido}"
        #info = f"\n - Número de control: {self.numero_controlM}, Nombre completo: {nombre_completo}, RFC: {self.rfc}, Sueldo: {self.sueldo}, Años de antiguedad{self.años_antiguedad}"
        #return info 