# Localiza el error en el bloque de código de abajo. Crea una excepción
# para evitar que el programa se bloquee y además explica en un mensaje al usuario
# la causa y/o solución:
resultado = 10/0


# Resolucion
try:
    resultado = 10/0
except ZeroDivisionError:
    print("No se puede dividir por 0")