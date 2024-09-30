from typing import List
from semestre.semestre import Semestre
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint

class Carrera:
    matricula: str
    nombre: str
    numero_semestres: int = 0
    semestres: List[Semestre]

    def __init__(self, matricula: str,  nombre: str):
        self.matricula = self.generar_id(nombre)
        self.nombre = nombre 

    def generar_id(self, nombre: chr) ->str:
        return f"{nombre}-{randint(0,10000)}-{randint(0,100000)}"
    
    def registrar_semestre(self, semestre: Semestre):
        self.numero_semestres =+ 1
        self.semestres.append(semestre)

    def mostrar_info_carrera(self):

        info = f"Matricula: {self.matricula}, Nombre: {self.nombre}, Numero de semestres: {self.numero_semestres}"
        return info 
    


