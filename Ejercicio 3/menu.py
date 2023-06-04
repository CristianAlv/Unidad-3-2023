from manejadorPersona import ManejadorPersona
from manejaInscriptos import ManejadorInscripto
from manejadorTaller import ManejadorTaller

class Menu(object):
    __switcher = None
    __list_Persona = []
    __Talleres = []
    __Inscriptos = []
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.opcion5,
            '6':self.opcion6,
            '0':self.salir
        }
        self.__list_Persona = ManejadorPersona()
        

        
        self.__Talleres = ManejadorTaller(4,4)
        self.__Inscriptos = ManejadorInscripto(5,0)

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
        self.__list_Persona.Cargar_Lista()
        self.__Talleres.CargarArreglo()
        self.__Talleres.mostrarArreglo()
        
    def opcion2(self):
        print ("Inscribiendo Persona")
        for persona in self.__list_Persona.getlista():
            self.__Talleres.inscribirPersona(persona, self.__Inscriptos)

        
    def opcion3 (self):
        self.__Talleres.Consultar(self.__Inscriptos)
        
    def opcion4 (self):
        taller = int(input("Ingrese el id del taller a listar: "))
        c= self.__Talleres.buscarTaller(taller)
        if c != None:
            self.__Talleres.listar(c, taller)
        
        
    def opcion5 (self):
        doc = str(input("Ingrese el documento para realizar el pago: "))
        self.__Inscriptos.actualizar(doc)
        
    def opcion6(self):
        self.__Inscriptos.NuevoCsv()