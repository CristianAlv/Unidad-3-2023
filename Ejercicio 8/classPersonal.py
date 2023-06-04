from abc import ABC
import abc
class Personal(ABC):
    def __init__(self, nombre, apellido, cuil, sueldoBasico, antig,carrera, cargo, catedra, areaInv, tipoInv):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldo = sueldoBasico
        self.__antiguedad = antig
    
    def getcuil(self):
        return self.__cuil
    def getapellido(self):
        return self.__apellido
    def getnombre(self):
        return self.__nombre
    def getsueldo(self):
        return self.__sueldo
    def getantiguedad(self):
        return self.__antiguedad
    def obtenerPersona(self):
        return f"{self.getnombre()}, {self.getapellido()}"
    def getdni(self):
        dni = self.__cuil[3:11]
        return dni
    def setBasico(self, nuevo):
        self.__sueldo = nuevo
        return self.__sueldo
    

    def getsueldo(self):
        return self.__sueldo
    def mostrarDatos (self):
        print("----Datos del Personal Universitario----\n")
        print("Nombre y Apellido:{} {}\nCUIL: {}\nSueldo Basico: {:.2f} - Antiguedad: {} años".format(self.getnombre(), self.getapellido(), self.getcuil(), self.getsueldo(), self.getantiguedad()))
    
    @abc.abstractmethod
    def ImporteSueldo(self):
        pass       