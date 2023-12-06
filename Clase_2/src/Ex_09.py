""" scribir un programa que le pida al usuario una temperatura en grados
Celsius y la convierta a grados Fahrenheit. Mostrar el resultado en pantalla. """



grados_C = float(input("Ingrese ºC: "))

grados_C = (grados_C * (9/5)) + 32

print("Grados ºF: ",grados_C)