# Pedir ingresar los lados de un triángulo e indicar de qué tipo es:
# Isósceles: 2 lados iguales
# Equilátero: 3 lados iguales
# Escaleno: 0 lados iguales

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self._lado1 = lado1
        self._lado2 = lado2
        self._lado3 = lado3
        
    def Tipo_triangulo(self):
        if self._lado1 == self._lado2 == self._lado3:
            self._tipot = "equilátero"
        elif self._lado1 != self._lado2 and self._lado2 != self._lado3 and self._lado1 != self._lado3:
            self._tipot = "escaleno"
        else:
            self._tipot = "isósceles"
        return self._tipot
    
    def __str__(self):
        return f"Triángulo {self.Tipo_triangulo()}"

triangulo1 = Triangulo(10, 11, 10)
print(triangulo1)