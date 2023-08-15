# Escribir un programa que le solicite al usuario ingresar las coordenadas
# en el espacio de 2 puntos( (x1,y1), (x2,y2)) y determine cuál de ellos se
# encuentra más cerca del origen (coordenadas (0,0)). La distancia al origen se
# calcula como: . Notar que raiz_cuadrada(𝑥2 + 𝑦2) raiz_cuadrada x= x exp 0.5



import math

def distancia_al_origen(x, y):
    return math.sqrt(x ** 2 + y ** 2)

x1 = float(input("Ingrese la coordenada x del primer punto: "))
y1 = float(input("Ingrese la coordenada y del primer punto: "))
x2 = float(input("Ingrese la coordenada x del segundo punto: "))
y2 = float(input("Ingrese la coordenada y del segundo punto: "))

distancia1 = distancia_al_origen(x1, y1)
distancia2 = distancia_al_origen(x2, y2)

if distancia1 < distancia2:
    print("El primer punto está más cerca del origen")
elif distancia2 < distancia1:
    print("El segundo punto está más cerca del origen")
else:
    print("Ambos puntos están a la misma distancia del origen")