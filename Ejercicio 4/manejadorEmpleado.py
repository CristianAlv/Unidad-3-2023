import csv
import numpy as np
from claseEmpleado import Empleado
from ClaseExterno import Externo
from Contratados import Contratado
from Planta import Planta

class ManejadorEmpleado:
    __dimension = int
    __cantidad = int
    __incremento = 0
    def __init__(self, dimension, incremento):
        self.__dimension = dimension
        self.__incremento = incremento
        self.__cantidad = 0
        self.__empleados = np.empty(self.__dimension, dtype=Empleado)
        
    
    def Agregar_Empleado(self, empleado):
        if isinstance(empleado, Empleado):
                self.__dimension += self.__incremento
                self.__empleados.resize(self.__dimension)
                self.__empleados[self.__cantidad] = empleado
                self.__cantidad += 1
        
                
    def CargarContratados(self):
        archivo = open("contratados.csv", encoding='UTF-8')
        reader = csv.reader(archivo, delimiter = ';')
        cabecera = True
        for fila in reader:
            if cabecera:
                cabecera = False
            else:
                contratados = Contratado(int(fila[1]), fila[0], fila[2], fila[3], fila[4], fila[5], int(fila[6]))
                self.Agregar_Empleado(contratados)
        archivo.close()
        
                
    def CargarPlanta(self):
        archivo2 = open("planta.csv", encoding='UTF-8')
        reader = csv.reader (archivo2, delimiter = ';')
        cabecera = True
        for fila in reader: 
            if cabecera:
                cabecera = not cabecera
            else:
                Planta1 = Planta(int(fila[1]), fila[0],fila[2], fila[3], float(fila[4]), int(fila[5]))
                self.Agregar_Empleado(Planta1)
        archivo2.close()
        
    def CargarExterno(self):
        archivo3 = open("externos.csv", encoding='UTF-8')
        reader = csv.reader (archivo3, delimiter = ';')
        cabecera = True
        for fila in reader: 
            if cabecera:
                cabecera = not cabecera
            else:
                Externo1 = Externo(int(fila[1]), fila[0], fila[2], fila[3], fila[4], fila[5], fila[6], float(fila[7]), float(fila[8]), float(fila[9]))
                self.Agregar_Empleado(Externo1)
        archivo3.close()
        
    def mostrarEmpleados (self):
        print("----Mostramos el listado de Empledos----\n")
        for i in range(self.__cantidad):
            self.__empleados[i].mostrar()
            
    #apartado 1
    def buscar (self, doc, canth):
        band = False
        i = 0
        while (i < (self.__cantidad) and band == False):
            if (self.__empleados[i].getdni() == doc):
                if isinstance(self.__empleados[i], Contratado):        
                    band = True
                    self.__empleados[i].setCantHoras(canth)
                    print("{:+^50}". format(""))
                    print("La persona {} incremento sus horas de trabajo".format(self.__empleados[i].getnombre()))
                    print("{:=^34}".format(""))
                else:
                    print("La persona ingresada no es un empleado de tipo Contratado\n")
            i += 1
    #apartado 2    
    def monto(self, fecha, tarea):
        band = False
        acum=0
        for i in range (len(self.__empleados)):
            if isinstance(self.__empleados[i], Externo):
                    if (self.__empleados[i].gettarea() == tarea):
                        print("Tarea encontrada")
                        band=True
                        
                        if (self.__empleados[i].getfechaF() > fecha):
                            acum += self.__empleados[i].getsueldo()
                            if acum < 0:
                                print("La tarea ya fue terminada")
                            else:
                                print("{:/^60}".format(""))
                                print ("La tarea {}, ha sido finalizada con un monto total de {:.2f}" .format(tarea, acum))
                                print("{:/^60}".format(""))
                    
    #apartado 3
    def ayuda(self):
        ayuda = 150000
        for i in range (self.__dimension):
            if isinstance(self.__empleados[i], Empleado):
                if (self.__empleados[i].getsueldo() < 150000):
                    solidaridad = self.__empleados[i].getsueldo() + ayuda
                    self.__empleados[i].setsueldo(solidaridad)
                    print("{:-^100}".format(""))
                    print ("Se le brindo ayuda al empleado con Nombre: {}, Dni: {} y Direccion: {}" .format(self.__empleados[i].getnombre(), self.__empleados[i].getdni(), self.__empleados[i].getdireccion()))
