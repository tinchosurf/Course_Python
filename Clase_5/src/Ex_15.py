# Calcula la suma de todos los números pares del 1 al 50 usando un bucle while.

number =0
num = 0
while True:
    num = num +1
    if num%2 == 0:
        number = number + num
        print(number)
    if num == 50:
        break
