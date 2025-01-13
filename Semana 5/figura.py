import math

class FiguraGeometrica:
    """
    Clase base para figuras geométricas.
    """
    def __init__(self, nombre: str):
        """
        Constructor de la clase FiguraGeometrica.

        Args:
            nombre: El nombre de la figura.
        """
        self.nombre = nombre

    def calcular_area(self) -> float:
        """
        Calcula el área de la figura. Este método debe ser implementado
        por las clases hijas.

        Raises:
            NotImplementedError: Si se intenta calcular el área directamente
                desde la clase base.

        Returns:
            El área de la figura.
        """
        raise NotImplementedError("El método calcular_area debe ser implementado por las clases hijas.")

    def mostrar_info(self):
        """Muestra información de la figura."""
        print(f"Figura: {self.nombre}")


class Cuadrado(FiguraGeometrica):
    """
    Clase para representar un cuadrado.
    """
    def __init__(self, lado: float):
        """
        Constructor de la clase Cuadrado.

        Args:
            lado: La longitud del lado del cuadrado.
        """
        super().__init__("Cuadrado")
        self.lado = lado

    def calcular_area(self) -> float:
        """Calcula el área del cuadrado."""
        return self.lado * self.lado


class Rectangulo(FiguraGeometrica):
    """
    Clase para representar un rectángulo.
    """
    def __init__(self, base: float, altura: float):
        """
        Constructor de la clase Rectangulo.

        Args:
            base: La longitud de la base del rectángulo.
            altura: La longitud de la altura del rectángulo.
        """
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula el área del rectángulo."""
        return self.base * self.altura


class Circulo(FiguraGeometrica):
    """
    Clase para representar un círculo.
    """
    def __init__(self, radio: float):
        """
        Constructor de la clase Circulo.

        Args:
            radio: El radio del círculo.
        """
        super().__init__("Círculo")
        self.radio = radio

    def calcular_area(self) -> float:
        """Calcula el área del círculo."""
        return math.pi * self.radio * self.radio


# Ejemplo de uso
cuadrado = Cuadrado(5.0)
rectangulo = Rectangulo(4.0, 6.0)
circulo = Circulo(3.0)

figuras = [cuadrado, rectangulo, circulo]

for figura in figuras:
    figura.mostrar_info()
    area = figura.calcular_area()
    print(f"Área: {area}")
    print("-" * 20)

#Ejemplo con datos incorrectos (para mostrar manejo de tipos)
#Intentar crear un cuadrado con un lado negativo
try:
    cuadrado_negativo = Cuadrado(-5)
except Exception as e:
    print(f"Error al crear el cuadrado: {e}")

#Ejemplo de uso de booleano (implícito en el bucle for y el try except)

#Ejemplo de uso de string (nombre de la figura)
