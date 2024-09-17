class Hospital:
    pacientes = []
    medicos = []
    consultas = []

    def registrar_consulta(self, id_paciente, id_medico):
        if not self.validar_cantidad_usuarios():
            return
        
        if self.validar_existencia_paciente(id_paciente) == False or self.validar_existencia_medico(id_medico) == False:
            print("No se puede registrar la consulta, no existe el médico o el paciente")
            return
        
        print("Continuamos con el registro")

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def registrar_medico(self, medico):
        self.medicos.append(medico)

    def mostrar_pacientes(self):
        print("*** Pacientes en el Sistema ***")
        año = 2024
        for paciente in self.pacientes:
            edad = año - paciente.ano_nacimiento
            if edad < 18:
                print("Menores de edad: ")
                paciente.mostrar_informacion()
            elif edad > 18:
                print("Mayores de edad: ")
                paciente.mostrar_informacion()

    def mostrar_medicos(self):
        print("*** Medicos en el Sistema ***")
        for medico in self.medicos:
            medico.info_medico()

    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
  
        return False
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
            
        return False
        
    def validar_cantidad_usuarios(self):
        if len(self.pacientes) == 0:
            print("No puedes registra una consulta, no existen pacientes")
            return False
        
        if len(self.medicos) == 0:
            print("No puedes registra una consulta, no existen médicos")
            return False
        
        return True
    
    def eliminar_paciente(self, id_paciente_a_eliminar):
        for paciente in self.pacientes:
            if paciente.id == id_paciente_a_eliminar:
                self.pacientes.remove(paciente)
                print("Se elimo el paciente con el ID: ", id_paciente_a_eliminar)
                break
    def eliminar_medico(self, id_medico_a_eliminar):
        for medico in self.medicos:
            if medico.id == id_medico_a_eliminar:
                self.medicos.remove(medico)
                print("Se elimo el medico con el ID: ", id_medico_a_eliminar)
                break