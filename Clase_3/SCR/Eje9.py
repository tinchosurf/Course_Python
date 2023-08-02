""" Escribir un programa que determine si el último dígito de un número
entero ingresado por el usuario es divisible por 4 """

numbertest = input ("input a number")

l = len(numbertest)
numbertest = int(numbertest[l-1])

if numbertest % 4 == 0: 
    print(f"the number {numbertest} is divisible by 4.")

else:
    print(f"the number {numbertest} is not divisible by 4.")

