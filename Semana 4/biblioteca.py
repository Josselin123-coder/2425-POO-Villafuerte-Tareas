class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True  # Inicialmente, el libro está disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro '{self.titulo}' prestado.")
            return True
        else:
            print(f"Libro '{self.titulo}' no disponible.")
            return False

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"Libro '{self.titulo}' devuelto.")
        else:
            print(f"Libro '{self.titulo}' ya está disponible.")

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Disponibilidad: {'Disponible' if self.disponible else 'Prestado'}")


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha tomado prestado '{libro.titulo}'.")
        else:
            print(f"{self.nombre} no pudo tomar prestado '{libro.titulo}'.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
          libro.devolver()
          self.libros_prestados.remove(libro)
          print(f"{self.nombre} ha devuelto '{libro.titulo}'.")
        else:
          print(f"{self.nombre} no tiene prestado el libro '{libro.titulo}'.")

    def mostrar_libros_prestados(self):
        if self.libros_prestados:
            print(f"Libros prestados por {self.nombre}:")
            for libro in self.libros_prestados:
                libro.mostrar_info()
        else:
            print(f"{self.nombre} no tiene libros prestados.")


libro1 = Libro("El tiempo","Jorge","editarial_cajas")

libro1.prestar()
libro1.mostrar_info()
libro1.devolver()