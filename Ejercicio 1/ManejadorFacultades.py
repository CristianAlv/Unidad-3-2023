import csv
from claseFacultad import Facultad
from claseCarrera import Carrera

class ManejadorFacultad():
    __facultades = []
    def __init__(self):
        self.__facultades = []
    def CargarLista(self):
        archivo = open("Facultades.csv", encoding= 'utf8')
        reader = csv.reader(archivo, delimiter = ",")
        facultad = None
        for fila in reader:
            if len(fila)==5:
                codigo = int(fila[0])
                nombre = str(fila[1])
                direccion = str(fila[2])
                localidad = str(fila[3])
                telefono = str(fila[4])
                
                facultad = Facultad(codigo, nombre, direccion, localidad, telefono)
                self.__facultades.append(facultad)
                
            elif len(fila)==6:
                cod = int(fila[1])
                nombre = str(fila[2])
                duracion = str(fila[4])
                titulo = str(fila[3])
                nivel = str(fila[5])
                carrera = Carrera(cod, nombre,duracion, titulo, nivel)
                facultad.agregar_carrera(carrera)
                
        archivo.close()
        
    def mostrarLista(self):
        for i in range (len(self.__facultades)):
            print("Facultad: {}" .format(self.__facultades[i].obtener_nombre()))
            
    def buscarCodigo(self,codigo):
        i=0
        c=0
        while (i< len(self.__facultades)):
            if (codigo == self.__facultades[i].obtener_codigo()):
                print ("El codigo de la facultad fue encontrado")
                c=i
            i+=1
            
        return c
    def mostrartodo(self, pos):
        
        carreras = self.__facultades[pos].obtener_carreras()
        
        for carrera in carreras:
            print("Nombre de facultad: {}, Nombre de la Carrera: {}, Duracion: {}" .format(self.__facultades[pos].obtener_nombre(), carrera.get_nombre(), carrera.getduracion()))
            

        
            
    def mostrarcarrera(self, carrera):
        i=0
        bandera = False
        while not bandera:
            c = self.__facultades[i].buscarcarrera(carrera)
            if (c != 0):
                bandera= True
                self.__facultades[i].mostrarFacultad(c)
            