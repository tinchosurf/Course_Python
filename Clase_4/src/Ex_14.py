# si hay un error capturalo
valor = int("diez")


# Resolucion
try:
    valor = int("diez")
except ValueError:
    print("Error de valor, no puedes tranformar letras a entero")