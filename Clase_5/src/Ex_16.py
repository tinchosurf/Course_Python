# Imprime la tabla de multiplicar de un número dado por el usuario, se debe utilizar el bucle while.

multiplie = 0
num = input("Enter a number to multiply: ")

try:
    num = int(num)
except ValueError:
    print("Please enter a valid number.")
    exit()

while True:
    multiplie = multiplie +1
    result = num * multiplie
    print(f"Number {num} multiplied by {multiplie} is {result}")
    if multiplie == 10:
        break