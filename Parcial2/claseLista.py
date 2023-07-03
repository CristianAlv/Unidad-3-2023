from nodo import Nodo
from claseCasa import Casa
from claseDepto import Departamento
class ListaEnlazada:
    __comienzo = Nodo
    __actual = Nodo
    __indice = int
    __tope = int
    
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__indice = 0
    
    def __iter__(self): #retorna a si mismo
        return self
    
    def __next__(self): #evalua una condicion, ¿el iterador ha llegado al final de la lista?
        if self.__indice == self.__tope: # si es asi, debo devolver el actual(con el q recorro la lista), al principio
            self.__actual = self.__comienzo
            self.__indice = 0 
            raise StopIteration
        else:                       #si no es asi, debo avanzar al siguiente, guardar el dato para mostrarlo (o trabajarlo), 
            self.__indice +=1       #y posteriormente dejar el actual con el siguiente
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
        return dato 
                
    def insertar (self, i, elemento): #insertar en una posicion
        aux = self.__comienzo
        cont = 0
        band = False
        ant = aux
        if (i <= self.__tope) and (i >= 0): ##Aplicar contador en caso de ser while
            if cont == i:
                if self.__comienzo == None:
                    nodo = Nodo(elemento)
                    nodo.setSiguiente(self.__comienzo)
                    self.__comienzo = nodo
                    self.__actual = nodo
                    self.__tope += 1
                else:
                    nodo = Nodo(elemento)
                    nodo.setSiguiente(aux)
                    aux.setSiguiente(aux.getSiguiente())
                    self.__comienzo = nodo
                    self.__actual = nodo
                    self.__tope += 1
            else:
                ant= aux
                while ant != None and band == False:
                    if cont == i:
                        band = True
                    else:
                        aux = aux.getSiguiente()
                        cont+=1
                            
                    if cont == i:
                        nodo = Nodo(elemento)
                        ant.setSiguiente(nodo)
                        nodo.setSiguiente(aux)
                        self.__tope += 1
                            
    
    
    def agregarElemento(self, unPersonal): #Para todos los casos es lo mismo, la unica diferencia esta en en objeto a agregar
        aux = self.__comienzo
        ant = aux
        if aux == None:                                    
            nodo = Nodo(unPersonal)
            nodo.setSiguiente(self.__comienzo)                         
            self.__actual = nodo
            self.__comienzo = nodo
            self.__tope += 1
        else:
            i = 0
            while ((aux != None) and (i < self.__tope)):
                ant = aux
                aux = aux.getSiguiente()
                i += 1

            if ant != None:                 
                nodo = Nodo(unPersonal) 
                ant.setSiguiente(nodo)                    
                nodo.setSiguiente (aux)                    
                self.__tope += 1           
                
    def OrdenarLista(self): 
        nodo = self.__comienzo
        p = None
        while nodo != None:
            p = nodo.getSiguiente()
            while (p != None):

                if (nodo.getDato().getapellido() > p.getDato().getapellido()):
                    aux = nodo.getDato
                    nodo.getDato = p.getDato
                    p.getDato = aux

                p = p.getSiguiente()

            nodo = nodo.getSiguiente()        
                      