# Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”. 
# Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato.

##### Si hacen este son genios!!!! #####
##### Nota: Este es un poco mas complicado, pero con lo que vimos hasta la fecha, lo pueden resolver. ##### 



verifie = input("Input a letter: ")
vowel = ("a", "e", "i", "o", "u")
if len(verifie) > 1:
    print("Error: Please input a single letter")
else:
    verifie = verifie.lower()  
    if verifie in vowel:  
        print("The letter is a vowel")
    else:
        print("The letter isn't a vowel")