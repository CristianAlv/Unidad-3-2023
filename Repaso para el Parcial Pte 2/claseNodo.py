from claseBebida import Bebida
from classBebidaCDesc import BebidaconDesc
from classBebidaDescuento import BebidasinDesc

class Nodo:
    __Bebida = None
    __siguiente = None
    def __init__(self, unaBebida):
        if isinstance(unaBebida, Bebida):
            self.__Bebida = unaBebida
        self.__siguiente = None
        
    def getDato(self):
        return self.__Bebida
    def setSiguiente(self, siguente):
        self.__siguiente = siguente
    def getsiguiente(self):
        return self.__siguiente