# Escribe una función llamada numero_mayor que tome dos números como argumentos y devuelva el número más grande entre ellos.


# Resolucion
def numero_mayor(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Ejemplo de uso
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

mayor = numero_mayor(numero1, numero2)
print(f"El número más grande es: {mayor}")