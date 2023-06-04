from claseEmpleado import Empleado
from ClaseExterno import Externo
from Contratados import Contratado
from Planta import Planta
from manejadorEmpleado import ManejadorEmpleado

class Menu:
    __switcher = None
    __arre_empleados = []
    def __init__(self, dimension):
        self.__switcher = { '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.opcion5,
            '6':self.opcion6,
            '0':self.salir
        }
        
        self.__arre_empleados = ManejadorEmpleado(dimension, 5)
        self.__arre_empleados.CargarContratados()
        self.__arre_empleados.CargarPlanta()
        self.__arre_empleados.CargarExterno()



    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self, op,numero):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(numero)
    
    def salir(self):
        print ("Terminando ejecucion del programa....")
        print ("======Gracias por ejecutar el programa======")
        print (":-)")
        
    
    def opcion1(self):
        dni = int(input("Ingrese un dni: "))
        horas = int(input("Ingrese la cantidad de horas trabajadas en el dia de la fecha: "))
        c = self.__arre_empleados.buscar(dni, horas)

        
    def opcion2(self):
        fechaactual = str(input("Ingrese la fecha actual con el siguiente formato: Por ejemplo: 25/05/2023: "))
        tarea = str(input("Ingrese la tarea a calcular el monto: "))
        self.__arre_empleados.monto(fechaactual, tarea)

        
    def opcion3 (self):
        self.__arre_empleados.ayuda()
        
    def opcion4 (self):
        self.__arre_empleados.mostrarEmpleados()
        
        
    def opcion5 (self):
        doc = str(input("Ingrese el documento para realizar el pago: "))
        self.__Inscriptos.actualizar(doc)
        
    def opcion6(self):
        self.__Inscriptos.NuevoCsv()