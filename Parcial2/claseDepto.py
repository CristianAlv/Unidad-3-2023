from claseInmuebles import Inmueble
class Departamento(Inmueble):
    __cantDormi = int
    __numMonoB = int
    __numDepto = int
    __numPiso = int
    
    def __init__(self,direc,loc,sup,cantD,monoB,numD,numP):
        super().__init__(direc,loc,sup)
        __cantDormi = cantD
        __numMonoB = monoB
        __numDepto = numD
        __numPiso = numP
        
    def getDormitorio (self):
        return self.__cantDormi
    def getMonoBlock (self):
        return self.__numMonoB
    def getNumDepto (self):
        return self.__numDepto
    def getNumPiso (self):
        return self.__numPiso
    
    def precioConstruccion(self):
       return (self.__cantDormi*17000)
       
    
    