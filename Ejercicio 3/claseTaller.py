from datetime import date
from inscriptos import Inscripto
from manejaInscriptos import ManejadorInscripto
class TallerCapacitacion(object):
    __idTaller = int
    __nombre = str
    __vacantes = int
    __monto = int
    __inscripto: list
    def __init__(self, iD, nombre, vacantes, monto):
        self.__idTaller = iD
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__monto = monto
        self.__inscripto = []

    def getIdTaller (self):
        return self.__idTaller
    def getNombreTaller(self):
        return self.__nombre
    def getVacantes (self):
        return self.__vacantes
    def getMonto (self):
        return self.__monto

    
    def actualizarVacante(self):
        self.__vacantes -= 1
        return self.__vacantes
    
    def addinscripto(self, inscripto, manejadorI, iD):
        i=0
        band=False
        while iD.getIdTaller() == self.__idTaller and band==False:
                fecha = date.today()
                print("La facha actual es: {}" .format(fecha))
                inscripto1 = Inscripto(fecha, inscripto, iD)
                manejadorI.agregarInscripto(inscripto1)
                print("La persona fue inscripta exitosamente")
                self.__inscripto.append(inscripto1)
                self.actualizarVacante()
                band=True
                i+=1
                
    def buscarInscripto (self, doc, nombreT, montoT):
        i = 0
        band = False
        while ((i < len(self.__inscripto)) and (band == False)):
            persona = self.__inscripto[i].getPersonaIns()
            if ((doc == persona.getDni()) and (self.__inscripto[i].getTallerIns() == nombreT)):     
                band = True    
            i += 1
        if band == True:    
            if (self.__inscripto[i-1].getPago() == False):
                print("Persona: {}, inscripta en taller: {}\nMonto que adeuda: {}".format(persona.getNombre(),nombreT, montoT))
            else:
                print("Persona: {}, inscripta en el taller:{}\nNO adeuda un monto, pues ya lo pago!".format(persona.getNombre(),nombreT))
        return band
    
    def lista(self, taller):
        i=0
        while i<len(self.__inscripto):
            if self.__inscripto[i].getIdTallerIns() == taller:
                    print ("La personas que estan inscriptas en el taller son: \n ")
                    print ("Nombre y Apellido: {}, Dni: {}, Direccion: {}" .format(self.__inscripto[i].getPersonaInsNombre(), self.__inscripto[i].getPersonaInsDni(), self.__inscripto[i].getPersonaInsDireccion()))
            i+=1
