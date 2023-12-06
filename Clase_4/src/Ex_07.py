# Escribe una función llamada calculadora que tome tres argumentos: dos números y un operador (+, -, *, /). La función debe realizar la operación correspondiente y devolver el resultado.
# Si quieres puedes tratar los posibles errores.


# Resolucion
def calculadora(num1, num2, operador):
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            raise ValueError("No se puede dividir por cero")
    else:
        raise ValueError("Operador no válido")
    
    return resultado

# Ejemplos de uso
try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    operador = input("Introduce el operador (+, -, *, /): ")
    
    resultado = calculadora(num1, num2, operador)
    print("Resultado:", resultado)
except ValueError as e:
    print("Error:", e)