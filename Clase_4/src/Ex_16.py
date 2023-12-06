# Crea un programa que convierta una cantidad en metros a su equivalente en centímetros. Asegúrate de manejar excepciones en caso de que el usuario ingrese un valor no numérico.

try:
    metros = float(input("Ingresa una cantidad en metros: "))
    centimetros = metros * 100
    print(f"{metros} metros son {centimetros} centímetros")
except ValueError:
    print("Error: Ingresa un valor numérico válido.")