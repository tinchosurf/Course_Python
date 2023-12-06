# Pide al usuario que ingrese una cadena y un carácter específico. Elimina todas las ocurrencias de ese carácter en la cadena.


# Solicitar al usuario que ingrese una cadena
cadena = input("Ingresa una cadena: ")

# Solicitar al usuario que ingrese un carácter específico
caracter_a_eliminar = input("Ingresa el carácter que deseas eliminar: ")

# Eliminar todas las ocurrencias del carácter en la cadena
cadena_sin_caracter = cadena.replace(caracter_a_eliminar, '')

print("Cadena original:", cadena)
print("Cadena sin el carácter:", cadena_sin_caracter)