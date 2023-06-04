from persona import persona
import csv
from manejaInscriptos import ManejadorInscripto
class ManejadorPersona():
    __lista_persona = list
    def __init__(self):
        self.__lista_persona = []
    
    def Cargar_Lista(self):
        dni= str(input("Ingrese el dni: "))
        nombre = str(input("Ingrese el nombre y apellido de la persona: "))
        direccion =str(input("Ingrese la direccion donde vive actualmente: "))
        persona1 = persona(nombre, direccion, dni)
        self.__lista_persona.append(persona1)
                        
    def mostrarlista(self):
        for i in range (len(self.__lista_persona)):
            print ("Nombre: {}, Direccion: {}" .format(self.__lista_persona[i].getNombre(), self.__lista_persona[i].getDireccion()))
            
    def getlista(self):
        return self.__lista_persona