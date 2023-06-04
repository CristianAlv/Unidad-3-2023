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
import unittest

class TestLista(unittest.TestCase):

    def test_Insertar_elemento(self):
        listaV = ListaVehiculos()
        vehiculo1 = VehiculoUsado("Nissan", 4, "Blanco", 9000, "Ford", "GHI012", 2013, 80000)
        vehiculo2 = VehiculoUsado("Toyota", 4, "Rojo", 10000, "Ford", "ABC123", 2015, 50000)
        vehiculo3 = VehiculoUsado("Ford", 2, "Azul", 8000, "Chevrolet", "XYZ456", 2012, 70000)
        #posicion inicial
        listaV.insertar(0, vehiculo1)
        self.assertEqual(vehiculo1, listaV.obtener_lista_vehiculos())
        #posicion intermedia
        listaV.insertar(1, vehiculo2)
        self.assertEqual(vehiculo2, listaV.obtener_lista_vehiculos())
        #posicion final
        listaV.insertar(2, vehiculo3)
        self.assertEqual(vehiculo3, listaV.obtener_lista_vehiculos())
        
    def test_agregar_vehiculo(self):
        # Prueba de agregación de vehículo a la lista
        listaV = ListaVehiculos()
        vehiculo1 = VehiculoNuevo("Ford", 2, "Azul", 15000, "full")
        vehiculo2 = VehiculoNuevo("Chevrolet", 5, "Negro", 18000, "base")
        listaV.agregarelemento(vehiculo1)
        self.assertEqual(vehiculo1, listaV.obtener_lista_vehiculos())
        listaV.agregarelemento(vehiculo2)
        self.assertEqual(vehiculo2, listaV.obtener_lista_vehiculos())
        
    def test_obtener_vehiculo(self):
        posicion = 2
        # Prueba de obtención de vehículo en una posición dada
        listaV = ListaVehiculos()
        vehiculo1 = VehiculoUsado("Honda", 2, "Gris", 7500, "Chevrolet", "JKL345", 2016, 90000)
        vehiculo2 = VehiculoUsado("Mazda", 5, "Plateado", 11000, "Toyota", "MNO678", 2014, 100000)
        vehiculo3 = VehiculoUsado("Suran", 4, "Rojo", 695429.3, "VW", "ODI-932", 2019, 3932.3)
        listaV.agregarelemento(vehiculo1)
        listaV.agregarelemento(vehiculo2)
        listaV.agregarelemento(vehiculo3)
        self.assertEqual(vehiculo3, listaV.obtenervehiculo(posicion), "La posicion coincide con el esperado")
        
    def test_modificar_precio_venta(self):
        # Prueba de modificación de precio de venta de un vehículo usado
        lista = ListaVehiculos()
        vehiculo3 = VehiculoUsado("Ford", 2, "Azul", 8000, "Chevrolet", "XYZ456", 2012, 70000)
        lista.agregarelemento(vehiculo3)
        patente = "XYZ456"
        newimp = lista.modPrecio(patente)
        importe = vehiculo3.ImporteVenta()
        self.assertEqual(newimp, importe) 
        
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
    unittest.main()
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