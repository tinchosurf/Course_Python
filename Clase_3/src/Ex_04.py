""" Escribir un programa que calcule el valor absoluto de un número sin
utilizar la función abs() """


numberabs = float(input("insert number: "))

if (numberabs < 0):
    numberabs*=-1
    print("number original is negative")

else:
    print("number original is positive")

print("number ABS: ",numberabs)
