import unittest
from claseDepto import Departamento
from claseCasa import Casa
from claseInmuebles import Inmueble
from claseLista import ListaEnlazada
from nodo import Nodo


class TestImporte(unittest.TestCase):
    def test_importeVenta(self):
        CasadeDonPete = Casa("San Martin 38 Este", "San Juan", 280, 200)
        self.assertEqual(CasadeDonPete.importeVenta(), 30240000000.0)
        print ("El resultado coincide")

if __name__ == '__main__':
    unittest.main()