# Escribe una función llamada suma_lista que tome una lista de números como argumento y devuelva la suma de todos los números en la lista.


# Resolucion
def suma_lista(lista):
    return sum(lista)

# Ejemplo de uso
lista_numeros = [1, 2, 3, 4, 5]
resultado = suma_lista(lista_numeros)
print("La suma de la lista es:", resultado)