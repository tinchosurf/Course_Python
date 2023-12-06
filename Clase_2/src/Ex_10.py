""" Escribir un programa que le pida al usuario una temperatura en grados
Fahrenheit y la convierta a grados Celsius. Mostrar el resultado en pantalla.
 """

grados_F = float(input("Ingrese ºF: "))

grados_F = ((grados_F - 32) * (5/9))

print("Grados ºC: ",grados_F)