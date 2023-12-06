""" Escribir un programa que le pida al usuario 3 números y muestre el
promedio en pantalla. """



valor = 0
for i in range (1,4):
    valor += float(input(f"ingrese el valor {str(i)}:" ))
    

valor = valor / 3

print(valor)

