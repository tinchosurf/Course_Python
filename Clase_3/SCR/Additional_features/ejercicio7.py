# Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo.


number = float(input("Insert number: "))

if 0 <= number <= 10:
    print(f"The number {number} is between zero and ten")
else:
    print(f"The number {number} isn't between zero and ten")