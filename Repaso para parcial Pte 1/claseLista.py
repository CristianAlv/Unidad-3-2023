from claseNodo import Nodo
from claseCarga import VehiculoCarga
from claseVehiculo import Vehiculo
from claseTransporte import VehiculoTransporte

class Lista():
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
        return dato
    
    def agregar(self, unVehiculo):
        aux = self.__comienzo
        cont = 0
        band = False
        ant = aux
        if aux == None:
                nodo = Nodo(unVehiculo)
                nodo.setSiguiente(self.__comienzo)
                self.__actual = nodo
                self.__comienzo = nodo
                self.__tope+=1
                print("Vehiculo agregado")
        else:
                i=0
                while aux != None and i< self.__tope:
                    ant = aux
                    aux = aux.getSiguiente()
                    i+=1
                if ant != None:
                    nodo = Nodo(unVehiculo)
                    ant.setSiguiente(nodo)
                    nodo.setSiguiente(aux)
                    self.__tope +=1
                    print ("Vehiculo Agregado Correctamente")
        
    def mostrar(self):
        aux = self.__comienzo
        i=0
        while aux is not None and i < self.__tope:
            if isinstance(aux.getDato(), VehiculoTransporte):
                if aux.getDato().getcantidadA() > 6:
                    print("El vehiculo de marca: {}, de modelo: {}, patente: {}, importe: {}, kilometraje: {}".format(aux.getDato().getmarca(), aux.getDato().getmodelo(), aux.getDato().getpatente(), aux.getDato().getimporte(), aux.getDato().getkilometraje()))
            aux = aux.getSiguiente()
            i+=1
    def contar(self, marca):
        aux = self.__comienzo
        cont = 0
        while aux != None:
            if aux.getDato().getmarca() == marca:
                cont+=1
            aux = aux.getSiguiente()
        print ("La cantidad de autos con la marca ingresada es: {}".format(cont))
    
    def Mostrar(self):
        aux = self.__comienzo
        print ("Marca:\t Modelo:\tTipo de Vehiculo:\tKilometros a recorrer:\tTotal Importe:")
        for dato in self:
            print ("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(dato.getmarca(), dato.getmodelo(), dato.getTipo(), dato.getkilometraje(), dato.TotalImporte()))