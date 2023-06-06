
from claseVehiculo import Vehiculo
from claseCarga import VehiculoCarga
from claseTransporte import VehiculoTransporte


class Nodo:
    __Vehiculo = None
    __siguiente = None
    def __init__(self, unvehiculo):
        if isinstance(unvehiculo, Vehiculo):
            self.__Vehiculo = unvehiculo
        self.__siguiente = None
        
    def getDato(self):
        return self.__Vehiculo
    def setSiguiente (self, siguienteP):
        self.__siguiente = siguienteP
    def getSiguiente (self):
        return self.__siguiente
    def getTipo(self):
        tipo = None
        if isinstance(self.__Vehiculo, VehiculoCarga):
            tipo = "Vehiculo de Carga"
        elif isinstance(self.__Vehiculo, VehiculoTransporte):
            tipo = "Vehiculo de Transporte"
            
        return tipo