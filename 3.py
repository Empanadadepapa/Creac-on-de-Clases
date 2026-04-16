class Producto:
    def __init__(self, nombre, precio, stock):
        """Inicializa las propiedades del producto."""
        self.nombre = nombre  # Establece el nombre del producto
        self.precio = precio  # Establece el precio del producto
        self.stock = stock    # Establece el stock disponible del producto

    def obtener_nombre(self):
        """Devuelve el nombre del producto."""
        return self.nombre

    def establecer_nombre(self, nombre):
        """Establece un nuevo nombre para el producto."""
        self.nombre = nombre

    def obtener_precio(self):
        """Devuelve el precio del producto."""
        return self.precio

    def establecer_precio(self, precio):
        """Establece un nuevo precio para el producto."""
        self.precio = precio

    def obtener_stock(self):
        """Devuelve el stock disponible del producto."""
        return self.stock

    def establecer_stock(self, stock):
        """Establece un nuevo stock disponible para el producto."""
        self.stock = stock

    def aumentar_stock(self, cantidad):
        """Aumenta el stock disponible en una cantidad específica."""
        self.stock += cantidad
        print(f"Se ha aumentado el stock en {cantidad} unidades.")

    def disminuir_stock(self, cantidad):
        """Disminuye el stock disponible en una cantidad específica, si hay suficiente stock."""
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Se ha disminuido el stock en {cantidad} unidades.")
        else:
            print("No hay suficiente stock para realizar la operación.")

# Ejemplo de uso de la clase Producto
if __name__ == "__main__":
    # Crear una instancia de Producto
    producto1 = Producto("Laptop", 1000.00, 50)

    # Mostrar las propiedades del producto
    print(f"Nombre: {producto1.obtener_nombre()}")
    print(f"Precio: ${producto1.obtener_precio()}")
    print(f"Stock disponible: {producto1.obtener_stock()} unidades")

    # Aumentar y disminuir el stock
    producto1.aumentar_stock(20)  # Aumentamos el stock en 20 unidades
    producto1.disminuir_stock(10)  # Disminuimos el stock en 10 unidades

    # Mostrar las propiedades después de los cambios
    print("\nDespués de actualizar el stock:")
    print(f"Stock disponible: {producto1.obtener_stock()} unidades")