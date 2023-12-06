""" Escribir un programa que le pida al usuario ingresar un número de 3
cifras, y muestre en pantalla el valor de las unidades, las decenas y las
centenas. Por ejemplo, si el número ingresado es “478”, el programa debería
mostrar en pantalla lo siguiente:
Unidades = 8
Decenas = 7
Centenas = 4 """

#  Pedimos al usuario ingresar un número de 3 cifras
numero = input("Ingrese un número de 3 cifras: ")

# Verificamos que el número tenga exactamente 3 cifras y no contenga decimales
if not numero.isdigit() or len(numero) != 3:
    print("Error: Debe ingresar un número entero de 3 cifras.")
else:
    # Obtenemos las unidades, decenas y centenas convirtiendo el número a entero
    unidades = int(numero[2])
    decenas = int(numero[1])
    centenas = int(numero[0])

    # Mostramos los resultados en pantalla
    print("Unidades =", unidades)
    print("Decenas =", decenas)
    print("Centenas =", centenas)