from claseEmpleado import Empleado

class Contratado(Empleado):
    valorHora = 3000
    __fecha_ini = None
    __fecha_fin = None
    __Cant_horasT = 0
    def __init__(self,nombre, dni, direccion, telefono, fecha_ini,fecha_fin,cant_horas):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fecha_ini = fecha_ini
        self.__fecha_fin = fecha_fin
        self.__Cant_horasT = cant_horas
        
    @classmethod
    def getvalorhora(cls):
        return cls.valorHora
    
    def getstartfecha(self):
        return self.__fecha_ini
    def getendfecha(self):
        return self.__fecha_fin
    def getcanthoras(self):
        return self.__Cant_horasT
    def getsueldo(self):
        sueldo = self.__Cant_horasT * Contratado.getvalorhora()
        return sueldo
    def setCantHoras(self, horas):
        self.__Cant_horasT += horas
        return self.__Cant_horasT
    def setsueldo(self, ayuda):
        sueldo = self.getsueldo()+ayuda
        return sueldo
    def mostrar (self):
        print("{:-^35}".format(""))
        print("---Datos del Empleado---\n")
        super().mostrar()
        print("{:=^35}".format(""))
        print("---Empleado Tipo Contratado---\n")
        print("Fecha Inicio Contrato: {} - Fecha Fin Contrato: {}\nCantidad de Horas: {}\nValor por Hora: {}".format(self.__fecha_ini, self.__fecha_fin, self.__Cant_horasT, Contratado.getvalorhora()))
        print("Sueldo Calculado a Cobrar: {:.2f}".format(self.getsueldo()))
    