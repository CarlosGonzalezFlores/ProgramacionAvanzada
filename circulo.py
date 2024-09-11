class Circulo:
    radio = 0

    def __init__(self, radio):
        self.radio = radio
        print("Este es el radio: ", self.radio)

    def calcular_area(self):
        self.area = 3.1416*self.radio**2
        print("Esta es la área del circulo: ", self.area)

    def calcular_perimetro(self):
        self.perimetro = 3.1416*2*self.radio
        print("Este es el perimetro del circulo: \n", self.perimetro)
