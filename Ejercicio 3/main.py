from claseTaller import TallerCapacitacion
from persona import persona
from manejadorPersona import ManejadorPersona
from manejadorTaller import ManejadorTaller
from menu import Menu
def test():
    manejaPersona = ManejadorPersona()
    manejaTaller = ManejadorTaller()

Mod_Menu = Menu()
Salir = True
while Salir:
        print("Bienvenido al Menú")
        print ("EJECUTAR TODAS LAS OPCIONES PARA QUE EL PROGRAMA SEA FACTIBLE")
        print("1. Opción 1: Cargar los datos de los talleres y las personas: ")
        print("2. Opción 2: Inscribir a una Persona en un taller:  ")
        print("3. Opción 3: Consultar inscripción: ")
        print("4. Opcion 4: Consultar inscriptos en un taller: ")
        print("5. Opcion 5: Registrar Pago: ")
        print("6. Opcion 6: Guardar Inscripciones: ")
        print("0. Salir")
        opcion = input("Ingrese la opcion: ")
        if opcion =='1':
            Mod_Menu.opcion1()
        elif opcion =='2':
            Mod_Menu.opcion2()
        elif opcion == '3':
            Mod_Menu.opcion3()
        elif opcion == '4':
            Mod_Menu.opcion4()
        elif opcion == '5':
            Mod_Menu.opcion5()
        elif opcion == '6':
            Mod_Menu.opcion6()  
        else:
            if (opcion == '0'):
                    Salir = False
                    Mod_Menu.salir()
            else:
                print ("Opcion invalida")
                Salir=False

if __name__ == '__main__':
    test()