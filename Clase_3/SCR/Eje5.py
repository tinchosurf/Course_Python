""" Escribir un programa que le pida al usuario que ingrese un número y
determine si es divisible por 2, por 3 o por ambos """

number = float(input("Put a number to test: "))

if (number %3 == 0) and (number %2 == 0):
    print(f"the number {number} is divisible by 2 and 3 .")

elif number %2 == 0:
    print(f"the number {number} is divisible by 2.")

elif number %3 == 0:
    print(f"the number {number} is divisible by 3.")

else:
    print( f"the number {number} is not divisible by 3 or 2")