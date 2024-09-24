from datetime import datetime
class Maestro:
    numero_controlM: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float


    def __init__(self, numero_controlM: str, nombre: str, apellido: str, rfc: str, sueldo: float):
        self.numero_controlM = numero_controlM
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo

    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Número de control: {self.numero_controlM}, Nombre completo: {nombre_completo}, RFC: {self.rfc}, Sueldo: {self.sueldo}"
        return info 