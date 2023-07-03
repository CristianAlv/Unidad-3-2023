from claseInmuebles import Inmueble
class Casa (Inmueble):
    __metros = int
    
    def __init__(self, direc, loc, sup, metros):
        super().__init__(direc, loc, sup)
        self.__metros = metros
        
    def getMetros(self):
        return self.__metros
    
    def precioConstruccion(self):
        return (self.__metros*1.80*20000)    