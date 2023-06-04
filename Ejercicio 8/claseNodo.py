from classPersonal import Personal
from classDocente import Docente
from classDocenteInvestigador import DocenteInvestigador
from classInvestigador import Investigador
from clasePersonalApoyo import PersonalApoyo

class Nodo:
    __personal = None
    __siguiente = None
    def __init__(self, unpersonal):
        if isinstance(unpersonal, Personal):
            self.__personal = unpersonal
        self.__siguiente = None
        
    def getDato(self):
        return self.__personal
    def setSiguiente (self, siguienteP):
        self.__siguiente = siguienteP
    def getSiguiente (self):
        return self.__siguiente
    def gettipo(self):
        tipo = None
        if isinstance(self.__personal, DocenteInvestigador):
            tipo = 'Docente e Investigador '
        elif isinstance(self.__personal, Docente):
            tipo = 'Docente'
        elif isinstance(self.__personal, Investigador):
            tipo = 'Investigador'
        elif isinstance(self.__personal, PersonalApoyo):
            tipo = 'Personal de Apoyo'
            
        return tipo
            
            
        