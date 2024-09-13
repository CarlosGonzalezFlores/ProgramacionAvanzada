class Estudiante:
    id_estudiante = 0
    nombre = ""
    edad = 0
    cursos = []

    def __init__(self, id_estudiante, nombre, edad):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.edad = edad
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def mostrar_info(self):
        print("\nNombre del estudiante: ", self.nombre)
        print("Edad: ", self.edad)
        print("ID: ", self.id_estudiante)

        for curso in self.cursos:
            print("Nombres de los cursos añadido: \n", curso.nombre_curso)


   