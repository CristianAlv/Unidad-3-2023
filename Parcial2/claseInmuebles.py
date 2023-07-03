from abc import ABC
import abc
class Inmueble(ABC):
    __direccion = str
    __localidad = str
    __superficie = str
    
    def __init__(self, direc, loc, sup):
        self.__direccion = direc
        self.__localidad = loc
        self.__superficie = sup
    
    @abc.abstractmethod
    def precioConstruccion(self):
        pass    
        
    def importeVenta(self):
        return self.__superficie*15*self.precioConstruccion()
    
  
    