# Solicitarle al usuario una palabra y luego verificar si la palabra ingresada es un palindromo.


# Solicitar al usuario una palabra
palabra = input("Ingresa una palabra: ")

# Eliminar espacios en blanco y convertir la palabra a minúsculas
palabra = palabra.lower().replace(" ", "")

# Verificar si la palabra es un palíndromo
if palabra == palabra[::-1]:
    print("La palabra ingresada es un palíndromo.")
else:
    print("La palabra ingresada no es un palíndromo.")