import abc
from abc import ABC
import json 
from pathlib import Path
class Vehiculo(ABC):
    __modelo = str
    __cantidadP = int
    __color = str
    __precio = float
    def __init__(self, modelo, cantidadP, color, precio):
        self.__modelo = modelo
        self.__cantidadP = cantidadP
        self.__color = color
        self.__precio = precio
        
    def getmodelo(self):
        return self.__modelo
    def getcantP(self):
        return self.__cantidadP
    def getcolor(self):
        return self.__color
    def getprecio(self):
        return self.__precio
    
    @abc.abstractmethod
    def ImporteVenta(self):
        pass
    
    @abc.abstractmethod
    def obtenerVehiculo (self):
        pass
    
    def setpreciobase(self, nuevo):
        self.__precio = nuevo
        return self.__precio
    
    def mostrar(self):             #metodo de ligadura dinamica #{:.2f} Toma dos decimales despues de la coma
        print("Modelo: {}\nCantidad de Puertas: {} - Color: {} \nPrecio Base de Venta: {:.2f}".format(self.__modelo, self.__cantidadP, self.__color, self.__precio))

        
        
    def toJSON(self): 
        d = dict( __class__=
                        self.__class__.__name__, 
                __atributos__ = dict (
                modelo = self.__modelo,
                cantPuertas = self.__cantidadP,
                color = self.__color,
                precio = self.__precio
            )
        )
        return d
    