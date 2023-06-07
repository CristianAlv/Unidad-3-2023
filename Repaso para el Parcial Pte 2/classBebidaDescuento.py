from claseBebida import Bebida
class BebidasinDesc(Bebida):
    def __init__(self, codigo, descripcion, tamaño, Retornable, precio):
        super().__init__(codigo, descripcion, tamaño, Retornable, precio)
        
    def gettipo(self):
        return "Bebida sin Descuento"
    
    def precioVenta(self):
        importe = super().getPrecio()
        if super().getRetornable() == True:
            importe += super().getPrecio() + (0.01 * super().getPrecio())
        return importe
        