""" Escribir un programa que le pida al usuario ingresar una palabra y un
número, y muestre en pantalla la palabra repetida tantas veces como lo
indica el número (separadas por un espacio) """

pal1 = str(input("palabra 1: "))
veces = int(input("cantidad de veces: "))

conca = (pal1 + " ") * veces

print(conca)