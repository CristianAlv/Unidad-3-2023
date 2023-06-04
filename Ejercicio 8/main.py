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
    Logeo = False
    usuarioTesorero = 'uTesoreso'
    contraseñaT = 'ag@74ck'
    ususarioDirector = 'uDirector'
    contraseñaD = 'ufC77#!1'
    nombre = str(input("Ingrese el nombre de usuario: "))
    password = str(input("Ingrese la contraseña: "))
    if nombre == ususarioDirector and password == contraseñaD:
        print ("Bienvenido Director")
        Logeo = True
    elif nombre == usuarioTesorero and password == contraseñaT:
        print ("Bienvenido Tesorero ")
        Logeo = True
    else: 
        print ("Ingrese nuevamente porque los datos son erroneos")
    
    if Logeo == True:
        while Salir:
            if Logeo == True and nombre == usuarioTesorero:
                print("1. Opción 1: dado un número de documento, podrá consultar el gasto de sueldos para el agente al que pertenece dicho número de documento")
                print("0. Salir")
                opcion = input("Ingrese la opcion: ")
            elif Logeo == True and nombre == ususarioDirector:
                print("10.1. Opción 10.1: Con un numero de dni, cambiar el sueldo basico: ")
                print("10.2. Opción 10.2: Con numero de dni, modificamos porcentaje o importe extra, dependiendo del respectivo cargo: ")
                print("0. Salir")
                opcion = input("Ingrese la opcion: ")
            
            if opcion == '1':
                    Mod_Menu.opcion9(lista)
            elif opcion == '10.1':
                    Mod_Menu.opcion10(lista)
            elif opcion == '10.2':
                    Mod_Menu.opcion11(lista)
            else:
                if (opcion == '0'):
                        Salir = False
                        Mod_Menu.salir()
                else:
                    print ("Opcion invalida")
                    Salir=False