from ClaseHelado import Helado
class ManejaHelados:
    def __init__(self):
        self.__helados_vendidos = []

    def agregar_helado(self, helado):
        self.__helados_vendidos.append(helado)

    def obtener_helados_vendidos(self):
        return self.__helados_vendidos
    
    def mostrarVendidos(self):
        
        for i in range(len(self.__helados_vendidos)):
            helado = self.__helados_vendidos[i]
            print ("Gramos: {}, Precio: {}, Sabores: {}" .format(helado.getgramos(), helado.getprecio(), helado.getsabores()))
    
    def getsaboresvendidos(self):
        helado = []
        for i in range (len(self.__helados_vendidos)):
            helado = self.__helados_vendidos[i]
        return helado.getsabores()
    
    def gestionarpedido(self, lista_Sabores):
        i=0
        sabores_encontrados = []
        gramos = float(input("Ingrese la cantidad de gramos a comprar: (100gr, 150 gr, 250 gr, 500 gr y 1000gr): "))
        if (gramos == 100):
            precio = 1200
        elif (gramos == 150):
            precio = 1500
        elif (gramos == 250):
            precio = 2100
        elif(gramos == 500):
            precio = 2500
        elif (gramos == 1000):
            precio = 3000
        sabores = int(input("Ingrese un id del sabor: "))
        
        while sabores != 0 and i<4:
            helados = lista_Sabores.buscar_helado(sabores)
            if (helados == True):
                    unSabor = lista_Sabores.get_sabor(sabores-1)
                    sabores_encontrados.append(unSabor)
                    helado1 = Helado(gramos, precio, sabores_encontrados)
                    
            sabores = int(input("Ingrese un id del sabor: "))
            i+=1
        
        return helado1
    
    def contar(self, Cantidad_sabores):
        aux = [0 for i in range(Cantidad_sabores)]
        for vendidos in self.__helados_vendidos:
            for sabor in vendidos.getsabores():
                aux [sabor.getIDsabor()-1] += 1

        # aux.sort(reverse=True)                      para ordenar de mayor a menor
        # aux.sort()                                   para ordenar de menor a mayor
        #ordenar por metodo de seleccion            metodo con max
        return aux

    
    def vendidos(self, Cantidad_sabores):
        top5 = []
        pedidos = self.contar(Cantidad_sabores)
        print (pedidos)
        for i in range (5):
            maximo = 0
            pos = 0
            for j in range (len(pedidos)):
                if pedidos[j] > maximo:
                    maximo = pedidos[j]
                    pos = j
            pedidos[pos]= 0
            top5.append(pos)
                
        return top5
    
    def mostrar_vendidos (self, manejadorS):
        top5 = self.vendidos(len(manejadorS.obtener_sabores()))
        print (top5)
        sabores = manejadorS.obtener_sabores()
        print("Los sabores mas vendidos son: ")
        for direccion in top5:
            print (sabores[direccion].getnombre())
    
    def recorrer(self, codigo):
        gramos = 0
        for helado in self.obtener_helados_vendidos():
            for sabor in helado.getsabores():
                if(codigo == sabor.getIDsabor()):
                    gramos += helado.getgramos()/len(helado.getsabores())
                    
        print ("El sabor con id: {}, se pidio {} g" .format(codigo,gramos))
        
    def tamano (self, helado, ms):
        sabores = len(ms.get_sabores())
        cont = [0 for i in range(sabores)]
        for helados in  self.obtener_helados_vendidos():
            if (helados.getgramos() == helado):
                for sabor in helados.getsabores():
                    cont[sabor.getIDsabor()-1]+=1
        
        return cont
    def mostrar_tamaño(self, aux, helado, manejadorS):
        sabores = manejadorS.get_sabores()
        print ("Los sabores vendidos en el tamaño {} g" .format(helado))
        print (sabores)
        print(aux)
        for i in range (len(sabores)):
            if aux[i] > 0:
                print (sabores[i].getnombre())
                
    def calculartotal(self):
        total=[0.0 for i in range(5)]
        for helados in (self.__helados_vendidos):
            tipo = helados.getgramos()
            if(tipo== 100):
                total[0] += helados.getprecio()
                
            if(tipo== 150):
                total[1] += helados.getprecio()
            
            if(tipo== 250):
                total[2] += helados.getprecio()
                
            if(tipo== 500):
                total[3] += helados.getprecio()
            
            if(tipo== 500):
                total[4] += helados.getprecio()
                
                
        return total
                
                
            
    def mostrartotal(self, manejadorS):
        print ("El total acumulado por la heladeria es:")
        total= self.calculartotal()
        for i in range(5):
                print(" Total: {}" .format(total[i]))