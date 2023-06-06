from claseVehiculo import Vehiculo

class VehiculoTransporte(Vehiculo):
    __cantasientos = int
    def __init__(self, marca, modelo, patente, importe, kilometraje, cantasientos):
        super().__init__(marca, modelo, patente, importe, kilometraje)
        self.__cantasientos = cantasientos
        
    def getcantidadA(self):
        return self.__cantasientos
    def getTipo(self):
        return "Vehiculo de Transporte"
    def TotalImporte(self):
        importe = self.getimporte()
        if self.getkilometraje() > 100:
            importe += (0.01 * self.getimporte()) * (self.getkilometraje()/10)
        if self.getcantidadA() > 4:
            importe += (0.01 * self.getimporte())
        return importe
    