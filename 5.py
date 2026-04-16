class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.diametro = radio * 2

    def obtener_radio(self):
        return self.radio

    def establecer_radio(self, radio):
        self.radio = radio
        self.diametro = radio * 2

    def calcular_area(self):
        pi = 3.1416
        return pi * (self.radio ** 2)

    def calcular_circunferencia(self):
        pi = 3.1416
        return 2 * pi * self.radio

    def mostrar_info(self):
        print("Radio:", self.radio)
        print("Diámetro:", self.diametro)
        print("Área:", self.calcular_area())
        print("Circunferencia:", self.calcular_circunferencia())


if __name__ == "__main__":
    c = Circulo(5)

    print(" datos iniciales ")
    c.mostrar_info()

    c.establecer_radio(7)

    print("\n datos actualizados ")
    c.mostrar_info()