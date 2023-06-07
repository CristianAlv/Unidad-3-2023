from claseBebida import Bebida
from claseNodo import Nodo
from classBebidaCDesc import BebidaconDesc
from classBebidaDescuento import BebidasinDesc
from classLista import Lista


if __name__=='__main__':
    ListaBebida = Lista()
    bebida2 = BebidaconDesc("B002", "Cerveza Amber Lager Patagonia", 330, False, 80.0, 10)
    bebida3 = BebidasinDesc("B003", "Agua Mineral", 1000, True, 30.0)
    bebida4 = BebidaconDesc("B004","Vino Tinto Malbec", 750, True, 200.0,15)
    ListaBebida.agregar(bebida2)
    ListaBebida.agregar(bebida4)
    ListaBebida.agregar(bebida3)
    codigo = str(input("Ingrese el codigo de bebida con descuento: "))
    ListaBebida.Indicar(codigo)
    ListaBebida.mostrar()
    