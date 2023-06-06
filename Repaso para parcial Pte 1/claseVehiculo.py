import abc
from abc import ABC

class Vehiculo(ABC):
    __marca = str
    __modelo = str
    __patente = str
    __importe = float
    __kilometraje = float
    def __init__(self, marca, modelo, patente, importe, kilometraje):
        self.__marca = marca
        self.__modelo = modelo
        self.__patente = patente
        self.__importe = importe
        self.__kilometraje = kilometraje
        
    def getmarca(self):
        return self.__marca
    def getmodelo(self):
        return self.__modelo
    def getpatente(self):
        return self.__patente
    def getimporte(self):
        return self.__importe
    def getkilometraje(self):
        return self.__kilometraje

    
    @abc.abstractclassmethod
    def TotalImporte(self):
        pass