# Escribir un programa que le solicite al usuario ingresar 2 números y un
# operador aritmético, y muestre en pantalla el resultado de la operación. Por
# ejemplo:
# Primer número: 7
# Segundo número: 4
# Operador: *
# El resultado de 7 * 4 es 28

primer_numero = float(input("Ingrese el primer número: "))
segundo_numero = float(input("Ingrese el segundo número: "))
operador = input("Ingrese el operador aritmético (+, -, *, /): ")

if operador == '+':
    resultado = primer_numero + segundo_numero
elif operador == '-':
    resultado = primer_numero - segundo_numero
elif operador == '*':
    resultado = primer_numero * segundo_numero
elif operador == '/':
    resultado = primer_numero / segundo_numero
else:
    resultado = "Operador inválido"

print(f"El resultado de {primer_numero} {operador} {segundo_numero} es {resultado}")
