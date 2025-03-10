class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario: ISBN -> Objeto Libro
        self.usuarios_registrados = set()  # Conjunto de IDs únicos de usuarios
        self.historial_prestamos = {}  # Diccionario: ID Usuario -> Libros prestados

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")
        else:
            print("El libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado con éxito.")
        else:
            print("El usuario ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} eliminado.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, isbn, usuario):
        if isbn in self.libros_disponibles and usuario.id_usuario in self.usuarios_registrados:
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("No se puede prestar el libro. Verifique que el libro y el usuario existan.")

    def devolver_libro(self, isbn, usuario):
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                return
        print("El usuario no tiene prestado este libro.")

    def buscar_libros(self, criterio, valor):
        resultados = [libro for libro in self.libros_disponibles.values() if getattr(libro, criterio) == valor]
        if resultados:
            print("Resultados de búsqueda:")
            for libro in resultados:
                print(f" - {libro.titulo} de {libro.autor} (Categoría: {libro.categoria})")
        else:
            print("No se encontraron libros con el criterio especificado.")

    def listar_libros_prestados(self, usuario):
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f" - {libro.titulo} de {libro.autor}")
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")

# Prueba del sistema
libro1 = Libro("1984", "George Orwell", "Ficción", "123456789")
libro2 = Libro("El Quijote", "Miguel de Cervantes", "Clásicos", "987654321")

usuario1 = Usuario("Javier", "USR001")

biblioteca = Biblioteca()

biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

biblioteca.registrar_usuario(usuario1)
biblioteca.prestar_libro("123456789", usuario1)

biblioteca.listar_libros_prestados(usuario1)
biblioteca.devolver_libro("123456789", usuario1)

biblioteca.buscar_libros("categoria", "Ficción")
