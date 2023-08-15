# Escribir un programa que almacene la cadena de caracteres digitalmind en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable

password_loing = "digitalmind"

while (True):
    password_usser = input("Enter Pasword: ")

    if password_loing == password_usser:
        print("Pass")
        break
    
    print("Incorrect Password ")
        


