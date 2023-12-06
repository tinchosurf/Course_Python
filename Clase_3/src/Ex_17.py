# Escribir un programa que le pida al usuario ingresar 3 o mas números y los
# ordene de mayor a menor, utilizando solamente condicionales.



class Ordenar_numeros():
    def __init__(self, numeros):
        self._numeros = numeros

    def Ordenar(self):
        n = len(self._numeros)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self._numeros[j] < self._numeros[j + 1]:
                    temp = self._numeros[j]
                    self._numeros[j] = self._numeros[j + 1]
                    self._numeros[j + 1] = temp
        return self._numeros

numeritos = [1, 3, 5, 9, 4]

listaa = Ordenar_numeros(numeritos.copy())  # Make a copy to preserve the original list
sorted_list = listaa.Ordenar()
print(sorted_list)  # Print the sorted list

