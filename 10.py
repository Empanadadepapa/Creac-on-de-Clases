class Libro:
    def __init__(self, titulo, autor, genero, paginas):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.paginas = paginas

    def obtener_titulo(self):
        return self.titulo

    def establecer_titulo(self, titulo):
        self.titulo = titulo

    def es_ficcion(self):
        return self.genero == "ficcion"

    def mostrar_info(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Género:", self.genero)
        print("Páginas:", self.paginas)
        print("Es ficción:", self.es_ficcion())


if __name__ == "__main__":
    l = Libro("1984", "Orwell", "ficcion", 300)
    l.mostrar_info()