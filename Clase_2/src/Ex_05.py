""" Escribir un programa que le pida al usuario 3 números y muestre el
máximo y el mínimo en pantalla. """



valor = []

for i in range (1,4):
    valor.append(float(input(f"ingrese el valor {str(i)}:" )))

print ("valor maximo", max(valor))
print ("valor minimo", min(valor))
