from estudiante import Estudiante
from curso import Curso

estudiante_uno = Estudiante(22121068, "González Flores Carlos", "20 años")
estudiante_dos = Estudiante(22121042, "Barreto Hernandez Ismalardo", "21 años")
curso_uno = Curso("Matematicas", 7362846, "Melchor Ponce de Leon Arturo")
curso_dos = Curso("Ingles", 28773592, "Mendez Lemus Miguel Angel")
curso_tres = Curso("Español", 263456, "Espinobarros Rodriguez Joshua Nataniel")
        
estudiante_uno.agregar_curso(curso_uno)
estudiante_uno.agregar_curso(curso_dos)
estudiante_uno.agregar_curso(curso_tres)
estudiante_dos.agregar_curso(curso_dos)
estudiante_dos.agregar_curso(curso_tres)

estudiante_uno.mostrar_info()
estudiante_dos.mostrar_info()

curso_uno.mostrar_informacion()
curso_dos.mostrar_informacion()
curso_tres.mostrar_informacion()
