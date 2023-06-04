from claseEmpleado import Empleado

class Externo(Empleado):
    __tarea = str
    __Fecha_inicio = None
    __Fecha_fin = None
    __Monto_Viatico = 0
    __costo_obra = 0
    __Monto_Seguro = 0
    def __init__(self,nombre, dni, direccion, telefono, tarea, fecha_inicio, fecha_fin, monto_viatico, costo_obra, monto_seguro):
        super().__init__(dni, nombre, direccion, telefono)
        self.__tarea = tarea
        self.__Fecha_inicio = fecha_inicio
        self.__Fecha_fin = fecha_fin
        self.__Monto_Viatico = monto_viatico
        self.__costo_obra = costo_obra
        self.__Monto_Seguro = monto_seguro
        
    def getsueldo(self):
        sueldo = self.__costo_obra - self.__Monto_Viatico  - self.__Monto_Seguro
        return sueldo
    def gettarea(self):
        return self.__tarea
    def getfechaI(self):
        return self.__Fecha_inicio
    def getfechaF(self):
        return self.__Fecha_fin
    def getmontoViatico(self):
        return self.__Monto_Viatico
    def getobra(self):
        return self.__costo_obra
    def getmontoseg(self):
        return self.__Monto_Seguro
    def setsueldo(self, ayuda):
        sueldo = self.getsueldo() + ayuda
        return sueldo
    
    def mostrar (self):
        print("{:-^35}".format(""))
        print("---Datos del Empleado---\n")
        super().mostrar()
        print("{:=^35}".format(""))
        print("---Empleado Tipo Externo---\n")
        print("Fecha Inicio: {} - Fecha Cierre Contrato: {}\n".format(self.__Fecha_inicio, self.__Fecha_fin))
        print("Tarea: {}\nMonto Viatico: {:.2f} - Costo de la Obra: {:.2f}\nSeguro de Vida: {:.2f}".format(self.__tarea, self.__Monto_Viatico, self.__costo_obra, self.__Monto_Seguro))
        print("Sueldo Calculado a Cobrar: {:.2f}".format(self.getsueldo()))
    