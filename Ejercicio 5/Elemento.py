from zope.interface import Interface, implementer

class IElemento(Interface):
    def insertarElemento(objeto, posicion):
        pass
    
    def agregarElemento(objeto):
        pass
    
    def mostrarElemento(posicion):
        pass