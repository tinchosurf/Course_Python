# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba "salir" que terminará.

while True:
    word = input("Type a word: ")
    
    if word == "q":
        print("Exit")
        break
    
    print(word + "\n")
