from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime

escuela = Escuela()

while True:
    print("** MINDBOX **")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Mostrar estudiante")
    print("7. Mostrar maestros") 
    print("8. Mostrar materias") 
    print("9. Mostrar grupos")
    print("10. Elimanar estudiante")
    print("11. Elimanar maestro") 
    print("12. Elimanar materia") 
    print("13. Salir")

    opcion = input("Ingrese la opción que desea: ")

    if opcion == "1":
        print("Selecionaste la opción para registrar un estudiante")

        numero_control = escuela.generar_numero_control()
        print(numero_control)
        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa la CURP del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el día de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano, mes, dia)
        estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento)
        escuela.registrar_estudiante(estudiante=estudiante)

    elif opcion == "2":
        print("Selecionaste la opción para registrar un maestro")

        nombre = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        rfc = input("Ingresa la RFC del maestro: ")
        sueldo = float(input("Ingresa el sueldo del maestro: "))
        ano_nacimiento = int(input("Ingrese el año de nacimiento del maestro: "))
        numero_controlM = escuela.numero_control_maestro(nombre=nombre, rfc=rfc, ano_nacimiento=ano_nacimiento)
        print(numero_controlM)
        maestro = Maestro(numero_controlM=numero_controlM, nombre=nombre, apellido=apellido, rfc=rfc, sueldo=sueldo)
        escuela.registrar_maestro(maestro=maestro)

    elif opcion == "3":
        print("Selecionaste la opción para registrar un materia")

        nombre = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa la descripción de la materia: ")
        semestre = int(input("Ingresa el semestre de la materia: "))
        creditos = int(input("Ingresa los creditos de la materia: "))
        id = escuela.generar_id_materia(nombre=nombre, semestre=semestre, creditos=creditos)
        print(id)
        materia = Materia(id=id, nombre=nombre, descripcion=descripcion, semestre=semestre, creditos=creditos)
        escuela.registrar_materia(materia=materia)

    elif opcion == "4":

        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        print("Informacióm estudiantes: ")
        escuela.listar_estudiante()

    elif opcion == "7":
        print("Información maestros: ")
        escuela.listar_maestros()


    elif opcion == "8":
        print("Información materias: ")
        escuela.listar_materias()

    elif opcion == "9":
        pass
    
    elif opcion == "10":
       print("\nSelecionaste la opción para eliminar un estudiante")

       numero_control = input("Ingresa el número de control del estudiante: ")
       escuela.eliminar_estudiante(numero_control=numero_control)

    elif opcion == "11":
        print("\nSelecionaste la opción para eliminar un maestro")

        numero_controlM = input("Ingresa el número de control del maestro: ")
        escuela.eliminar_maestro(numero_controlM=numero_controlM)


    elif opcion == "12":
        print("\nSelecionaste la opción para eliminar un materia")

        id = input("Ingresa la ID de la materia: ")
        escuela.eliminar_materia(id=id)


    elif opcion == "13":
       print("\nHasta luego")
       break