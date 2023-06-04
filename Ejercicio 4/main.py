import csv
import numpy as np
from claseEmpleado import Empleado
from ClaseExterno import Externo
from Contratados import Contratado
from Planta import Planta
from manejadorEmpleado import ManejadorEmpleado
from menu import Menu

def test():
    print("{:*^45}".format(""))
    dimension = int(input("Ingrese el tamaño del arreglo a crear: "))
    print("{:*^45}".format(""))
    Mod_Menu = Menu(dimension)
    Salir = True
    while Salir:
            print("{:=^60}".format(""))
            print("Bienvenido al Menú")
            print("{:-^60}".format(""))
            print ("EJECUTAR TODAS LAS OPCIONES PARA QUE EL PROGRAMA SEA FACTIBLE")
            print("{:=^60}".format(""))
            print("1. Opción 1: Registrar Horas: ")
            print("{:=^35}".format(""))
            print("2. Opción 2: Total de Tarea: ")
            print("{:=^35}".format(""))
            print("3. Opción 3: Ayuda Economica: ")
            print("{:=^35}".format(""))
            print("4. Opcion 4: Calcular Sueldo: ")
            print("{:=^35}".format(""))

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
            else:
                if (opcion == '0'):
                        Salir = False
                        Mod_Menu.salir()
                else:
                    print ("Opcion invalida")
                    Salir=False
        
        


if __name__=='__main__':
    test()