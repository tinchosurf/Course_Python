# Implementar el juego de “piedra, papel, tijera”. Solicitar a cada jugador
# que ingrese una string (“piedra”, “papel” o “tijera”) y muestre en pantalla quién
# gana o si hay empate. Por ejemplo:
# Jugador 1: piedra
# Jugador 2: papel
# Jugador 2 le gana a Jugador 1 ya que papel le gana a piedra.



jugador1 = input("Jugador 1: ")
jugador2 = input("Jugador 2: ")

if jugador1 == jugador2:
    print("Empate")
elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
    print("Jugador 1 gana")
else:
    print("Jugador 2 gana")
    
