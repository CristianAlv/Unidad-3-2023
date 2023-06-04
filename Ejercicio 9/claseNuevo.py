from clasevehiculo import Vehiculo
import json
from pathlib import Path
class VehiculoNuevo(Vehiculo):
    marca = None
    __version = str
    def __init__(self, modelo, cantPuertas, color, precio, version): #Los atributos deben coincidir con los del archivo json
        super().__init__(modelo, cantPuertas, color, precio)
        self.__version = version
        
    def getversion(self):
        return self.__version
    @classmethod
    def setmarca(cls, marca):
        cls.marca = marca
        return cls.marca
        
    @classmethod
    def getmarca(cls):
        return cls.marca
    def obtenerVehiculo (self):
        return {self.getmodelo()},'' ,{VehiculoNuevo.getmarca()}
    def ImporteVenta(self):
        importe = self.getprecio() + self.getprecio()*0.10
        if self.__version == 'full':
            importe += self.getprecio()*0.02
        return importe
    
    def mostrar(self):
        super().mostrar()
        print ("Version: {}" .format(self.__version))
    
    
    def toJSON(self): 
        d = dict( __class__=
                            self.__class__.__name__, 
                    __atributos__ = dict (
                    modelo = self.getmodelo(),
                    cantPuertas = self.getcantP(),
                    color = self.getcolor(),
                    precio = self.getprecio(),
                    version = self.__version
                )
        )
        return d
