from claseVehiculo import Vehiculo

class VehiculoCarga(Vehiculo):
    __Peso = float
    def __init__(self, marca, modelo, patente, importe, kilometraje, Peso):
        super().__init__(marca, modelo, patente, importe, kilometraje)
        self.__Peso = Peso
        
    def getPeso(self):
        return self.__Peso
    def getTipo(self):
        return "Vehiculo de Carga"
    def TotalImporte(self):
        importe = self.getimporte()
        if self.getkilometraje() > 100:
            importe += (0.05 * self.getimporte()) * (self.getkilometraje()/10)
        if self.getPeso() > 500:
            importe += (0.1 * self.getimporte()) * (self.getPeso()/100)
        return importe
    