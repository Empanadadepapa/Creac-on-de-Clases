class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.notas = []

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Carrera:", self.carrera)
        print("Notas:", self.notas)
        print("Promedio:", self.calcular_promedio())


if __name__ == "__main__":
    e = Estudiante("Ana", 20, "Ingeniería")
    e.agregar_nota(8)
    e.agregar_nota(7)
    e.agregar_nota(9)
    e.mostrar_info()