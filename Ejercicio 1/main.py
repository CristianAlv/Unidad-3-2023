from claseCarrera import Carrera
from claseFacultad import Facultad
from ManejadorFacultades import ManejadorFacultad
from Menu import Menu


def test():
    pos=0
    Manejador = ManejadorFacultad()
    Manejador.CargarLista()
    Manejador.mostrarLista()
    Mod_Menu = Menu()
    Salir = True
    while Salir:
            print("Bienvenido al Menú")
            print("1. Opción 1:  Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre y duración de cada una de las carreras que se dictan en esa facultad")
            print("2. Opción 2: Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta")
            print("0. Salir")
            opcion = input("Ingrese la opcion: ")
            if opcion =='1':
                codigo = float(input("Ingrese el codigo de una facultad: "))
                Mod_Menu.opcion1(codigo)
            elif opcion =='2':
                nombre_carrera = str(input("Ingrese el nombre de la carrera: "))
                Mod_Menu.opcion2(nombre_carrera)
            else:
                if (opcion == '0'):
                        Salir = False
                        Mod_Menu.salir()
                else:
                    print ("Opcion invalida")
                    Salir=False


if __name__ == '__main__':
        test()

        