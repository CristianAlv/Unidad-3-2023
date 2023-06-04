from Elemento import IElemento
from zope.interface import implementer

@implementer(IElemento)
class Coleccion:
    def __init__(self):
        self.__coleccion = []
        
    def insertarElemento(self, objeto, posicion):
        if posicion != 0 and posicion < len(self.__coleccion):
            self.__coleccion.insert(posicion, objeto)
        else:
            raise ValueError("Posicion de insercion incorrecta")
        
    def agregarElemento(self, objeto):
        self.__coleccion.append(objeto)
        
    def mostrarElemento(self, posicion):
        if posicion > 0 and posicion < len(self.__coleccion):
            return self.__coleccion[posicion]
        else:
            raise ValueError("No existe el elemento en esta posición")