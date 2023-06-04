from ManejadorHelado import ManejaHelados
from ManejadorSabores import ManejaSabores
from ClaseHelado import Helado
from ClaseSabores import sabor
from menu import Menu
def test():
    Ms = ManejaSabores()
    Ms.Cargar()
    Ms.mostrar_sabores()
    Mh = ManejaHelados()
Mod_Menu = Menu()
Salir = True
while Salir:
        print("Bienvenido al Menú")
        print("1. Opción 1: Registrar Pedido")
        print("2. Opción 2: Mostrar aquellos sabores mas pedidos")
        print("3. Opción 3: Gramos de un sabor:  ")
        print ("4. Opcion 4: Tamaño en gramos de los sabores vendidos")
        print ("5. Opcion 5: Tamaño en gramos de los sabores vendidos")
        print("0. Salir")
        opcion = input("Ingrese la opcion: ")
        if opcion =='1':
            Mod_Menu.opcion1()
        elif opcion =='2':
            Mod_Menu.opcion2()
        elif opcion == '3':
            Mod_Menu.opcion3()
        elif opcion == '4':
            Mod_Menu.opcion4() 
        elif opcion == '5':
            Mod_Menu.opcion5()    
        else:
            if (opcion == '0'):
                    Salir = False
                    Mod_Menu.salir()
            else:
                print ("Opcion invalida")
                Salir=False
    

if __name__ == '__main__':
    test()
    
    
