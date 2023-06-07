from claseBebida import Bebida
class BebidaconDesc(Bebida):
    __porcentaje = float
    def __init__(self, codigo, descripcion, tamaño, Retornable, precio, porcentaje):
        super().__init__(codigo, descripcion, tamaño, Retornable, precio)
        self.__porcentaje = porcentaje
        
    def getporcentaje(self):
        return self.__porcentaje
    
    def gettipo(self):
        return "Bebida con descuento"
    
    def setdescuento(self, descuento):
        self.__porcentaje = descuento
        
    def precioVenta(self):
        importe = super().getPrecio() - (super().getPrecio() * self.__porcentaje/100)
        if super().getRetornable() == True:
            importe += super().getPrecio() + (0.01 * super().getPrecio())
        return importe
        
        