class Empleado:
    __nombre = str
    __dni = int
    __direccion = str
    __telefono = str
    def __init__(self, nombre, dni, direccion, telefono):
        self.__nombre = nombre
        self.__dni = dni
        self.__direccion = direccion
        self.__telefono = telefono
        
    def getdni(self):
        return self.__dni
    def getnombre(self):
        return self.__nombre
    def getdireccion(self):
        return self.__direccion
    def gettelefono(self):
        return self.__telefono
    
    def getsueldo(self):
        pass
    def setsueldo(self, ayuda):
        sueldo = self.getsueldo() + ayuda
        return sueldo
    
    def mostrar (self):
        print("Nombre: {}\nDNI: {}\nDireccion: {}\nTelefono: {}\n".format(self.__nombre, self.__dni, self.__direccion, self.__telefono))