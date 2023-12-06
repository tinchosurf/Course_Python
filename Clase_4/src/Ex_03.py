# Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura
# Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.


# Resolucion
def area_rectangulo(base, altura):
    area = base * altura
    return area

base_rectangulo = 15
altura_rectangulo = 10

area_del_rectangulo = area_rectangulo(base_rectangulo, altura_rectangulo)
print("El área del rectángulo es:", area_del_rectangulo)