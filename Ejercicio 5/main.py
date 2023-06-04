from Elemento import IElemento
from Coleccion import Coleccion

def test():
    coleccion = Coleccion()
    coleccion.agregarElemento("Pelota")
    coleccion.agregarElemento("Camiseta")
    coleccion.agregarElemento("Botines")
    coleccion.insertarElemento("Lentes", 1)
    elemento = coleccion.mostrarElemento(2)
    print ("{:=^50}".format(""))
    print(elemento)
    print ("{:=^50}".format(""))

if __name__ == '__main__':
    test()