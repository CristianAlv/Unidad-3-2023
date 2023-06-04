from ClaseSabores import sabor
import csv
from collections import Counter
class ManejaSabores:
    def __init__(self):
        self.__sabores = []
        
    def Cargar(self):
        archivo = open("sabores.csv")
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            sabor1 = sabor(int(fila[0]), str(fila[1]), str(fila[2]))
            self.__sabores.append(sabor1)
        archivo.close()

    def get_sabores(self):
        return self.__sabores
    
    def mostrar_sabores(self):
        for i in range (len(self.__sabores)):
            print ("{}; {}; {}" .format(self.__sabores[i].getIDsabor(), self.__sabores[i].getingredientes(), self.__sabores[i].getnombre()))

    def buscar_helado(self, sabor):
        i=0
        band = False
        while i<len(self.__sabores) and band == False:
            if (sabor == self.__sabores[i].getIDsabor()):
                print("El sabor fue encontrado")
                band = True
            i+=1
           
        return band
    def get_sabor(self, pos):
        return self.__sabores[pos]
    
    def getlista(self):
        return len(self.__sabores)
