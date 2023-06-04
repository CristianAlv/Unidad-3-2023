from inscriptos import Inscripto
import numpy as np
import csv
class ManejadorInscripto:
    __cantidad = 0
    __incremento = 5
    __dimension = 0
    def __init__(self, incremento=5, dimension=0):
        self.__cantidad = 0
        self.__incremento = incremento
        self.__dimension = dimension
        self.__inscripciones = np.empty((self.__dimension), dtype=Inscripto)
    
    def agregarInscripto(self, inscripto):
        if (self.__cantidad == self.__dimension):
            self.__dimension += self.__incremento
            self.__inscripciones.resize(self.__dimension)
            self.__inscripciones[self.__cantidad]= inscripto
            self.__cantidad += 1
            
    def getcantidad(self):
        return self.__cantidad
    def getdimension(self):
        return self.__dimension
    def actualizar(self, doc):
        i=0
        c=0
        while i < self.__cantidad:
            if(doc == self.__inscripciones[i].getDniPersIns()):
                otroPago = True
                pago = self.__inscripciones[i].setpago(otroPago)
                if pago == True:
                    print ("La persona {} completo el pago en forma exitosa" .format(self.__inscripciones[i].getPersonaInsNombre()))
            i+=1
    def NuevoCsv(self):
        
        archivo = open("newInscripPago.csv", 'w')
        writer = csv.writer(archivo, delimiter = ';')
        for fila in range (self.__cantidad):
            lista = []
            self.__inscripciones[fila].crear(lista)
            print("Lista es: ", lista)
            
        for i in range(self.__cantidad):
            writer.writerow ([self.__inscripciones[i].getPersonaInsDni(), str(self.__inscripciones[i].getIdTallerIns()), str(self.__inscripciones[i].getFechaIns()), str(self.__inscripciones[i].getPago())])
        
        
        archivo.close()