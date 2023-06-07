import abc
from abc import ABC

class Bebida(ABC):
    __codigo = str
    __descripcion = str
    __tamaño = float
    __Retornable = bool
    __precio = float
    def __init__(self, codigo, descripcion, tamaño, Retornable, precio):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__tamaño = tamaño
        self.__Retornable = Retornable
        self.__precio = precio
        
    def getcodigo (self):
        return self.__codigo
    def getdescripcion (self):
        return self.__descripcion
    def gettamaño(self):
        return self.__tamaño
    def getRetornable(self):
        return self.__tamaño
    def getPrecio(self):
        return self.__precio
    @abc.abstractmethod
    def gettipo(self):
        pass
    @abc.abstractmethod
    def precioVenta(self):
        pass
    