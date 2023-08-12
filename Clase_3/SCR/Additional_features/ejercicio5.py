# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y 
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 80 ARS y si es mayor de 18 años, 150 ARS.


age = int(input("Enter your age: "))

if age < 4:
    print("You are a babe and don't have to pay")
elif 4 <= age <= 18:  
    print("You are a child and must pay $80")
else:
    print("You are an adult and must pay $150")