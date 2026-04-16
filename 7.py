class Banco:
    def __init__(self, nombre, tasa_interes):
        self.nombre = nombre
        self.tasa_interes = tasa_interes

    def calcular_interes(self, capital, tiempo):
        return capital * self.tasa_interes * tiempo

    def calcular_monto_total(self, capital, tiempo):
        return capital + self.calcular_interes(capital, tiempo)

    def tiempo_duplicar(self):
        return 1 / self.tasa_interes

    def mostrar_info(self):
        print("Banco:", self.nombre)
        print("Tasa de interés:", self.tasa_interes)


if __name__ == "__main__":
    b = Banco("Banco Nación", 0.05)
    b.mostrar_info()
    print("Interés:", b.calcular_interes(1000, 2))
    print("Monto total:", b.calcular_monto_total(1000, 2))
    print("Tiempo para duplicar:", b.tiempo_duplicar())