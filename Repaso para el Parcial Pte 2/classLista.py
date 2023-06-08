from claseBebida import Bebida
from claseNodo import Nodo
from classBebidaCDesc import BebidaconDesc
from classBebidaDescuento import BebidasinDesc

class Lista:
    def __init__(self):
        self.__actual = None
        self.__comienzo = None
        self.__tope = 0
        self.__indice = 0
        
    def __iter__(self):
        self.__indice = 0
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getsiguiente()
        return dato
        
    def agregar(self, elemento):
        aux = self.__comienzo
        if aux == None:
                nodo = Nodo(elemento)
                nodo.setSiguiente(self.__comienzo)
                self.__actual = nodo
                self.__comienzo = nodo
                self.__tope += 1
        else:
            cont = 0
            ant = aux
            band = False
            while aux != None and cont <= self.__tope:
                ant = aux
                aux = aux.getsiguiente()
                cont+=1
            if ant != None:
                nodo = Nodo(elemento)
                ant.setSiguiente(nodo)
                nodo.setSiguiente(aux)
                self.__tope+=1
        print ("Elemento Agregado")
        
    def Insertar(self, posicion, elemento):
        aux = self.__comienzo
        cont = 0
        band = False
        if posicion <= self.__tope and posicion >= 0:
            if cont == posicion:
                if self.__comienzo == None:
                    nodo = Nodo(elemento)
                    nodo.setSiguiente(self.__comienzo)
                    self.__actual = nodo
                    self.__comienzo = nodo
                    self.__tope += 1
                else:
                    nodo = Nodo(elemento)
                    nodo.setSiguiente(aux)
                    aux.setsiguiente(aux.getsiguiente())
                    self.__actual = nodo
                    self.__comienzo = nodo
                    self.__tope += 1
                    
            else:
                ant = aux
                while aux != None and band == False:
                    if cont == posicion:
                        band = True
                    else:
                        aux = aux.getsiguiente()
                        cont+=1
                if band == True:
                    nodo = Nodo(elemento)
                    nodo.setSiguiente(aux)
                    ant.setSiguiente(nodo)
                    self.__tope += 1
                    
                    print ("El elemento fue insertado en la posicion {}".format(posicion))
        else:
            raise Exception("Posicion no valida")
    def Indicar(self, codigo):
        aux = self.__comienzo
        band = False
        if isinstance(aux.getDato(), BebidaconDesc):
            while aux != None and band == False:
                    if codigo == aux.getDato().getcodigo():
                            band = True
                            new = float(input("Ingrese el nuevo porcentaje de descuento: "))
                            aux.getDato().setdescuento(new)
                            print ("Porcentaje cambiado a {}" .format(aux.getDato().getporcentaje()))   
                    aux = aux.getsiguiente()
                    
    def eliminar (self, codigo):
        aux = self.__comienzo
        cont = 0
        band = False
        ant= None
        if aux.getDato().getcodigo() == codigo:
            band = True
            self.__comienzo = aux.getsiguiente()
            self.__tope -= 1
            del aux
            print ("Elemento eliminado")
            return
        while aux is not None and not band:
            if aux.getDato().getcodigo() == codigo:
                band = True
            else:
                ant = aux
                aux = aux.getsiguiente()
        if band:
            ant.setSiguiente(aux.getsiguiente())
            self.__tope -= 1
            del aux
            print("Elemento eliminado")
        else:
            print("No se encontró un elemento con el código especificado")
        
        
    def mostrar(self):
        for dato in self:
            print("Descripcion: {}, Precio Venta: {}".format(dato.getdescripcion(), dato.precioVenta()))
            