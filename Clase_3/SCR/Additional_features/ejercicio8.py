# Escribí un programa que solicite al usuario el ingreso de dos números diferentes y muestre en pantalla al mayor de los dos.

##### Nota: Este es un poco mas complicado, pero con lo que vimos hasta la fecha, lo pueden resolver. #####

number1 = float(input("Insert number one: "))
number2 = float(input("Insert number two: "))

if number1 > number2:
    print("Number 1 is greater than number 2")
elif number1 < number2:
    print("Number 2 is greater than number 1")
else:
    print("Number 1 is equal to number 2")