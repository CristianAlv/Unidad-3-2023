import json
from pathlib import Path
from claseInterface import IElemento
from claseNodo import Nodo
from clasevehiculo import Vehiculo
from claseNuevo import VehiculoNuevo
from claseusado import VehiculoUsado
from zope.interface import Interface, implementer
from classObjectEncoder import ObjectEncoder
from claseLista import ListaVehiculos
from classMenu import Menu



def testLista():
        lista = ListaVehiculos()
        archivoJson = ObjectEncoder()
        diccionario = archivoJson.leerArchJSON("vehiculos.json")
        print("Diccionario: {}" .format(diccionario))
        lista = archivoJson.decodificarDicc(diccionario)
        print ("{:=^177}".format(""))
        print ("Lista de Autos cargada")
        return lista

        
    
    



if __name__== '__main__':
    lista = ListaVehiculos()
    archivoJson = ObjectEncoder()
    diccionario = archivoJson.leerArchJSON("vehiculos.json")
    print("Diccionario: {}" .format(diccionario))
    lista = archivoJson.decodificarDicc(diccionario)
    print ("{:=^177}".format(""))
    print ("Lista de Autos cargada")
    Mod_Menu = Menu()
    Salir = True

    while Salir:
        print("Bienvenido al Menú")
        print("1. Opción 1: Insertar un vehículo en la colección en una posición determinada.")
        print("2. Opción 2: Agregar un vehículo a la colección: ")
        print("3. Opción 3: Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición ")
        print("4. Opción 4: Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta ")
        print("5. Opción 5: Mostrar todos los datos, incluido el importe de venta, del vehículo más económico ")
        print("6. Opción 6: Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.")
        print("7. Opción 7: Almacenar los objetos de la colección Lista en el archivo “vehiculos.json” ")
        print("0. Salir")
        opcion = input("Ingrese la opcion: ")
        if opcion =='1':
            Mod_Menu.opcion1(lista)
        elif opcion =='2':
            Mod_Menu.opcion2(lista)
        elif opcion == '3':
            Mod_Menu.opcion3(lista)
        elif opcion == '4':
            Mod_Menu.opcion4(lista)
        elif opcion == '5':
            Mod_Menu.opcion5(lista)
        elif opcion == '6':
            Mod_Menu.opcion6(lista)
        elif opcion == '7':
            Mod_Menu.opcion7(lista)
        else:
            if (opcion == '0'):
                    Salir = False
                    Mod_Menu.salir()
            else:
                print ("Opcion invalida")
                Salir=False