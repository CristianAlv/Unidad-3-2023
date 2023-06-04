class persona(object):
    __nombre = str
    __direccion = str
    __dni = str
    def __init__(self, nombre, direccion, Dni):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = Dni
    def getNombre (self):
        return self.__nombre
    def getDireccion (self):
        return self.__direccion
    def getDni (self):
        return self.__dni
    def mostrarPersona (self):
        print("Nombre: {}\nDireccion: {}\nDNI: {}\n".format(self.__nombre, self.__direccion, self.__dni))