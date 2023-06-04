from classPersonal import Personal
from classDocente import Docente
from classDocenteInvestigador import DocenteInvestigador
from classInvestigador import Investigador
from clasePersonalApoyo import PersonalApoyo
import json
from claseLista import ListaPersonalUniv

class ObjectEncoderP:
    def guardarArchJSON (self, dicc, archivo):
        with open(archivo, 'w', encoding='UTF-8') as destino:
            json.dump(dicc, destino, indent=4)
            destino.close()
    
    def leerArchivoJSON (self, archivo):
        with open(archivo, 'r', encoding='UTF-8') as fuente:
            dicc = json.load(fuente)
            fuente.close()
            return dicc
    def decodificarDicc(self, dicc):
        if "__class__" not in dicc:
            return dicc
        else:
            class_name = dicc["__class__"]
            class_ = eval(class_name)
            if class_name == "ListaPersonalUniv":
                personas = dicc["personal"]
                manejador = class_()
                for i in range(len(personas)):
                    dPers = personas[i]
                    class_name = dPers.pop("__class__")
                    class_ = eval(class_name)
                    atributos = dPers["__atributos__"]
                    unPersonal = class_(**atributos)
                    manejador.agregarElemento(unPersonal)

                return manejador