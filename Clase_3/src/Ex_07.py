""" Escribir un programa que le pida al usuario ingresar un número entre 1 y
12, y muestre en pantalla el mes del año al que corresponde. Contemplar
números fuera de ese rango. """

number = 0
while (number == 0):
    number = int(input("Put a number betewn 1 and 12: "))

    if number>12 or number<1:
        print("isert a number beten 1 and 12")
        number = 0

if number == 1:
    print("January")
elif number == 2:
    print("February")
elif number == 3:
    print("March")
elif number == 4:
    print("April")
elif number == 5:
    print("May")
elif number == 6:
    print("June")
elif number == 7:
    print("July")
elif number == 8:
    print("August")
elif number == 9:
    print("September")
elif number == 10:
    print("October")
elif number == 11:
    print("November")
elif number == 12:
    print("December")