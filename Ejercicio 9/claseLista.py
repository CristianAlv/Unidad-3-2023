import json
from pathlib import Path
from claseInterface import IElemento
from claseNodo import Nodo
from clasevehiculo import Vehiculo
from claseNuevo import VehiculoNuevo
from claseusado import VehiculoUsado
from zope.interface import Interface, implementer


@implementer(IElemento)
class ListaVehiculos:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0
    
    def __init__ (self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    
    def __iter__ (self):                #metodo iterador
        self.indice = 0  # inicializar el índice del iterador
        return self
    
    def agregarelemento(self, unVehiculo): #Agregar elemento es la misma metodologia que el insertar unicamente que agregamos un objeto independientemente de su posicion
        aux= self.__comienzo
        ant= aux
        if aux == None:
            nodo = Nodo(unVehiculo)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
            self.__actual = nodo
            self.__tope += 1
        else:
            i=0
            while (aux != None) and i<self.__tope:
                ant = aux
                aux = aux.getSiguiente()
                i+=1
            if ant != None:
                nodo = Nodo(unVehiculo)
                nodo.setSiguiente(aux) 
                ant.setSiguiente(nodo)
                self.__tope+=1
                print("Vehiculo agregado")
                
    def insertar(self, posicion, elemento): #el insertar permite a partir de dos parametros fundamentales insertar un elemento en el comienzo o dentro de la lista
            aux = self.__comienzo
            cont = 0
            band = False
            ant = aux
            if (posicion <= self.__tope) and (posicion >= 0): ##Aplicar contador en caso de ser while
                if cont == posicion:
                    if self.__comienzo == None:
                        nodo = Nodo(elemento)
                        nodo.setSiguiente(self.__comienzo)
                        self.__comienzo = nodo
                        self.__actual = nodo
                        self.__tope += 1
                    else:
                        nodo = Nodo(elemento)
                        nodo.setSiguiente(aux)
                        aux.setSiguiente(aux.getSiguiente())
                        self.__comienzo = nodo
                        self.__actual = nodo
                        self.__tope += 1
                else:
                    ant= aux
                    while ant != None and band == False:
                        if cont == posicion:
                            band = True
                        else:
                            
                            aux = aux.getSiguiente()
                            cont+=1
                            
                    if cont == posicion:
                        nodo = Nodo(elemento)
                        ant.setSiguiente(nodo)
                        nodo.setSiguiente(aux)
                        self.__tope += 1
                print ("Vehiculo insertado")
                            
            else:
                raise Exception("Posicion de coleccion incorrecta")
            
            
    def __next__(self):  
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            if self.__indice < self.__tope and self.__actual is not None:  
                dato = self.__actual.getDato()
                self.__indice += 1
                self.__actual = self.__actual.getSiguiente()
                return dato
            else:
                raise StopIteration
            
        
    def mostrarlista(self, posicion): #el metodo realizado por la profe en clase no responde ante una lista con iterador
        cont = 0
        band = False
        aux = self.__comienzo
        if posicion <= self.__tope and posicion >= 0:
            while cont <= posicion and band == False:
                if cont == posicion:
                    band = True
                    unVehiculo = aux.getDato().obtenerVehiculo()
                    if isinstance(unVehiculo, VehiculoUsado):
                        print("Es un auto usado")
                    else:
                        print ("Es un auto nuevo")
                else:
                    aux = aux.getSiguiente()
                cont += 1
            if band == True:
                print ("El elemento fue encontrado con exito")
            else:
                print ("Vuelva a intentarlo")
        else:
            raise Exception("La posicion no fue encontrada") #Una excepción es un objeto que representa un error o una situación excepcional que ocurre durante la ejecución de un programa
                
    def obtenervehiculo(self, posicion):
        aux = self.__comienzo
        cont = 0
        band = False
        retorno = None  
        while aux is not None and not band:  
            if cont == posicion:
                band = True
                print("El vehiculo se encuentra en la posicion indicada")
                retorno = aux.getDato()
            cont += 1
            aux = aux.getSiguiente()
        return retorno   
    
    def obtener_lista_vehiculos(self):
        aux = self.__comienzo
        retorno = None
        while aux is not None:
            print(aux.getDato())
            retorno = aux.getDato()
            aux = aux.getSiguiente()
        return retorno
    
    def mostrarPatentesUsados(self):
        aux = self.__comienzo
        i = 0
        while aux != None:
            unVehiculo = aux.getDato()
            if isinstance(unVehiculo, VehiculoUsado):
                print ("Patentes: {}" .format(unVehiculo.getpatente()))
                
            aux = aux.getSiguiente()
    def modPrecio(self, patente):
        aux = self.__comienzo
        i = 0
        band = False
        while aux != None and band==False:
            vehiculo = aux.getDato()
            if isinstance(vehiculo, VehiculoUsado):
                if patente == vehiculo.getpatente():
                    newPrecio = float(input("Ingrese el nuevo precio base: "))
                    vehiculo.setpreciobase(newPrecio)
                    newimp = vehiculo.ImporteVenta()
                    band = True     
            aux = aux.getSiguiente()
        if patente == vehiculo.getpatente():
            print ("El nuevo importe es: {}" .format(newimp))
        return newimp
            
    def economico(self):
        minimo = 999999999
        aux = self.__comienzo
        retorno = None
        while aux != None:
            if minimo > aux.getDato().ImporteVenta():
                minimo = aux.getDato().ImporteVenta()
                retorno = aux.getDato()
            
            aux = aux.getSiguiente()
        print ("{:=^150}".format(""))
        retorno.mostrar()
        print ("{:=^150}".format(""))
        
    def mostrar6(self):
        aux = self.__comienzo
        print("{:=^150}".format(""))
        while aux != None:
            if isinstance(aux.getDato(), VehiculoUsado):
                print(aux.getDato().mostrar())
                print("{:-^150}".format(""))
            elif isinstance(aux.getDato(), VehiculoNuevo):
                print(aux.getDato().mostrar())
                print("{:-^150}".format(""))
            aux = aux.getSiguiente()
        print("{:=^150}".format(""))
    def toJSON (self):
        d = dict (
            __class__ = self.__class__.__name__,
            comienzo = [dato.toJSON() for dato in self]                      
        )
        return d
    
    
                
        