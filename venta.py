from datetime import datetime
class Venta:
    def __init__(self, cliente):
        self.cliente = cliente
        self.producto = []
        self.precio = []
    
    def menu(self):
        opciones = """
        ****************MENU SUPERMERCADO****************
        1.- Agregar al Carrito
        2.- Mostrar Carrito
        3.- Total a Pagar
        4.- Salir
        """
        print(opciones)

        eleccion = int(input("Elija una Opcion: \n"))
        if (eleccion == 1):
            print(self.agregarCarrito())
            self.menu()
        elif (eleccion == 2):
            print(self.mostrarCarrito())
            self.menu()
        elif (eleccion == 3):
            print("{}".format(self.totalPagarSum()))
            self.menu()
        elif (eleccion == 4):
            print("Fin de la Transaccion")
        else:
            print("Elija una opcion del Menu!!")
            self.menu()
    
    def mostrarCarrito(self):
        if self.producto:
            print("**********************DETALLE DE VENTA**********************")
            print("***************LISTA DE PRODUCTOS DEL CARRITO***************")
            print("CLIENTE: {}".format(self.cliente))
            print("FECHA: {}".format(datetime.now()))
            print("--PRODUCTO--      --PRECIO--")
            i = 0
            while i < len(self.producto):
                print("{}          {} Bs.".format(self.producto[i], self.precio[i]))
                i += 1
            print("---EL TOTAL A PAGAR ES: {} Bs.---".format(self.totalPagarSum()))
        else:
            print("{} NO AGREGO PRODUCTO AL CARRITO!!".format(self.cliente))

    def totalPagar(self):
        total = sum(self.precio)
        totals = str(total)
        print("{}".format(totals))
    
    def totalPagarSum(self):
        return sum(self.precio)

    def agregarCarrito(self):
        producto = input("Ingresar Producto: \n")
        precio = int(input("Ingresar Precio: \n"))
        print(self.guardarCarrito(producto, precio))
        agregarOtro = input("Desea agregar mas  Productos al Carrito? y/n: \n")
        if (agregarOtro == "y"):
            self.agregarCarrito()
        return "Productos agregados al Carrito"

    def guardarCarrito(self, producto, precio):
        self.producto.append(producto)
        self.precio.append(precio)
        return "Producto {} Agregado Correctamente".format(self.producto)

pedro = Venta("Pedro Perez")

pedro.menu()
