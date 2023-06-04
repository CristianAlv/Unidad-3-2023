from ClaseSabores import sabor
class Helado():
    __gramos = float
    __precio = float
    __sabores = list
    def __init__(self, gramos, precio, sabores):
        self.__gramos = gramos
        self.__precio = precio
        self.__sabores = sabores

        
    def getgramos(self):
        return self.__gramos
    def getprecio(self):
        return self.__precio
    def getsabores(self):
        return self.__sabores
    