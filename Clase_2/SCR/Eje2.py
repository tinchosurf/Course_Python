""" Escribir un programa que le pida al usuario un precio de alojamiento por
noche y una cantidad de días de alojamiento, para luego calcular y mostrar
en pantalla el precio total de la estadía. """



dias = float(input("Cantidad de dias: "))
precio = float(input("Precio dia: "))
total = precio*dias

print("precio total", total)