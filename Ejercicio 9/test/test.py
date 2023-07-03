import unittest


class TestNumeros(unittest.TestCase):
    def test_numeros(self):
        numero1 = 8
        numero2 = 16
        self.assertEqual(numero1,numero2)
        print ("Los numeros son iguales")


if __name__ == '__main__':
    unittest.main()