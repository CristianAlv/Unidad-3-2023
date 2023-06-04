from ManejadorFacultades import ManejadorFacultad
from claseCarrera import Carrera
from claseFacultad import Facultad
class Menu(object):
    __switcher = None
    __lista_facultades = []

    def __init__(self):
        self.__switcher = { '1':self.opcion1,
            '2':self.opcion2,
            '0':self.salir
        }
        self.__lista_facultades = ManejadorFacultad()
        self.__lista_facultades.CargarLista()

    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self, op,numero):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(numero)
    
    def salir(self):
        print ("Terminando ejecucion del programa....")
        print ("======Gracias por ejecutar el programa======")
        print (":-)")
    
    def opcion1(self, codigo):
        pos = self.__lista_facultades.buscarCodigo(codigo)
        self.__lista_facultades.mostrartodo(pos)
        
    def opcion2(self, carrera):
        self.__lista_facultades.mostrarcarrera(carrera)

        