# Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio


# Resolucion
def area_circulo(radio):
    area = 3.14 * radio ** 2
    return area

radio = 5
area_del_circulo = area_circulo(radio)
print("El área del círculo con radio", radio, "es:", area_del_circulo)