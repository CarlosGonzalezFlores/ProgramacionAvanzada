from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime

escuela = Escuela()

while True:
    print("** MINDBOX **")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar grupo")
    print("4. Registrar materia")
    print("5. Registrar horario")
    print("6. Salir")

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

    elif opcion == "2":
        print("Selecionaste la opción para registrar un maestro")

        nombre = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        rfc = input("Ingresa la RFC del maestro: ")
        sueldo = int(input("Ingresa el sueldo del maestro: "))
        ano_nacimiento = int(input("Ingrese el año de nacimiento del maestro: "))
        numero_controlM = escuela.numero_control_maestro(nombre=nombre, rfc=rfc, ano_nacimiento=ano_nacimiento)
        print(numero_controlM)
    elif opcion == "3":
        pass
    elif opcion == "4":

        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
       print("\nHasta luego")
       break




