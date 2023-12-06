# En la función de nuestro ejercicio hay un fallo potencial, averigua cuándo sucede y retorna el valor None en ese caso especial, 
# en cualquier otro caso devuelve el resultado normal de la función.
def dividir(a, b):
    return a/b


# Resolucion
def dividir(a, b):
    if b == 0:
        return None
    else:
        return a/b

print(dividir(10,0))