# Ingresa un número y muestra su tabla de multiplicar del 1 al 10 utilizando un bucle for.

num = input("Enter a number to multiply: ")

# Asegúrate de convertir la entrada a un número entero
try:
    num = int(num)
except ValueError:
    print("Please enter a valid number.")
    exit()

# Itera del 1 al 10 e imprime los resultados de la multiplicación
for multiplie in range(1, 11):
    result = num * multiplie
    print(f"Number {num} multiplied by {multiplie} is {result}")