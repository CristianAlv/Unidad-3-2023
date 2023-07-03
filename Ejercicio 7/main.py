from classPersonal import Personal
from classDocente import Docente
from classDocenteInvestigador import DocenteInvestigador
from classInvestigador import Investigador
from clasePersonalApoyo import PersonalApoyo
from claseInterface import IElemento
from zope.interface import Interface, implementer
from claseNodo import Nodo
from claseLista import ListaPersonalUniv
import json
from claseObjectEncoderP import ObjectEncoderP
from claseMenu import Menu


if __name__ == '__main__':
    lista = ListaPersonalUniv()
    archivoJson = ObjectEncoderP()
    diccionario = archivoJson.leerArchivoJSON('personal.json')
    print (diccionario)
    lista = archivoJson.decodificarDicc(diccionario)
    print ("Lista Personal Cargada")
    Mod_Menu = Menu()
    Salir = True

    while Salir:
        print("Bienvenido al Menú")
        print("1. Opción 1: Insertar a agentes a la colección: ")
        print("2. Opción 2: Agregar a Agentes a la coleccion: ")
        print("3. Opción 3:  Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición")
        print("4. Opción 4: El nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.")
        print("5. Opción 5: Dada un area de investigacion contar ")
        print("6. Opción 6: Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.")
        print("7. Opción 7: Con una categoria ingresada por teclado listar apellido, nombre e importe extra, y mostrar Total")
        print("8. Opción 8: Almacenar los datos de todos los agentes en el archivo “personal.json”")
        print("0. Salir")
        opcion = input("Ingrese la opcion: ")
        if opcion =='1':
            Mod_Menu.opcion1(lista)
        elif opcion =='2':
            Mod_Menu.opcion2(lista)
        elif opcion == '3':
            Mod_Menu.opcion3(lista)
        elif opcion == '4':
            Mod_Menu.opcion4(lista)
        elif opcion == '5':
            Mod_Menu.opcion5(lista)
        elif opcion == '6':
            Mod_Menu.opcion6(lista)
        elif opcion == '7':
            Mod_Menu.opcion7(lista)
        elif opcion == '8':
            Mod_Menu.opcion8(lista)
        else:
            if (opcion == '0'):
                    Salir = False
                    Mod_Menu.salir()
            else:
                print ("Opcion invalida")
                Salir=False