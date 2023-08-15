# Escribir un programa que le solicite al usuario ingresar 2 números de
# punto flotante y muestre por pantalla si son iguales o no. Contemplar el caso
# en el que el usuario no ingresa un número.


def es_numero(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

numero1 = input("Ingrese el primer número: ")
numero2 = input("Ingrese el segundo número: ")

if es_numero(numero1) and es_numero(numero2):
    num1 = float(numero1)
    num2 = float(numero2)

    if num1 == num2:
        print("Los números son iguales")
    else:
        print("Los números no son iguales")
else:
    print("Debe ingresar números válidos")

