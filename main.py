from paciente.paciente import Paciente
from medico.medico import Medico
from hospital.hospital import Hospital

hospital = Hospital()

while True:
    print("Bienvenido al sistema central")
    print("1. Registrar paciente")
    print("2. Registrar medicos")
    print("3. Mostrar pacientes")
    print("4. Mostrar medicos")
    print("5. Eliminar paciente")
    print("6. Eliminar medico")
    print("7. Mostrar pacientes menores de edad")
    print("8. Mostrar pacientes mayores de edad")
    print("9. Salir")

    opcion = input ("Selecciona una opción: ")

    if opcion == "1":
        print("Seleccionaste la opción de registrar paciente")
        nombre = input("Ingresa el nombre: ")
        ano_nacimiento = int(input("Ingrese el año de nacimiento: "))
        peso = float(input ("Ingrese el peso: "))
        estatura = float(input ("Ingrese la estatura: "))
        direccion = input("Ingrese la direccion: ")

        paciente = Paciente(nombre=nombre, ano_nacimiento=ano_nacimiento, peso=peso, estatura=estatura, direccion=direccion)
        hospital.registrar_paciente(paciente=paciente)

        print("Paciente registrado correctamente")

    elif opcion == "2":
        print("Seleccionaste la opción de registrar medico")
        nombre = input("Ingresa el nombre: ")
        ano_nacimiento = int(input("Ingrese el año de nacimiento: "))
        rfc = input ("Ingrese la RFC: ")
        direccion = input("Ingrese la direccion: ")

        medico = Medico(nombre=nombre, ano_nacimiento=ano_nacimiento, rfc=rfc, direccion=direccion)
        hospital.registrar_medico(medico=medico)

        print("Medico registrado correctamente")

    elif opcion == "3":
        hospital.mostrar_pacientes()
       
    elif opcion == "4":
       hospital.mostrar_medicos()
       
    elif opcion == "5":
          print("Seleccionaste la opción de eliminar paciente")
          elim_paciente = int(input("Ingrese el ID del paciente a eliminar: "))
          hospital.eliminar_paciente(elim_paciente)
          print("Paciente eliminado correctamente")
          hospital.mostrar_pacientes()
     
    elif opcion == "6":
        print("Seleccionaste la opción de eliminar medico")
        elim_medico = int(input("Ingrese el ID del medico a eliminar: "))
        hospital.eliminar_medico(elim_medico)
        print("Medico eliminado")
        hospital.mostrar_medicos()

    elif opcion == "7":
        print("Seleccionaste la opción de mostrar pacientes menores de edad")
        año = 2024
        for paciente in Paciente:
            edad = año - paciente.ano_nacimiento
            if edad < 18:
                print("Menores de edad: ")
                paciente.mostrar_informacion()
     
    elif opcion == "8":
        print("Seleccionaste la opción de mostrar pacientes mayores de edad")
        año = 2024
        for paciente in Paciente:
            edad = año - paciente.ano_nacimiento
            if edad > 18:
                print("Mayores de edad: ")
                paciente.mostrar_informacion()
    elif opcion == "9":
        print("Saliendo del sistema")
        break