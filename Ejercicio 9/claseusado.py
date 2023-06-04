from clasevehiculo import Vehiculo
from datetime import date

class VehiculoUsado(Vehiculo): #En python no es necesario declarar tipo 
    def __init__(self, modelo, cantPuertas, color, precio, marca, patente, año, kilometraje):
        super().__init__(modelo, cantPuertas, color, precio)
        self.__Marca = marca
        self.__patente = patente
        self.__año = año
        self.__kilometraje = kilometraje

    
    def getpatente(self):
        return self.__patente
    def getaño(self):
        return self.__año
    def getkilometraje(self):
        return self.__kilometraje
    def getmarca(self):
        return self.__Marca
    def obtenerVehiculo (self):
        return {self.getmodelo()}, '',{self.getmarca()}
    
    def ImporteVenta(self):
        fecha = str(date.today())
        i = fecha.find('-')
        año_actual = int(fecha[:i])
        importe = self.getprecio() -(0.01 *(año_actual-self.__año))
        if self.__kilometraje > 100000:
            importe -= 0.02 * self.__kilometraje
        return importe
    
        return importe
    def mostrar(self):
        super().mostrar()
        print ("Marca: {}, Patente: {}, Año: {}, Kilometraje: {}" .format(self.__Marca, self.__patente, self.__año, self.__año, self.__kilometraje))
    

    def toJSON(self): 
        d = dict( __class__=
                            self.__class__.__name__, 
                 __atributos__ = dict (
                    modelo = self.getmodelo(),
                    cantPuertas = self.getcantP(),
                    color = self.getcolor(),
                    precio = self.getprecio(),
                    marca = self.__Marca,
                    patente = self.__patente,
                    año = self.__año,
                    kilometraje = self.__kilometraje
            )
        )
        
        return d