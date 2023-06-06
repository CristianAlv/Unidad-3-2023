from claseNodo import Nodo
from claseCarga import VehiculoCarga
from claseVehiculo import Vehiculo
from claseTransporte import VehiculoTransporte
from claseLista import Lista

    

if __name__ == '__main__':
    listaV = Lista()
    vehiculo1 = VehiculoCarga("VW", "Sharan", "PHM-173", 80000, 5000, 400)
    vehiculo2 = VehiculoTransporte("Renault", "Kangoo", "THY-777", 50000, 300, 7)
    vehiculo3 = VehiculoCarga("Mercades Benz", "AO-788", "PYJ-666", 70000, 5000, 600)
    listaV.agregar(vehiculo1)
    listaV.agregar(vehiculo2)
    listaV.agregar(vehiculo3)
    listaV.mostrar()
    marca = str(input("Ingrese un marca: "))
    listaV.contar(marca)
    listaV.Mostrar()