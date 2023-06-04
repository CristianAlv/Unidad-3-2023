class sabor:
    Nro_Sabor = 0
    __id = int
    __ingredientes = str
    __nombre = str
    def __init__(self, iD, ingredientes, nombre):
        self.__id = iD
        self.__ingredientes = ingredientes
        self.__nombre = nombre
    

        
    def getIDsabor(self):
        return self.__id
    def getingredientes(self):
        return self.__ingredientes
    def getnombre(self):
        return self.__nombre
