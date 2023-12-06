# JUEGO "Adivinanza del numero"
# Generaremos un número entre 1 y 10.
# Nuestro objetivo es adivinar el número. Si fallamos nos dirán si es mayor o menor que el número buscado. También poner el número de intentos requeridos.

# NOTA IMPORTANTE, estas dos lineas de abajo generan un numero aleatorio entre 1 y 10. Puse el print para que vean que cada vez que ejecutan el codigo 
# va a generarse un numero distinto.
# Mas adelante lo vamos a ver, asi que quedense tranquilos. Solamente utilicen la variable numero para realizar el ejercicio.


import random

rannum = random.randint(1, 10)

num = input("Type your number: ")
num = int(num)  # Convertir la entrada a un número entero

if rannum == num:
    print("You guessed correctly!")
elif rannum > num:
    print("Your number is smaller.")
elif rannum < num:
    print("Your number is greater.")

print(f"The random number was: {rannum}")
