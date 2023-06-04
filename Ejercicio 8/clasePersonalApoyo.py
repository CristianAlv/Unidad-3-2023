from classPersonal import Personal

class PersonalApoyo(Personal):
    def __init__(self, nombre, apellido, cuil, sueldoBasico, antig, carrera= '', cargo= '', catedra= '', areaInv= '', tipoInv= '', categoria= 0):
        super().__init__(nombre, apellido, cuil, sueldoBasico, antig, carrera, cargo, catedra, areaInv, tipoInv)
        self.__categoria = categoria
        
        
    def getcategoria(self):
        return self.__categoria
    def tipoP(self):
        return "Personal de Apoyo"
    
    def ImporteSueldo(self):
        sueldo = self.getsueldo() + (self.getsueldo() + (self.getantiguedad()/100))
        if self.__categoria >= 1 or self.__categoria <= 10:
            sueldo += (self.getsueldo() * 10)/100
        elif self.__categoria >= 11 or self.__categoria <= 20:
            sueldo += (self.getsueldo() * 20)/100
        elif self.__categoria == 21 or self.__categoria == 22:
            sueldo+= (self.getsueldo() *30)/100
        return sueldo
    def setCategoria(self, categoria):
        sueldo = self.getsueldo() + (self.getsueldo() + (self.getantiguedad()/100))
        if self.__categoria >= 1 or self.__categoria <= 10:
            sueldo += (self.getsueldo() * categoria)/100
        elif self.__categoria >= 11 or self.__categoria <= 20:
            sueldo += (self.getsueldo() * categoria)/100
        elif self.__categoria == 21 or self.__categoria == 22:
            sueldo+= (self.getsueldo() *categoria)/100
        return sueldo
    
    
    def toJSON(self):
        d = dict(__clase__ = self.__class__.__name__,
                 __atributos__ = dict(
                 cuil = self.getcuil(),
                 apellido = self.getapellido(),
                 nombre = self.getnombre(),
                 sueldo = self.getsueldo(),
                 antiguedad = self.getantiguedad(),
                 categoria = self.__categoria
                 )
                )
        return d