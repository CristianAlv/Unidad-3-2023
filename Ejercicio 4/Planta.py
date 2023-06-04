from claseEmpleado import Empleado
class Planta(Empleado):
    __SueldoBasic = 0.0
    __Antig = 0
    def __init__(self, nombre, dni, direccion, telefono, SueldoBasic, Antig):
        super().__init__(dni, nombre, direccion, telefono)
        self.__SueldoBasic = SueldoBasic
        self.__Antig = Antig
        
    def getsueldo(self):
        sueldo = self.__SueldoBasic + (self.__SueldoBasic*0.01)*self.__Antig
        return sueldo
    def getSueldo(self):
        return self.__SueldoBasic
    def getantiguedad(self):
        return self.__Antig
    def setsueldo(self, ayuda):
        sueldo = self.getsueldo()+ayuda
        return sueldo
    def mostrar (self):
        print("{:-^35}".format(""))
        print("---Datos del Empleado---\n")
        super().mostrar()
        print("{:=^35}".format(""))
        print("---Empleado Tipo Planta---\n")
        print("Sueldo Basico: {} - Antiguedad: {}\n".format(self.__SueldoBasic, self.__Antig))
        print("Sueldo Calculado a Cobrar: {:.2f}".format(self.getSueldo()))
