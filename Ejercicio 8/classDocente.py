from classPersonal import Personal

class Docente(Personal):
    def __init__(self, nombre, apellido, cuil, sueldoBasico, antig, carrera, cargo, catedra, areaInv='', tipoInv= ''):
        super().__init__(nombre, apellido, cuil, sueldoBasico, antig, carrera, cargo, catedra, areaInv, tipoInv)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
        
    def getcarrera(self):
        return self.__carrera
    def getcargo(self):
        return self.__cargo
    def getcatedra(self):
        return self.__catedra
    def tipoP(self):
        return "Docente"
    def ImporteSueldo(self):
        sueldo = self.getsueldo() + (self.getsueldo() + (self.getantiguedad()/100))
        if self.__cargo == 'simple':
            sueldo += (self.getsueldo() * 10)/100
        elif self.__cargo == 'semiexclusivo':
            sueldo += (self.getsueldo() * 20)/100
        elif self.__cargo == 'esclusivo':
            sueldo+= (self.getsueldo() *50)/100
        return sueldo
    def setPorcentaje(self, unPorcentaje):
        sueldo = self.getsueldo() + (self.getsueldo() + (self.getantiguedad()/100))
        if self.__cargo == 'simple':
            sueldo += (self.getsueldo() * unPorcentaje)/100
        elif self.__cargo == 'semiexclusivo':
            sueldo += (self.getsueldo() * unPorcentaje)/100
        elif self.__cargo == 'esclusivo':
            sueldo+= (self.getsueldo() *unPorcentaje)/100
        return sueldo
    
    def toJSON (self):
        d = dict (
            __class__ = self.__class__.__name__,
            __atributos__ = dict (
                nombre = self.getnombre(),              
                apellido = self.getapellido(),
                cuil = self.getcuil(),
                sueldoBasico = self.getsueldo(),
                antig = self.getantiguedad(),
                carrera = self.__carrera,
                cargo = self.__cargo,
                catedra = self.__catedra
            )
        )
        return d