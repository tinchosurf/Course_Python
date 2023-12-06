""" Escribir un programa que le pida al usuario que ingrese un número y
determine si es positivo, negativo o cero """


number = float(input("Put a number to test: "))

if number < 0:
    print(f"The number {number} is negative")
elif number > 0:
    print(f"The number {number} is positive")
else:
    print(f"The number is zero")