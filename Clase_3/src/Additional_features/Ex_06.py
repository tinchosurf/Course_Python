# Escribir un programa que pida al usuario dos números y devuelva su división. 
# Si el usuario introduce el divisor cero debera imprimir un mensaje de error.
##### Nota: Este es un poco mas complicado, pero con lo que vimos hasta la fecha, lo pueden resolver. #####


number1 = float(input("Insert number one: "))
number2 = float(input("Insert number two: "))

if number2 == 0:
    print("The numbers aren't divisible by zero")
else:
    total = number1 / number2
    print(f"The numbers are divisible. The result is {total}")