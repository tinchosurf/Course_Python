'''Escribir un programa que determine el tipo de triángulo en base a los 3
lados ingresados por el usuario (equilátero = 3 lados iguales, isósceles = 2
lados iguales, escaleno = todos los lados desiguales).'''

class Triangulo:
    def __init__(self, lado1, lado2,lado3):
        self._lado1 = lado1
        self._lado2 = lado2
        self._lado3 = lado3
        
    def Tipo_triangulo (self):
        if self._lado1 == self._lado2 == self._lado3:
            self._tipot = "equilatero"
        elif self._lado1 != self._lado2 != self._lado3:
            self._tipot = "escaleno"
        else:
            self._tipot = "isoceles"
        return self._tipot
    
    def __str__(self):
        return f"{self.Tipo_triangulo()}"

triangulo1 = Triangulo(10, 10, 10)

print(f"El tipo es: {triangulo1}")

triangulo2 = Triangulo(10, 20, 10)

print(f"El tipo es: {triangulo2}")

triangulo3 = Triangulo(10, 20, 30)

print(f"El tipo de triandulo es: {triangulo3}")