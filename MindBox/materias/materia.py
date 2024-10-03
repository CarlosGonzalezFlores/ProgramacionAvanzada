class Materia:
    
    id: int #MT{ultimos 2 digitos dle nombre}{semestre}{cantidad creditos}{random(1,1000)}
    nombre: str
    descripción: str
    semestre: int
    creditos: int
  
    def __init__(self, id: int, nombre: str, descripcion: str, semestre: int, creditos: int):
        self.id = id
        self.nombre = nombre
        self.descripción = descripcion
        self.semestre = semestre
        self.creditos = creditos
    def mostrar_info_materia(self):

        info = f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripción}, Creditos: {self.creditos}"
        return info 