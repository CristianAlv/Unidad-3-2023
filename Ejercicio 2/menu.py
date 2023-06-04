from ManejadorHelado import ManejaHelados
from ManejadorSabores import ManejaSabores
from ClaseHelado import Helado
from ClaseSabores import sabor
class Menu(object):
    __switcher = None
    __helados_vendidos = []
    __sabores = []
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.opcion5,
            '0':self.salir
        }
        self.__helados_vendidos = ManejaHelados()

        
        self.__sabores = ManejaSabores()
        self.__sabores.Cargar()

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
        self.__sabores.mostrar_sabores()
        Helado1=self.__helados_vendidos.gestionarpedido(self.__sabores)
        print ("{}, {}, {}" .format(Helado1.getgramos(), Helado1.getprecio(), Helado1.getsabores()))
        self.__helados_vendidos.agregar_helado(Helado1)
        self.__helados_vendidos.mostrarVendidos()
        
    def opcion2(self):
        self.__helados_vendidos.mostrar_vendidos(self.__sabores)

        
    def opcion3 (self):
        codigo = int(input("Ingrese el Id del sabor: "))
        self.__helados_vendidos.recorrer(codigo)
        
    def opcion4 (self):
        helado = float(input("Ingrese el tipo de helado: "))
        conteo =  self.__helados_vendidos.tamano(helado, self.__sabores)
        self.__helados_vendidos.mostrar_tamaño(conteo, helado, self.__sabores)
        
    def opcion5 (self):
        self.__helados_vendidos.mostrartotal(self.__sabores)
