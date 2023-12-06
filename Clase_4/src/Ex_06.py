# Realizar una función llamada par_o_impar:

# 1-Recibirá un número por parámetro
# 2-Imprimirá Par si el número es par
# 3-Imprimirá Impar si el número es impar
# 4-Si se ingresa algo que no sea número debe indicar que se ingrese un número. (Para pensar un poco más) 


# Resolucion
def par_o_impar(numero):
    if type(numero) == int:
        if numero % 2 == 0:
            print("Par")
        else:
            print("Impar")
    else:
        print("Por favor, ingresa un número.")

# Ejemplos de uso
numero1 = 10
numero2 = 7
numero3 = "Hola"

par_o_impar(numero1)  
par_o_impar(numero2)
par_o_impar(numero3)