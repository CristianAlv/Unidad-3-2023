from classPersonal import Personal
from classDocente import Docente
from classDocenteInvestigador import DocenteInvestigador
from classInvestigador import Investigador
from clasePersonalApoyo import PersonalApoyo
from claseInterface import IElemento
from zope.interface import Interface, implementer
from claseNodo import Nodo
from claseLista import ListaPersonalUniv
import json
from claseObjectEncoderP import ObjectEncoderP

@implementer(IElemento)
class Menu(object):
    __switcher = None
    __JSONfile = None
    __MarcaNuevo = None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.opcion5,
            '6':self.opcion6,
            '7':self.opcion7,
            '8':self.opcion8,
            '0':self.salir
        }
        self.__JSONfile = ObjectEncoderP()

    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self, op, lista):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(lista)
    
    def salir(self):
        print ("Terminando ejecucion del programa....")
    
    def NuevoAgente(self):
        agente = None
        carga = ("Que tipo de carga desea: 1: Automatica o 2: Manual")
        tipo = str(input("Ingrese el tipo de agente a insertar: "))
        nombre = str(input("Ingrese el nombre:"))
        apellido = str(input("Ingrese el apellido: "))
        cuil = str(input("Ingrese el cuil: "))
        sueldoBasico = str(input("Ingrese el sueldo: "))
        antig = int(input("Ingrese sus años de experiencia: "))

        if tipo == 'Docente':
                carrera = str(input("Ingrese la carrera: "))
                cargo = str(input("Ingrese su cargo: "))
                catedra = str(input("Ingrese en la catedra donde participa: "))
                agente = Docente(nombre, apellido, cuil, sueldoBasico, antig, carrera, cargo, catedra)
        if tipo == 'Personal de Apoyo':
                categoria = str(input("Ingrese la categoria: "))
                agente = PersonalApoyo(nombre, apellido, cuil, sueldoBasico, antig, categoria)
        if tipo == 'Investigador':
                area = str(input("Ingrese el area de investigacion: "))
                tipoInv = str(input("Ingrese el tipo de investigacion que realiza: "))
                agente = Investigador(cuil, apellido, nombre, sueldoBasico, antig, area, tipoInv)
        if tipo == 'Docente Investigador':
                carrera = str(input("Ingrese la carrera: "))
                cargo = str(input("Ingrese su cargo: "))
                catedra = str(input("Ingrese en la catedra donde participa: "))
                area = str(input("Ingrese el area de investigacion: "))
                tipoInv = str(input("Ingrese el tipo de investigacion que realiza: "))
                CategoriaI = str(input("Ingrese la categoria de investigacion: "))
                Extra = float(input("Ingrese el importe extra a recibir: "))
                agente = DocenteInvestigador(nombre, apellido, cuil, sueldoBasico, antig, carrera, cargo, catedra, area, tipoInv, CategoriaI, Extra)
            
                
        return agente
    
    def opcion1(self, lista):
        carga = int(input("Ingrese el tipo de carga a realizar: 1: Automatica o 2: Manual "))
        if carga == 2:
            Agente = self.NuevoAgente()
            posicion = int(input("Ingrese la posicion donde desea insertar: "))
            if Agente != None:
                lista.insertarElemento(posicion, Agente)
                print("Agente insertado correctamente")
            else:
                print("Agente no existente, intentelo nuevamente")
        if carga == 1:
            unAgente = Investigador('Rodrigo', 'Perez', '25-3756232-3', 30001.3, 5, 'Tecno', 'OS')
            posicion = int(input("Ingrese la posicion donde desea insertar: "))
            lista.insertarElemento(posicion, unAgente)
            
            
            
        
    def opcion2(self, lista):
        print("Opcion 1 elegida")
        carga = int(input("Desea realizar la carga: 1:si o 0:no "))
        if carga == 1:
            Agente = self.NuevoAgente()
            posicion = int(input("Ingrese la posicion donde desea insertar: "))
            if Agente != None:
                lista.agregarelemento(Agente)
                print("Agente agregado correctamente")
            else:
                print("Agente no existente, intentelo nuevamente")
        else:
            Agente = DocenteInvestigador ('Javier', 'Rodriguez', '20-19472384-6', 57210.4, 6, 'Cientifica', 'IA', 'LCC', 'semiexclusivo', 'POO', 'II', 2334.2)
            lista.agregarElemento(Agente)
            print("Agente agregado correctamente")
        
    def opcion3 (self, lista):
        posicion = int(input("Ingrese la posicion del elemento a buscar: "))
        lista.mostrarElemento(posicion)
        
    def opcion4(self,lista):
        lista.listarCarreras()
        carrera = str(input("Ingrese la carrera en donde se desempeña el agente: "))
        lista.ordenar(carrera)
        

    def opcion5(self, lista):
        lista.mostrararea()
        area = str(input("Ingrese el area: "))
        lista.contar(area)
        
    def opcion6(self,lista):
        lista.OrdenarLista()
        
    def opcion7(self, lista):
        categoriaInv = str(input("Ingrese una categoria de investigacion: (I, II, III, IV o V): "))
        lista.Indicar(categoriaInv)
        
    def opcion8(self, lista):
        diccionario = lista.toJSON()
        print (diccionario)
        if diccionario != None:
            self.__JSONfile.guardarArchJSON(diccionario, "personal.json")
            print("Archivo Guardado Correctamente")
    def opcion9(self, lista):
        dni = str(input("Ingrese el dni:  "))
        lista.gastosSueldoPorEmpleado(dni)
    def opcion10(self, lista):
        dni = str(input("Ingrese el dni:  "))
        lista.modificarSueldoBasico(dni)
    def opcion11(self, lista):
        dni = str(input("Ingrese el dni:  "))
        lista.modificarcondni(dni)
        
    
    