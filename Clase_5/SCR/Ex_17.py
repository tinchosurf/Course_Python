# Validación de entrada:
# Solicita al usuario un número entre 1 y 10, y sigue solicitando hasta que se ingrese un valor válido.


while True:
    num = int(input("Type a number (1 to 10): "))  # Convertir la entrada a un número entero

    if not (1 <= num <= 10):
        print("Please enter a valid number between 1 and 10.")
    else:
        print(f"You entered: {num}")
        break
