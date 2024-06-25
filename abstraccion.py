from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Rectangulo(FiguraGeometrica):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(FiguraGeometrica):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio

    def area(self):
        return 3.14 * self.radio**2

    def perimetro(self):
        return 2 * 3.14 * self.radio

# Crear instancias de Rectangulo y Circulo
mi_rectangulo = Rectangulo("Rectángulo", 5, 10)
mi_circulo = Circulo("Círculo", 7)

# Calcular área y perímetro de las figuras
print(f"Área del {mi_rectangulo.nombre}: {mi_rectangulo.area()}")
print(f"Perímetro del {mi_rectangulo.nombre}: {mi_rectangulo.perimetro()}")

print(f"Área del {mi_circulo.nombre}: {mi_circulo.area()}")
print(f"Perímetro del {mi_circulo.nombre}: {mi_circulo.perimetro()}")
