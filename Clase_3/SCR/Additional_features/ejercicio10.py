# Dos equipos de futbol están disputando el saque inicial del juego. 
# Los capitanes de cada equipo deciden jugar el clásico juego "Piedra, papel o tijera" para definir quien hace el saque. 
# Las reglas son las usuales: Piedra vence a Tijera, Tijera vence a Papel y Papel vence a Piedra.
# Juegan una sola vez.
import random

while True:
    my_hand = input("Enter rock, paper, or scissors: ")
    my_hand = my_hand.lower()
    if my_hand in ("rock", "paper", "scissors"):
        break

possible_hands = random.choice(("rock", "paper", "scissors"))

if possible_hands == my_hand:
    print("It's a tie")
elif possible_hands == "rock" and my_hand == "paper":
    print("You win against rock")
elif possible_hands == "rock" and my_hand == "scissors":
    print("You lose against rock")
elif possible_hands == "scissors" and my_hand == "paper":
    print("You lose against scissors")
elif possible_hands == "scissors" and my_hand == "rock":
    print("You win against scissors")
    
    
