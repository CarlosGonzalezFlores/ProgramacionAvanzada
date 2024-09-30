from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from datetime import datetime
from random import randint


class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []
    lista_carreras: List[Carrera] = []
    lista_semestres: List[Semestre] = []

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
    
    def registrar_carrera(self, carrera: Carrera):
        self.lista_carreras.append(carrera)

    def registrar_grupo(self, grupo: Grupo):
        id_semestre = grupo.id_semestre
        for semestre in self.lista_semestres:
            if id_semestre == semestre.id:
                semestre.registrar_gurpo_en_semestre(grupo=grupo)
                break

        self.lista_grupos.append(grupo)

    def registrar_semestre(self, semestre: Semestre):
        id_carrera = semestre.id
        for carrera in self.lista_carreras:
            if carrera.matricula == id_carrera:
                carrera.registrar_semestre(semestre=semestre)
                break
        self.lista_semestres.append(semestre)
    
    def listar_estudiante(self):
        print("** Estudiantes **")
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante())
    
    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("Estudiante eliminado")
                return
        print(f"No se encontró el estudiante con el numero de control: {numero_control}")

    def listar_maestros(self):
        print("** Maestros **")
        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro())
    
    def eliminar_maestro(self, numero_controlM: str):
        for maestro in self.lista_maestros:
            if maestro.numero_controlM == numero_controlM:
                self.lista_maestros.remove(maestro)
                print("Maestro eliminado")
                return
        print(f"No se encontró el maestro con el numero de control: {numero_controlM}")

    def listar_materias(self):
        print("** Materias **")
        for materia in self.lista_materias:
            print(materia.mostrar_info_materia())
    
    def eliminar_materia(self, id: int):
        for materia in self.lista_materias:
            if materia.id == id:
                self.lista_materias.remove(materia)
                print("Materia eliminada")
                return
        print(f"No se encontró la materia con la ID: {id}")

    def listar_grupos(self):
        print("** Grupos **")
        for grupo in self.lista_grupos:
            print(grupo.mostrar_info_grupo())
    
    def listar_carreras(self):
        print("** Carreras **")
        for carrera in self.lista_carreras:
            print(carrera.mostrar_info_carrera())

    def listar_semestres(self):
        print("** Semestres **")
        for semestre in self.lista_semestres:
            print(semestre.mostrar_info_semestre())
