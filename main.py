from paciente import Paciente
from medico import Medico
from hospital import Hospital

hospital = Hospital()

paciente = Paciente("Juan", 2004, 76, 1.78, "Avenida Madero") # 5
paciente_dos = Paciente("Jonathan", 2005, 70, 1.90, "Avenida Madero") # 5
paciente_tres = Paciente("Miguel", 2010, 57, 1.65, "La Hacienda") # 5

medico = Medico("Alberto", 1900, "ALB4817BNDDDF", "Av. Periodismo") # 8

hospital.registrar_paciente(paciente=paciente)
hospital.registrar_paciente(paciente=paciente_dos)
hospital.registrar_paciente(paciente=paciente_tres)

hospital.registrar_medico(medico=medico)

hospital.mostrar_pacientes()

hospital.mostrar_medicos()

while True:
    print("Ingrese la opción que desea: ")
    print("1. Eliminar paciente")
    print("2. Eliminar medico")
    print("3. Salir")

    opcion = input("Ingrese la opción: ")
    if opcion == "1":
        elim_paciente = int(input("Ingrese el ID del paciente a eliminar: "))
        hospital.eliminar_paciente(elim_paciente)
        print("Paciente eliminado")
        hospital.mostrar_pacientes()
    elif opcion == "2":
        elim_medico = int(input("Ingrese el ID del medico a eliminar: "))
        hospital.eliminar_medico(elim_medico)
        print("Medico eliminado")
        hospital.mostrar_medicos()
    else:
        print("\n Adiós")
        break
#hospital.registrar_consulta(id_paciente=1, id_medico=1)

