from clases.vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, tipo, num_velocidades):
        super().__init__()
        self.tipo = tipo
        self.num_velocidades = num_velocidades

    def describir(self):
        print("Tipo de bicicleta:", self.tipo)
        print("Número de velocidades:", self.num_velocidades)

    def acelerar(self):
        self.velocidad += 5
        print("La bicicleta está avanzando")