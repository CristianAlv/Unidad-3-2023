
class Carrera():
    __cod = int
    __nombre = str
    __duracion = str
    __titulo = str
    __nivel= str
    def __init__(self, cod, nombre,duracion, titulo, nivel):
        self.__cod = cod
        self.__nombre = nombre
        self.__duracion = duracion
        self.__titulo = titulo
        self.__nivel = nivel
        
    def getcod(self):
        return self.__cod
    def get_nombre(self):
        return self.__nombre
    def getfecha(self):
        return self.__fecha
    def getduracion(self):
        return self.__duracion
    def gettitulo(self):
        return self.__titulo
