from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint


class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def generar_numero_control(self):
        # L - 2024 - 09 - longitud lista estudiantes + 1 + random(0,100000)
        numero_control = f"L{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(0,10000)}"
        return numero_control
    
    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)

    def numero_control_maestro(self, rfc, ano_nacimiento, nombre):
        letras_rfc = rfc[-2:].upper()
        letras_nombre = nombre[:2].upper()
        numero_controlM = f"M{ano_nacimiento}{datetime.now().day}{randint(500,5000)}{letras_rfc}{letras_nombre}{len(self.lista_maestros) + 1}"
        return numero_controlM
    
    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)

    def generar_id_materia(self, nombre, semestre, creditos):
      #MT{ultimos 2 digitos dle nombre}{semestre}{cantidad creditos}{random(1,1000)}
        digitos_nombre = nombre[-2:].upper()
        id = f"MT{digitos_nombre}{semestre}{creditos}{randint(1,1000)}"
        return id