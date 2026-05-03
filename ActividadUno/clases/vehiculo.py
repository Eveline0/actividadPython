class Vehiculo:
    
    def __init__(self):
        self.velocidad = 0
    
    def acelerar(self):
        self.velocidad += 10
        print("El vehículo está acelerando")
        