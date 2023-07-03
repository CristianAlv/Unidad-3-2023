from persona import persona

class Inscripto(object):
    __fecha = None
    __pago = False
    __persona: object
    __taller: object
    def __init__(self, fecha, persona, taller):
        self.__fecha = fecha
        self.__pago = False
        self.__persona = persona
        self.__taller = taller
        
    
    def getFechaIns (self):
        return self.__fecha
    
    def getPago (self):
        return self.__pago

    def getPersonaInsNombre (self):
        return self.__persona.getNombre()
    def getPersonaIns (self):
        return self.__persona
    def getPersonaInsDni (self):
        return self.__persona.getDni()
    def getPersonaInsDireccion (self):
        return self.__persona.getDireccion()
    def getDniPersIns (self):
        return self.__persona.getDni()
    def setPago(self, valor):
        self.__pago = valor         
    def getTallerIns(self):
        return self.__taller.getNombreTaller()
    def getIdTallerIns(self):
        return self.__taller.getIdTaller()
    def setpago(self, pago):
        self.__pago = pago
        return self.__pago
    def crear (self, lista):
        fila = [self.__persona.getDni(), self.__taller.getIdTaller(), self.__fecha, self.__pago]
        lista.append(fila)
