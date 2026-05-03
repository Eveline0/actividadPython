from clases.vehiculo import Vehiculo
from clases.motor import Motor
from clases.coche import Coche
from clases.bicicleta import Bicicleta
from clases.excepcion import ExcesoVelocidadException
from clases.animal import Animal
from clases.gato import Gato
from clases.perro import Perro
from clases.volador import Volador
from clases.pajaro import Pajaro
from clases.avion import Avion

def ejercicio_1():
    print("=== Ejercicio 1: Creacion de una Clase Basica ===")
    print()
 
    m1 = Motor("180 CV", "Gasolina")
    m2 = Motor("220 CV", "Hibrido")
    m3 = Motor("130 CV", "Diesel")

    coche1 = Coche("Chevrolet", "Onix", 2021, m1)
    coche2 = Coche("Kia", "Rio", 2020, m2)
    coche3 = Coche("Renault", "Logan", 2019, m3)

    print("Coche 1:")
    coche1.describir()
    print()

    print("Coche 2:")
    coche2.describir()
    print()

    print("Coche 3:")
    coche3.describir()
    print()

def ejercicio_2():
    print("=== Ejercicio 2: Encapsulamiento y Modificadores de Acceso ===")
    print()

    m1 = Motor("175 CV", "Gasolina")
    coche1 = Coche("Chevrolet", "Onix", 2021, m1)

    print("Datos iniciales del coche:")
    print()
    coche1.describir()
    print()

    print("Actualizando datos del coche...")
    print()

    coche1.setmarca("Ford")
    coche1.setmodelo("Fiesta")
    coche1.setanio(2018)

    print("Datos modificados:")
    print("Marca:", coche1.getmarca())
    print("Modelo:", coche1.getmodelo())
    print("anio:", coche1.getanio())
    print()

    print("Información final del coche:")
    print()
    coche1.describir()
    print()

def ejercicio_3():
    print("=== Ejercicio 3: Constructores ===")
    print()

    m4 = Motor("200 CV", "Gasolina")
    m5 = Motor("140 CV", "Diesel")

    coche4 = Coche("Hyundai", "Elantra", 2022, m4)
    coche5 = Coche("Nissan", "Versa", 2021, m5)

    print("Coche 4:")
    coche4.describir()
    print()

    print("Coche 5:")
    coche5.describir()
    print()

def ejercicio_4(): 
    print("=== Ejercicio 4: Herencia ===")
    print()

    print("Prueba de vehículo:")
    print()

    vehiculo1 = Vehiculo()
    print("Velocidad inicial:", vehiculo1.velocidad, "km/h")
    vehiculo1.acelerar()
    print("Velocidad después:", vehiculo1.velocidad, "km/h")
    print()

    print("Prueba con bicicleta:")
    print()

    bicicleta1 = Bicicleta("Urbana", 7)
    bicicleta1.describir()
    bicicleta1.acelerar()
    print("Velocidad actual de la bicicleta:", bicicleta1.velocidad, "km/h")
    print()

def ejercicio_5():
    print("=== Ejercicio 5: Sobreescritura ===")
    print()

    m1 = Motor("190 CV", "Gasolina")
    coche1 = Coche("Ford", "Focus", 2020, m1)
    bicicleta1 = Bicicleta("Urbana", 7)

    print("Coche:")
    coche1.describir()
    coche1.acelerar()
    print("Velocidad:", coche1.velocidad, "km/h")
    print()

    print("Bicicleta:")
    bicicleta1.describir()
    bicicleta1.acelerar()
    print("Velocidad:", bicicleta1.velocidad, "km/h")
    print()

def ejercicio_6():
    print("=== Ejercicio 6: Polimorfismo ===")
    print()

    m1 = Motor("190 CV", "Gasolina")
    coche1 = Coche("Ford", "Focus", 2020, m1)
    bicicleta1 = Bicicleta("Urbana", 7)

    transportes = [coche1, bicicleta1]

    for transporte in transportes:
        print("Tipo:", type(transporte).__name__)
        print()

        transporte.describir()
        print()

        transporte.acelerar()
        print("Velocidad actual:", transporte.velocidad, "km/h")
        print() 

def ejercicio_7():
    print("=== Ejercicio 7: Clases abstractas ===")
    print()

    perro1 = Perro()
    gato1 = Gato()

    animales = [perro1, gato1]

    print("Sonidos de los animales:")
    print()

    for animal in animales:
        animal.hacerSonido()
        print()

def ejercicio_8():
    print("=== Ejercicio 8: Interfaces ===")
    print()

    avion1 = Avion()
    pajaro1 = Pajaro()

    voladores = [avion1, pajaro1]
    
    print("Objetos voladores:")
    print()

    for v in voladores:
        v.volar()
        print()

def ejercicio_9():
    print("=== Ejercicio 9: Composicion ===")
    print()

    m1 = Motor("200 CV", "Híbrido")
    coche1 = Coche("Toyota", "Corolla Cross", 2023, m1)

    print("Información del vehículo:")
    print()

    coche1.describir()
    print()

    print("Probando aceleración...")
    coche1.acelerar()
    print("Velocidad actual:", coche1.velocidad, "km/h")
    print()

def ejercicio_10():
    print("=== Ejercicio 10: Excepciones ===")
    print()

    m1 = Motor("120 CV", "Gasolina")
    coche1 = Coche("Kia", "Picanto", 2015, m1)

    try:
        coche1.incrVelocidad(210)
    except ExcesoVelocidadException as e:
        print(e)

    print()

def main():
    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
    ejercicio_4()
    ejercicio_5()
    ejercicio_6()
    ejercicio_7()
    ejercicio_8()
    ejercicio_9()
    ejercicio_10()
main()
