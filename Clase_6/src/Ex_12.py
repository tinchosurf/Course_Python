# Nos dieron la siguiente cadena con nombres de empleados:
nombres = "Juan, Martina, Pedro, Mariana, Tomas"
# y nos solicitarion que guardemos en variables cada uno de los nombres e imprimamos por pantalla.

# Usar el método split para dividir la cadena en nombres individuales
nombres_lista = nombres.split(', ')

# Asignar los nombres a variables individuales
nombre1, nombre2, nombre3, nombre4, nombre5 = nombres_lista

# Imprimir los nombres
print("Nombre 1:", nombre1)
print("Nombre 2:", nombre2)
print("Nombre 3:", nombre3)
print("Nombre 4:", nombre4)
print("Nombre 5:", nombre5)