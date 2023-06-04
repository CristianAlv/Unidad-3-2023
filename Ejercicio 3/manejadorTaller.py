from claseTaller import TallerCapacitacion
import csv
import numpy as np
from inscriptos import Inscripto
class ManejadorTaller():
    __cantidad = 0
    __incremento = 4
    __dimension = 0
    def __init__(self, inc = 4, dim = 4):
        self.__incremento = inc
        self.__dimension = dim
        self.__Talleres = np.empty((self.__dimension), dtype=TallerCapacitacion)
        self.__cantidad = 0
    def CargarArreglo(self):
        archivo = open("Talleres.csv")
        reader = csv.reader(archivo, delimiter = ';')
        cabecera = True
        indice = 0
        for fila in reader:
            if cabecera:
                cabecera = not cabecera
            else:
                tallers = TallerCapacitacion(int(fila[0]), str(fila[1]), int(fila[2]), int(fila[3]))
                self.__Talleres[self.__cantidad] = tallers
                self.__cantidad +=1
                print("Carga Exitosa")
        archivo.close()
        
    def mostrarArreglo(self):
        for i in range (len(self.__Talleres)):
            print("id: {}, NombreTaller: {}" .format(self.__Talleres[i].getIdTaller(), self.__Talleres[i].getNombreTaller()))
            
    def obtenerid(self, id):
        i=0
        while i< self.__dimension:
            if (id == self.__Talleres[i].getIdTaller()):
                return self.__Talleres[i]
            i+=1
            
    def buscarTaller(self, idTaller):
        i=0
        c=0
        while(i<len(self.__Talleres)):
            if (idTaller == self.__Talleres[i].getIdTaller()):
                print("El taller fue encontrado")
                c=i
            i+=1
        return c
            
    def inscribirPersona(self, persona, manejaInscriptos):
        print ("La persona a inscribir es: {}" .format(persona.getNombre()))
        print ("Los talleres disponibles son: ")
        for i in range (self.__dimension):
            print ("Taller {}: {}".format(self.__Talleres[i].getIdTaller(), self.__Talleres[i].getNombreTaller()))
        
        idTaller = int(input("Ingrese la id del taller por el que se quiere inscribir: "))
        Taller = self.buscarTaller(idTaller)
        if Taller >= 0:
            obtener_id = self.obtenerid(idTaller)
            obtener_id.addinscripto(persona, manejaInscriptos, obtener_id)
            
    def Consultar(self, manejadorI):
        i=0
        band=False
        dni= str(input("Ingrese el dni de la persona a buscar:"))
        while i < self.__cantidad and band == False:
            monto= self.__Talleres[i].getMonto()
            nombre = self.__Talleres[i].getNombreTaller()
            band = self.__Talleres[i].buscarInscripto(dni, nombre, monto)
            i+=1
    def listar(self, c, taller):
        for i in range (self.__dimension):
            if (c == i):
                c= self.__Talleres[i].lista(taller)

