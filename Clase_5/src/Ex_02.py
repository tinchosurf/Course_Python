# Calcula la suma de todos los números pares del 1 al 50 utilizando un bucle for.
cont = 0
for num in range(1,51):
    if num%2 == 0:
        cont= cont + num
print(cont)