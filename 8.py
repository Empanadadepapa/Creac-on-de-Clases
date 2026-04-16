class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos.remove(producto)

    def obtener_productos(self):
        return self.productos

    def mostrar_info(self):
        print("Tienda:", self.nombre)
        print("Productos:", self.productos)


if __name__ == "__main__":
    t = Tienda("Mi Tienda")
    t.agregar_producto("Pan")
    t.agregar_producto("Leche")
    t.agregar_producto("Queso")
    t.mostrar_info()
    t.eliminar_producto("Pan")
    print("\nDespués de eliminar:")
    t.mostrar_info()