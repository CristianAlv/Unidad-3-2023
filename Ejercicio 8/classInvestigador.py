from classPersonal import Personal
class Investigador(Personal):
    def __init__(self, nombre, apellido, cuil, sueldoBasico, antig, carrera= '', cargo='', catedra= '', areaInv = '', tipoInv= ''):
        super().__init__(nombre, apellido, cuil, sueldoBasico, antig, carrera, cargo, catedra, areaInv, tipoInv)
        self.__area = areaInv
        self.__tipo = tipoInv
        
    def getarea(self):
        return self.__area
    def gettipo(self):
        return self.__tipo
    def tipoP(self):
        return "Investigador"
    def ImporteSueldo(self):
        sueldo = self.getsueldo() + (self.getsueldo() + (self.getantiguedad()/100))
        return sueldo
    
    def toJSON (self):
        d = dict (
            __class__ = self.__class__.__name__,
            __atributos__ = dict (
                nombre = self.getnombre(),          #puedo colocar:     super().getNombre(), metodo de la clase base
                apellido = self.getapellido(),
                cuil = self.getcuil(),
                sueldoBasico = self.getsueldo(),
                antig = self.getantiguedad(),
                areaInv = self.__area,
                tipoInv = self.__tipo
            )
        )
        return d