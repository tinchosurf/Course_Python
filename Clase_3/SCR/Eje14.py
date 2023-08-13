"""Escribir un programa que le pida al usuario ingresar los nombres de dos
equipos de fútbol y la cantidad de goles que hizo cada uno, para luego
mostrar en pantalla el resultado del partido, indicando qué equipo ganó o si
hubo un empate."""

class Team:
    def __init__(self, name):
        self.name = name
        self.goals = 0

    def record_goals(self, quantity):
        self.goals = quantity

    def __str__(self):
        return f"{self.name}: {self.goals} goals"


def main():
    team1_name = input("Enter the name of the first team: ")
    team2_name = input("Enter the name of the second team: ")

    team1 = Team(team1_name)
    team2 = Team(team2_name)

    team1_goals = int(input(f"Enter the number of goals scored by {team1_name}: "))
    team2_goals = int(input(f"Enter the number of goals scored by {team2_name}: "))

    team1.record_goals(team1_goals)
    team2.record_goals(team2_goals)

    print("\nMatch result:")
    print(team1)
    print(team2)

    if team1.goals > team2.goals:
        print(f"{team1.name} won the match.")
    elif team2.goals > team1.goals:
        print(f"{team2.name} won the match.")
    else:
        print("The match ended in a draw.")


if __name__ == "__main__":
    main()