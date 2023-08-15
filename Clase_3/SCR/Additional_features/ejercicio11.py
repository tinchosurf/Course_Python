# Nos solicitaron que realicemos un programa que le pida al usuario un numero y mostrar si el numero que ingreso tiene un solo digito, si tiene dos digitos o mas de dos.

# Luego nos solicitaron que sumemos una mejora, que consta de que muestre si el numero es negativo

while True:
    number = input("Input a number: ")
    if number.replace("-", "").isdecimal():  # Allowing for negative numbers
        break

number = int(number)  # Convert the input to an integer
cant_digit = len(str(abs(number)))

print(f"Number of digits: {cant_digit} and the number is {number}")

if number < 0:
    print("The number is negative")
else:
    print("The number is non-negative (positive or zero)")