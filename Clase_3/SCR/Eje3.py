""" Escribir un programa que le pida al usuario que ingrese 2 números y
determine si son divisibles entre sí. """

number1 = float(input("insert number one: "))
number2 = float(input("insert number two: "))

try:
    total = number1 / number2
    print("the number aren divisible")
except:
    print("the number are`t divisible")

