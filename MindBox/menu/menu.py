from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from materias.materia import Materia
from grupos.grupo import Grupo
from coordinador.coordinador import Coordinador
from datetime import datetime

class Menu:
    escuela = Escuela()
    usuario_estudiante: str = "Juan123"
    usuario_maestro: str = "Miguel123"
    contraseña_estudiante: str = "12345"
    contraseña_maestro: str = "54321"


    def login(self):
        intentos = 0
        while intentos < 5:
            print("\n** BIENVENIDO **")
            print("Inicia sesión para continuar")

            nombre_usuario = input("Ingresea tu nombre de usuario: ")
            contraseña_usuario = input("Ingrese su contraseña: ")

            if nombre_usuario == self.usuario_estudiante:
                if contraseña_usuario == self.contraseña_estudiante:
                    self.mostrar_menu_estudiante()
                    intentos = 0
                else: 
                    intentos = self.mostrar_intento_sesion_fallido(intentos_usuario=intentos)

            elif nombre_usuario == self.usuario_maestro:
                if contraseña_usuario == self.contraseña_maestro:
                    self.mostrar_menu_maestro()
                    intentos = 0
                else: 
                    intentos = self.mostrar_intento_sesion_fallido(intentos_usuario=intentos)

            else: 
                intentos = self.mostrar_intento_sesion_fallido(intentos_usuario=intentos)
            
        print("Intentos maximos alcanzados :( ")

    def mostrar_intento_sesion_fallido(self, intentos_usuario):
        print("Usuario o contraseña incorrectos. Intenta de nuevo")
        return intentos_usuario + 1
            


    def mostrar_menu_estudiante(self):
        opcion = 0
        #agregar las opciones que van
        while opcion !=5:
            print(" MINDBOX ALUMNO")
            print("1. Ver horario")
            print("2. Ver grupos")
            print("3. Ver carreras")
            print("4. Ver maestros")
            print("5. Salir")
            opcion= int(input("Ingresa una opcion: "))

            if opcion == 5:
                break
    def mostrar_menu_maestro(self):
          opcion = 0
          #agregar las opciones que van
          while opcion !=6:
            print(" MINDBOX MAESTRO")
            print("1. Ver horario")
            print("2. Ver grupos")
            print("3. Ver materias")
            print("4. Ver carreras")
            print("5. Ver alumnos")
            print("6. Salir")
            opcion= int(input("Ingresa una opcion: "))

            if opcion == 6:
                break

    def mostrar_menu(self):
            while True:
                print("** MINDBOX **")
                print("1. Registrar estudiante")
                print("2. Registrar maestro")
                print("3. Registrar materia")
                print("4. Registrar grupo")
                print("5. Registrar horario")
                print("6. Registrar Coordinador")
                print("7. Mostrar estudiante")
                print("8. Mostrar maestros") 
                print("9. Mostrar materias") 
                print("10. Mostrar grupos")
                print("11. Mostrar carreras")
                print("12. Mostrar semestres")
                print("13. Mostrar coordinador")
                print("14. Elimanar estudiante")
                print("15. Elimanar maestro") 
                print("16. Elimanar materia")
                print("17. Registrar carrera")
                print("18. Registrar semestre")
                print("19. Salir")

                opcion = input("Ingrese la opción que desea: ")

                if opcion == "1":
                    print("Selecionaste la opción para registrar un estudiante")

                    numero_control = self.escuela.generar_numero_control()
                    print(numero_control)
                    nombre = input("Ingresa el nombre del estudiante: ")
                    apellido = input("Ingresa el apellido del estudiante: ")
                    curp = input("Ingresa la CURP del estudiante: ")
                    ano = int(input("Ingresa el año de nacimiento del estudiante: "))
                    mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
                    dia = int(input("Ingresa el día de nacimiento del estudiante: "))
                    fecha_nacimiento = datetime(ano, mes, dia)

                    contraseña = input("Ingresa la contraseña del estudiante: ")
                    estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento, contraseña=contraseña)
                    self.escuela.registrar_estudiante(estudiante=estudiante)

                elif opcion == "2":
                    print("Selecionaste la opción para registrar un maestro")

                    nombre = input("Ingresa el nombre del maestro: ")
                    apellido = input("Ingresa el apellido del maestro: ")
                    rfc = input("Ingresa la RFC del maestro: ")
                    sueldo = float(input("Ingresa el sueldo del maestro: "))
                    ano_nacimiento = int(input("Ingrese el año de nacimiento del maestro: "))
                    numero_controlM = self.escuela.numero_control_maestro(nombre=nombre, rfc=rfc, ano_nacimiento=ano_nacimiento)

                    contraseña = input("Ingresa la contraseña del maestro: ")

                    maestro = Maestro(numero_controlM=numero_controlM, nombre=nombre, apellido=apellido, rfc=rfc, sueldo=sueldo, contraseña=contraseña)
                    self.escuela.registrar_maestro(maestro=maestro)

                elif opcion == "3":
                    print("Selecionaste la opción para registrar un materia")

                    nombre = input("Ingresa el nombre de la materia: ")
                    descripcion = input("Ingresa la descripción de la materia: ")
                    semestre = int(input("Ingresa el semestre de la materia: "))
                    creditos = int(input("Ingresa los creditos de la materia: "))
                    id = self.escuela.generar_id_materia(nombre=nombre, semestre=semestre, creditos=creditos)
                    print(id)
                    materia = Materia(id=id, nombre=nombre, descripcion=descripcion, semestre=semestre, creditos=creditos)
                    self.escuela.registrar_materia(materia=materia)

                elif opcion == "4":
                    print("Selecionaste la opción para registrar un grupo")
                    tipo = input("Ingresa el tipo del grupo (A/B):")
                    id_semestre = input("Ingrese el ID del semestre al que pertenece el grupo: ")
                    grupo = Grupo(tipo=tipo, id_semestre=id_semestre)

                    self.escuela.registrar_grupo(grupo=grupo)

                elif opcion == "5":
                    #registrar horario
                    pass
                elif opcion == "6":
                    #registrar coordinador
                    pass
                elif opcion == "7":
                    print("Informacióm estudiantes: ")
                    self.escuela.listar_estudiante()

                elif opcion == "8":
                    print("Información maestros: ")
                    self.escuela.listar_maestros()


                elif opcion == "9":
                    print("Información materias: ")
                    self.escuela.listar_materias()

                elif opcion == "10":
                    print("Información grupos: ")
                    self.escuela.listar_grupos()

                elif opcion == "11":
                    print("Información carreras: ")
                    self.escuela.listar_carreras()

                elif opcion == "12":
                    print("Información semestres: ")
                    self.escuela.listar_semestres()

                elif opcion == "13":
                    #mostrar coordinador
                    pass
                
                elif opcion == "14":
                    print("\nSelecionaste la opción para eliminar un estudiante")

                    numero_control = input("Ingresa el número de control del estudiante: ")
                    self.escuela.eliminar_estudiante(numero_control=numero_control)

                elif opcion == "15":
                    print("\nSelecionaste la opción para eliminar un maestro")

                    numero_controlM = input("Ingresa el número de control del maestro: ")
                    self.escuela.eliminar_maestro(numero_controlM=numero_controlM)


                elif opcion == "16":
                    print("\nSelecionaste la opción para eliminar un materia")

                    id = input("Ingresa la ID de la materia: ")
                    self.escuela.eliminar_materia(id=id)

                elif opcion == "17":
                    print("\nSelecionaste la opción para registrar una carrera")

                    nombre = input("Ingresa el nombre de la carrera: ")
                    matricula = int(input("Ingresa la matricula de la carrera: "))
                    carrera = Carrera(nombre=nombre, matricula=matricula)
                    self.escuela.registrar_carrera(carrera=carrera)

                elif opcion == "18":
                    print("\nSelecionaste la opción para registrar un semestre")

                    numero = input("Ingresa el numero del semestre: ")
                    id_carrera = input("Ingresa el ID de la carrera: ")

                    semestre = Semestre(numero=numero, id_carrera=id_carrera)

                    self.escuela.registrar_semestre(semestre=semestre)
            

                elif opcion == "19":
                    print("\nHasta luego")
                    break