class Producto:  #Creamos nuestra clase producto
    def __init__(self, id_producto, nombre, cantidad, precio):  #Creamos nuestro constructor y agregamos los atriubutos que se va a inicializar
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):  #Definimos el metodo get para visualizar
        return self.id_producto

    def get_nombre(self): #Definimos el metodo get para visualizar
        return self.nombre

    def get_cantidad(self): #Definimos el metodo get para visualizar
        return self.cantidad

    def get_precio(self): #Definimos el metodo get para visualizar
        return self.precio

    def set_cantidad(self, cantidad): #Creamos el metodo set
        self.cantidad = cantidad

    def set_precio(self, precio): #Creamos el metodo set
        self.precio = precio

#Creamos nuestra clase de inventario

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_productos()

    def cargar_productos(self):
        """Carga los productos desde el archivo al iniciar"""
        try:  #Utilizamos try para manejar excepciones
            with open(self.archivo, 'r') as f:  #Abrimos  el archivo cuyo nombre está almacenado en self.archivo en modo lectura ('r')
                lineas = f.readlines() #Nos permite leer todas las líneas del archivo y se almacenan en la lista lineas.
                for linea in lineas: #Creamos un bucle que recorre cada línea en la lista lineas
                    if linea.strip():  # Ignora líneas vacías
                        datos = linea.strip().split(',')  #Utilizamos strip() para eliminar espacios en blanco al inicio y al final de la línea.
                        producto = Producto(datos[0], datos[1], int(datos[2]), float(datos[3]))  # Creamos  una instancia de la clase Producto utilizando los datos extraídos.
                        self.productos.append(producto)  # El objeto producto se agrega a la lista self.productos
            print(f"Se cargaron {len(self.productos)} productos del archivo.")  #Imprimimos un mensaje indicando cuántos productos se han cargado desde el archivo.
        except FileNotFoundError:  # Capturamos  la excepción FileNotFoundError, que ocurre si el archivo no se encuentra.
            print("Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")  #Imprimimos un mensaje informando que el archivo no fue encontrado
        except PermissionError:  # Capturamos la excepción PermissionError, que ocurre si no hay permisos para leer el archivo.
            print(f"Error: No hay permiso para leer el archivo {self.archivo}")
        except Exception as e:  #Capturamos cualquier otra excepción que no haya sido manejada previamente.
            print(f"Error al cargar el archivo: {str(e)}")

    def guardar_productos(self):
        #Guarda los productos en el archivo
        try:
            with open(self.archivo, 'w') as f:  # Abrimos el archivo en modo escritura ('w'). Si el archivo ya existe, se sobrescribirá
                for p in self.productos:  #Iniciamos un bucle que recorre cada producto en la lista self.productos.
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")  #Escribimos una línea en el archivo para cada producto, utilizando los métodos get
            return True  #Si se completa la escritura sin errores, se devuelve True.
        except Exception as e:  #Capturamos cualquier excepción que pueda ocurrir durante la escritura.
            print(f"Error al guardar en el archivo: {str(e)}")  #Imprimimos un mensaje con la descripción del error.
            return False  #Si ocurre un error, se devuelve False.


    #Creamos un metodo para añadir el producto
    def añadir_producto(self, producto):
         for p in self.productos:  #Con un for vamos a iterar sobre la lista de productos
            if p.get_id() == producto.get_id():  #Con una condicional si el id del prodcuto es igual al prodcuto que ingresamos
                print("Error: El ID ya existe.")  #Vamos a colocafr un print con un mensaje que ya existe el producto
                return
         self.productos.append(producto)  # Sino entra al if, agregaremos a nuestra lista de prodcutos el nuevo prodcuto ingresado
         print("Producto añadido exitosamente.")  #Mostramos un mensaje

    #Creamos un metodo para eliminar el producto
    def eliminar_producto(self, id_producto):
        # Eliminar el producto si el ID coincide
        for p in self.productos:  #Iteramos sobre nuestra lista de productos
            if p.get_id() == id_producto:
                self.productos.remove(p)  #Eliminamos el producto con remove
                print("Producto eliminado exitosamente.")  #Enviamos un mensaje de que se elimino el prodcuto exitosamente
                return
        print("Error: Producto no encontrado.")  #Nos aseguramos con un mensaje que si no hay, no se encontro el producto


    #Ahora cremoas un metodo para actualizar
    def actualizar_producto(self, id_producto, cantidad=None, precio=None): #Creamos el constructor y colocamos atriubutos que sean igual a none
        for p in self.productos:  #Iteramos sobre la lista
            if p.get_id() == id_producto:
                if cantidad is not None:  #Si la cantidad no es none
                    p.set_cantidad(cantidad)  #Llamamos al metodo set y podemos actualizar la nueva cantidad proporcionada
                if precio is not None: #Si la cantidad no es none
                    p.set_precio(precio) #Establece el precio del producto al nuevo precio proporcionado
                print("Producto actualizado exitosamente.")  #Enviamos un mensaje que el producto fue exitosamente actualizado
                return
        print("Error: Producto no encontrado.")

    #Cremos un metodo para buscar el producto

    def buscar_producto(self, nombre):
        resultados = [] #Los resultados vamos a guardar en una lista
        for p in self.productos:  #Iteramos sobre los productos
            if nombre.lower() in p.get_nombre().lower():  #Verifcamos si el nombre en minuscula esta contenido en el nombre del producto
                resultados.append(p)  #Si se cumple el  producto p se añade a la lista resultados.
        return resultados # retornamos la lista resultados que contiene todos los productos

    #Creamos un metodo para mostrar los productos
    def mostrar_productos(self):
        if len(self.productos) == 0:  #Si la longitud de prodcutos en igual a cero
            print("No hay productos en el inventario.") #Enviamos un mensake que no existe prodcutos
        else: #Sino
            for p in self.productos: #Iteramos la lista de prodcutos
                print(
                    f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")  #Imprimimos los prodcutos con los atributos

#Creamos una funcion para el menu
def menu():
        inventario = Inventario()
        while True:  #Creamos un bucle while y colocamos opciones
            print("\nMenú de Gestión de Inventarios ")
            print("1. Añadir producto")
            print("2. Eliminar producto")
            print("3. Actualizar producto")
            print("4. Buscar producto")
            print("5. Mostrar todos los productos")
            print("6. Salir")

            try:
                opcion = input("\nSeleccione una opción: ")

                if opcion == '1':
                    print("\n Añadir nuevo producto")
                    id_producto = input("ID del producto: ")
                    nombre = input("Nombre: ")
                    cantidad = int(input("Cantidad: "))
                    precio = float(input("Precio: $"))
                    producto = Producto(id_producto, nombre, cantidad, precio)
                    inventario.añadir_producto(producto)

                elif opcion == '2':
                    print("\n Eliminar producto ")
                    id_producto = input("ID del producto a eliminar: ")
                    inventario.eliminar_producto(id_producto)

                elif opcion == '3':
                    print("\n Actualizar producto ")
                    id_producto = input("ID del producto a actualizar: ")
                    try:
                        cantidad = input("Nueva cantidad (Enter para mantener): ")
                        precio = input("Nuevo precio (Enter para mantener): ")
                        cantidad = int(cantidad) if cantidad.strip() else None
                        precio = float(precio) if precio.strip() else None
                        inventario.actualizar_producto(id_producto, cantidad, precio)
                    except ValueError:
                        print("! Error: Los valores deben ser numéricos")

                elif opcion == '4':
                    print("\n-- Buscar producto --")
                    nombre = input("Nombre a buscar: ")
                    resultados = inventario.buscar_producto(nombre)
                    if resultados:
                        print("\nProductos encontrados:")
                        print("-" * 50)
                        for p in resultados:
                            print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, "
                                  f"Cantidad: {p.get_cantidad()}, Precio: ${p.get_precio():.2f}")
                        print("-" * 50)
                    else:
                        print("! No se encontraron productos")

                elif opcion == '5':
                    inventario.mostrar_productos()

                elif opcion == '6':
                    print("\n¡Hasta luego!")
                    break

                else:
                    print("\n! Opción no válida")

            except ValueError:
                print("! Error: Ingrese valores válidos")
            except Exception as e:
                print(f"! Error: {str(e)}")

if __name__ == "__main__":
    menu()