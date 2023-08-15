# Cree un programa que calcule el IMC (Indice de masa corporal). Formula --> IMC=Peso/Altura2 (Peso sobre altura al cuadrado)
# El usuario debera ingresar su peso y su altura (su nombre si quieren y despues imprimirlo concatenado) y el programa ademas de 
# calcular el IMC debera decir en que clasificacion se encuentra.
# La clasificacion la encontraran el archivo de imagen: IMC_clasificacion.jpg

name = input("input your name: ")
weight = float(input("input your weight (kg): "))  
height = float(input("input your height (m): "))
value_IMC = weight / (height ** 2)

if value_IMC < 18.5:
    state = "underweight"
elif 18.5 <= value_IMC < 24.9:
    state = "proper weight"
elif 25 <= value_IMC < 29.9:
    state = "overweight"
elif 30 <= value_IMC < 34.9:
    state = "grade 1 obesity"
elif 35 <= value_IMC < 39.9:
    state = "grade 2 obesity"
else:
    state = "grade 3 obesity"  
    
print(f"{name} has an IMC of {value_IMC:.2f} and your state is {state}")
