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