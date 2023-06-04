from classPersonal import Personal
from classDocente import Docente
from classDocenteInvestigador import DocenteInvestigador
from classInvestigador import Investigador
from clasePersonalApoyo import PersonalApoyo
from claseInterface import IElemento
from zope.interface import Interface, implementer
from claseNodo import Nodo
@implementer(IElemento)

class ListaPersonalUniv:
    def __init__(self):
        self.__comienzo = None
        self.__indice = 0
        self.__actual = None
        self.__tope = 0
        
    def __iter__(self):
        return self
    
    def __next__(self): 
        if self.__indice==self.__tope: 
            self.__actual=self.__comienzo 
            self.__indice=0 
            raise StopIteration 
        else: 
            self.__indice+=1 
            dato = self.__actual.getDato() 
            self.__actual=self.__actual.getSiguiente() 
            return dato
    
    def insertarElemento(self, posicion, elemento):
            aux = self.__comienzo
            cont = 0
            band = False
            ant = aux
            if (posicion <= self.__tope) and (posicion >= 0): ##Aplicar contador en caso de ser while
                if cont == posicion:
                    if self.__comienzo == None:
                        nodo = Nodo(unpersonal)
                        nodo.setSiguiente(self.__comienzo)
                        self.__comienzo = nodo
                        self.__actual = nodo
                        self.__tope += 1
                    else:
                        nodo = Nodo(unpersonal)
                        nodo.setSiguiente(aux)
                        aux.setSiguiente(aux.getSiguiente())
                        self.__comienzo = nodo
                        self.__actual = nodo
                        self.__tope += 1
                else:
                    ant= aux
                    while ant != None and band == False:
                        if cont == posicion:
                            band = True
                        else:
                            aux = aux.getSiguiente()
                            cont+=1
                            
                    if cont == posicion:
                        nodo = Nodo(elemento)
                        ant.setSiguiente(nodo)
                        nodo.setSiguiente(aux)
                        self.__tope += 1
                print ("Agente insertado")
                            
            else:
                raise Exception("Posicion de coleccion incorrecta")
    
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
             
        
    
    def mostrarElemento(self, posicion):
        aux = self.__comienzo
        cont = 0
        band = False
        if posicion <= self.__tope and posicion >= 0:
            while aux != None and band == False:
                if cont == posicion:
                    band = True
                    print ("Cont: {}, Persona: {}" .format(cont, aux.getDato().obtenerPersona()))
                    aux = aux.getSiguiente()
                    cont+=1
                else:
                    aux = aux.getSiguiente()
                    cont+=1
            if (band == True):
                print("El elemento encontrado es de tipo: {}\n".format(aux.gettipo()))
            else:
                print("Se ha producido un eror\n")
        else:
            raise Exception("No se encontro esa posicion en la lista")    
                
            
    def listarCarreras(self):
        aux = self.__comienzo
        i=0
        carreras = set()
        while aux != None and i < self.__tope:
                if isinstance(aux.getDato(), DocenteInvestigador):
                    print ("Carrera Docente Investigador: {}".format(aux.getDato().getcarrera()))
                elif isinstance(aux.getDato(), Docente):
                    print ("Carrera Docente: {}".format(aux.getDato().getcarrera()))
                aux = aux.getSiguiente()
                i+=1
                
    def evaluar(self, dato):
        aux = self.__comienzo

        band = False
        while aux != None:
            if aux.getDato().getnombre() == dato.getnombre() and aux.getDato().getapellido() == dato.getapellido():
                if aux.getDato().getcuil() == dato.getcuil():
                    band=True
            aux = aux.getSiguiente()
        return band
    
                
    def ordenar(self, carrera):
        nodo = self.__comienzo
        p = None
        while nodo != None:
            p = nodo.getSiguiente()
            while (p != None):

                if (nodo.getDato().getnombre() > p.getDato().getnombre()):
                    aux = nodo.getDato
                    nodo.getDato = p.getDato
                    p.getDato = aux

                p = p.getSiguiente()
            
            nodo = nodo.getSiguiente()
        unico = False
        for dato in self:
            if isinstance(dato, Docente):
                if carrera == dato.getcarrera():
                    evaluar = self.evaluar(dato)
                    if evaluar == True:
                        dato.mostrarDatos()
                        
    def mostrararea(self):
        aux = self.__comienzo
        i=0
        while aux != None and i < self.__tope:
                if type(aux.getDato()) == DocenteInvestigador:
                    print ("Areas: {}".format(aux.getDato().getarea()))
                elif isinstance(aux.getDato(), Investigador):
                    print ("Areas: {}".format(aux.getDato().getarea()))
                aux = aux.getSiguiente()
                i+=1
    
    def contar (self, area):
        aux = self.__comienzo
        cont = 0
        contA = 0
        while aux != None:
            if isinstance(aux.getDato(), DocenteInvestigador):
                if area == aux.getDato().getarea():
                    cont +=1
            if (type(aux.getDato()) == Investigador):
                if area == aux.getDato().getarea():
                    contA += 1
            aux = aux.getSiguiente()
        print ("La cantidad de docentes investigadores de esa area son: {}".format(cont))
        print ("La cantidad de investigadores que se desempeñan en el area {} son: {}".format(area,contA))
        
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
        unico = False
        print ("{:=^150}".format(""))
        for dato in self:
            if isinstance(dato, Personal):
                evaluar = self.evaluar(dato)
                if evaluar == True:
                    print("Nombre: {}, Apellido: {}, Tipo:{}, Importe de Sueldo: {:.2f}".format(dato.getnombre(),dato.getapellido(),dato.tipoP(), dato.ImporteSueldo()))
                    print ("{:=^150}".format(""))
                    
    def Indicar(self, categoria):
        aux = self.__comienzo
        TotalExtra = 0
        while aux != None:
            if isinstance(aux.getDato(), DocenteInvestigador):
                if categoria == aux.getDato().getcategoriaI():
                    print ("Nombre: {}, Apellido: {}, Importe Extra: {}".format(aux.getDato().getnombre(), aux.getDato().getapellido(), aux.getDato().getImporte()))
                    TotalExtra += aux.getDato().getImporte()
            aux = aux.getSiguiente()
            if aux == None:
                print ("El total de dinero que le debe solicitar la Secretaria de Investigacion al ministerio es de: {}".format(TotalExtra))
        
    def toJSON (self):
        d = dict (
            __class__ = self.__class__.__name__,
            comienzo = [dato.toJSON() for dato in self]                       #contiene el primer vehiculo, el sig vehiculo, etc.
        )
        return d