from clasevehiculo import Vehiculo
from claseNuevo import VehiculoNuevo
from claseusado import VehiculoUsado
class Nodo: 
    __vehiculo: None 
    __siguiente: object 
    def __init__(self, unVehiculo):
        if isinstance(unVehiculo, Vehiculo):
            self.__Vehiculo = unVehiculo
        self.__siguiente=None 
        
    def setSiguiente(self, siguiente): 
        self.__siguiente=siguiente
         
    def getSiguiente(self): 
        return self.__siguiente 
    
    def getDato(self): 
        return self.__Vehiculo

            