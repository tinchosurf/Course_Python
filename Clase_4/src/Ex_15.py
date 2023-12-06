# Escribe un programa que convierta una temperatura en grados Celsius a grados Fahrenheit. Asegúrate de manejar posibles errores de entrada, como ingresar letras en lugar de números.

try:
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("La temperatura en grados Fahrenheit es:", fahrenheit)
except ValueError:
    print("Error: Ingresa una temperatura válida.")
except Exception as e:
    print("Error inesperado:", e)