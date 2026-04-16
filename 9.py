class Empleado:
    def __init__(self, nombre, edad, salario, cargo):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.cargo = cargo

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def calcular_salario_anual(self):
        return self.salario * 12

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Cargo:", self.cargo)
        print("Salario mensual:", self.salario)
        print("Salario anual:", self.calcular_salario_anual())


if __name__ == "__main__":
    emp = Empleado("Luis", 35, 1000, "Gerente")
    emp.mostrar_info()