""" Escribir un programa que le pida al usuario que ingrese 2 números y
determine cuál es el mayor """

number1 = float(input("insert number one: "))
number2 = float(input("insert number two: "))

if number1 > number2:
    print(f"number one = {number1} is greater than number two = {number2}")
elif number1 < number2:
    print(f"number one = {number1} is smaller than number two = {number2}")

else:
    print(f"number one = {number1} is equal than number two = {number2}")