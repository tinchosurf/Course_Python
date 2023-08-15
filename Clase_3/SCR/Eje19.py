# Escribir un programa que determine si un año es bisiesto.

def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    return False

año = int(input("Ingrese un año: "))
if es_bisiesto(año):
    print(f"{año} es un año bisiesto")
else:
    print(f"{año} no es un año bisiesto")





