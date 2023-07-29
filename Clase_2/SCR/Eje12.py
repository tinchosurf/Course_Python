""" Escribir un programa que le pida al usuario el año actual y su edad, y le
diga en qué año cumpliría 1000 años. Asumir que la edad es menor a 1000.
Recordar usar el tipo de variable correcto. """

# Pedimos al usuario que ingrese el año actual y su edad
year_actual = int(input("Ingresa el año actual: "))
edad_actual = int(input("Ingresa tu edad actual (menor a 1000): "))

# Asumimos que la edad es menor a 1000 (según la descripción del problema)
# Calculamos el año en que cumpliría 1000 años
year_cumplir_1000 = year_actual + (1000 - edad_actual)

# Imprimimos el resultado
print("Cumplirás 1000 años en el año:", year_cumplir_1000)