import datetime

class Coche:
    def __init__(self, marca, modelo, año_fabricacion):
        """Inicializa las propiedades del coche."""
        self.marca = marca                # Establece la marca del coche
        self.modelo = modelo              # Establece el modelo del coche
        self.año_fabricacion = año_fabricacion  # Establece el año de fabricación

    def obtener_marca(self):
        """Devuelve la marca del coche."""
        return self.marca

    def establecer_marca(self, marca):
        """Establece una nueva marca para el coche."""
        self.marca = marca

    def obtener_modelo(self):
        """Devuelve el modelo del coche."""
        return self.modelo

    def establecer_modelo(self, modelo):
        """Establece un nuevo modelo para el coche."""
        self.modelo = modelo

    def obtener_año_fabricacion(self):
        """Devuelve el año de fabricación del coche."""
        return self.año_fabricacion

    def establecer_año_fabricacion(self, año_fabricacion):
        """Establece un nuevo año de fabricación para el coche."""
        self.año_fabricacion = año_fabricacion

    def calcular_edad(self):
        """Calcula el número de años que han pasado desde que se fabricó el coche."""
        # Obtenemos el año actual
        año_actual = datetime.datetime.now().year
        # Calculamos la diferencia entre el año actual y el año de fabricación
        return año_actual - self.año_fabricacion

# Ejemplo de uso de la clase Coche
if __name__ == "__main__":
    # Crear una instancia de Coche
    coche1 = Coche("Toyota", "Corolla", 2015)

    # Obtener y mostrar las propiedades
    print(f"Marca: {coche1.obtener_marca()}")
    print(f"Modelo: {coche1.obtener_modelo()}")
    print(f"Año de fabricación: {coche1.obtener_año_fabricacion()}")

    # Calcular y mostrar la edad del coche
    print(f"\nEl coche tiene {coche1.calcular_edad()} años de antigüedad.")