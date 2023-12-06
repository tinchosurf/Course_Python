# Escribir un programa que le solicite al usuario ingresar un idioma y luego
# imprima en pantalla un mensaje de “Bienvenido” en ese idioma. Contemplar
# el ingreso de un idioma desconocido por el programa. Se debe aceptar el
# idioma escrito todo en minúsculas, todo en mayúsculas o comenzando con
# mayúscula (es decir que “español”, “ESPAÑOL” y “Español” son todas
# entradas válidas).




idiomas = {
    "español": "Bienvenido",
    "inglés": "Welcome",
    "francés": "Bienvenue",
    # Agrega más idiomas si lo deseas
}

idioma = input("Ingrese un idioma: ").lower()

if idioma in idiomas:
    print(idiomas[idioma])
else:
    print("Idioma desconocido")