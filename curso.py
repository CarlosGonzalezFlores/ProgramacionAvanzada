class Curso:
    nombre_curso = ""
    codigo_curso = 0
    instructor = ""

    def __init__(self, nombre_curso, codigo_curso, instructor):
        self.nombre_curso = nombre_curso
        self.codigo_curso = codigo_curso
        self.instructor = instructor

    def mostrar_informacion(self):
        print("\nNombre del curso: ", self.nombre_curso)
        print("Codigo del curso: ", self.codigo_curso)
        print("Nombre del instructor: ", self.instructor)

    

  

        