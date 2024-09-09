class Coche: 
    marca = ""
    modelo = ""
    año = ""
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    def mostrar_info(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Año: ", self.año)
        

