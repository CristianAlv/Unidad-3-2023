from classDocente import Docente
from classInvestigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    def __init__(self, nombre, apellido, cuil, sueldoBasico, antig, carrera, cargo, catedra, areaInv, tipoInv, categInvestigacion, importeExtra):
        super().__init__(nombre, apellido, cuil, sueldoBasico, antig, carrera, cargo, catedra, areaInv, tipoInv)
        self.__categoriaI = categInvestigacion      
        self.__Importe = importeExtra
        
    def getImporte(self):
        return self.__Importe
    def getcategoriaI(self):
        return self.__categoriaI
    def setImporte(self, importe):
        self.__Importe = importe
        return self.__Importe
    
    def ImporteSueldo(self):
        sueldo = self.getsueldo() + self.__Importe
        return sueldo
    
    def tipoP(self):
        return "Docente Investigador"
    
    def toJSON (self):
        d = dict (
            __class__ = self.__class__.__name__,
            __atributos__ = dict (
                nombre = self.getnombre(),              
                apellido = self.getapellido(),
                cuil = self.getcuil(),
                sueldoBasico = self.getsueldo(),
                antig = self.getantiguedad(),
                carrera = self.getcarrera(),
                cargo = self.getcargo(),
                catedra = self.getcatedra(),
                areaInv = self.getarea(),
                tipoInv = self.gettipo(),
                categInvestigacion = self.__categoriaI,
                importeExtra = self.__Importe
            )
        )
        return d
    
    