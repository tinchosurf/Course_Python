# a = int(input("Ingrese un numero entero: "))
# if a % 2 == 0:
#     print("El numero ingresado es par")
#     print("Esto se ejecuta adentro del if")
# else:
#     print("El numero ingresado es impar")

# print("Esto se ejecuta siempre")



# a = 10
# b = 15
# if a > b:
#     print("a es mayor que b")
# elif a + 5 == b:
#     print("a + 5 es igual a b")
# elif a < b:
#     print("a es menor que b")
# else:
#     print("a y b son iguales")

# if a + 5 == b:
#     print("a + 5 es igual a b")
# if a < b:
#     print("a es menor que b")



# if True and "hola":
#     print("Verdadero")
# else:
#     print("Falso")



# a = 10
# if a % 2 == 0:
#     texto = "par"
# else:
#     texto = "impar"

# print(texto)
# texto_2 = "par" if a % 2 == 0 else "impar"
# print(texto_2)



# a = 10
# if a == 10:
#     condicion = True
# else:
#     condicion = False

# print(condicion)
# condicion_2 = (a == 10)
# print(condicion_2)



# a = 0.1
# b = 0.2
# if a + b == 0.3:
#     print("Verdadero")
# else:
#     print("Falso")

# c = a + b
# tolerancia = 0.00000001
# if abs(c - 0.3) < tolerancia:
#     print("Verdadero con tolerancia")


# try:
#     numero = float(input("Ingrese un numero: "))
#     if numero % 2 == 0:
#         print("Par")
#     else:
#         print("Impar")
# except ValueError:
#     print("Ingrese un numero por favor")


# try:
#     numero_1 = float(input("Ingrese un numero: "))
#     numero_2 = float(input("Ingrese otro numero: "))

#     division = numero_1 / numero_2
#     print(division)
# except ValueError:
#     print("Ingrese solamente numeros")
# except ZeroDivisionError:
#     print("El segundo numero no debe ser 0")



try:
    numero_1 = float(input("Ingrese un numero: "))
    numero_2 = float(input("Ingrese otro numero: "))

    try:
        division = numero_1 / numero_2
        print(division)
    except:
        print("El segundo numero no debe ser 0")
except:
    print("Ingrese solamente numeros")
