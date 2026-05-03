from clases.vehiculo import Vehiculo
from clases.excepcion import ExcesoVelocidadException


class Coche(Vehiculo):
        def __init__(self,marca,modelo,anio, motor):
            super().__init__()
            self.__marca = marca
            self.__modelo = modelo 
            self.__anio = anio 
            self.motor = motor 

    # getters
        def getmarca(self):
            return self.__marca

        def getmodelo(self):
            return self.__modelo
       
        def getanio(self):
            return self.__anio

     # setters
        def setmarca(self,marca):
            self.__marca = marca

        def setmodelo(self,modelo):
            self.__modelo = modelo

        def setanio(self, anio):
            self.__anio =  anio 

        def describir(self):
            print("=== Información del coche ===")
            print(f"Marca: {self.__marca}")
            print(f"Modelo: {self.__modelo}")
            print(f"Año: {self.__anio}")
            print(f"Motor:{self.motor.tipo} - {self.motor.potencia}")

#Metodo acelerar para coche
        def acelerar(self):
            self.velocidad += 20
            print("El coche acelera más rápido")

#Metodo incrementar velocidad para coche 
        def incrVelocidad(self, velocidad):
            self.velocidad += velocidad
            if self.velocidad > 200:
                raise ExcesoVelocidadException("¡CUIDADO! EXCESO DE VELOCIDAD")