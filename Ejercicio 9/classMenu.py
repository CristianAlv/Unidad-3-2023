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
@implementer(IElemento)
class Menu(object):
    __switcher = None
    __JSONfile = None
    __MarcaNuevo = None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '0':self.salir
        }
        self.__JSONfile = ObjectEncoder()
        marca= str(input("Ingrese una marca para el vehiculo nuevo: "))
        VehiculoNuevo.setmarca(marca)

    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self, op, lista):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(lista)
    
    def salir(self):
        print ("Terminando ejecucion del programa....")
    
    def NuevoVehiculo(self):
        elvehiculo = None
        tipo = str(input("Ingrese el tipo de vehiculo a comprar (Nuevo | Usado): "))
        if tipo == 'Nuevo':
            print ("Usted quiere comprar un auto nuevo")
            modelo = str(input("Ingrese el modelo del vehiculo: "))
            cantP = int(input("INgrese la cantidad de puertas: "))
            color = str(input("Ingrese el color: "))
            precioB = float(input("Ingrese el precio de Base: "))
            version = str(input("Ingrese la version del vehiculo a comprar: (full o base)"))
            elvehiculo = VehiculoNuevo(modelo, cantP, color, precioB, version) #Generamos el vehiculo
            print("Vehiculo registrado")
            
        elif tipo == 'Usado':
            print ("Usted quiere comprar un auto usado")
            Marca = str(input("Ingrese la  marca del vehiculo: "))
            modelo = str(input("Ingrese el modelo del vehiculo: "))
            cantP = int(input("INgrese la cantidad de puertas: "))
            color = str(input("Ingrese el color: "))
            precioB = float(input("Ingrese el precio de Base: ")) ##
            patente = str("Ingrese la patente del vehiculo a comprar: ")
            año = int(input("Ingrese el año del vehiculo: "))
            kilometraje = float(input("Ingrese el kilometraje del vehiculo"))
            elvehiculo = VehiculoUsado(modelo, cantP, color, precioB, Marca, patente, año, kilometraje)
            print("Vehiculo Registrado")
            
        return elvehiculo
    
    def opcion1(self, lista):
        print("Opcion 1 elegida")
        unVehiculo = self.NuevoVehiculo()
        posicion = int(input("Ingrese la posicion donde desea insertar: "))
        if unVehiculo != None:
            lista.insertar(posicion, unVehiculo)
            print("Vehiculo insertado correctamente")
        else:
            print("Vehiculo no existente, intentelo nuevamente")
            
        
    def opcion2(self, lista):
        print("Opcion 1 elegida")
        carga = int(input("Desea realizar la carga: 1:si o 0:no "))
        if carga == 1:
            unVehiculo = self.NuevoVehiculo()
            posicion = int(input("Ingrese la posicion donde desea insertar: "))
            if unVehiculo != None:
                lista.agregarelemento(unVehiculo)
                print("Vehiculo agregado correctamente")
            else:
                print("Vehiculo no existente, intentelo nuevamente")
        else:
            unVehiculo = VehiculoNuevo('Focus 2', 4, 'Gris', 736382.3, 'Base')
            lista.agregarelemento(unVehiculo)
            print("Vehiculo agregado correctamente")
        
    def opcion3 (self, lista):
        posicion = int(input("Ingrese la posicion del elemento a buscar: "))
        lista.mostrarlista(posicion)
        
    def opcion4(self,lista):
        lista.mostrarPatentesUsados()
        patente = str(input("Ingrese una patente: "))
        if patente != None:
            print("Hasta aqui")
            lista.modPrecio(patente)
    def opcion5(self, lista):
        lista.economico()
        
    def opcion6(self,lista):
        lista.mostrar6()
    def opcion7(self, lista):
        diccionario = lista.toJSON()
        print (diccionario)
        if diccionario != None:
            self.__JSONfile.guardarArchJSON(diccionario, "vehiculos.json")
            print("Archivo Guardado Correctamente")

        
    
    