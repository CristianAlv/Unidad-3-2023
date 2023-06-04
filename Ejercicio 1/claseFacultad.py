from claseCarrera import Carrera

class Facultad:
    __codigo = int
    __nombre = str
    __direccion = str
    __localidad = str
    __telefono = str
    __carreras: list
    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carreras = []
        
    def agregar_carrera(self, carrera):
        self.__carreras.append(carrera)

    def obtener_codigo(self):
        return self.__codigo

    def obtener_nombre(self):
        return self.__nombre

    def obtener_direccion(self):
        return self.__direccion

    def obtener_localidad(self):
        return self.__localidad

    def obtener_telefono(self):
        return self.__telefono

    def obtener_carreras(self):
        return self.__carreras
    
    def buscarcarrera(self, carrera):
        band = False
        i=0
        c=0
        while i<len(self.__carreras) and not band:

            if (carrera == self.__carreras[i].get_nombre()):
                print ("La carrera fue encontrada")
                band = True
                c=i
            i+=1
        return c

    def mostrarFacultad(self, pos):
        carreras = []
        for i in range (len(self.__carreras)):
            carreras = self.__carreras[i]
            if (i == pos):
                print ("Codigo: {}.{}, Nombre: {}, Localidad: {}" .format(self.__codigo,carreras.getcod(), self.__nombre, self.__localidad))
    
